import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, Label
from PIL import Image, ImageTk, ImageFont, ImageDraw
import PIL
import matplotlib as plt

window = tk.Tk()
window.geometry = ("560x800")
ttk.Label(text="Preview:").pack()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()
name_label = ttk.Label(window, text="Teyt of your watermark:").pack()
name_input = ttk.Entry(window)
name_input.pack()


def imageUploader():
    global pic, img, watermark_image, path, rendered
    fileTypes = [('Image files', "*.png *.jpg *.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)

    # if file is selected
    if len(path):
        img = Image.open(path)

        w, h = img.size
        x, y = int(w / 2), int(h / 2)
        watermark_image = img.copy()
        # draw = ImageDraw.Draw(watermark_image)
        font_used = ImageFont.truetype("Arial.ttf", int(int(h/3)))
        draw = ImageDraw.Draw(watermark_image)
        draw.text((x, y), name_input.get(), fill=(255, 255, 255, 128), font=font_used, anchor='ms',)

        width, height = img.size
        ratio = width/height
        img_r = watermark_image.resize((450, round(450/ratio)), resample=Image.Resampling.LANCZOS)
        canvas.pic = ImageTk.PhotoImage(img_r)
        # re-sizing the app window in order to fit picture
        # and buttom
        # window.geometry("560x300")
        rendered = canvas.create_image(250, 250, anchor=tk.CENTER, image=canvas.pic)
        # return a, pic, img_r

    # if no file is selected, then we are displaying below message
    else:
        print("No file is chosen !! Please choose a file.")


def print_ou():
    img = Image.open(path)

    w, h = img.size
    x, y = int(w / 2), int(h / 2)
    ratio = w/h
    watermark_image = img.copy()
    # draw = ImageDraw.Draw(watermark_image)
    font_used = ImageFont.truetype("Arial.ttf", int(int(h/3)))
    draw = ImageDraw.Draw(watermark_image)
    draw.text((x, y), name_input.get(), fill=(255, 255, 255, 128), font=font_used, anchor='ms',)

    img_r = watermark_image.resize((450, round(450/ratio)), resample=Image.Resampling.LANCZOS)

    canvas.new_pic = ImageTk.PhotoImage(img_r)
    canvas.itemconfig(rendered, image=canvas.new_pic)

    # canvas.create_image(250, 250, anchor=tk.CENTER, image=pic)
    # canvas.delete("all")
    # watermark_image = img.copy()
    # ----
    # draw = ImageDraw.Draw(i)
    # font_used = ImageFont.truetype("Arial.ttf", int(int(h/3)))
    # draw.text((x, y), name_input.get(), fill=(255, 255, 255, 128), font=font_used, anchor='ms',)
    # create_image(250, 250, anchor=tk.CENTER, image=pic)


button = tk.Button(window, text="Watermark me!!", command=print_ou).pack()

uploadButton = tk.Button(window, text="Locate Image", command=imageUploader).pack()
# uploadButton.pack(side=tk.BOTTOM, pady=20)

window.mainloop()
