import services.lookup as lookup
import PIL.Image as Image
import io
import base64


class WindowApi:
    def __init__(self, model: str) -> None:
        lookup.init(model)

    def global_search(self, query: str):
        res = lookup.query(query)
        return lookup.lookup_result_serialize(res)

    def get_screenshot_image(self, screenshot_path: str) -> str:
        screenshot = Image.open(screenshot_path)

        buffered = io.BytesIO()
        screenshot.save(buffered, format="PNG")

        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return img_str
