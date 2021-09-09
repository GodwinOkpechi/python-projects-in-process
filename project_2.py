from pytube import YouTube
from playsound import playsound
import tkinter as tk

width=550
height=150
title='CodeX Youtube downloader'
button_sound='click'

class YoutubeDownloader:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry('{}x{}'.format(width,height))
        self.window.configure(by='#29211#')
        self.window.title(title)

        self.link_label=tk.Label(self.window,text='Paste Download Link')
        self.link_label.grid(column=0,row=0)
        self.link_label=tk.Label(self.window,text='Save File as')
        self.link_label.grid(column=0,row=1)
        self.link_label=tk.Label(self.window,text='Save File Path')
        self.link_label.grid(column=0,row=2)

    def run_app(self):
        self.window.mainloop()
        return
if __name__=="__main__":
    app=YoutubeDownloader()
    app.run_app()