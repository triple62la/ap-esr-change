import tkinter as tk
from tkinter import ttk
from storage import app_storage
from ..fixed_entry import FixedEntry

def format_mac(mac:str)->str:
    return "".join(map(lambda let:let.lower(), mac))


def setup_params(app):

    def handle_mac_input(evt:tk.Event):
        mac = mac_input.get()
        mac = format_mac(mac)
        mac_input.delete(0,tk.END)
        mac_input.insert(0, mac)



    mac_var= tk.StringVar(app, value="")
    esr_var=tk.StringVar(app, value="")
    kea_var=tk.StringVar(app, value="kea-msk")
    frame = tk.Frame(app, borderwidth=1, relief=tk.SOLID, padx=10, pady=10)
    #title
    tk.Label(frame, text="Параметры переноса ТД").grid(column=0, row=0, columnspan=2, pady=10)
    #mac
    tk.Label(frame, text="mac").grid(column=0, row=1)
    mac_input = FixedEntry(frame, textvariable=mac_var )
    mac_input.grid(column=1, row=1)
    mac_input.bind("<KeyRelease>", handle_mac_input)

    #esr
    tk.Label(frame, text="ESR").grid(column=0, row=2)
    FixedEntry(frame, textvariable=esr_var).grid(column=1, row=2)
    #cluster
    tk.Label(frame, text="clustername").grid(column=0, row=3)
    ttk.Combobox(frame,
                 state="readonly",
                 values=["kea-msk", "kea-nvs"],
                 textvariable=kea_var,
                 width=17
                 ).grid(column=1, row=3)

    frame.pack()
    return mac_var, esr_var, kea_var