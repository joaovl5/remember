from dataclasses import dataclass
from services.ai_provider import AIProviderService
from typing import Any, Callable, Optional


@dataclass
class ParseResult:
    success: bool
    data: Any


@dataclass
class Agent:
    provider: AIProviderService
    system_prompt: str
    parser: Optional[Callable[[str], ParseResult]] = None
    temperature: float = 0.5

    def make(self, prompt: str) -> Any:
        attempts = 1
        while attempts <= 5:
            output = self.provider.generate(
                self.system_prompt, prompt, temperature=self.temperature
            )
            if self.parser:
                parser_result = self.parser(output)
                if parser_result.success:
                    return parser_result.data
                else:
                    attempts += 1
                    print(f"Failed attempt: {output}")
                    continue
            else:
                return output
        raise Exception()
