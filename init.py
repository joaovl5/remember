from gui.api import WindowApi
import gui.init as gui
import asyncio


async def main():
    api = WindowApi("gemma2-9b-it")
    gui.window_init(api=api)
    gui.window_start()


asyncio.run(main())
