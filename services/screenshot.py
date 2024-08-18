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


def init():
    global loop
    platform = "wayland"
    loop = asyncio.get_running_loop()
    match platform:
        case "wayland" | "x11":
            start_dbus_thread()


def handle_dbus_screenshot(response, results, object_path, loop):
    uri = results["uri"]
    image = load_image_from_uri(uri)
    asyncio.run_coroutine_threadsafe(handle_dbus_callback(image), loop)


async def handle_dbus_callback(img):
    global future, event
    future.set_result(img)
    event.set()


def start_dbus_thread() -> None:
    global dbus_interface
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    obj = bus.get_object(
        "org.freedesktop.portal.Desktop", "/org/freedesktop/portal/desktop"
    )
    dbus_interface = dbus.Interface(obj, "org.freedesktop.portal.Screenshot")
    bus.add_signal_receiver(
        functools.partial(handle_dbus_screenshot, loop=loop),
        signal_name="Response",
        dbus_interface="org.freedesktop.portal.Request",
        bus_name="org.freedesktop.portal.Desktop",
        path_keyword="object_path",
    )
    dbus_thread = Thread(target=dbus_screencap, daemon=True)
    dbus_thread.start()


async def take_screenshot() -> Image.Image:
    global future, event
    if dbus_interface:  # Handle X11/Wayland
        future = Future()
        event = asyncio.Event()
        dbus_interface.Screenshot("", {})

        await event.wait()
        return future.result()
    else:
        raise Exception()


init()
