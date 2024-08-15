from pydantic import BaseModel


class Snapshot(BaseModel):
    timestamp: float
    description: str  # LLM generated screenshot description
    description_embedding: list[float]
    screenshot_embedding: list[float]
    screenshot_path: str  # Path to actual screenshot
