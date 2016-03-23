from tkinter import Tk
from copilot.home import HomeFrame
from copilot.file_server import FileServer
import argparse

parser = argparse.ArgumentParser(description='Run stuff')
parser.add_argument('--server', action='store_true', default=False)
parser.add_argument('--debug', action='store_true', default=False)

args = parser.parse_args()
print(args)


if args.server:
    fs = FileServer(4000)
    fs.run()
else:
    root = Tk()
    # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    # print('w: {}, h: {}'.format(w, h))
    # root.overrideredirect(1)
    # root.geometry("%dx%d+0+0" % (w, h))
    root.title('copilot')
    app = HomeFrame(root)
    root.mainloop()
