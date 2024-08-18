from dataclasses import dataclass

import agents.definitions as agents
from agents.agent import agent_run
from models.snapshot import Snapshot
import services.ai_provider as ai
import services.database as db
import services.embedding as embedding
from typing_extensions import Any, Optional


@dataclass
class LookupResult:
    success: bool
    snapshot: Optional[Snapshot] = None
    summary: Optional[str] = None


def lookup_result_serialize(result: LookupResult) -> dict[str, Any]:
    return {
        "success": result.success,
        "snapshot": (
            result.snapshot.model_dump(
                exclude={"embedding", "description_embedding"},
            )
            if result.snapshot
            else {}
        ),
        "summary": result.summary,
    }


def init(model: str) -> None:
    global query_generator, result_evaluator, result_provider
    provider = ai.llm_backend_groq
    query_generator = agents.agent_query(provider=provider, model=model)
    result_evaluator = agents.agent_eval(provider=provider, model=model)
    result_provider = agents.agent_result(provider=provider, model=model)


def query(user_query: str):
    attempts = 1
    max_attempts = 5
    while attempts <= max_attempts:
        parsed_query = agent_run(query_generator, user_query)
        parsed_keywords = parsed_query.get("keywords")
        vectorized_keywords = embedding.embed(" ".join(parsed_keywords))

        best_fit: Any = None
        best_fit_acc: float = 0

        for snapshot in db.yield_snapshots():
            acc = embedding.compare(vectorized_keywords, snapshot.description_embedding)

            if acc > best_fit_acc:
                best_fit = snapshot
                best_fit_acc = acc

        query_result = f'User query: "{user_query}", Result:"{best_fit.description}"'

        result_evaluation = agent_run(result_evaluator, query_result)

        if not result_evaluation:
            attempts += 1
            continue

        result_summary = agent_run(result_provider, query_result)

        return LookupResult(True, best_fit, result_summary)
    return LookupResult(False)
