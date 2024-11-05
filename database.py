import sqlite3

def get_db_connection():
    conn = sqlite3.connect('chocolate_house.db')
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        available_from TEXT,
        available_until TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_suggestions (
        id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL,
        flavor_suggestion TEXT,
        allergies TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

def insert_seasonal_flavor(name, description, available_from, available_until):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO seasonal_flavors (name, description, available_from, available_until)
    VALUES (?, ?, ?, ?)
    ''', (name, description, available_from, available_until))
    conn.commit()
    conn.close()

def insert_ingredient(name, quantity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO ingredients (name, quantity)
    VALUES (?, ?)
    ''', (name, quantity))
    conn.commit()
    conn.close()

def insert_customer_suggestion(customer_name, flavor_suggestion, allergies):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergies)
    VALUES (?, ?, ?)
    ''', (customer_name, flavor_suggestion, allergies))
    conn.commit()
    conn.close()

def fetch_seasonal_flavors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM seasonal_flavors')
    flavors = cursor.fetchall()
    conn.close()
    return flavors

def fetch_ingredients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ingredients')
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients

def fetch_customer_suggestions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customer_suggestions')
    suggestions = cursor.fetchall()
    conn.close()
    return suggestions