from tkinter import *
from PIL import Image, ImageFont, ImageDraw
from tkinter import filedialog
 

def upload_image():
    global image, w, h, watermark_image, bt_text, bt_img
    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    w, h = image.size
    watermark_image = image.copy()

    b1.destroy()
    bt_text = Button(text="Text Watermark", command=text_watermark)
    bt_text.grid(row=1, column=0)
    bt_img = Button(text="Image Watermark", command=img_watermark)
    bt_img.grid(row=1, column=1)


def text_watermark():
    bt_text.destroy()
    bt_img.destroy()

    bt_white = Button(text="White Watermark", command= lambda: color_text_watermark("white"))
    bt_white.grid(row=1, column=0)

    bt_black = Button(text="Black Watermark", command= lambda: color_text_watermark("black"))
    bt_black.grid(row=1, column=1)


def color_text_watermark(color):
    draw = ImageDraw.Draw(watermark_image)

    x, y = int(w / 2), int(h / 2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x
    font = ImageFont.truetype("MoonDance-Regular.ttf", int(font_size/6))

    if color == "black":  
        draw.text((x, y), "puppy", fill=(0, 0, 0), font=font, anchor='ms')
    elif color == "white":
        draw.text((x, y), "puppy", fill=(255, 255, 255), font=font, anchor='ms')
    
    watermark_image.save(filedialog.asksaveasfilename(defaultextension=".png"), "PNG")
    watermark_image.show()
    window.destroy()


def img_watermark():
    global watermark, bt_img, bt_text
    bt_text.destroy()
    bt_img.destroy()

    filename = filedialog.askopenfilename()
    watermark = Image.open(filename)

    bt_text = Button(text="Crop Watermark?", command=crop_watermark)
    bt_text.grid(row=1, column=0)
    bt_img = Button(text="Don't Crop", command=add_watermark)
    bt_img.grid(row=1, column=1)


def crop_watermark():
    crop_watermark = watermark.copy()
    crop_watermark.thumbnail((200, 200))

    watermark_image.paste(crop_watermark, (int(w/2), int(h/2)))
    watermark_image.save(filedialog.asksaveasfilename(defaultextension=".png"), "PNG")
    watermark_image.show()
    window.destroy()


def add_watermark():
    watermark_image.paste(watermark, (0, 0))
    watermark_image.save(filedialog.asksaveasfilename(defaultextension=".png"), "PNG")
    watermark_image.show()
    window.destroy()


# GUI
window = Tk()

window.title("Watermarker")
window.config(padx=50, pady=50, bg="white")

title = Label(text="Watermarker", bg="white", font=("lucida", 50, ("bold", "italic")))
title.grid(row=0, column=0, columnspan=2)

b1 = Button(text='Upload Image', command = upload_image)
b1.grid(row=1,column=0, columnspan=2) 

window.mainloop()