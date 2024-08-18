# Service should automatically schedule logging functions
# Each X minutes take snapshot
from datetime import datetime
from models.snapshot import Snapshot
import services.screenshot as screenshot
from services.ocr import recognize_image
import services.database as db
import services.ai_provider as ai
import services.embedding as embedding
from agents.agent import Agent, agent_run
from agents.systems import logger_summarizer
from PIL.Image import Image
from uuid import uuid4
import os


SCREENSHOT_PATH = "data/screenshots/"


def init(provider: ai.llm_backend_type, model: str) -> None:
    global agent
    provider = provider
    agent = Agent(model, provider, logger_summarizer)
    os.makedirs(SCREENSHOT_PATH, exist_ok=True)


def __save_screenshot(scr: Image) -> str:
    path = os.path.join(SCREENSHOT_PATH, f"{uuid4().hex}.png")
    scr.save(path)
    return path


async def take_snapshot():
    image: Image = await screenshot.take_screenshot()
    image_ocr: str = recognize_image(image)
    image_description = agent_run(agent, image_ocr)
    image_embedding = embedding.embed(image_ocr)
    image_description_embedding = embedding.embed(image_description)
    snapshot = Snapshot(
        timestamp=datetime.now().timestamp(),
        description=image_description,
        screenshot_path=__save_screenshot(image),
        screenshot_embedding=image_embedding,
        description_embedding=image_description_embedding,
    )
    db.register_snapshot(snapshot=snapshot)
