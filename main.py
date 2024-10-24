import tkinter as tk
from tkinter import ttk
import json
import ny_varer as ny
import endre_varer as en
USER_DETAILS_FILEPATH = "users.txt"



class SearchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Search Application")
        self.master.geometry("400x300")
        self.toggleStock = True
        self.togglePrice = True
        self.filtered_books = []  # Store filtered books
        self.setup_signup_frame()

    def setup_signup_frame(self):

        def authenticate(username, password):
            self.errormessage.destroy()
            with open(USER_DETAILS_FILEPATH, "r") as file:
                for line in file:
                    username_password = line.split()
                    if username_password[0] == username and username_password[1] == password:
                        self.setup_mainFrame()
                        self.mainFrame.tkraise()
                        self.signup_frame.destroy()
                        return True
            self.errormessage = ttk.Label(self.signup_frame, text="Feil brukernavn eller passord")
            self.errormessage.pack()

        def submit():
            username = self.username_entry.get().lower()
            password = self.password_entry.get()
            authenticate(username, password)
        
        #Login Widgets
        self.signup_frame = tk.Frame(self.master, bg='#141414')
        self.signup_frame.pack(fill=tk.BOTH, expand=True)
        self.username = ttk.Label(self.signup_frame, text="Brukernavn:", background='#141414', foreground='white')
        self.username.pack()
        self.username_entry = ttk.Entry(self.signup_frame)
        self.password_entry = ttk.Entry(self.signup_frame, show="*")
        self.submitLoginButton = ttk.Button(self.signup_frame, text="Logg inn", command=submit)
        self.username_entry.pack()
        self.password = ttk.Label(self.signup_frame, text="Passord:", background='#141414', foreground='white')
        self.password.pack()
        self.password_entry.pack()
        self.submitLoginButton.pack()
        self.errormessage = ttk.Label(self.signup_frame, text="Feil brukernavn eller passord")
        self.password_entry.bind("<Return>", lambda event: submit())



        def signup():
            def append_newuser():
                username = self.newuser_entry.get().strip().lower()
                password = self.newpass_entry.get().strip()

                if username and password:  # Ensure both fields are filled
                # Check for duplicate username
                    try:
                        with open("users.txt", "r") as file:
                            existing_users = {line.split()[0] for line in file}  # Create a set of existing usernames
            
                            if username in existing_users:
                                ttk.Label(self.signup_frame, text="Brukernavnet finnes allerede!", background='#141414', foreground='red').pack(pady=5)
                            else:
                                with open("users.txt", "a") as file:
                                    file.write(f"{username} {password}\n")
                # Clear the entries and raise the main frame
                                self.newuser_entry.delete(0, tk.END)
                                self.newpass_entry.delete(0, tk.END)
                                self.setup_mainFrame()
                                self.mainFrame.tkraise()
                                self.signup_frame.destroy()
                                return True
                    except:
                        ttk.Label(self.signup_frame, text="Script kjørt fra feil directory, ERRNO2", background="black", foreground="white").pack(pady=5)
                else:
                    ttk.Label(self.signup_frame, text="Vennligst fyll ut begge felt!", background='#141414', foreground='red').pack(pady=5)
            def signup_widgets():
                self.newuser = ttk.Label(self.signup_frame, text="Nytt Brukernavn:", background='#141414', foreground='white')
                self.newuser_entry = ttk.Entry(self.signup_frame)
                self.newuser.pack(pady=2)
                self.newuser_entry.pack(pady=5)
                self.newpass = ttk.Label(self.signup_frame, text="Nytt Passord:", background='#141414', foreground='white')
                self.newpass_entry = ttk.Entry(self.signup_frame)
                self.newpass.pack(pady=2)
                self.newpass_entry.pack(pady=5)
                self.newuser_button = ttk.Button(self.signup_frame, text="Lag ny bruker", command=append_newuser)
                self.newuser_button.pack(pady=10)
            self.username_entry.pack_forget()
            self.password_entry.pack_forget()
            self.submitLoginButton.pack_forget()
            self.username.pack_forget()
            self.password.pack_forget()
            self.signup_button.pack_forget()
            signup_widgets()
            


        #Sign up widget
        self.signup_button = ttk.Button(self.signup_frame, text="Lag bruker", command=signup)
        self.signup_button.pack(pady=20)
        

            

    def setup_mainFrame(self):
        self.mainFrame = tk.Frame(self.master, bg='#141414')
        # Create menubar
        menubar = tk.Menu(self.mainFrame, bg="black", fg="white")
        self.master.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_command(label="Quit", command=self.master.quit)


        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="lege til nye varer", command=ny.varer.ny_vare)
        help_menu.add_command(label="endre på varer", command=en.start)
        menubar.add_cascade(label="vareinfo", menu=help_menu)


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
        self.sortPriceButton.pack(side=tk.LEFT, padx=5)
        self.sortStockButton.pack(side=tk.LEFT, padx=5)
        for book in books: 
            self.sortStockButton.pack(side=tk.LEFT, padx=5)
            self.listbox.insert(tk.END, f"{book['title']} by {book['author']}, price: {book['price']}, stock: {book['stock']}")

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

        # Toggle the sorting order
        self.toggleStock = not self.toggleStock
        if self.toggleStock:
            self.sortStockButton.config(text="Sort stock, Descending")
        else:
            self.sortStockButton.config(text="Sort stock, Ascending")

        # Sort the books based on stock
        stock_sorted_books = sorted(books, key=lambda x: x['stock'], reverse=self.toggleStock)

        # Insert the sorted books into the listbox
        for book in stock_sorted_books:
            self.listbox.insert(tk.END, f"{book['title']} by {book['author']}, stock: {book['stock']}")

        # Update filtered_books
        self.filtered_books = stock_sorted_books


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

