import database
import datetime

menu = """What would you like to do?
        1) Enter a new note
        2) Display all note
        3) Search notes by category
        4) Search note by labels
        5) Exit
Your choice: """

database.create_table()
user_input = input(menu)

def prompt_new_note():
    cat = input("Note category: ")
    lab = input("Note label: ")
    content = input("Enter your note: ")
    database.note(content)
    database.category(cat)
    database.label(lab)

def show_note():
    notes = database.display()
    for note in notes:
        print(f"""{note[0]} | {note[1]} 
-------------------------------------------  
{note[2]}
-------------------------------------------\n\n""")

def show_search_result():
    cat = input("Enter the category your are looking for: ")
    search_result = database.search_cat(cat) 
    for search in search_result:
        print(f"""\n{search[0]} | {search[1]} 
-------------------------------------------  
{search[2]}
-------------------------------------------\n\n""")

def show_label_search():
    lab = input("Enter the label you are looking for: ")
    search_result = database.search_lab(lab)
    for search in search_result:
        print(f"""\n{search[0]} | {search[1]} 
-------------------------------------------  
{search[2]}
-------------------------------------------\n\n""")
            

    


while user_input !="5":
    if user_input =="1":
        prompt_new_note()
    elif user_input =="2":
        show_note()
    elif user_input == "3":
        show_search_result()
    elif user_input == "4":
        show_label_search()        
    user_input = input(menu)


