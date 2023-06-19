# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:00:08 2023

@author: joshu
"""

from flask import Flask
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = Flask(__name__)

class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(f'Event type: {event.event_type}, Path: {event.src_path}')

@app.route('/')
def index():
    return 'Flask Watchdog Example'

if __name__ == '__main__':
    observer = Observer()
    event_handler = MyEventHandler()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    app.run(debug=True)
