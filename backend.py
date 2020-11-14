import sqlite3

def connect():
    """ Establish connection to database file """
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year, isbn):
    """ adds book record to databse """
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year, isbn))
    conn.commit()
    conn.close()

def view(widget):
    """ displays the books in the database in the listbox widget  """
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    widget.delete(0, "end")
    for book in rows:
        widget.insert("end", book)

def update(id, widget, title, author, year, isbn):
    """ update the selected row """
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()
    view(widget)

def delete(id, widget):
    """ deletes selected row """
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id = ?", (id,))
    conn.commit()
    conn.close()
    view(widget)

def search(widget, title = "", author = "", year ="", isbn = ""):
    """ search and display query """
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * from book WHERE title = ? or author = ? or year = ? or isbn = ?",(title, author, year, isbn))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    widget.delete(0, "end")
    for book in rows:
        widget.insert("end", book)
