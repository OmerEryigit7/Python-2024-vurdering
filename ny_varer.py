#!/bin/python
import tkinter as tk
def ny_vare():
    root = tk.Tk()
    root.title("ny vare")
    def ting():
         text_widget = tk.Text(root)
         text_widget.pack(padx=10, pady=10, fill="both")
         pris= tk.Button(root, text="leg til prisen", command=ting)
         pris.pack(pady=10)
    
    text_widget = tk.Text(root)
    text_widget.pack(padx=10, pady=10, fill="both")

    ny_vare= tk.Button(root, text="leg til ny vare", command=ting)
    ny_vare.pack(pady=10)

    status_label = tk.Label(root, text="", padx=1, pady=1)
    status_label.pack()



    root.mainloop()
