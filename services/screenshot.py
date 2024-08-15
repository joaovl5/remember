from threading import Thread
from urllib.parse import urlparse
from concurrent.futures import Future
import asyncio
import dbus
import dbus.mainloop.glib
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from PIL import Image
import functools


def dbus_screencap():
    loop = GLib.MainLoop()
    loop.run()


def load_image_from_uri(uri: str) -> Image.Image:
    # Parse the URI to get the path
    parsed_uri = urlparse(uri)

    # Construct the file path
    file_path = parsed_uri.path

    # Open and return the image using Pillow
    return Image.open(file_path)


class ScreenshotService:
    def __init__(self) -> None:
        self.platform = "wayland"
        self.loop = asyncio.get_running_loop()
        match self.platform:
            case "wayland" | "x11":
                self.start_dbus_thread()

    def handle_dbus_screenshot(self, response, results, object_path, loop):
        uri = results["uri"]
        image = load_image_from_uri(uri)
        asyncio.run_coroutine_threadsafe(self.handle_dbus_callback(image), loop)

    async def handle_dbus_callback(self, img):
        self.future.set_result(img)
        self.event.set()

    def start_dbus_thread(self) -> None:
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus = dbus.SessionBus()
        obj = bus.get_object(
            "org.freedesktop.portal.Desktop", "/org/freedesktop/portal/desktop"
        )
        self.dbus_interface = dbus.Interface(obj, "org.freedesktop.portal.Screenshot")
        bus.add_signal_receiver(
            functools.partial(self.handle_dbus_screenshot, loop=self.loop),
            signal_name="Response",
            dbus_interface="org.freedesktop.portal.Request",
            bus_name="org.freedesktop.portal.Desktop",
            path_keyword="object_path",
        )
        self.dbus_thread = Thread(target=dbus_screencap, daemon=True)
        self.dbus_thread.start()

    async def take_screenshot(self) -> Image.Image:
        if hasattr(self, "dbus_interface"):  # Handle X11/Wayland
            self.future = Future()
            self.event = asyncio.Event()
            self.dbus_interface.Screenshot("", {})

            await self.event.wait()
            return self.future.result()
        else:
            raise Exception()
            return Image.Image()
