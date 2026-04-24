import requests

def GetHyrule(compendium):
    response = requests.get(f'https://botw-compendium.herokuapp.com/api/v3/compendium/entry/{compendium.lower()}')
    if response.status_code != 200:
        print ('Error fetching data')
        return None

    data = response.json()
    return data

import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Hyrule Compendium") 
window.geometry("1200x900") 
window.resizable(False, False) 
# window.configure(bg='#716fc2')

from tkinter import font
import pyglet
import os
# font_path = os.path.join(os.path.dirname(__file__), 'totk.ttf')
# pyglet.font.add_file(font_path)
# totk_font_family = "The Legend of Zelda"
# custom_font = font.Font(family=totk_font_family)

prompt = tk.Label(window, text="Input Name or ID", 
font=("Arial", 14))
prompt.place(y=10, x=150) 
entry = tk.Entry(window, font=("Arial", 14), width=40)
entry.place(x=20,y=52)

name_label = tk.Label(window, text="", font=("Custom_Font", 20),
fg="black")
name_label.pack(pady=100)

description_label = tk.Label(window, text="", font=("Arial", 13,),
fg="black", wraplength=600,)
description_label.place(x=530, y=155)

Category_label = tk.Label(window, text="", font=("Arial", 20, "bold"),
fg="black")
Category_label.place(x=800, y=52)

image_label = tk.Label(window)
image_label.place(x=50, y=150)

def get_reply():
    # print(entry.get)
    hyrule = GetHyrule(entry.get())
    name_label.config(text= (hyrule['data']['name'], hyrule['data']['id']))
    description_label.config(text= (hyrule['data']['description']))
    Category_label.config(text= (hyrule['data']['category']))
 
    from io import BytesIO
    img_url = hyrule['data']['image']
    response = requests.get(img_url)
    pil_image = Image.open(BytesIO(response.content))
    pil_image = pil_image.resize((450, 450))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=tk_image)
    image_label.image = tk_image

    # print (hyrule)

    # print(hyrule['data']['category'])
    # print(hyrule['data']['description'])

enter_button = tk.Button(window, text="⌕",
font=("Arial", 14),

command=get_reply)

enter_button.place(x=480, y=45)
window.mainloop()