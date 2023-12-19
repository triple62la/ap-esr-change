import tkinter as tk
from threading import Thread
from ssh_api import change_esr
class ProgressWindow(tk.Toplevel):

    def __init__(self,job_params,on_job_finish,  *args):
        super().__init__(*args)
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.title("Ход выполнения")
        self.geometry(f"800x400+{int(x)}+{int(y) - 200}")
        self.text = tk.Text(self, state=tk.DISABLED, width=800)
        self.text.pack()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.focus_set()
        self.job_params = job_params
        self.job_params["output_handler"] = self.add_line
        self.on_job_finish = on_job_finish
    def add_line(self, line: str):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END, line + "\n")
        self.text.config(state=tk.DISABLED)

    def on_close(self):
        if self.job_thread.is_alive():
            result = tk.messagebox.askquestion("Незавершенная задача",
                                               "Закрытие данного окна до завершения задачи НЕ ПРИВЕДЕТ "
                                               "к прекращению текущего переноса ТД, а так же вызовет закрытие основного окна"
                                               " желаете ли продолжить? ")
            if result == "yes":
                self.destroy()
                self.master.destroy()
            else:
                return
        else:
            self.destroy()
    def start_job(self):
        try:
            self.job_thread = Thread(target=change_esr,kwargs=self.job_params, daemon=True)
            self.job_thread.start()
            self.check_thread_results()
        except Exception as e:
            progress_window.add_line(f"Произошла ошибка {e}")
            self.submit_btn.config(state="normal")

    def check_thread_results(self):
        if self.job_thread.is_alive():
            self.after(200, self.check_thread_results)
        else:
            self.on_job_finish()