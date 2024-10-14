import tkinter as tk
from tkinter import ttk
import json

class SearchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Search Application")
        self.master.geometry("400x300")

        # Create menubar
        menubar = tk.Menu(self.master, bg="black", fg="white")
        self.master.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Set background color to black
        self.master.configure(bg='black')

        # Create custom style
        self.style = ttk.Style(self.master)
        self.style.theme_use('clam')  # Use a theme that supports custom colors
        self.style.configure("SearchFrame.TFrame", background="black", foreground="white")
        self.style.map("SearchFrame.TFrame", background=[('active', 'gray75')])

        # Search bar frame
        self.search_frame = ttk.Frame(self.master, style="SearchFrame.TFrame")
        self.search_frame.pack(pady=10, padx=10, fill=tk.X)
    
        # Search label
        self.search_label = ttk.Label(self.search_frame, text="Search:", style="SearchFrame.TLabel")
        self.search_label.pack(side=tk.LEFT)

        # Search entry
        self.search_entry = ttk.Entry(self.search_frame, width=30, style="SearchFrame.TEntry")
        self.search_entry.pack(side=tk.LEFT, padx=5)

        # Search button
        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search, style="SearchFrame.TButton")
        self.search_button.pack(side=tk.LEFT, padx=5)

        # Display all books button
        self.show_all = ttk.Button(self.search_frame, text="Show All books", command=self.show_books)
        self.show_all.pack(side=tk.LEFT, padx=5)

        # Sort buttons
        self.sortPriceButton = ttk.Button(self.search_frame, text="Sort price, Ascending", command=self.show_books_price_acsending)

        self.sortStockButton = ttk.Button(self.search_frame, text="Sort stock, Ascending", command=self.show_books_stock_acsending)

        # Listbox to display results
        self.listbox = tk.Listbox(self.master, height=10, width=40, bg='black', fg='white')
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    def show_books(self):
        self.listbox.delete(0, tk.END)  # Clear existing items
        with open('varer.json', 'r') as f:
            books = json.load(f)
        
        for book in books:
            self.listbox.insert(tk.END, f"{book['title']} by {book['author']}, price: {book['price']}, stock: {book['stock']}")
        
        self.sortPriceButton.pack(side=tk.LEFT, padx=5)
        self.sortStockButton.pack(side=tk.LEFT, padx=5)
        
    def show_books_price_acsending(self):
        self.listbox.delete(0, tk.END)  # Clear existing items
        with open('varer.json', 'r') as f:
                books = json.load(f)
            
            # Sort books based on price
        price_sorted_books = sorted(books, key=lambda x: x['price'], reverse=True)
            
            # Print sorted books to listbox
        for book in price_sorted_books:
                self.listbox.insert(tk.END, f"{book['title']} by {book['author']}, Price: {book['price']}")
        
    def show_books_stock_acsending(self):
        self.listbox.delete(0, tk.END)  # Clear existing items
        with open('varer.json', 'r') as f:
                books = json.load(f)
            
            # Sort books based on price
        stock_sorted_books = sorted(books, key=lambda x: x['stock'], reverse=True)
            
            # Print sorted books to listbox
        for book in stock_sorted_books:
                self.listbox.insert(tk.END, f"{book['title']} by {book['author']}, stock: {book['stock']}")
        
    

    def show_about(self):
        about_window = tk.Toplevel(self.master)
        about_window.title("About")
        about_window.configure(bg='black')
        label = tk.Label(about_window, text="This is a simple search application.", bg='black', fg='white')
        label.pack()

    def search(self):
        self.sortPriceButton.pack_forget()
        self.sortStockButton.pack_forget()

        query = self.search_entry.get()
    
        if not query:
            self.listbox.delete(0, tk.END)
            self.listbox.insert(tk.END, "Please enter a search term")
            return
        
        with open('varer.json') as data:    
            items = json.load(data)

        items = items
        titles = [item['title'] for item in items]
        
        # Perform the search on the titles
        filtered_titles = [title for title in titles if query.lower() in title.lower()]
        
    
        self.listbox.delete(0, tk.END)
    
        if not filtered_titles:
            self.listbox.insert(tk.END, "Search not found")
        else:
            for item in filtered_titles:
                self.listbox.insert(tk.END, item)
        

        

if __name__ == "__main__":
    root = tk.Tk()
    app = SearchApp(root)
    root.mainloop()