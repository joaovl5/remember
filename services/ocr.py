from PIL.Image import Image
import pytesseract


def recognize_image(image: Image) -> str:
    return pytesseract.image_to_string(image=image)
