import tkinter as tk
from PIL import Image, ImageTk
import cv2
import utils.constants


class MainWindow:
    def __init__(self, window, canvas, img_bg):
        self.window = window
        self.canvas = canvas
        self.img_bg = img_bg
        self.cap = cv2.VideoCapture(self.img_bg)
        self.speed = 20  # Interval in ms to get the latest frame
        self.y = 20
        self.update_image()

    def update_image(self):
        try:
            self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)  # to RGB
            self.image = Image.fromarray(self.image)  # to PIL format
            self.image = ImageTk.PhotoImage(self.image)  # to ImageTk format
            self.frame = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
            self.canvas.tag_lower(self.frame)
            self.window.after(self.speed, self.update_image)
        except:
            MainWindow(utils.constants.statistics_club_window, utils.constants.statistics_club_canvas, self.img_bg)

