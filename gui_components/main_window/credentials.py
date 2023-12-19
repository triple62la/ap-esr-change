import tkinter as tk
from storage import app_storage


def setup_credentials(app, init_login, init_passw, init_remeber_passw):

    def handle_passw_save(evt):

        if remember_passw.get():
            app_storage.write("password", passw_input.get())
        else:
            app_storage.write("password", "")

    def handle_check_click(evt:tk.Event) -> None:

        app_storage.write("remember_passw", not remember_passw.get())
        handle_passw_save(evt)

    def handle_login_save(evt:tk.Event):

        app_storage.write("login", login_input.get())

    login_var = tk.StringVar(app, value=init_login)
    passw_var = tk.StringVar(app, value=init_passw)
    remember_passw = tk.BooleanVar(app, value=init_remeber_passw)
    frame = tk.Frame(app)
    label = tk.Label(frame, text="Авторизация sys.local")
    label.grid(column=0, row=0, columnspan=2)
    login_label= tk.Label(frame, text="Логин")
    login_label.grid(column=0, row=1)
    login_input = tk.Entry(frame, textvariable=login_var)
    login_input.grid(column=1, row=1)
    passw_label = tk.Label(frame, text="Пароль")
    passw_input = tk.Entry(frame, show="*", textvariable=passw_var)
    passw_label.grid(column=0, row=2)
    passw_input.grid(column=1, row=2)
    frame.config(padx=5, pady=10, borderwidth=1, relief=tk.SOLID)
    frame.pack()
    checkbox = tk.Checkbutton(frame, text="Запоминать пароль", variable=remember_passw, onvalue=1, offvalue=0)
    checkbox.grid(column=0, row=3, columnspan=2)
    login_input.bind("<KeyRelease>", handle_login_save)
    passw_input.bind("<KeyRelease>", handle_passw_save)
    checkbox.bind("<Button-1>", handle_check_click)
    return login_var, passw_var

