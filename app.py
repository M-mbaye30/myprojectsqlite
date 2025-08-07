from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3

app = Flask(__name__)
DATABASE = 'books.db'

# Configuration de la base de données SQLite
def get_db_connection():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db
# --- Gestion de la connexion à la base de données ---
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
# --- Exécution des requêtes SQL ---
def execute_query(query, params=None, fetch_all=False):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        if fetch_all:
            return cursor.fetchall()
        
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Erreur lors de l'exécution de la requête : {e}")
        conn.rollback()
        return False
    
@app.route('/')
def home():
    return render_template('home.html')

# --- Routes pour la gestion des livres ---

@app.route('/books')
def list_books():
    books = execute_query('SELECT * FROM books', fetch_all=True)
    return render_template('books/books.html', books=books)

@app.route('/books/add')
def add_book():
    return render_template('books/add_book.html')

@app.route('/books/add_book', methods=['POST'])
def save_add_book():
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']
    rating = request.form['rating']
    status = request.form['status']
    
    query = 'INSERT INTO books (title, author, year, rating, status) VALUES (?, ?, ?, ?, ?)'
    params = (title, author, year, rating, status)
    
    if execute_query(query, params):
        return redirect(url_for('list_books'))
    
    return "Erreur lors de l'ajout du livre", 500

@app.route('/books/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form.get('year')
        rating = request.form.get('rating')
        status = request.form['status']

        query = 'UPDATE books SET title = ?, author = ?, year = ?, rating = ?, status = ? WHERE id = ?'
        params = (title, author, year, rating, status, id)

        if execute_query(query, params):
            return redirect(url_for('list_books'))
    
    book = execute_query('SELECT * FROM books WHERE id = ?', (id,), fetch_all=True)
    if book:
        return render_template('books/edit_book.html', book=book[0])
    
    return "Livre non trouvé", 404
        
@app.route('/books/delete/<int:id>')
def delete_book(id):
    query = 'DELETE FROM books WHERE id = ?'
    if execute_query(query, (id,)):
        return redirect(url_for('list_books'))
    
    return "Erreur lors de la suppression", 500

# --- Routes pour la gestion des bibliothèques ---
@app.route('/libraries')
def list_libraries():
    libraries = execute_query('SELECT * FROM library', fetch_all=True)
    return render_template('libraries/libraries.html', libraries=libraries)

@app.route('/libraries/add')
def add_library():
    return render_template('libraries/add_library.html')

@app.route('/libraries/add_library', methods=['POST'])
def save_add_library():
    name = request.form['name']
    created_by = request.form['created_by']
    date_of_creation = request.form['date_of_creation']
    city = request.form['city']
    country = request.form['country']
    
    query = 'INSERT INTO library (name, created_by, date_of_creation, city, country) VALUES (?, ?, ?, ?, ?)'
    params = (name, created_by, date_of_creation, city, country)
    
    if execute_query(query, params):
        return redirect(url_for('list_libraries'))
        
    return "Erreur lors de l'ajout de la bibliothèque", 500

@app.route('/libraries/edit/<int:id>', methods=['GET', 'POST'])
def edit_library(id):
    if request.method == 'POST':
        name = request.form['name']
        created_by = request.form['created_by']
        date_of_creation = request.form['date_of_creation']
        city = request.form['city']
        country = request.form['country']
        
        query = 'UPDATE library SET name = ?, created_by = ?, date_of_creation = ?, city = ?, country = ? WHERE id = ?'
        params = (name, created_by, date_of_creation, city, country, id)
        
        if execute_query(query, params):
            return redirect(url_for('list_libraries'))
            
    library = execute_query('SELECT * FROM library WHERE id = ?', (id,), fetch_all=True)
    if library:
        return render_template('libraries/edit_library.html', library=library[0])
    
    return "Bibliothèque non trouvée", 404

@app.route('/libraries/delete/<int:id>')
def delete_library(id):
    query = 'DELETE FROM library WHERE id = ?'
    if execute_query(query, (id,)):
        return redirect(url_for('list_libraries'))
    
    return "Erreur lors de la suppression", 500

# --- Routes pour la gestion des prix ---
@app.route('/pricies')
def list_prices():
    prices = execute_query('SELECT * FROM price', fetch_all=True)
    return render_template('pricies/prices.html', prices=prices)

@app.route('/pricies/add')
def add_price():
    return render_template('pricies/add_price.html')

@app.route('/pricies/add_price', methods=['POST'])
def save_add_price():
    form_data = {key: request.form[key] for key in request.form}
    
    query = 'INSERT INTO price ({}) VALUES ({})'.format(
        ', '.join(form_data.keys()),
        ', '.join(['?'] * len(form_data))
    )
    params = tuple(form_data.values())

    if execute_query(query, params):
        return redirect(url_for('list_prices'))
    
    return "Erreur lors de l'ajout du prix", 500

@app.route('/pricies/edit/<int:id>', methods=['GET', 'POST'])
def edit_price(id):
    if request.method == 'POST':
        form_data = {key: request.form[key] for key in request.form}
        
        set_clause = ', '.join([f"{key} = ?" for key in form_data.keys()])
        query = f'UPDATE price SET {set_clause} WHERE id = ?'
        params = tuple(list(form_data.values()) + [id])

        if execute_query(query, params):
            return redirect(url_for('list_prices'))
    
    price = execute_query('SELECT * FROM price WHERE id = ?', (id,), fetch_all=True)
    if price:
        return render_template('pricies/edit_price.html', price=price[0])
    
    return "Prix non trouvé", 404

@app.route('/pricies/delete/<int:id>')
def delete_price(id):
    query = 'DELETE FROM price WHERE id = ?'
    if execute_query(query, (id,)):
        return redirect(url_for('list_prices'))
    
    return "Erreur lors de la suppression", 500

# ---recherche ---
@app.route('/search')
def search():
    query_text = request.args.get('query', '')
    
    # Si la requête est vide, rediriger vers une page de résultats vide.
    if not query_text:
        return render_template('search/search_results.html', 
                               query=query_text, 
                               results_books=[],
                               results_libraries=[],
                               results_prices=[])

    # Recherche dans les livres (titre, auteur)
    books_query = 'SELECT * FROM books WHERE title LIKE ? OR author LIKE ?'
    books_params = ('%' + query_text + '%', '%' + query_text + '%')
    results_books = execute_query(books_query, books_params, fetch_all=True)

    # Recherche dans les bibliothèques (nom, ville, pays)
    libraries_query = 'SELECT * FROM library WHERE name LIKE ? OR city LIKE ? OR country LIKE ?'
    libraries_params = ('%' + query_text + '%', '%' + query_text + '%', '%' + query_text + '%')
    results_libraries = execute_query(libraries_query, libraries_params, fetch_all=True)

    # Recherche dans les prix (devise)
    prices_query = 'SELECT * FROM price WHERE senegal_currency LIKE ? OR france_currency LIKE ? OR canada_currency LIKE ?'
    prices_params = ('%' + query_text + '%', '%' + query_text + '%', '%' + query_text + '%')
    results_prices = execute_query(prices_query, prices_params, fetch_all=True)

    return render_template('search/search_results.html',
                           query=query_text,
                           results_books=results_books,
                           results_libraries=results_libraries,
                           results_prices=results_prices)

@app.route('/about')
def about():
    """Affiche la page À propos."""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)