import multiprocessing.pool
import sys
import tkinter.messagebox

from gui_components.main_window.credentials import setup_credentials
from gui_components.main_window.hostname import setup_sever_add
from gui_components.main_window.icons import APP_ICON
from gui_components.main_window.params import setup_params
from ..job_progress.progres_window import ProgressWindow
import tkinter
from types import FunctionType



class App(tkinter.Tk):
    def __init__(self,
                 init_login:str,
                 init_passw:str,
                 init_remember_pasw:bool,
                 ):
        super().__init__()
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.title("Перенос ТД")
        self.geometry(f"250x320+{int(x)}+{int(y) - 200}")
        self.init_login = init_login
        self.init_passw = init_passw
        self.init_remember_pasw = init_remember_pasw
        self.thread_results = []
        self.terminate_flag=False

    def render_components(self):
        icon = tkinter.PhotoImage(data=APP_ICON)

        self.iconphoto(True, icon)
        self.login_var, self.passw_var=setup_credentials(self, self.init_login, self.init_passw, self.init_remember_pasw)
        self.hostname = setup_sever_add(self)
        self.mac_var,self.esr_var, self.kea_var =  setup_params(self)
        self.submit_btn = tkinter.Button(self, text="Перенести", command=self.handle_submit)
        self.submit_btn.pack(pady=10)



    def handle_submit(self):
        self.submit_btn.config(state="disabled")
        kwds = self.gather_job_kwargs()
        validation_res = self.validate_params(kwds)
        if not validation_res["isValid"]:
            tkinter.messagebox.showwarning("Валидация полей",validation_res["msg"])
            self.submit_btn.config(state="normal")
            return
        progress_window = ProgressWindow(job_params=kwds, on_job_finish=self.on_job_finish)
        progress_window.start_job()

    def gather_job_kwargs(self):

        return {"username":self.login_var.get(),
                "passw":self.passw_var.get(),
                "hostname":self.hostname.get(),
                "mac":self.mac_var.get(),
                "esr":self.esr_var.get(),
                "core_at":self.kea_var.get(),
                }

    def validate_params(self, job_kwargs:dict):
        username = job_kwargs.get("username", "")
        if not username.endswith("@sys.local"):
            return {"isValid": False, "msg": f"Логин должен оканчиваться на @sys.local"}
        for key,value in job_kwargs.items():
            if not value:
                return {"isValid": False, "msg": f"Поле {key} не должно быть пустым. Заполните все поля"}
        return {"isValid": True, "msg": None}

    def on_job_finish(self):

        self.submit_btn.config(state="normal")

    def copy(self, event):
        try:
            start = self.index("sel.first")
            end = self.index("sel.last")
        except tk.TclError:
            pass
        else:
            self.clipboard_clear()
            self.clipboard_append(self.get(start, end))

    def paste(self, event):
        try:
            start = self.index("sel.first")
            end = self.index("sel.last")
            self.delete(start, end)
        except tk.TclError:
            pass
        clipboard = self.clipboard_get()
        self.insert("insert", clipboard)







