import tkinter as tk
from tkinter import ttk
import json
import ny_varer as ny
import endre_varer as en


class SearchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Search Application")
        self.master.geometry("400x300")
        self.toggleStock = True
        self.togglePrice = True
        self.filtered_books = []  # Store filtered books


        # Create menubar
        menubar = tk.Menu(self.master, bg="black", fg="white")
        self.master.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="lege til ny varer", command=ny.varer.ny_vare)
        help_menu.add_command(label="endre på varer", command=en.start)
        menubar.add_cascade(label="vare info", menu=help_menu)


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
        self.sortPriceButton = ttk.Button(self.search_frame, text="Sort price, Ascending", command=self.show_books_price)
        self.sortStockButton = ttk.Button(self.search_frame, text="Sort stock, Ascending", command=self.show_books_stock)

        # Listbox to display results
        self.listbox = tk.Listbox(self.master, height=10, width=40, bg='black', fg='white', selectbackground='gray')
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.details_label = tk.Label(self.master, text="", bg='black', fg='white', wraplength=300)
        self.details_label.pack(pady=10)

        # Bind events
        self.search_entry.bind("<KeyPress>", lambda event: self.search())
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def on_select(self, event):
        selected_index = self.listbox.curselection()
        # Reset all items' background to black first
        for i in range(self.listbox.size()):
            self.listbox.itemconfig(i, {'bg': 'black'})

        if selected_index:
            self.listbox.itemconfig(selected_index, {'bg': 'gray'})
            # Use the filtered books to display details
            self.display_book_details(selected_index[0])

    def display_book_details(self, index):
        # Check if there are filtered books
        if index < len(self.filtered_books):
            book = self.filtered_books[index]
            self.details_label.config(text=f"Title: {book['title']}\nAuthor: {book['author']}\nPrice: {book['price']}\nStock: {book['stock']}")

    def show_books(self):
        self.listbox.delete(0, tk.END)  # Clear existing items
        with open('varer.json', 'r') as f:
            books = json.load(f)

        self.filtered_books = books  # Store all books in filtered_books

        for book in books:
            self.listbox.insert(tk.END, f"{book['title']} by {book['author']}, price: {book['price']}, stock: {book['stock']}")

        self.sortPriceButton.pack(side=tk.LEFT, padx=5)
        self.sortStockButton.pack(side=tk.LEFT, padx=5)

    def show_books_price(self):
        self.listbox.delete(0, tk.END)  # Clear existing items
        with open('varer.json', 'r') as f:
            books = json.load(f)

        self.togglePrice = not self.togglePrice
        if self.togglePrice:
            self.sortPriceButton.config(text="Sort price, Descending")
        else:
            self.sortPriceButton.config(text="Sort price, Ascending")

        # Sort books based on price
        price_sorted_books = sorted(books, key=lambda x: x['price'], reverse=self.togglePrice)

        for book in price_sorted_books:
            self.listbox.insert(tk.END, f"{book['title']} by {book['author']}, Price: {book['price']}")

    def show_books_stock(self):
        self.listbox.delete(0, tk.END)  # Clear existing items
        with open('varer.json', 'r') as f:
            books = json.load(f)

        self.toggleStock = not self.toggleStock
        if self.toggleStock:
            self.sortStockButton.config(text="Sort stock, Descending")
        else:
            self.sortStockButton.config(text="Sort stock, Ascending")

        stock_sorted_books = sorted(books, key=lambda x: x['stock'], reverse=self.toggleStock)

        for book in stock_sorted_books:
            self.listbox.insert(tk.END, f"{book['title']} by {book['author']}, stock: {book['stock']}")


        # Listbox to display results
        self.listbox = tk.Listbox(self.master, height=10, width=40, bg='black', fg='white')
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)


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
            self.details_label.config(text="")  # Clear detail
            self.filtered_books = []  # Clear filtered books
            return

        with open('varer.json') as data:
            items = json.load(data)

        # Store filtered books
        self.filtered_books = [item for item in items if query.lower() in item['title'].lower()]

        self.listbox.delete(0, tk.END)

        if not self.filtered_books:
            self.listbox.insert(tk.END, "Search not found")
            self.details_label.config(text="")  # Clear detail
        else:
            for item in self.filtered_books:
                self.listbox.insert(tk.END, f"{item['title']} by {item['author']}")

        query = self.search_entry.get()


if __name__ == "__main__":
    root = tk.Tk()
    app = SearchApp(root)
    root.mainloop()

