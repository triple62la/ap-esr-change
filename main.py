import asyncio
import time
from ssh_api import change_esr
import base64
from async_tkinter_loop import async_mainloop
from gui_components.main_window.main_window import App
from storage import app_storage
from types import FunctionType

app = App(init_login=app_storage.read("login", default=""),
          init_passw=app_storage.read("password", default=""),
          init_remember_pasw=app_storage.read("remember_passw", default=False))
app.render_components()

if __name__ == "__main__":
    app.mainloop()
