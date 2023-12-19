from gui_components.main_window.credentials import setup_credentials
from gui_components.main_window.hostname import setup_sever_add
from gui_components.main_window.icons import APP_ICON
from gui_components.main_window.params import setup_params
import tkinter
from types import FunctionType
from threading import Thread

class App(tkinter.Tk):
    def __init__(self,
                 init_login:str,
                 init_passw:str,
                 init_remember_pasw:bool,
                 onSubmit:FunctionType):
        super().__init__()
        self.init_login = init_login
        self.init_passw = init_passw
        self.init_remember_pasw = init_remember_pasw
        self.onSubmit = onSubmit
        self.thread_results = []


    def render_components(self):
        icon = tkinter.PhotoImage(data=APP_ICON)
        self.title("Перенос ТД")
        self.geometry("250x350")
        self.iconphoto(True, icon)
        self.login_var, self.passw_var=setup_credentials(self, self.init_login, self.init_passw, self.init_remember_pasw)
        self.hostname = setup_sever_add(self)
        self.mac_var,self.esr_var, self.kea_var =  setup_params(self)
        self.submit_btn = tkinter.Button(self, text="Перенести", command=self.handle_submit)
        self.submit_btn.pack()



    def handle_submit(self):
        self.submit_btn.config(state="disabled")
        try:
            self.job_thread = Thread(target=self.onSubmit,args=(self.thread_results,) )
            self.job_thread.start()
            self.check_thread_results()
        except Exception as e:
            print(e)
            self.submit_btn.config(state="normal")


    def on_job_finish(self):
        print("закончено")
        self.submit_btn.config(state="normal")


    def check_thread_results(self):
        if  self.job_thread.is_alive():
            self.after(200, self.check_thread_results)
        else:
            self.on_job_finish()


    # def check_result(self):
    #     if thread.is_alive():
    #         self.after(100, lambda: self.check_thread(thread))
    #     else:
    #         self.submit_btn.config(state="normal")
    #         print(self.ssh_results)