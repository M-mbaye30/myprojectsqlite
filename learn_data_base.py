import sqlite3

DATABASE_NAME = "books.db"

class DatabaseManager:
    """
    Gestionnaire de contexte pour la connexion à la base de données.
    Cela garantit que la connexion et le curseur sont toujours gérés correctement.
    """
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        # Permet d'accéder aux colonnes par leur nom au lieu de leur index
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            print(f"Erreur détectée. Annulation des modifications : {exc_val}")
            self.conn.rollback() # Annule les modifications en cas d'erreur
        self.cursor.close()
        self.conn.close()

def execute_query(query, params=None, fetch_all=False): #Fonction générique pour exécuter une requête SQL
 
    try:
        with DatabaseManager(DATABASE_NAME) as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if fetch_all:
                return cursor.fetchall()
            
            # Les opérations comme INSERT ou UPDATE ne retournent rien, donc on n'affiche rien.
            # On peut ajouter un print ici pour le feedback si besoin.

    except sqlite3.Error as e:
        print(f"Erreur lors de l'exécution de la requête : {e}")
        return None

def create_tables():
    """
    Crée toutes les tables nécessaires si elles n'existent pas.
    """
    print("Création des tables...")
    # On exécute les requêtes de création de table dans une seule transaction.
    with DatabaseManager(DATABASE_NAME) as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                rating REAL,
                status TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS library (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                created_by TEXT NOT NULL,
                date_of_creation TEXT NOT NULL,
                city TEXT NOT NULL,
                country TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS price (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                senegal INTEGER NOT NULL,
                senegal_currency TEXT NOT NULL,
                france INTEGER  NOT NULL,
                france_currency TEXT NOT NULL,
                canada INTEGER  NOT NULL,
                canada_currency TEXT NOT NULL,
                maroc INTEGER  NOT NULL,
                maroc_currency TEXT NOT NULL,
                arabi_saoudite INT NOT NULL,
                arabi_saoudite_currency TEXT NOT NULL
            )
        ''')
    print("Tables créées avec succès.")


def add_book(title, author, year, rating, status):
    """ Ajoute un nouveau livre à la table 'books'. """
    query = "INSERT INTO books (title, author, year, rating, status) VALUES (?, ?, ?, ?, ?)"
    params = (title, author, year, rating, status)
    execute_query(query, params)
    print(f"Livre '{title}' ajouté avec succès.")

def show_all_books():
    """ Affiche tous les livres de la table 'books'. """
    query = "SELECT * FROM books"
    books = execute_query(query, fetch_all=True)
    if books:
        for book in books:
            print(f"ID: {book['id']}, Titre: {book['title']}, Auteur: {book['author']}, Année: {book['year']}, Note: {book['rating']}, Statut: {book['status']}")
    else:
        print("Aucun livre trouvé.")

def add_library(name, created_by, date_of_creation, city, country):
    """ Ajoute une nouvelle bibliothèque à la table 'library'. """
    query = "INSERT INTO library (name, created_by, date_of_creation, city, country) VALUES (?, ?, ?, ?, ?)"
    params = (name, created_by, date_of_creation, city, country)
    execute_query(query, params)
    print(f"Bibliothèque '{name}' ajoutée avec succès.")

def show_all_library():
    """ Affiche toutes les bibliothèques de la table 'library'. """
    query = "SELECT * FROM library"
    libraries = execute_query(query, fetch_all=True)
    if libraries:
        for library in libraries:
            print(f"ID: {library['id']}, Nom: {library['name']}, Créé par: {library['created_by']}, Date: {library['date_of_creation']}, Ville: {library['city']}, Pays: {library['country']}")
    else:
        print("Aucune bibliothèque trouvée.")

def add_price(senegal, senegal_currency, france, france_currency, canada, canada_currency, maroc, maroc_currency, arabi_saoudite, arabi_saoudite_currency):
    """ Ajoute un nouveau prix à la table 'price'. """
    query = "INSERT INTO price (senegal, senegal_currency, france, france_currency, canada, canada_currency, maroc, maroc_currency, arabi_saoudite, arabi_saoudite_currency) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    params = (senegal, senegal_currency, france, france_currency, canada, canada_currency, maroc, maroc_currency, arabi_saoudite, arabi_saoudite_currency)
    execute_query(query, params)
    print("Prix ajouté avec succès.")

def show_all_price():
    """ Affiche tous les prix de la table 'price'. """
    query = "SELECT * FROM price"
    prices = execute_query(query, fetch_all=True)
    if prices:
        for price in prices:
            print(f"ID: {price['id']}, Sénégal: {price['senegal']} {price['senegal_currency']}, France: {price['france']} {price['france_currency']}, Canada: {price['canada']} {price['canada_currency']}, Maroc: {price['maroc']} {price['maroc_currency']}, Arabie Saoudite: {price['arabi_saoudite']} {price['arabi_saoudite_currency']}")
    else:
        print("Aucun prix trouvé.")

# --- Point d'entrée principal du programme ---
if __name__ == "__main__":
    create_tables()

    # Ajout des livres
    add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 4.2, "read")
    add_book("To Kill a Mockingbird", "Harper Lee", 1960, 4.3, "reading")
    add_book("1984", "George Orwell", 1949, 4.5, "to-read")
    add_book("Pride and Prejudice", "Jane Austen", 1813, 4.6, "read")
    add_book("The Catcher in the Rye", "J.D. Salinger", 1951, 4.0, "reading")
    add_book("The Lord of the Rings", "J.R.R. Tolkien", 1954, 4.8, "to-read")
    add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 4.2, "read")
    add_book("une si longue lettre", "Mariama Bâ", 1979, 4.1, "read")
    add_book("The Alchemist", "Paulo Coelho", 1988, 4.4, "to-read")
    add_book("The Book Thief", "Markus Zusak", 2005, 4.5, "reading")
    add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, 4.2, "to-read")

    print("\n--- Ajout des livres terminé ---")

    # Ajout des bibliothèques
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

    print("\n--- Ajout des bibliothèques terminé ---")

    # Ajout des prix
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
    
    print("\n--- Ajout des prix terminé ---")

    # Affichage des données pour vérifier
    print("\n\n=== AFFICHAGE DE TOUTES LES DONNÉES ===")
    print("\n--- Tous les Livres ---")
    show_all_books()
    
    print("\n--- Toutes les Bibliothèques ---")
    show_all_library()

    print("\n--- Tous les Prix ---")
    show_all_price()