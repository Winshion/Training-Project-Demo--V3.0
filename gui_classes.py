import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd


"""
写label类，canvas类，button类和entry类
"""


class wslabel:
    # 文本标签类
    def __init__(self, master, text, font=("华文中宋", 10), x=0, y=0):
        self.master = master
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.lbl = tk.Label(master=self.master, text=self.text, font=self.font)

    def place(self):
        self.lbl.place(x=self.x, y=self.y)


class wsbutton:
    # 按钮类
    def __init__(self, master, text, font=("华文中宋", 10), height=1, width=2, x=0, y=0, bg="#efefef"):
        self.master = master
        self.text = text
        self.font = font
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.btn = tk.Button(master=self.master, text=self.text, font=self.font, bg=bg)

    def place(self):
        self.btn.place(x=self.x, y=self.y)
        self.btn.configure(width=self.width, height=self.height)

    def trigger(self, func_name):
        """
        用于绑定按钮的鼠标点击事件
        """
        self.btn.bind('<ButtonRelease-1>', func_name)


# wscanvas类的两个需要全局引用的变量的声明
# ttk中的create函数需要持续引用才能实现展示图片
cloudimage = None
cloudim = None


class wscanvas:
    # 画布类            父界面    高度    宽度   放置x 放置y
    def __init__(self, master, height, width, x=0, y=0):
        self.master = master
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.canvas = tk.Canvas(master=self.master, width=self.width, height=self.height,
                                bg='#ffffff')

    def place(self):
        self.canvas.place(x=self.x, y=self.y)

    def forget(self):
        self.canvas.forget()

    def show_image(self, abs_path):
        global cloudimage
        global cloudim
        self.canvas.delete("all")
        cloudimage = Image.open(abs_path)
        cloudim = ImageTk.PhotoImage(cloudimage)
        self.canvas.create_image(455, 250, image=cloudim)


class wsentry:
    def __init__(self, master, x, y):
        self.master = master
        self.x = x
        self.y = y
        self.text = tk.StringVar()
        self.entry = tk.Entry(master=self.master, textvariable=self.text)

    def place(self):
        self.entry.place(x=self.x, y=self.y)

    def get_text(self):
        return self.text.get()
