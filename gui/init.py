import webview

from gui.api import WindowApi


def window_init(api: WindowApi) -> None:
    global window
    window = webview.create_window(
        "Remember",
        url=get_entry_point(),
        js_api=api,
    )


def get_entry_point() -> str:
    return "http://localhost:9002/"


def execute_js(js: str):
    global window
    window.evaluate_js(
        js,
    )


def window_start():
    webview.start(debug=True)
