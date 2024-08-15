import services.logger
import services.ai_provider
from agents.agent import Agent, ParseResult
from agents.systems import logger_summarizer, query_generator
from agents.definitions import QueryAgent, ResultEvalAgent
from services.lookup import LookupService


def ocr_test(provider):
    agent = Agent(provider=provider, system_prompt=logger_summarizer)
    ocr = ""
    with open("ocr-1.txt", "r") as f:
        ocr = f.read()
    res = agent.make(ocr)
    print(res)


# Keywords: iPad, price
# daterange: 07-08-2024-00-00,07-08-2024-23
def query_gen_test(provider):
    agent = QueryAgent(provider=provider)
    # prompt = "What was the price for the iPad I saw earlier?"
    prompt = "When is my appointment with the doctor?"
    res = agent.make(prompt)
    print(res)


def lookup_test():
    provider = services.ai_provider.GroqProviderService("gemma2-9b-it")
    result_eval = ResultEvalAgent(provider)
    lookup = LookupService()
    # query = "What music was I listening to on Spotify?"
    query = "What was I coding earlier?"
    print("Query: " + query)
    res = lookup.query(query)
    print("Answer: " + str(res.summary))


def main():
    # provider = services.ai_provider.AIProviderService("llama3.1:8b-instruct-q2_K")
    # provider = services.ai_provider.GroqProviderService("gemma2-9b-it")
    # query_gen_test(provider=provider)
    lookup_test()


main()
