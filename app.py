import database

menu = """What would you like to do?
        1) Enter a new note
        2) Display all note
        3) Search notes by category
        4) Search notes by labels
        5) Search keywords
        6) Exit
Your choice: """

database.create_table()
user_input = input(menu)

cat_operation = {1:"Statistics", 2:"data science", 3:"cybersecurity", 4:"networking",5:"linux" }

def prompt_new_note():
    cat = input("""1.Statistics 
2.data science
3.cybersecurity
4.networking
5.linux
Category of this note: """)
    lab = input("Note label: ")
    content = input("Enter your note: ")
    database.note(cat_operation[int(cat)], lab, content)

def show_note():
    notes = database.display()
    for note in notes:
        print(f"""{note[2]} | {note[3]}                           on {note[1]} 
-------------------------------------------  
{note[4]}
-------------------------------------------\n\n""")

def show_cat_search():
    cat = input("Enter the category your are looking for: ")
    search_result = database.search_cat(cat) 
    for search in search_result:
        print(f"""\n{search[1]} | {search[2]} | {search[3]} 
-------------------------------------------  
{search[4]}
-------------------------------------------\n\n""")

def show_label_search():
    lab = input("Enter the label you are looking for: ")
    search_result = database.search_lab(lab)
    for search in search_result:
        print(f"""\n{search[1]} | {search[2]} | {search[3]} 
-------------------------------------------  
{search[4]}
-------------------------------------------\n\n""")
            
def show_keyword_search():
    keyword = input("Enter a keyword: ")
    search_result = database.search_keyword(keyword)
    for search in search_result:
        print(f"""\n{search[1]} | {search[2]} | {search[3]} 
-------------------------------------------  
{search[4]}
-------------------------------------------\n\n""")

    


while user_input !="6":
    if user_input =="1":
        prompt_new_note()
    elif user_input =="2":
        show_note()
    elif user_input == "3":
        show_cat_search()
    elif user_input == "4":
        show_label_search()        
    elif user_input == "5":
        show_keyword_search()        

    user_input = input(menu)


