from agents.agent import Agent, ParseResult
from agents.systems import (
    logger_summarizer,
    query_generator,
    result_evaluator,
    result_provider,
)
from services.ai_provider import AIProviderService


class QueryAgent(Agent):
    def agent_parser(self, val: str) -> ParseResult:
        try:
            lines = val.split("\n")
            if not lines[0].lower().startswith("keywords"):
                raise Exception()

            keywords = lines[0].split(":")[1].strip(" ").split(",")
            if not len(keywords) > 0:
                raise Exception()

            for k, _ in enumerate(keywords):
                keywords[k] = keywords[k].strip()

            if not lines[1].lower().startswith("daterange"):
                raise Exception()

            dates = lines[1].split(":")[1].strip().split(",")
            date_start = dates[0]
            date_end = dates[1]

            return ParseResult(
                True,
                {"keywords": keywords, "date_start": date_start, "date_end": date_end},
            )

        except Exception:
            return ParseResult(False, None)

    def __init__(self, provider: AIProviderService):
        super().__init__(
            provider=provider,
            system_prompt=query_generator,
            temperature=1,
            parser=self.agent_parser,
        )


class ResultEvalAgent(Agent):
    def agent_parser(self, val: str) -> ParseResult:
        try:
            parsed_val = val.lower().strip()
            if parsed_val in ["yes", "no"]:
                return ParseResult(True, parsed_val == "yes")
            else:
                raise Exception()
        except Exception:
            return ParseResult(False, None)

    def __init__(self, provider: AIProviderService):
        super().__init__(
            provider=provider,
            system_prompt=result_evaluator,
            temperature=1,
            parser=self.agent_parser,
        )


class ResultProviderAgent(Agent):
    def __init__(self, provider: AIProviderService):
        super().__init__(
            provider=provider,
            system_prompt=result_provider,
            temperature=1,
        )
