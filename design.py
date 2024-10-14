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
        self.master.configure(bg='#141414')

        # Create custom style
        self.style = ttk.Style(self.master)
        self.style.theme_use('clam')  # Use a theme that supports custom colors
        self.style.configure("SearchFrame.TFrame", background="black", foreground="white")
        self.style.map("SearchFrame.TFrame", background=[('active', 'gray75')])

        # Search bar frame
        self.search_frame = ttk.Frame(self.master, style="SearchFrame.TFrame")
        self.search_frame.pack()

        # Search entry
        self.search_entry = ttk.Entry(self.search_frame, width=30, style="SearchFrame.TEntry")
        self.search_entry.grid(column=0, row=0)

        # Search button
        self.search_button = ttk.Button(self.search_frame, text="Søk", command=self.search, style="SearchFrame.TButton")
        self.search_button.grid(column=1, row=0)

        # Listbox to display results
        self.listbox = tk.Listbox(self.master, height=10, width=40, bg='#141414', fg='white', highlightthickness=0, bd=0)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    def show_about(self):
        about_window = tk.Toplevel(self.master)
        about_window.title("About")
        about_window.configure(bg='black')
        label = tk.Label(about_window, text="This is a simple search application.", bg='black', fg='white')
        label.pack()

    def search(self):
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