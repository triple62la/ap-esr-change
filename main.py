import asyncio
import time

from ssh_api import change_esr
import base64
from async_tkinter_loop import async_mainloop
from gui_components.main_window.main_window import App
from storage import app_storage


# out, err = change_esr(username="rakhimzhon.dovidov@sys.local",
#                                    passw="f;DB;S7;1QL!Ow8",
#                                    hostname="10.62.18.110",
#                                    mac="a8:f9:4b:b5:6f:00",
#                                    esr="wifi-cnt-esr08",
#                                    core_at="kea-msk"
# )
#
# for line in out:
#     print(line)
# for line in err:
#     print(line)

def test(result:list):
    print("Спу")
    time.sleep(5)
    print("Поспал")
    raise ZeroDivisionError
    result.append(54)


app = App(init_login=app_storage.read("login", default=""),
               init_passw=app_storage.read("password", default=""),
               init_remember_pasw=app_storage.read("remember_passw", default=False),
               onSubmit=test)
app.render_components()

if __name__ == "__main__":

    app.mainloop()