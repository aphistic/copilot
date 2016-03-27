from tkinter import Toplevel
from tkinter.ttk import Frame, Button

from copilot.frame import CopilotMainFrame
from copilot.file_server import FileServerFrame
from copilot.copy_from import CopyFromFrame
from copilot.options import OptionsFrame

class HomeFrame(CopilotMainFrame):
    def __init__(self, master, config):
        super(HomeFrame, self).__init__(master, config)

        self.copy_btn = Button(
            self._master,
            text='Copy Files',
            command=self._new_window(CopyFromFrame)
        )
        self.copy_btn.grid(row=0, column=0)

        self.copy_btn = Button(
            self._master,
            text='Upload Files',
            command=self._new_window(FileServerFrame)
        )
        self.copy_btn.grid(row=1, column=0)

        self.quit_btn = Button(
            self._master,
            text='Quit',
            command=self._cmd_quit
        )
        self.quit_btn.grid(row=2, column=0)

    def _cmd_quit(self):
        self._master.destroy()
