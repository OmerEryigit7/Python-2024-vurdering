#!/bin/python
import tkinter as tk
import json
from os import path
filename="varer.json"
def ny_vare():
    root = tk.Tk()
    root.title("ny vare")
    def prisen():
        with open(filename, "r+") as fp:
            jsonVarer=json.load(fp)

            jsonVarer.append({
                "title": "Test",
                "author": "J.R.R. Tolkien",
                "genre": "High Fantasy",
                "publicationYear": 1954,
                "summary": "A hobbit named Frodo Baggins inherits the One Ring and embarks on a perilous journey to destroy it in the fires of Mount Doom.",
                "price": 200,
                "stock": 4
                   

              })
            fp.seek(0)
            json.dump(jsonVarer, fp, indent=4)
    
    def ting():
         text_widget = tk.Text(root)
         text_widget.pack(padx=10, pady=10, fill="both")
         pris= tk.Button(root, text="leg til prisen", command=prisen)
         pris.pack(pady=10)
    
    text_widget = tk.Text(root)
    text_widget.pack(padx=10, pady=10, fill="both")

    ny_vare= tk.Button(root, text="leg til ny vare", command=ting)
    ny_vare.pack(pady=10)

    status_label = tk.Label(root, text="", padx=1, pady=1)
    status_label.pack()



    root.mainloop()
