import tkinter as tk
import backend as bd

root = tk.Tk()

root.title("BookStore")
root.configure(bg = "powderblue")

def select():
    """ returns the selected row of listbox widget  """
    return textBox.get(textBox.curselection())
    
def viewCommand():
    """ displays the books in the database in the listbox widget  """
    listOfBooks = bd.view()
    textBox.delete(0, "end")
    for book in listOfBooks:
        textBox.insert("end", book)

def close():
    """ closes the window """
    root.destroy()

def delete():
    """ deletes selected row """ 
    id = select()[0]
    bd.delete(id)
    viewCommand()
    
def search(title = "", author = "", year ="", isbn = ""):
    """ search and display query """
    listOfBooks = bd.search(title, author, year, isbn)
    print(listOfBooks)
    textBox.delete(0, "end")
    for book in listOfBooks:
        textBox.insert("end", book)
        print("Search")

def show(*event):
    """ shows the selected row in their entries"""
    titleInput.set(select()[1])
    yearInput.set(select()[2])
    authorInput.set(select()[3])
    isbnInput.set(select()[4])

def update():
    """ update the selected row """
    bd.update(select()[0],titleInput.get(),authorEntry.get(),yearEntry.get(), isbnEntry.get())
    viewCommand()

title = tk.Label(root, text = "Title", font = ("Arial", 13))
title.grid(row = 0, column = 0)

author = tk.Label(root, text = "Author", font = ("Arial", 13))
author.grid(row = 0, column = 2, sticky = "E")

year = tk.Label(root, text = "Year", font = ("Arial", 13))
year.grid(row = 1, column = 0)

isbn = tk.Label(root, text = "ISBN", font = ("Arial", 13))
isbn.grid(row = 1, column = 2, sticky = "E")

titleInput = tk.StringVar()
titleEntry = tk.Entry(root, textvariable = titleInput)
titleEntry.grid(row = 0, column = 1, sticky = "w")

yearInput = tk.StringVar()
yearEntry = tk.Entry(root, textvariable = yearInput)
yearEntry.grid(row = 1, column = 1, sticky = "w")

authorInput = tk.StringVar()
authorEntry = tk.Entry(root, textvariable = authorInput)
authorEntry.grid(row = 0, column = 3)

isbnInput = tk.StringVar()
isbnEntry = tk.Entry(root, textvariable = isbnInput)
isbnEntry.grid(row = 1, column = 3)

textBox = tk.Listbox(root, width = 30, height = 8)
textBox.bind("<<ListboxSelect>>", show)
textBox.grid(row = 2, column = 0, rowspan = 5, columnspan = 2, pady = 10, padx = 10 )

scrollBar = tk.Scrollbar(root)
scrollBar.grid(row = 3, column = 2, rowspan = 2)

textBox.configure(yscrollcommand = scrollBar.set)
scrollBar.configure(command = textBox.yview)

view = tk.Button(root, text = "View All", width = 13, bd = 3, command = viewCommand)
view.grid(row = 2,column = 3, pady = 0)

searchEntry = tk.Button(root, text = "Search Entry", width = 13, bd = 3,
                        command = lambda: search(titleInput.get(),authorEntry.get(),yearEntry.get(), isbnEntry.get()))
searchEntry.grid(row = 3,column = 3, pady = 0)

addEntry = tk.Button(root, text = "Add Entry", width = 13, bd = 3,
                     command = lambda:bd.insert(titleInput.get(),authorEntry.get(),yearEntry.get(), isbnEntry.get()))
addEntry.grid(row = 4,column = 3, pady = 0)

updateSelected = tk.Button(root, text = "Update Selected", width = 13, bd = 3, command = update)
updateSelected.grid(row = 5,column = 3, pady = 0)

deleteSelected = tk.Button(root, text = "Delete Selected", width = 13, bd = 3,
                           command = delete)
deleteSelected.grid(row = 6,column = 3, pady = 0)

close = tk.Button(root, text = "Close", bg = "Red", width = 13, bd = 3, command = close)
close.grid(row = 7,column = 3, pady = 0)


root.mainloop()
