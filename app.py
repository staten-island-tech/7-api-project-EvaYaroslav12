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
window.configure(bg='#402B30')

from tkinter import font
import pyglet
import os
#font_path = "The Wild Breath of Zelda.otf"
#pyglet.font.add_file(font_path)
totk_font_family = "The Wild Breath of Zelda"
#custom_font = font.Font(family=totk_font_family)

prompt = tk.Label(window, text="Input Name or ID", 
font=(totk_font_family, 20), bg="#402B30", fg='white')
prompt.place(y=10, x=150) 
entry = tk.Entry(window, font=("Arial", 14), width=40)
entry.place(x=20,y=52)

name_label = tk.Label(window, text="", font=( totk_font_family, 25, "bold"),
fg="white",
bg="#402B30")
name_label.place(x=550,y=52)

description_label = tk.Label(window, text="", font=("Arial", 14,),
fg="white", wraplength=400, bg="#402B30")
description_label.place(x=530, y=155)

Category_label = tk.Label(window, text="", font=("Arial", 10,),
fg="white",  bg="#402B30")
Category_label.place(x=800, y=800)

image_label = tk.Label(window, bg="#402B30")
image_label.place(x=50, y=150)

common_locations_label = tk.Label(window, text="",compound="center", font=(totk_font_family, 20,), 
fg="white", bg="#402B30")
common_locations_label.place(x=100, y=560)

common_places_label = tk.Label(window, text="",compound="center", font=("Arial", 14,),
fg="white", bg="#402B30")
common_places_label.place(x=150, y=620)

Droppable_items_label = tk.Label(window, text="", compound="center", font=(totk_font_family, 20,), 
fg="white", bg="#402B30")
Droppable_items_label.place(x=500, y=560)

drops_label = tk.Label(window, text="", compound="center", font=("Arial", 14,),
fg="white", bg="#402B30")
drops_label.place(x=520, y=620)

Cooking_effects_label = tk.Label(window, text="", compound="center", font=(totk_font_family, 20,), 
fg="white", bg="#402B30")
Cooking_effects_label.place(x=500, y=560)

effects_label = tk.Label(window, text="", compound="center", font=("Arial", 14,), 
fg="white", bg="#402B30")
effects_label.place(x=520, y=620)

background_image_label = tk.Label(window)
background_image_label.place(x=0, y=550)

category_image_label = tk.Label(window, bg="#402B30")
category_image_label.place(x=947, y=496)

def get_reply():
    # print(entry.get)
    hyrule = GetHyrule(entry.get())
    hyrule_name = (hyrule['data']['name']).upper() + " " + str(hyrule['data']['id'])

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
   
    background_url = f'https://images3.alphacoders.com/137/thumb-350-1370190.webp'
    responsebg = requests.get(background_url)
    pil_imagebg = Image.open(BytesIO(responsebg.content))
    pil_imagebg = pil_imagebg.resize((1000, 400))
    tk_imagebg = ImageTk.PhotoImage(pil_imagebg)
    background_image_label.config(image=tk_imagebg)
    background_image_label.image = tk_imagebg

    animal_url = f'https://cdn.discordapp.com/attachments/1074781218899513465/1498374454802255932/Screenshot_2026-04-27_130446.png?ex=69f0ed74&is=69ef9bf4&hm=aade76c2d6904538074b50974e329f331026e6200a0ab757a403c30d3e71188b&'


    common_locations_label.config(text = "COMMON LOCATIONS")
    locations = hyrule['data'].get('common_locations', [])
    if locations == None:
        common_places_label.config(text="".join('No Common Locations'))
    else:
        common_places_label.config(text="\n\n".join(locations))

    if hyrule['data']['category'] == "creatures" or "monster" or "treasure":
        Droppable_items_label.config(text = "DROPPABLE ITEMS")
        drops = hyrule['data'].get('drops', [])
        drops_label.config(text="\n\n".join(drops))
        if drops == []:
            drops_label.config(text="".join('None'))
        if hyrule['data']['category'] == "creatures":
            animal_url = f'https://cdn.discordapp.com/attachments/1074781218899513465/1498374454802255932/Screenshot_2026-04-27_130446.png?ex=69f0ed74&is=69ef9bf4&hm=aade76c2d6904538074b50974e329f331026e6200a0ab757a403c30d3e71188b&'
        if hyrule['data']['category'] == "monster":
            animal_url = f'https://cdn.discordapp.com/attachments/1074781218899513465/1498455142142443620/image.png?ex=69f13899&is=69efe719&hm=8e9af6edf17af4404fbc6c0f545066157413f5798cf5fedc62d09f83baed02cd&'
        if hyrule['data']['category'] == "treasue":
            animal_url = f'https://cdn.discordapp.com/attachments/1074781218899513465/1498455894445527080/image.png?ex=69f1394d&is=69efe7cd&hm=f4eef3be288b83638cff560deeccbc82bba19772900199abd8e4faf98e69e271&'
    else:
        Droppable_items_label.config(text="")
        drops_label.config(text="")
    if hyrule['data']['category'] == "materials":
        Cooking_effects_label.config(text = "COOKING EFFECTS")
        effects = hyrule['data'].get('cooking_effect', [])
        effects_label.config(text="".join(effects))
        if effects == []:
            effects_label.config(text="".join('None'))

        animal_url = f'https://cdn.discordapp.com/attachments/1074781218899513465/1498454018572423269/image.png?ex=69f1378d&is=69efe60d&hm=662e3e28c6ba1e08332e7478fe7f872b320aadfd2f857c710b5bf868e7cd2c1b&'

    else:
        Cooking_effects_label.config(text="")
        effects_label.config(text="")
    if hyrule['data']['category'] == "weapons":
        animal_url = f'https://cdn.discordapp.com/attachments/1074781218899513465/1498456334142537808/image.png?ex=69f139b6&is=69efe836&hm=265034e7581c45319def17dc14cb6ee8561cf32dfe40024fb30d3f6b6cc16400&'

    responsean = requests.get(animal_url)
    pil_imagean = Image.open(BytesIO(responsean.content))
    pil_imagean = pil_imagean.resize((50, 50))
    tk_imagean = ImageTk.PhotoImage(pil_imagean)
    category_image_label.config(image=tk_imagean)
    category_image_label.image = tk_imagean


    common_locations_label.lift()
    common_places_label.lift()
    Droppable_items_label.lift()
    drops_label.lift()
    Cooking_effects_label.lift()
    effects_label.lift()
    # print (hyrule)

    # print(hyrule['data']['category'])
    # print(hyrule['data']['description'])

enter_button = tk.Button(window, text="⌕",
font=("Arial", 14),

command=get_reply)

enter_button.place(x=480, y=45)
window.mainloop()