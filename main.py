import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, Label
from PIL import Image, ImageTk, ImageFont, ImageDraw
import PIL
import matplotlib as plt
import textwrap

window = tk.Tk()
window.title("Supercool Watermarker")
window.geometry = ("560x800")
preview_label = ttk.Label(text="Preview:")
canvas = tk.Canvas(window, width=500, height=500)
name_label = ttk.Label(window, text="Text of your watermark:")
name_input = ttk.Entry(window)

font_size_label = ttk.Label(window, text="Font size:")
font_size_input = ttk.Entry(window, validate="key")


def testVal(inStr, acttyp):
    if acttyp == '1':  # insert
        if not inStr.isdigit():
            return False
    return True


def left(event):
    global x, y, a
    x -= 10
    a = Image.new('RGBA', img.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(a)
    d.text((x, y), wrapped, fill=(255, 255, 255, 100), font=font_used)
    combined = Image.alpha_composite(img, a)
    img_r = combined.resize((450, round(450/ratio)), resample=Image.Resampling.LANCZOS)
    canvas.new_pic = ImageTk.PhotoImage(img_r)
    rendered = canvas.create_image(250, 250, anchor=tk.CENTER, image=canvas.new_pic)


def right(event):
    global x, y, a
    x += 10
    a = Image.new('RGBA', img.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(a)
    d.text((x, y), wrapped, fill=(255, 255, 255, 100), font=font_used)
    combined = Image.alpha_composite(img, a)
    img_r = combined.resize((450, round(450/ratio)), resample=Image.Resampling.LANCZOS)
    canvas.new_pic = ImageTk.PhotoImage(img_r)
    rendered = canvas.create_image(250, 250, anchor=tk.CENTER, image=canvas.new_pic)


def up(event):
    global x, y, a
    y -= 10
    a = Image.new('RGBA', img.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(a)
    d.text((x, y), wrapped, fill=(255, 255, 255, 100), font=font_used)
    combined = Image.alpha_composite(img, a)
    img_r = combined.resize((450, round(450/ratio)), resample=Image.Resampling.LANCZOS)
    canvas.new_pic = ImageTk.PhotoImage(img_r)
    rendered = canvas.create_image(250, 250, anchor=tk.CENTER, image=canvas.new_pic)


def down(event):
    global x, y, a
    y += 10
    a = Image.new('RGBA', img.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(a)
    d.text((x, y), wrapped, fill=(255, 255, 255, 100), font=font_used)
    combined = Image.alpha_composite(img, a)
    img_r = combined.resize((450, round(450/ratio)), resample=Image.Resampling.LANCZOS)
    canvas.new_pic = ImageTk.PhotoImage(img_r)
    rendered = canvas.create_image(250, 250, anchor=tk.CENTER, image=canvas.new_pic)


def imageUploader():
    global pic, img, watermark_image, path, rendered
    fileTypes = [('Image files', "*.png *.jpg *.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)
    preview_label.grid(row=0, column=0, columnspan=2, pady=10)
    canvas.grid(row=1, columnspan=2, column=0, padx=10, pady=5)
    instructions = ttk.Label(text="You can move the watermark with the arrow keyt")
    instructions.grid(row=2, column=0, columnspan=2, pady=10)
    name_label.grid(row=3, column=0, pady=10)
    name_input.grid(row=4, column=0, pady=5)
    font_size_label.grid(row=3, column=1, pady=10)
    font_size_input['validatecommand'] = (font_size_input.register(testVal), '%P', '%d')
    font_size_input.grid(row=4, column=1, pady=5)
    export_button.grid(row=6, column=0, pady=10)
    impressum_label = ttk.Label(window, text="Made by Daniel with <3").grid(row=6, column=1, pady=10)
    button.grid(row=5, column=1, pady=5)

    # if file is selected
    if len(path):
        img = Image.open(path)

        watermark_image = img.copy()

        width, height = img.size
        ratio = width/height
        img_r = watermark_image.resize((450, round(450/ratio)), resample=Image.Resampling.LANCZOS)
        canvas.pic = ImageTk.PhotoImage(img_r)
        try:
            if rendered:
                canvas.delete(rendered)
        except NameError:
            pass
        rendered = canvas.create_image(250, 250, anchor=tk.CENTER, image=canvas.pic)

    # if no file is selected, then we are displaying below message
    else:
        print("No file is chosen !! Please choose a file.")


def print_ou():
    global rendered, x, y, text, wrapped, font_used, img, ratio, txt, d, watermark_image, combined
    img = Image.open(path).convert("RGBA")

    w, h = img.size
    x, y = int(w / 2), int(h / 2)
    ratio = w/h
    watermark_image = img.copy()
    font_used = ImageFont.truetype("Arial.ttf", int(font_size_input.get()))
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))
    wrapped = textwrap.fill(text=name_input.get(), width=10)
    d = ImageDraw.Draw(txt)
    d.text((x, y), wrapped, fill=(255, 255, 255, 100), font=font_used)

    combined = Image.alpha_composite(watermark_image, txt)

    img_r = combined.resize((450, round(450/ratio)), resample=Image.Resampling.LANCZOS)
    canvas.new_pic = ImageTk.PhotoImage(img_r)
    rendered = canvas.create_image(250, 250, anchor=tk.CENTER, image=canvas.new_pic)

    window.bind("<Left>", left)
    window.bind("<Right>", right)
    window.bind("<Up>", up)
    window.bind("<Down>", down)


def save():
    file = filedialog.asksaveasfile(mode='wb')
    if file:
        combined = Image.alpha_composite(img, a)
        combined.save(file)
        # Image.SAVE(combined)  # saves the image to the input file name.


button = tk.Button(window, text="Watermark me!!", command=print_ou)

export_button = tk.Button(window, text="Export me!!", command=save)

uploadButton = tk.Button(window, text="Locate Image", command=imageUploader)
uploadButton.grid(row=5, column=0, pady=20)

window.mainloop()
