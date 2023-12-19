import tkinter as tk
from storage import app_storage
from ..fixed_entry import FixedEntry
def setup_sever_add(app):

    def handle_input(evt):
        app_storage.write("hostname", hostname_input.get())

    frame = tk.Frame(app)
    hostname_var = tk.StringVar(frame, value=app_storage.read("hostname", default="10.62.18.110"))
    tk.Label(frame, text="Адрес техсервера").grid(column=0, row=0)
    hostname_input = FixedEntry(frame,textvariable=hostname_var, width=15)
    hostname_input.grid(column=1, row=0)
    hostname_input.bind("<KeyRelease>", handle_input)
    frame.pack(padx=5, pady=5)
    return hostname_var