from tkinter import Tk
from copilot.home import HomeFrame

root = Tk()
# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# print('w: {}, h: {}'.format(w, h))
# root.overrideredirect(1)
# root.geometry("%dx%d+0+0" % (w, h))
root.title('copilot')
app = HomeFrame(root)
root.mainloop()
