from PIL.Image import Image
import pytesseract


class OCRService:
    def __init__(self) -> None:
        pass

    def recognize_image(self, image: Image) -> str:
        return pytesseract.image_to_string(image=image)
