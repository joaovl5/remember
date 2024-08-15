from dataclasses import dataclass

from agents.definitions import QueryAgent, ResultEvalAgent, ResultProviderAgent
from models.snapshot import Snapshot
from services.ai_provider import AIProviderService, GroqProviderService
from services.credential import CredentialService
from services.database import DatabaseService
from services.embedding import EmbeddingService
from typing_extensions import Any, Optional


@dataclass
class LookupResult:
    success: bool
    snapshot: Optional[Snapshot] = None
    summary: Optional[str] = None

    def serialize(self) -> dict[str, Any]:
        return {
            "success": self.success,
            "snapshot": (
                self.snapshot.model_dump(
                    exclude={"embedding", "description_embedding"},
                )
                if self.snapshot
                else {}
            ),
            "summary": self.summary,
        }


class LookupService:
    def __init__(self, credentials: CredentialService) -> None:
        self.provider = GroqProviderService("gemma2-9b-it", credentials=credentials)
        self.db = DatabaseService()
        self.embedding = EmbeddingService()
        self.query_generator = QueryAgent(self.provider)
        self.result_evaluator = ResultEvalAgent(self.provider)
        self.result_provider = ResultProviderAgent(self.provider)

    def query(self, user_query: str):
        attempts = 1
        max_attempts = 5
        while attempts <= max_attempts:
            parsed_query = self.query_generator.make(user_query)
            parsed_keywords = parsed_query.get("keywords")
            vectorized_keywords = self.embedding.embed(" ".join(parsed_keywords))

            best_fit: Any = None
            best_fit_acc: float = 0

            for snapshot in self.db.yield_snapshots():
                acc = self.embedding.compare(
                    vectorized_keywords, snapshot.description_embedding
                )

                if acc > best_fit_acc:
                    best_fit = snapshot
                    best_fit_acc = acc

            query_result = (
                f'User query: "{user_query}", Result:"{best_fit.description}"'
            )

            result_evaluation = self.result_evaluator.make(query_result)

            if not result_evaluation:
                attempts += 1
                continue

            result_summary = self.result_provider.make(query_result)

            return LookupResult(True, best_fit, result_summary)
        return LookupResult(False)
