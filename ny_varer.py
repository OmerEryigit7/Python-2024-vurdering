#!/bin/python
import tkinter as tk
import json
from os import path

class varer:
    def ny_vare():
        global sssssss
        sssssss = 0
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
        stock = ""
        summary = ""
        Year = ""
        author = ""
        tall = ""
        navn = ""
        genre = ""

        root = tk.Tk()
        root.title("ny vare")

        # Create a Canvas and Scrollbar
        canvas = tk.Canvas(root)
        scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        # Configure the scrollable frame
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a window in the canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Pack the canvas and scrollbar
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Link the scrollbar to the canvas
        canvas.configure(yscrollcommand=scrollbar.set)

        def prisen():
            filename = "varer.json"
            with open(filename, "r+") as fp:
                jsonVarer = json.load(fp)

                stock = stock_widget.get("1.0", "end-1c")
                summary = summary_widget.get("1.0", "end-1c")
                Year = Year_widget.get("1.0", "end-1c")
                genre = genre_widget.get("1.0", "end-1c")
                navn = text_widget.get("1.0", "end-1c")
                tall = talll_widget.get("1.0", "end-1c")
                author = author_widget.get("1.0", "end-1c")

                try:
                    jsonVarer.append({
                        "title": str(navn),
                        "author": str(author),
                        "genre": str(genre),
                        "publicationYear": int(Year),
                        "summary": str(summary),
                        "price": int(tall),
                        "stock": int(stock)
                    })
                    fp.seek(0)
                    json.dump(jsonVarer, fp, indent=4)
                except ValueError:
                    error_window = tk.Tk()
                    error_window.title("Error")
                    label = tk.Label(error_window, text="Skriv tall på pris, år og stock ikke bokstaver")
                    label.pack(pady=10)

        # Function to create text input fields
        def create_text_input(label_text):
            label = tk.Label(scrollable_frame, text=label_text, font=('Arial', 12))
            label.pack(pady=10)
            text_widget = tk.Text(scrollable_frame, height=3)
            text_widget.pack(padx=10, pady=10, fill="both")
            return text_widget

        # Create text input fields
        text_widget = create_text_input("Bok navn")
        talll_widget = create_text_input("Bok pris")
        author_widget = create_text_input("Bok forfatter")
        genre_widget = create_text_input("Bok genre")
        Year_widget = create_text_input("Utgit år")
        summary_widget = create_text_input("Summary")
        stock_widget = create_text_input("Stock")

        # Button to add a new item
        ny_vare = tk.Button(scrollable_frame, text="Legg til ny vare", command=prisen)
        ny_vare.pack(pady=10)

        root.mainloop()


