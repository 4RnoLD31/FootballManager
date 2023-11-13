import cv2
import tkinter as tk
import utils.constants as const
from PIL import Image, ImageTk


class PlayVideo:
    def __init__(self, window, canvas, picture, speed=20, first=False):
        self.window = window
        self.canvas = canvas
        self.picture = picture
        self.cap = cv2.VideoCapture(self.picture)
        self.speed = speed
        self.first = first
        self.window.protocol("WM_DELETE_WINDOW", self.__destroy__)
        self.update_image()

    def update_image(self):
        try:
            self.clear()
            if self.picture not in const.used_in_video.keys() or self.first:
                self.first = True
                const.used_in_video[self.picture] = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)))
            self.window = self.canvas.create_image(0, 0, anchor=tk.NW, image=const.used_in_video[self.picture])
            self.canvas.tag_lower(self.window)
            self.window.after(self.speed, self.update_image)
        except:
            self.clear()
            self.__init__(self.window, self.canvas, self.picture, first=self.first)

    def clear(self):
        try:
            self.canvas.delete(self.window)
        except:
            pass

    def __destroy__(self):
        if self.first:
            del const.used_in_video[self.picture]
        self.canvas.destroy()
        self.window.destroy()
        del self
