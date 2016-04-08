from tkinter import Listbox

from copilot.copy_state import CopyState
from copilot.device_to import DeviceToFrame
from copilot.frame import CopilotInnerFrame
from copilot.usbdevices import usb_drives

class DriveOption(object):
    def __init__(self, drive, part):
        self._drive = drive
        self._part = part

        self._parts = []

    def __str__(self):
        return '{} ({})'.format(self._drive, self._part)

    def drive(self):
        return self._drive

    def part(self):
        return self._part

class SelectDeviceFrame(CopilotInnerFrame):
    def __init__(self, master, config):
        super(SelectDeviceFrame, self).__init__(master, config)

        self._frame_lbl['text'] = 'Copy To Device'

        self._next_btn['command'] = self._next_cmd

        self._dev_list = Listbox(self._master, font=self._config.item_font)
        self._dev_list.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self._refresh_drives()

    def _next_cmd(self):
        if len(self._dev_list.curselection()) > 0:
            item_idx = int(self._dev_list.curselection()[0])
            state = CopyState()
            state.to_device = self._parts[item_idx]
            self._new_state_window(DeviceToFrame, state)

    def _refresh_drives(self):
        self._parts = []
        for drive in usb_drives():
            for part in drive.partitions():
                drive_opt = DriveOption(drive, part)
                self._parts.append(drive_opt)
                self._dev_list.insert('end', drive_opt)
