from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.linalg import norm

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def embed(text: str) -> list[float]:
    embeddings = model.encode([text])
    return embeddings[0].tolist()


def compare(a: list[float], b: list[float]) -> float:
    A = np.array(a)
    B = np.array(b)
    return np.dot(A, B) / (norm(A) * norm(B))
