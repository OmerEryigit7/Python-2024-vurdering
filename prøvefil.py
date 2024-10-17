import tkinter as tk
from tkinter import ttk
import os

USER_DETAILS_FILEPATH = "users.txt"

class SearchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Search Application")
        self.master.geometry("400x300")

        self.search_frame = tk.Frame(self.master, bg='#141414')
        self.signup_frame = tk.Frame(self.master, bg='#141414')

        self.setup_signup_frame()
        self.setup_search_frame()

        self.show_search_frame()  # Start by showing the search frame

    def setup_signup_frame(self):
        """Setup the signup frame UI."""
        ttk.Label(self.signup_frame, text="Create a New Account", background='#141414', foreground='white').grid(column=0, row=0, columnspan=2)

        ttk.Label(self.signup_frame, text="Username:", background='#141414', foreground='white').grid(column=0, row=1, pady=5)
        self.username_entry = ttk.Entry(self.signup_frame)
        self.username_entry.grid(column=1, row=1, pady=5)

        ttk.Label(self.signup_frame, text="Password:", background='#141414', foreground='white').grid(column=0, row=2, pady=5)
        self.password_entry = ttk.Entry(self.signup_frame, show='*')
        self.password_entry.grid(column=1, row=2, pady=5)

        signup_button = ttk.Button(self.signup_frame, text="Create Account", command=self.create_account)
        signup_button.grid(column=0, row=3, columnspan=2, pady=10)

        back_button = ttk.Button(self.signup_frame, text="Back", command=self.show_search_frame)
        back_button.grid(column=0, row=4, columnspan=2)

        self.signup_frame.pack(fill=tk.BOTH, expand=True)  # Make the frame fill the window

    def show_signup_frame(self):
        """Raise the signup frame to the front."""
        self.signup_frame.tkraise()

    def show_search_frame(self):
        """Raise the search frame to the front."""
        self.search_frame.tkraise()

    def create_account(self):
        """Create a new user account."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username and password:
            if not self.if_user_exists(username):
                with open(USER_DETAILS_FILEPATH, "a") as file:
                    file.write(f"{username} {password}\n")
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.show_search_frame()  # Switch back to search frame after signup
            else:
                self.show_error("User already exists. Please choose another username.")
        else:
            self.show_error("Please enter both username and password.")

    def if_user_exists(self, username):
        """Check if the user already exists in the file."""
        if os.path.exists(USER_DETAILS_FILEPATH):
            with open(USER_DETAILS_FILEPATH, "r") as f:
                for line in f:
                    parts = line.split()
                    if parts[0] == username:
                        return True
        return False

    def show_error(self, message):
        """Display error messages."""
        error_window = tk.Toplevel(self.master)
        error_window.title("Error")
        ttk.Label(error_window, text=message, background='black', foreground='white').pack(pady=10)
        ttk.Button(error_window, text="OK", command=error_window.destroy).pack(pady=5)

    def setup_search_frame(self):
        """Setup the search frame UI."""
        # The setup for the search frame goes here (omitted for brevity)

if __name__ == "__main__":
    root = tk.Tk()
    app = SearchApp(root)
    root.mainloop()
