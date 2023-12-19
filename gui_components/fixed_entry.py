import tkinter as tk
import clipboard


class FixedEntry(tk.Entry):
    """Класс исправляющий баг с неработающими сочетаниями клавиш в Entry на русской раскладке"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Control-KeyPress>",self._keypress)

    def _keypress(self, e: tk.Event):
        if e.keycode == 86 and e.keysym != 'v':
            if self.selection_present():
                self.delete(tk.SEL_FIRST,tk.SEL_LAST)
            self.insert(tk.INSERT,clipboard.paste())
        elif e.keycode == 67 and e.keysym != 'c':
            if self.selection_present():
                clipboard.copy(self.selection_get())
        elif e.keycode == 88 and e.keysym != 'x':
            if self.selection_present():
                clipboard.copy(self.selection_get())
                self.delete(tk.SEL_FIRST,tk.SEL_LAST)