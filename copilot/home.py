from tkinter import Toplevel
from tkinter.ttk import Frame, Button

from copilot.file_server import FileServerFrame
from copilot.select_device import SelectDeviceFrame
from copilot.options import OptionsFrame


class HomeFrame(Frame):
    def __init__(self, master):
        super(HomeFrame, self).__init__(master)
        self.master = master

        self.copy_btn = Button(
            self.master,
            text='Copy Files',
            command=self._cmd_copy
        )
        self.copy_btn.grid(row=0, column=0)

        self.quit_btn = Button(
            self.master,
            text='Quit',
            command=self._cmd_quit
        )
        self.quit_btn.grid(row=1, column=0)

    def _cmd_copy(self):
        new_window = Toplevel(self.master)
        app = SelectDeviceFrame(new_window)

    def _new_window(self):
        self.new_window = Toplevel(self.master)
        #self.app = OptionsFrame(self.new_window)
        self.app = FileServerFrame(self.new_window)

    def _cmd_quit(self):
        self.master.destroy()
