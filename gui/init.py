import webview

from gui.api import WindowApi


class Window:
    def __init__(self, api: WindowApi) -> None:
        self.api = api
        self.window = webview.create_window(
            "Remember",
            url=self.get_entry_point(),
            js_api=self.api,
        )

    def get_entry_point(self) -> str:
        return "http://localhost:9002/"

    def execute_js(self, js: str):
        self.window.evaluate_js(
            js,
        )

    def start(self):
        webview.start(debug=True)
