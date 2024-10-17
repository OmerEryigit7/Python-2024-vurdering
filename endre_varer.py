import tkinter as tk
from tkinter import messagebox
import json
def start():
    def load_bøker():
        with open('varer.json', 'r') as f:
            return json.load(f)

    def find_bøker(title):
        products = load_bøker()
        for product in products:
            if product['title'] == title:
                return product
        return None

    def delete_bøker():
        title = product_entry.get()
        product = find_bøker(title)
        
        if product:
            products = load_bøker()
            products = [p for p in products if p['title'] != title]
            
            with open('varer.json', 'w') as f:
                json.dump(products, f)
            

            product_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Feil", f"Ingen vare funnet med tittelen '{title}'.")
    def lagre():
        title = product_entry.get()
        product = find_bøker(title)
        
        if product:
            # Update existing product
            product['price'] = float(product_pris.get())
            product['stock'] = int(product_stock.get())
            
            # Load the entire file
            with open("varer.json", "r") as file:
                data = json.load(file)
            
            # Find the index of the product to update
            for i, prod in enumerate(data):
                if prod['title'] == title:
                    data[i] = product
                    break
            
            # Save the updated data
            with open("varer.json", "w") as file:
                json.dump(data, file, indent=4)
            
            messagebox.showinfo("Suksess", f"Varen '{title}' er oppdatert.")
        else:
            # Add new product
            new_product = {
                "title": title,
                "price": float(product_pris.get()),
                "stock": int(product_stock.get())
            }
            
            # Load the entire file
            with open("varer.json", "r") as file:
                data = json.load(file)
            
            # Add the new product
            data.append(new_product)
            
            # Save the updated data
            with open("varer.json", "w") as file:
                json.dump(data, file, indent=4)
            

            
            with open("varer.json", "w") as file:
                json.dump(data, file, indent=4)

                
            

            

    root = tk.Tk()
    root.title("endre på vare")

    product_label = tk.Label(root, text="bok navn:")
    product_label.grid(row=0, column=0, padx=5, pady=5)

    product_entry = tk.Entry(root, width=30)
    product_entry.grid(row=0, column=1, padx=5, pady=5)

    product_label = tk.Label(root, text="bok pris:")
    product_label.grid(row=1, column=0, padx=5, pady=5)

    product_pris = tk.Entry(root, width=30)
    product_pris.grid(row=1, column=1, padx=5, pady=5)

    product_label = tk.Label(root, text="bok stock:")
    product_label.grid(row=2, column=0, padx=5, pady=5)

    product_stock = tk.Entry(root, width=30)
    product_stock.grid(row=2, column=1, padx=5, pady=5)

    save_button = tk.Button(root, text="lagre endringer", command=lagre)
    save_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

    delete_button = tk.Button(root, text="Slett boken", command=delete_bøker)
    delete_button.grid(row=3, column=6, columnspan=2, padx=5, pady=5)

    root.mainloop()