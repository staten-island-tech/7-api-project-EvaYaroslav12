import requests

def GetHyrule(compendium):
    response = requests.get(f'https://botw-compendium.herokuapp.com/api/v3/compendium/entry/{compendium.lower()}')
    if response.status_code != 200:
        print ('Error fetching data')
        return None

    data = response.json()
    return data



import tkinter as tk
window = tk.Tk()
window.title("Hyrule Compendium") 
window.geometry("450x600") 
window.resizable(False, False) 

prompt = tk.Label(window, text="Input Name or ID",
font=("Arial", 14))
prompt.pack(pady=10) 
entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)

name_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="black")
name_label.pack(pady=10)
description_label = tk.Label(window, text="", font=("Arial", 9,),
fg="black", wraplength=400,)
description_label.pack(pady=10)

def get_reply():
    # print(entry.get)
    hyrule = GetHyrule(entry.get())
    name_label.config(text= (hyrule['data']['name']))
    description_label.config(text= (hyrule['data']['description']))
    # print (hyrule)
    # print(hyrule['data']['name'])
    # print(hyrule['data']['id'])
    # print(hyrule['data']['category'])
    # print(hyrule['data']['description'])

enter_button = tk.Button(window, text="⌕",
font=("Arial", 14),

command=get_reply)

enter_button.place(x=400, y=45)
window.mainloop()