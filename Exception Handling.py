import json
import os

Library_file = 'library_data.json'


def load_library():
    if not os.path.exists(Library_file):
        return {}
    try:
        with open(Library_file, 'r') as fMegha:
            return json.load(fMegha)
    except Exception as e:
      print("error loading library data:-", {e})
      return {}

def save_library(library):
    try:
        with open(Library_file, 'w') as fMegha:
            json.dump(library, fMegha)

    except Exception as e:
        print(F"Error saving library data:- {e}")
        
def add_book(library, title, author, quantity):
    if title in library:
        print("Book already exists. updating the quantity.")
        library[title]['quantity'] += quantity
    else:
        library[title] = {'author' : author, 'quantity': quantity, 'borrowed_by':None}

    save_library(library)
    print(F"Book '{title}' added successfully!")


#Function to view all books in the library 
def view_books(library):
    if not library:
        print("th")
 


    







    