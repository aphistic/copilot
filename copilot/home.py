from tkinter import Toplevel
from tkinter.ttk import Frame, Button

from copilot.options import OptionsFrame
from copilot.file_server import FileServerFrame


class HomeFrame(Frame):
    def __init__(self, master):
        super(HomeFrame, self).__init__(master)
        self.master = master

        self.button1 = Button(
            self,
            text='New Window',
            width=25,
            command=self._new_window)
        self.button1.pack()
        self.button2 = Button(
            self,
            text='Quit',
            width=25,
            command=self._close)
        self.button2.pack()
        self.pack()

    def _new_window(self):
        self.new_window = Toplevel(self.master)
        #self.app = OptionsFrame(self.new_window)
        self.app = FileServerFrame(self.new_window)
        print('after options')

    def _close(self):
        self.master.destroy()
