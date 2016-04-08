from tkinter import Toplevel
from tkinter.ttk import Frame, Button

from copilot.frame import CopilotMainFrame
from copilot.file_server import FileServerFrame
from copilot.select_device import SelectDeviceFrame
from copilot.options import OptionsFrame

class HomeFrame(CopilotMainFrame):
    def __init__(self, master, config):
        super(HomeFrame, self).__init__(master, config)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        self.copy_btn = Button(
            self._master,
            text='Copy Files',
            command=self._new_window_cb(SelectDeviceFrame)
        )
        self.copy_btn.grid(row=0, column=0, sticky='snew')

        self.copy_btn = Button(
            self._master,
            text='Upload Files',
            command=self._new_window_cb(FileServerFrame)
        )
        self.copy_btn.grid(row=1, column=0, sticky='snew')

        self.quit_btn = Button(
            self._master,
            text='Quit',
            command=self._cmd_quit
        )
        self.quit_btn.grid(row=2, column=0, sticky='snew')

    def _cmd_quit(self):
        self._master.destroy()
