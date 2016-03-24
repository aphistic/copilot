from tkinter import Tk
from copilot.home import HomeFrame
from copilot.select_device import SelectDeviceFrame
from copilot.file_server import FileServer
import argparse
import logging

log = logging.getLogger()
log.setLevel(logging.ERROR)

parser = argparse.ArgumentParser(description='Run stuff')
parser.add_argument('--server', action='store_true', default=False)
parser.add_argument('--debug', action='store_true', default=False)

args = parser.parse_args()

if args.debug:
    log.setLevel(logging.DEBUG)

if args.server:
    fs = FileServer(4000)
    fs.run(debug=True)
else:
    root = Tk()

    # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    # print('w: {}, h: {}'.format(w, h))
    # root.overrideredirect(1)
    # root.geometry("%dx%d+0+0" % (w, h))

    root.title('copilot')
    app = HomeFrame(root)
    #app = SelectDeviceFrame(root)
    root.mainloop()

    from copilot.usbdevices import usb_drives
    for drive in usb_drives():
        print('{}'.format(drive))
        print('size: {}GB'.format(drive.size('g')))
        print('path: {}'.format(drive.path()))
        print('vendor: {}'.format(drive.vendor()))
        print('model: {}'.format(drive.model()))
        print('partitions:')
        for p in drive.partitions():
            print('  {}: {}'.format(p.path(), p.type()))
        print('')
