from tkinter.ttk import Treeview, Style
import os

from copilot.frame import CopilotInnerFrame
from copilot.select_device import SelectDeviceFrame
from copilot.utils import sizeof_fmt

class CopyFileFrame(CopilotInnerFrame):
    def __init__(self, master, config):
        super(CopyFileFrame, self).__init__(master, config)

        self._frame_lbl['text'] = 'Copy File'
        self._next_btn['command'] = self._new_window(SelectDeviceFrame)

        self._tree = Treeview(self._master, columns=('size'))
        self._tree.heading('size', text='Size')
        self._tree.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self._populate_tree(self._config.file_root)

    def _populate_tree(self, tree_root):
        def insert_path(tree, path, parent_id):
            dirs = [e for e in os.scandir(path) if e.is_dir()]
            dirs.sort(key=lambda e: e.name)

            for d in dirs:
                dir_name = d.name
                dir_id = '{}-{}'.format(parent_id, dir_name)
                tree.insert(parent_id, 'end', dir_id, text=dir_name, tags=('dir'))
                insert_path(tree, os.path.join(path, dir_name), dir_id)

            files = [e for e in os.scandir(path) if e.is_file()]
            files.sort(key=lambda e: e.name)

            for idx, f in enumerate(files):
                file_name = f.name
                file_id = '{}-{}'.format(parent_id, file_name)
                file_stat = f.stat()
                file_size = sizeof_fmt(file_stat.st_size)

                if idx % 2 == 0:
                    file_bg = 'file_even'
                else:
                    file_bg = 'file_odd'

                tree.insert(
                    parent_id,
                    'end',
                    file_id,
                    text=file_name,
                    tags=('file', file_bg),
                    values=(file_size)
                )

        insert_path(self._tree, self._config.file_root, '')

        tree = self._tree
        tree.tag_configure('dir', font=self._config.item_font)
        tree.tag_configure('file', font=self._config.item_font)
        tree.tag_configure('file_odd', background='light grey')
