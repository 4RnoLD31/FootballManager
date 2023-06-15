from tkinter import *
from PIL import Image, ImageTk
import cv2
import utils.constants


class PlayVideo:
    def __init__(self, window, canvas, picture, speed=20):
        self.window = window
        self.canvas = canvas
        self.picture = picture
        self.cap = cv2.VideoCapture(self.picture)
        self.speed = speed
        self.update_image()

    def update_image(self):
        try:
            self.clear()
            self.imageTK = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)))  # to ImageTk format
            self.frame = self.canvas.create_image(0, 0, anchor=NW, image=self.imageTK)
            self.canvas.tag_lower(self.frame)
            self.window.after(self.speed, self.update_image)
        except:
            self.clear()
            PlayVideo(self.window, self.canvas, self.picture)
            del self

    def clear(self):
        try:
            del self.imageTK
            self.canvas.delete(self.frame)
        except:
            pass
