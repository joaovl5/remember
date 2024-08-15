import ollama
import groq
from services.credential import CredentialService


class AIProviderService:
    def __init__(self, model: str) -> None:
        self.model = model

    def generate(self, system: str, prompt: str, temperature: float) -> str:
        return ollama.chat(
            model=self.model,
            messages=[
                ollama.Message(role="system", content=system),
                ollama.Message(role="user", content=prompt),
            ],
            options=ollama.Options(temperature=temperature),
        )["message"]["content"]


class GroqProviderService(AIProviderService):
    def __init__(self, model: str, credentials: CredentialService) -> None:
        super().__init__(model)
        self.API_KEY = credentials.get_env_key("API_GROQ")
        self.client = groq.Groq(api_key=self.API_KEY)

    def generate(self, system: str, prompt: str, temperature: float) -> str:
        res = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            model=self.model,
            temperature=temperature,
        )

        return res.choices[0].message.content or "Error!"
