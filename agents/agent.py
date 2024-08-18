from dataclasses import dataclass
import services.ai_provider as ai
from typing import Any, Callable, Optional


@dataclass
class ParseResult:
    success: bool
    data: Any


@dataclass
class Agent:
    model: str
    provider: ai.llm_backend_type
    system_prompt: str
    parser: Optional[Callable[[str], ParseResult]] = None
    temperature: float = 0.5


def agent_run(agent: Agent, prompt: str) -> Any:
    attempts = 1
    while attempts <= 5:
        output = agent.provider(
            agent.model, agent.system_prompt, prompt, agent.temperature
        )
        if agent.parser:
            parser_result = agent.parser(output)
            if parser_result.success:
                return parser_result.data
            else:
                attempts += 1
                print(f"Failed attempt: {output}")
                continue
        else:
            return output
    raise Exception()
