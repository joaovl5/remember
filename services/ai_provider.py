import ollama
import groq
import services.credential as credential
from typing import Callable

llm_backend_type = Callable[[str, str, str, float], str]


def llm_backend_llama(model: str, system: str, prompt: str, temperature: float):
    return ollama.chat(
        model=model,
        messages=[
            ollama.Message(role="system", content=system),
            ollama.Message(role="user", content=prompt),
        ],
        options=ollama.Options(temperature=temperature),
    )["message"]["content"]


def llm_backend_groq(model: str, system: str, prompt: str, temperature: float):
    API_KEY = credential.get_env_key("API_GROQ")
    client = groq.Groq(api_key=API_KEY)
    res = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        model=model,
        temperature=temperature,
    )

    return res.choices[0].message.content or "Error!"
