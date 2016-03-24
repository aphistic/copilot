from tkinter import Listbox
from tkinter.ttk import Frame, Button, Label
from tkinter.font import Font

from copilot.usbdevices import usb_drives

class SelectDeviceFrame(Frame):
    def __init__(self, master):
        super(SelectDeviceFrame, self).__init__(master)
        self.master = master

        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.back_btn = Button(
            self.master,
            text='< Back',
            command=self._cmd_back
        )
        self.back_btn.grid(row=0, column=0, sticky='w')

        self.frame_lbl = Label(
            self.master,
            text='Copy To Device',
            anchor='center'
        )
        self.frame_lbl.grid(row=0, column=1, sticky='ew')

        self.next_btn = Button(
            self.master,
            text='Next >'
        )
        self.next_btn.grid(row=0, column=2, sticky='e')

        self._dev_list = Listbox(self.master, font=Font(size=20))
        self._dev_list.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self._refresh_drives()

    def _refresh_drives(self):
        for drive in usb_drives():
            self._dev_list.insert('end', drive)

    def _cmd_back(self):
        self.master.destroy()
