import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, Label
from PIL import Image, ImageTk, ImageFont, ImageDraw
import PIL
import matplotlib as plt

window = tk.Tk()
window.geometry = ("560x800")

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

path = "/Users/danielnyakas/projects/4. watermarking gui/PNG image.png"


def imageUploader():
    global edit
    img = Image.open(path)
    canvas.image = pic = ImageTk.PhotoImage(img)
    edit = canvas.create_image(250, 250, anchor=tk.CENTER, image=canvas.image)
    window.update()
    print(path, img, pic)
    # rendered = canvas.create_image(250, 250, anchor=tk.CENTER, image=pic)
    # print(rendered)


def imgChanger():
    global edit
    path = "/Users/danielnyakas/projects/4. watermarking gui/Screenshot 2022-09-05 at 20.50.30.jpg"

    img = Image.open(path)
    canvas.a = ImageTk.PhotoImage(img)
    canvas.itemconfig(edit, image=canvas.a)
    canvas.pack()
    # rendered = canvas.create_image(250, 250, anchor=tk.CENTER, image=pic)


button = tk.Button(window, text="Show me!!", command=imageUploader).pack()
button2 = tk.Button(window, text="Change me!!", command=imgChanger).pack()

window.mainloop()
