from services.ai_provider import GroqProviderService
from services.credential import CredentialService
from services.lookup import LookupService
import PIL.Image as Image
import io
import base64


class WindowApi:
    def __init__(self, credentials: CredentialService) -> None:
        self._provider = GroqProviderService("gemma2-9b-it", credentials=credentials)
        self._lookup = LookupService(credentials=credentials)

    def global_search(self, query: str):
        res = self._lookup.query(query)
        return res.serialize()

    def get_screenshot_image(self, screenshot_path: str) -> str:
        screenshot = Image.open(screenshot_path)

        buffered = io.BytesIO()
        screenshot.save(buffered, format="PNG")

        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return img_str
