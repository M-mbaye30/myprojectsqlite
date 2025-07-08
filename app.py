
from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask (__name__)
@app.route('/')
def home():
    return render_template('home.html')


# This route will display the list of books from the database
@app.route('/books')
def list_books():
    conn= sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row # This allows us to access columns by name
    cursor = conn.cursor()
    cursor.execute(' SELECT * FROM books')
    books= cursor.fetchall()
    conn.close()
    return render_template('books.html', books=books) 

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    # This route will handle the form submission to add a new book # # Récupération des données du formulaire
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        rating = request.form['rating']
        status = request.form['status']
        # Connect to the database and insert the new book
        
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author, year, rating, status) VALUES (?, ?, ?, ?, ?)', (title, author, year, rating, status))
        conn.commit()
        conn.close()
        
        return redirect(url_for('list_books'))
    
    return render_template('add_book.html')
@app.route('/edit_book/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        # On récupère les nouvelles valeurs
        title = request.form['title']
        author = request.form['author']
        year = request.form.get('year')
        rating = request.form.get('rating')
        status = request.form['status']

        # Mise à jour dans la BDD
        cursor.execute('''
            UPDATE books
            SET title = ?, author = ?, year = ?, rating = ?, status = ?
            WHERE id = ?
        ''', (title, author, year, rating, status, id))
        conn.commit()
        conn.close()
        return redirect(url_for('list_books'))
    else:
        # On récupère le livre existant pour pré-remplir le formulaire
        cursor.execute('SELECT * FROM books WHERE id = ?', (id,))
        book = cursor.fetchone()
        conn.close()
        if book:
            return render_template('edit_book.html', book=book)
        else:
            return "Livre non trouvé", 404
        
@app.route('/delete_book/<int:id>')
def delete_book(id):
    conn= sqlite3.connect('books.db')
    cursor= conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('list_books'))

@app.route('/library')
def library():
    conn= sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM library')
    libraries = cursor.fetchall()
    conn.close()
    return render_template('libraries.html', libraries=libraries)

@app.route('/add_library', methods=['GET', 'POST'])
def add_library():
    if request.method == 'POST':
        name = request.form['name']
        created_by = request.form['created_by']
        date_of_creation = request.form['date_of_creation']
        city = request.form['city']
        country = request.form['country']
# Connect to the database and insert the new library
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO library (name, created_by, date_of_creation, city, country) VALUES (?, ?, ?, ?, ?)', (name, created_by, date_of_creation, city, country))
        conn.commit()
        conn.close()
# Redirect to the libraries page after adding the library
        return redirect(url_for('library'))
# If the request method is GET, render the add_library template
    
    return render_template('add_library.html')

@app.route('/edit_library/<int:id>', methods=['GET', 'POST'])
def edit_library(id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        # On récupère les nouvelles valeurs
        name = request.form['name']
        created_by = request.form['created_by']
        date_of_creation = request.form['date_of_creation']
        city = request.form['city']
        country = request.form['country']

        # Mise à jour dans la BDD
        cursor.execute('''
            UPDATE library
            SET name = ?, created_by = ?, date_of_creation = ?, city = ?, country = ?
            WHERE id = ?
        ''', (name, created_by, date_of_creation, city, country, id))
        conn.commit()
        conn.close()
        return redirect(url_for('library'))
    else:
        # On récupère la bibliothèque existante pour pré-remplir le formulaire
        cursor.execute('SELECT * FROM library WHERE id = ?', (id,))
        library = cursor.fetchone()
        conn.close()
        if library:
            return render_template('edit_library.html', library=library)
        else:
            return "Library not found", 404
@app.route('/delete_library/<int:id>')
def delete_library(id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM library WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('library'))

@app.route('/prices')
def prices():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM price')
    prices = cursor.fetchall()
    conn.close()
    return render_template('prices.html', prices=prices)   
@app.route('/add_price', methods=['GET', 'POST'])
def add_price():
    if request.method == 'POST':
        senegal = request.form['senegal']
        senegal_currency = request.form['senegal_currency']
        france = request.form['france']
        france_currency = request.form['france_currency']
        canada = request.form['canada']
        canada_currency = request.form['canada_currency']
        maroc = request.form['maroc']
        maroc_currency = request.form['maroc_currency']
        arabi_saoudite = request.form['arabi_saoudite']
        arabi_saoudite_currency = request.form['arabi_saoudite_currency']

        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO price (senegal, senegal_currency, france, france_currency, canada, canada_currency, maroc, maroc_currency, arabi_saoudite, arabi_saoudite_currency) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                       (senegal, senegal_currency, france, france_currency, canada, canada_currency, maroc, maroc_currency, arabi_saoudite, arabi_saoudite_currency))
        conn.commit()
        conn.close()
        
        return redirect(url_for('prices'))
    
    return render_template('add_price.html')
@app.route('/price/<int:id>', methods=['GET', 'POST'])
def price(id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        senegal = request.form['senegal']
        senegal_currency = request.form['senegal_currency']
        france = request.form['france']
        france_currency = request.form['france_currency']
        canada = request.form['canada']
        canada_currency = request.form['canada_currency']
        maroc = request.form['maroc']
        maroc_currency = request.form['maroc_currency']
        arabi_saoudite = request.form['arabi_saoudite']
        arabi_saoudite_currency = request.form['arabi_saoudite_currency']

        cursor.execute('''
            UPDATE price
            SET senegal = ?, senegal_currency = ?, france = ?, france_currency = ?, canada = ?, canada_currency = ?, maroc = ?, maroc_currency = ?, arabi_saoudite = ?, arabi_saoudite_currency = ?
            WHERE id = ?
        ''', (senegal, senegal_currency, france, france_currency, canada, canada_currency, maroc, maroc_currency, arabi_saoudite, arabi_saoudite_currency, id))
        conn.commit()
        conn.close()
        return redirect(url_for('prices'))
    else:
        cursor.execute('SELECT * FROM price WHERE id = ?', (id,))
        price = cursor.fetchone()
        conn.close()
        if price:
            return render_template('edit_price.html', price=price)
        else:
            return "Price not found", 404
@app.route('/delete_price/<int:id>')
def delete_price(id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM price WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('prices'))

# Search functionality
@app.route('/search')
def search():
    query = request.args.get('query', '')
    if not query:
        return redirect(url_for('list_books'))

    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", 
                   ('%' + query + '%', '%' + query + '%'))
    results_books = cursor.fetchall()

    conn.close()

    return render_template('search_results.html', query=query, results_books=results_books)

if __name__ == '__main__':
    app.run(debug=True)

    