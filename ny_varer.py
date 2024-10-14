#!/bin/python
import tkinter as tk
import json
from os import path
class varer:
    def ny_vare():
        # legger til alle globale verdier
        global sssssss
        sssssss=0
        global navn
        global text_widget
        global talll_widget
        global tall
        tall=""
        navn=""
        

        root = tk.Tk()
        root.title("ny vare")
        tall_widget=tk.Text(root)
        def endre_variabel():
            global navn
            global text_widget

            navn=text_widget
        def talle():
            global tall
            global talll_widget
            tall=talll_widget
          


        def prisen():
            talle()
            filename="varer.json"
            with open(filename, "r+") as fp:
                jsonVarer=json.load(fp)
                global navn
                global tall
                global tall_widget
                navn=text_widget.get("1.0", "end-1c")
                tall=talll_widget.get("1.0", "end-1c")

                jsonVarer.append({
                    "title": str(navn),
                    "author": "J.R.R. Tolkien",
                    "genre": "High Fantasy",
                    "publicationYear": 1954,
                    "summary": "A hobbit named Frodo Baggins inherits the One Ring and embarks on a perilous journey to destroy it in the fires of Mount Doom.",
                    "price": str(tall),
                    "stock": 4
                    

                })
                fp.seek(0)
                json.dump(jsonVarer, fp, indent=4)
                root.destroy
                root.quit


    
        def ting():
            endre_variabel()
            global sssssss   
            global talll_widget
            if sssssss ==0 :
                talll_widget = tk.Text(root)
                talll_widget.pack(padx=10, pady=10, fill="both")
                sssssss=1
                pris= tk.Button(root, text="leg til prisen", command=prisen)
                pris.pack(pady=10)

        #legger til text inputen
        text_widget = tk.Text(root)
        text_widget.pack(padx=10, pady=10, fill="both")
        #legger til knappen
        ny_vare= tk.Button(root, text="leg til ny vare", command=ting)
        ny_vare.pack(pady=10)

        #status_label = tk.Label(root, text="", padx=1, pady=1)
        #status_label.pack()



        root.mainloop()

