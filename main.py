import tkinter

from PIL import ImageFont, ImageDraw, ImageTk, Image
from tkinter import Tk, Entry, Button


def watermark_adder(clean_image, size: int, watermark_text: str):
    with Image.open(clean_image).convert("RGBA") as im:
        txt = Image.new('RGBA', im.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype("SourceSansPro-Bold.ttf", size=size)
        d = ImageDraw.Draw(txt)
        d.text((0, 0), watermark_text, font=fnt, fill=(255, 255, 255, 128))
        out = Image.alpha_composite(im, txt)
        out.show()


window = Tk()
window.title("Watermark Adder")


def get_data():
    text = entry.get()
    watermark_adder(text, 800, watermark_text="Your name")


img_canvas = tkinter.Canvas()
img_canvas.grid(padx=0, pady=0)
entry = Entry(window)
img_canvas.create_window(200, 140, window=entry)
create_button = Button(window, text="Create", command=get_data)
create_button.grid(padx=1, pady=1)
window.mainloop()
