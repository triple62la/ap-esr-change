from ssh_api import change_esr
import tkinter

out, err = change_esr(username="rakhimzhon.dovidov@sys.local",
                                   passw="f;DB;S7;1QL!Ow8",
                                   hostname="10.62.18.110",
                                   mac="a8:f9:4b:b5:6f:00",
                                   esr="wifi-cnt-esr08",
                                   core_at="kea-msk"
)

for line in out:
    print(line)
for line in err:
    print(line)

app = tkinter.Tk()
