from tkinter import Listbox

from copilot.frame import CopilotInnerFrame
from copilot.usbdevices import usb_drives

class SelectDeviceFrame(CopilotInnerFrame):
    def __init__(self, master, config):
        super(SelectDeviceFrame, self).__init__(master, config)

        self._frame_lbl['text'] = 'Copy To Device'

        self._dev_list = Listbox(self._master, font=self._config.item_font)
        self._dev_list.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self._refresh_drives()

    def _refresh_drives(self):
        for drive in usb_drives():
            self._dev_list.insert('end', drive)
