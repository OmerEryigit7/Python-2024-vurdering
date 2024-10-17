import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget, QLabel, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import json

class SearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Application")
        self.setGeometry(100, 100, 600, 400)

        # Create menubar
        menubar = self.menuBar()
        file_menu = QMenu("File", self)
        help_menu = QMenu("Help", self)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

        menubar.addMenu(file_menu)
        menubar.addMenu(help_menu)

        # Set background color to black
        self.setStyleSheet("background-color: black; color: white")

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        # Search frame
        search_frame = QWidget()
        search_layout = QVBoxLayout()
        
        search_label = QLabel("Search:", search_frame)
        search_label.setStyleSheet("color: white")
        
        self.search_entry = QLineEdit(search_frame)
        self.search_entry.setPlaceholderText("Enter search term")
        self.search_entry.setStyleSheet("background-color: gray; color: white")
        
        search_button = QPushButton("Search", search_frame)
        search_button.clicked.connect(self.search)
        search_button.setStyleSheet("background-color: blue; color: white")
        
        cancel_button = QPushButton("Cancel", search_frame)
        cancel_button.clicked.connect(lambda: self.listbox.clear())
        cancel_button.setStyleSheet("background-color: red; color: white")
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_entry)
        search_layout.addWidget(search_button)
        search_layout.addWidget(cancel_button)
        
        search_frame.setLayout(search_layout)
        main_layout.addWidget(search_frame)

        # Book display area
        self.listbox = QListWidget()
        self.listbox.setStyleSheet("background-color: black; color: white")
        main_layout.addWidget(self.listbox)

        central_widget.setLayout(main_layout)

        # Initialize book list
        self.show_books()

    def show_books(self):
        self.listbox.clear()
        with open('varer.json', 'r') as f:
            books = json.load(f)
        
        for book in books:
            self.listbox.addItem(f"{book['title']} by {book['author']}, price: {book['price']}, stock: {book['stock']}")

    def search(self):
        query = self.search_entry.text()
        if not query:
            self.listbox.clear()
            self.listbox.addItem("Please enter a search term")
            return
        
        with open('varer.json') as data:    
            items = json.load(data)

        titles = [item['title'] for item in items]
        
        filtered_titles = [title for title in titles if query.lower() in title.lower()]
    
        self.listbox.clear()
    
        if not filtered_titles:
            self.listbox.addItem("Search not found")
        else:
            for item in filtered_titles:
                self.listbox.addItem(item)

    def show_about(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("About")
        msg_box.setText("This is a simple search application.")
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SearchApp()
    ex.show()
    sys.exit(app.exec_())
