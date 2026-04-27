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
window.geometry("1000x900") 
window.resizable(False, False) 
# window.configure(bg='#402B30')

from tkinter import font
import pyglet
import os
#font_path = "The Wild Breath of Zelda.otf"
#pyglet.font.add_file(font_path)
totk_font_family = "The Wild Breath of Zelda"
#custom_font = font.Font(family=totk_font_family)

prompt = tk.Label(window, text="Input Name or ID", 
font=("Arial", 14))
prompt.place(y=10, x=150) 
entry = tk.Entry(window, font=("Arial", 14), width=40)
entry.place(x=20,y=52)

name_label = tk.Label(window, text="", font=( totk_font_family, 20, "bold"),
fg="black")
name_label.place(x=550,y=52)

description_label = tk.Label(window, text="", font=("Arial", 14,),
fg="black", wraplength=400,)
description_label.place(x=530, y=155)

Category_label = tk.Label(window, text="", font=("Arial", 10,),
fg="black")
Category_label.place(x=800, y=800)

image_label = tk.Label(window)
image_label.place(x=50, y=150)

common_locations_label = tk.Label(window, text="", font=("Arial", 20,), 
fg="black")
common_locations_label.place(x=100, y=560)

common_places_label = tk.Label(window, text="", font=("Arial", 14,),
fg="black")
common_places_label.place(x=150, y=620)

Droppable_items_label = tk.Label(window, text="", font=("Arial", 20,), 
fg="black")
Droppable_items_label.place(x=500, y=560)

drops_label = tk.Label(window, text="", font=("Arial", 14,),
fg="black")
drops_label.place(x=520, y=620)

Cooking_effects_label = tk.Label(window, text="", font=("Arial", 20,), 
fg="black")
Cooking_effects_label.place(x=500, y=560)

effects_label = tk.Label(window, text="", font=("Arial", 14,),
fg="black")
effects_label.place(x=520, y=620)

def get_reply():
    # print(entry.get)
    hyrule = GetHyrule(entry.get())
    hyrule_name = hyrule['data']['name'] + " " + str(hyrule['data']['id'])

    name_label.config(text= (hyrule_name))
    description_label.config(text= (hyrule['data']['description']))
    Category_label.config(text= (hyrule['data']['category']))
 
    from io import BytesIO
    img_url = hyrule['data']['image']
    response = requests.get(img_url)
    pil_image = Image.open(BytesIO(response.content))
    pil_image = pil_image.resize((400, 400))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=tk_image)
    image_label.image = tk_image

    common_locations_label.config(text = "Common Locations")
    locations = hyrule['data'].get('common_locations', [])
    if locations == None:
        common_places_label.config(text="".join('No Common Locations'))
    else:
        common_places_label.config(text="\n\n".join(locations))

    if hyrule['data']['category'] == "creatures" or "monster" or "treasure":
        Droppable_items_label.config(text = "Droppable Items")
        drops = hyrule['data'].get('drops', [])
        drops_label.config(text="\n\n".join(drops))
        if drops == []:
            drops_label.config(text="".join('None'))
    else:
        Droppable_items_label.config(text="")
        drops_label.config(text="")
    if hyrule['data']['category'] == "materials":
        Cooking_effects_label.config(text = "Cooking Effect")
        effects = hyrule['data'].get('cooking_effect', [])
        effects_label.config(text="".join(effects))
        if effects == []:
            effects_label.config(text="".join('None'))
    else:
        Cooking_effects_label.config(text="")
        effects_label.config(text="")
    # print (hyrule)

    # print(hyrule['data']['category'])
    # print(hyrule['data']['description'])

enter_button = tk.Button(window, text="⌕",
font=("Arial", 14),

command=get_reply)

enter_button.place(x=480, y=45)
window.mainloop()