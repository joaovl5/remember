# Service should automatically schedule logging functions
# Each X minutes take snapshot
from datetime import datetime
from models.snapshot import Snapshot
from services.screenshot import ScreenshotService
from services.ocr import OCRService
from services.database import DatabaseService
from services.ai_provider import AIProviderService
from services.embedding import EmbeddingService
from agents.agent import Agent
from agents.systems import logger_summarizer
from PIL.Image import Image
from uuid import uuid4
import os


class LoggerService:
    SCREENSHOT_PATH = "data/screenshots/"

    def __init__(self, provider: AIProviderService) -> None:
        self.ocr = OCRService()
        self.db = DatabaseService()
        self.screenshot = ScreenshotService()
        self.provider = provider
        self.embedding = EmbeddingService()
        self.agent = Agent(self.provider, logger_summarizer)
        os.makedirs(self.SCREENSHOT_PATH, exist_ok=True)

    def __save_screenshot(self, screenshot: Image) -> str:
        path = os.path.join(self.SCREENSHOT_PATH, f"{uuid4().hex}.png")
        screenshot.save(path)
        return path

    async def take_snapshot(self):
        image: Image = await self.screenshot.take_screenshot()
        image_ocr: str = self.ocr.recognize_image(image)
        image_description = self.agent.make(image_ocr)
        image_embedding = self.embedding.embed(image_ocr)
        image_description_embedding = self.embedding.embed(image_description)
        snapshot = Snapshot(
            timestamp=datetime.now().timestamp(),
            description=image_description,
            screenshot_path=self.__save_screenshot(image),
            screenshot_embedding=image_embedding,
            description_embedding=image_description_embedding,
        )
        self.db.register_snapshot(snapshot=snapshot)
