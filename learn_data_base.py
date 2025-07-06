import sqlite3

#conn= sqlite3.connect("books.db")
with sqlite3.connect("books.db") as conn:
    cursor= conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS books(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TXT NOT NULL,
                   author TXT NOT NULL,
                   year INTEGER,
                   rating REAL,
                   status TXT NOT NULL
                   )
                   ''')
    conn.commit()


    def add_books(title, author, year, rating, status):
        try:
            with sqlite3.connect("books.db") as conn:
                cursor= conn.cursor()               
                cursor.execute(
                    "INSERT INTO books (title, author, year, rating, status) VALUES(?, ?, ?, ?, ?)",
                    (title, author, year, rating, status))
                
                conn.commit()
                print(f"book '{title}' added successfully")
        except sqlite3.Error as e:
             print(f" error of adding bokk: {e}") #le e 
    def show_all_books():
        try:
            with sqlite3.connect("books.db") as conn:

                cursor = conn.cursor()
                cursor.execute("SELECT * FROM books")
                rows= cursor.fetchall() # permet de recuperer les lignes de la table books
                for row in rows:
                    print(row)
        except sqlite3.Error as e:
            print(f"error retrieving books: {e}")
    # Create a library table
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS library(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       created_by TXT NOT NULL,
                       date_of_creation DATE NOT NULL,
                       city TEXT NOT NULL,
                       country TEXT NOT NULL
                   )
                   ''')
    conn.commit()
    def add_library(name, created_by, date_of_creation, city, country):
        try:
            with sqlite3.connect("books.db") as conn:
                cursor= conn.cursor()
                cursor.execute(
                    "INSERT INTO library (name, created_by, date_of_creation, city, country) VALUES(?, ?, ?, ?, ?)",

                    (name, created_by, date_of_creation, city, country))
                
                conn.commit()

                print(f"library '{name}' added sucessfully")
        except sqlite3.Error as e:
                print(f"error of adding labrary: {e}")
    def show_all_library():
        try:
            with sqlite3.connect("books.db") as conn:
                cursor= conn.cursor()
                cursor.execute( "SELECT * FROM library")
                rows= cursor.fetchall() # permet de recuperer les lignes de la table library
                for row in rows:
                    print(row)
        except sqlite3.Error as e: #cette ligne permet de capturer les erreurs 
            print(f"error retriving library: {e}") #per
    #create a price table
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS price(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   senegal INTEGER NOT NULL,
                   senegal_currency TXT NOT NULL,
                   france INTEGER  NOT NULL,
                   france_currency TXT NOT NULL,
                   canada INTEGER  NOT NULL,
                   canada_currency TXT NOT NULL,
                   maroc INTEGER  NOT NULL,
                   maroc_currency TXT NOT NULL,
                   arabi_saoudite INT NOT NULL,
                   arabi_saoudite_currency TXT NOT NULL
                
                   )
                   """)
    conn.commit()
    def add_price(
            senegal, senegal_currency,
            france, france_currency,
            canada, canada_currency,
            maroc, maroc_currency,
            arabi_saoudite, arabi_saoudite_currency
            ):
        try:
            with sqlite3.connect("books.db") as conn:
                cursor= conn.cursor()
                cursor.execute(
                    "INSERT INTO price (senegal, senegal_currency, france, france_currency, canada, canada_currency, maroc, maroc_currency, arabi_saoudite, arabi_saoudite_currency) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                     (senegal, senegal_currency, france, france_currency, canada, canada_currency, maroc, maroc_currency, arabi_saoudite, arabi_saoudite_currency)
                     )
                conn.commit()
                print(f"price added successfully")
        except sqlite3.Error as e:
            print(f"error of adding price: {e}")
    def show_all_price():
        try:
            with sqlite3.connect("books.db") as conn:
                cursor= conn.cursor()
                cursor.execute('SELECT * FROM price')
                rows= cursor.fetchall()
                for row in rows:
                    print(row)
        except sqlite3.Error as e:
            print (f"error retirevin price: {e}")
    
if __name__ == "__main__":
    add_books("The Great Gatsby", "F. Scott Fitzgerald", 1925, 4.2, "read")
    add_books("To Kill a Mockingbird", "Harper Lee", 1960, 4.3, "reading")
    add_books("1984", "George Orwell", 1949, 4.5, "to-read")
    add_books("Pride and Prejudice", "Jane Austen", 1813, 4.6, "read")
    add_books("The Catcher in the Rye", "J.D. Salinger", 1951, 4.0, "reading")
    add_books("The Lord of the Rings", "J.R.R. Tolkien", 1954, 4.8, "to-read")
    add_books("The Great Gatsby", "F. Scott Fitzgerald", 1925, 4.2, "read")
    add_books("une si longue lettre", "Mariama Bâ", 1979, 4.1, "read")
    add_books("The Alchemist", "Paulo Coelho", 1988, 4.4, "to-read")
    add_books("The Book Thief", "Markus Zusak", 2005, 4.5, "reading")
    add_books("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, 4.2, "to-read")
    # Add libraries
    add_library("City Library", "Alice Smith", "2023-01-15", "New York", "USA")
    add_library("université cheikh anta diop", "cheikh anta diop", "2023-01-15", "Dakar", "Senegal")
    add_library("National Library", "John Doe", "2022-05-20", "London", "UK")
    add_library("Community Library", "Jane Doe", "2021-08-10", "Los Angeles", "USA")
    add_library("University Library", "Dr. Smith", "2020-03-05", "Cambridge", "UK")
    add_library("Public Library", "Sarah Johnson", "2019-11-25", "Toronto", "Canada")
    add_library("Research Library", "Dr. Brown", "2018-07-30", "Sydney", "Australia")
    add_library("Children's Library", "Emily White", "2017-02-14", "Paris", "France")
    add_library("Digital Library", "Michael Green", "2016-09-01", "Berlin", "Germany")
    add_library("Historical Library", "Laura Black", "2015-12-20", "Rome", "Italy")
    add_library("Science Library", "Dr. Taylor", "2014-06-10", "Tokyo", "Japan")
    # Add prices

    add_price(1000, "CFA", 15, "DOLLAR", 20, "EURO", 10, "DIRHAM", 25, "RIAL")
    add_price(850, "CFA", 14, "DOLLAR", 18, "EURO", 9, "DIRHAM", 22, "RIAL")
    add_price(950, "CFA", 16, "DOLLAR", 20, "EURO", 11, "DIRHAM", 24, "RIAL")
    add_price(800, "CFA", 13, "DOLLAR", 17, "EURO", 8, "DIRHAM", 21, "RIAL")
    add_price(1100, "CFA", 18, "DOLLAR", 23, "EURO", 12, "DIRHAM", 28, "RIAL")
    add_price(1200, "CFA", 20, "DOLLAR", 25, "EURO", 14, "DIRHAM", 30, "RIAL")
    add_price(1300, "CFA", 22, "DOLLAR", 27, "EURO", 16, "DIRHAM", 32, "RIAL")
    add_price(1400, "CFA", 24, "DOLLAR", 29, "EURO", 18, "DIRHAM", 34, "RIAL")
    add_price(950, "CFA", 15, "DOLLAR", 19, "EURO", 10, "DIRHAM", 23, "RIAL")
    add_price(1050, "CFA", 17, "DOLLAR", 21, "EURO", 13, "DIRHAM", 26, "RIAL")
    add_price(1150, "CFA", 19, "DOLLAR", 24, "EURO", 15, "DIRHAM", 29, "RIAL")
    
    # Show all data
    print("All Books:")
    print("-----------------")
    show_all_books()
    print("All Libraries:")
    print("-----------------")
    show_all_library()
    print("All Prices:")
    print("-----------------")
    show_all_price()
  