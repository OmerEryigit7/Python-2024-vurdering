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
        global author
        global author_widget
        global genre
        global genre_widget
        global Year
        global Year_widget
        global summary
        global summary_widget
        global stock
        global stock_widget
        stock=""
        summary=""
        Year=""
        author=""
        tall=""
        navn=""
        genre=""
        

        root = tk.Tk()
        root.title("ny vare")
        tall_widget=tk.Text(root)


          


        def prisen():
            #lagrer filnavnet
            filename="varer.json"
            with open(filename, "r+") as fp:
                jsonVarer=json.load(fp)
                global navn
                global tall
                global talll_widget
                global author
                global genre
                global genre_widget
                global Year
                global Year_widget
                global summary
                global summary_widget
                global stock
                global stock_widget

                stock=stock_widget.get("1.0", "end-1c")
                summary=summary_widget.get("1.0", "end-1c")
                Year=Year_widget.get("1.0", "end-1c")
                genre=genre_widget.get("1.0", "end-1c")
                navn=text_widget.get("1.0", "end-1c")
                tall=talll_widget.get("1.0", "end-1c")
                author=author_widget.get("1.0", "end-1c")
                try:

                    jsonVarer.append({
                        #hva som skal bli puttet in i systemet
                        "title": str(navn),
                        "author": str(author),
                        "genre": str(genre),
                        "publicationYear": int(Year),
                        "summary": str(summary),
                        "price": int(tall),
                        "stock": int(stock)
                        

                    })
                    #legger til den nye boken
                    fp.seek(0)
                    json.dump(jsonVarer, fp, indent=4)
                    root.destroy
                except ValueError:
                    root = tk.Tk()
                    root.title("error")
                    label=tk.Label(root, text="skriv tall på pris, år og stock ikke bokstaver")
                    label.pack(pady=10)



        #legger til text inputen
        
        text_widget = tk.Text(root, height=5)
        label=tk.Label(root, text="bok navn", font=('Arial', 12))
        label.pack(pady=10)
        text_widget.pack(padx=10, pady=10, fill="both")
        

        global talll_widget
        
        #legger til text inputen
        label=tk.Label(root, text="bok pris", font=('Arial', 12))
        label.pack(pady=10)
        talll_widget = tk.Text(root, height=5)
        talll_widget.pack(padx=10, pady=10, fill="both")
        
        #legger til text inputen
        label=tk.Label(root, text="bok forfatter", font=('Arial', 12))
        label.pack(pady=10)
        author_widget = tk.Text(root, height=5)
        author_widget.pack(padx=10, pady=10, fill="both")
        
        label=tk.Label(root, text="bok genre", font=('Arial', 12))
        label.pack(pady=10)
        genre_widget = tk.Text(root, height=5)
        genre_widget.pack(padx=10, pady=10, fill="both")
        
        label=tk.Label(root, text="utgit år", font=('Arial', 12))
        label.pack(pady=10)
        Year_widget = tk.Text(root, height=5)
        Year_widget.pack(padx=10, pady=10, fill="both")

        label=tk.Label(root, text="summary", font=('Arial', 12))
        label.pack(pady=10)
        summary_widget = tk.Text(root, height=5)
        summary_widget.pack(padx=10, pady=10, fill="both")

        label=tk.Label(root, text="stock", font=('Arial', 12))
        label.pack(pady=10)
        stock_widget = tk.Text(root, height=5)
        stock_widget.pack(padx=10, pady=10, fill="both")
        
        #button
        ny_vare= tk.Button(root, text="leg til ny vare", command=prisen)
        ny_vare.pack(pady=10)



        root.mainloop()

