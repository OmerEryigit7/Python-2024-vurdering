import tkinter as tk
from tkinter import messagebox
import json
def start():
    def load_products():
        with open('varer.json', 'r') as f:
            return json.load(f)

    def find_product(title):
        products = load_products()
        for product in products:
            if product['title'] == title:
                return product
        return None

    def delete_product():
        title = product_entry.get()
        product = find_product(title)
        
        if product:
            products = load_products()
            products = [p for p in products if p['title'] != title]
            
            with open('varer.json', 'w') as f:
                json.dump(products, f)
            
            messagebox.showinfo("Suksess", f"Varen '{title}' er slettet.")
            product_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Feil", f"Ingen vare funnet med tittelen '{title}'.")

    root = tk.Tk()
    root.title("Slett Vare")

    product_label = tk.Label(root, text="Tittel:")
    product_label.grid(row=0, column=0, padx=5, pady=5)

    product_entry = tk.Entry(root, width=30)
    product_entry.grid(row=0, column=1, padx=5, pady=5)

    delete_button = tk.Button(root, text="Slett Vare", command=delete_product)
    delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()