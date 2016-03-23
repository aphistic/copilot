from flask import Flask, request, render_template
from http.client import HTTPConnection
from pathlib import Path
from threading import Thread
from tkinter import Toplevel
from tkinter.ttk import Frame, Button, Label
from werkzeug import secure_filename
import logging
import os.path
import socket
import time

from copilot.options import OptionsFrame

#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

class FileServerFrame(Frame):
    def __init__(self, master):
        super(FileServerFrame, self).__init__(master)
        self.master = master

        self.quit_button = Button(
            self.master,
            text='< Back',
            command=self._close_window)
        self.quit_button.grid(row=0, column=0, sticky='w')

        http_addr = 'http://{}:{}'.format(socket.gethostbyname(socket.gethostname()), 4000)
        Label(self.master, text=http_addr, background='red', anchor='center').grid(row=1, column=0, columnspan=2, sticky='ew')

        self.server = FileServer(4000)
        self.server.start()

    def _close_window(self):
        self.server.stop()
        self.server.join(timeout=5)
        self.master.destroy()

class FileServer(Thread):
    def __init__(self, port):
        super(FileServer, self).__init__()
        self.root_path = '/home/aphistic/tmp'
        self.port = port

    def run(self):
        app = Flask(__name__)
        app.config['ROOT_PATH'] = self.root_path

        @app.route('/', methods=['GET', 'POST'])
        def home():
            if request.method == 'POST':
                print('got post')
                f = request.files['file']
                if f:
                    print('got file')
                    fname = secure_filename(f.filename)
                    print('fname {}'.format(fname))
                    fpath = os.path.join(app.config['ROOT_PATH'], fname)
                    print('saving {} in {}'.format(fpath, os.path.dirname(fpath)))
                    f.save(fpath)
            elif request.method == 'DELETE':
                print('deleting')

            web_path = request.args.get('path') or ''
            actual_path = os.path.join(app.config['ROOT_PATH'], web_path)
            path = Path(actual_path)
            dirs = {n.name: os.path.join(web_path, n.name) for n in path.iterdir() if n.is_dir()}
            files = {n.name: os.path.join(web_path, n.name) for n in path.iterdir() if n.is_file()}

            return render_template("home.html",
                current_dir=web_path,
                parent_dir=os.path.dirname(web_path),
                dirs=dirs,
                files=files)

        @app.route('/shutdown')
        def shutdown():
            request.environ.get('werkzeug.server.shutdown')()

        app.run(host='0.0.0.0', port=self.port, debug=True)

    def stop(self):
        client = HTTPConnection('localhost', port=self.port)
        client.request('GET', '/shutdown')