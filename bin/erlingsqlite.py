import sqlite3

def print_books_by_title(search_term):
    try:
        # Connect to SQLite database. It will be created if it doesn't exist.
        conn = sqlite3.connect('books.db')
        
        # Create a cursor object
        cur = conn.cursor()
        
        # SQL query to select books whose title contains the search term
        query = """
        SELECT id, title, author, genre, publication_year, price, stock
        FROM books
        WHERE LOWER(title) LIKE ? ESCAPE '?'
        ORDER BY title ASC
        """
        
        # Execute the SELECT query with the search term
        cur.execute(query, ('%' + search_term.lower() + '%',))
        
        # Fetch all rows
        rows = cur.fetchall()
        
        # Print header
        print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Genre':<10} {'Year':<10} {'Price':<10} {'Stock':<10}")
        print("-" * 75)
        
        # Print each row
        for row in rows:
            id, title, author, genre, year, price, stock = row
            print(f"{id:<5} {title:<30} {author:<20} {genre:<10} {year:<10.0f} ${price:<10.2f} {stock:<10d}")
        
        # Close the connection
        conn.close()
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Example usage:
# print_books_by_title('Diary')  # This would find books starting with "Diary"
# print_books_by_title('Harry Potter')  # This would find books containing "Harry Potter"

# You can run this function with any keyword you want

