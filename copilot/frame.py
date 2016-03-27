from tkinter import Toplevel
from tkinter.ttk import Frame, Button, Label

class CopilotBaseFrame(Frame):
    def __init__(self, master, config):
        super(CopilotBaseFrame, self).__init__(master)
        self._master = master
        self._config = config

    def _new_window(self, frame_type):
        def _cb(cb_self, cb_type):
            new_window = Toplevel(cb_self._master)
            cb_type(new_window, self._config)

        return lambda: _cb(self, frame_type)

class CopilotMainFrame(CopilotBaseFrame):
    def __init__(self, master, config):
        super(CopilotMainFrame, self).__init__(master, config)


class CopilotInnerFrame(CopilotBaseFrame):
    def __init__(self, master, config):
        super(CopilotInnerFrame, self).__init__(master, config)

        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self._create_header()

        self._next_hidden = False

    def _cmd_back(self):
        self.master.destroy()

    def _create_header(self):
        self.back_btn = Button(
            self._master,
            text='< Back',
            command=self._cmd_back
        )
        self.back_btn.grid(row=0, column=0, sticky='w')

        self._frame_lbl = Label(
            self.master,
            text='',
            anchor='center'
        )
        self._frame_lbl.grid(row=0, column=1, sticky='ew')

        self._next_btn = Button(
            self.master,
            text='Next >'
        )
        self._next_btn.grid(row=0, column=2, sticky='e')

    def _hide_next(self):
        if not self._next_hidden:
            self._next_btn.grid_remove()
            self._next_hidden = True

    def _show_next(self):
        if self._next_hidden:
            self._next_btn.grid(row=0, column=2, sticky='e')
            self._next_hidden = False
