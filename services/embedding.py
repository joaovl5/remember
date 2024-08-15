from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.linalg import norm


class EmbeddingService:
    def __init__(self) -> None:
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def embed(self, text: str) -> list[float]:
        embeddings = self.model.encode([text])
        return embeddings[0].tolist()

    def compare(self, a: list[float], b: list[float]) -> float:
        A = np.array(a)
        B = np.array(b)
        return np.dot(A, B) / (norm(A) * norm(B))
