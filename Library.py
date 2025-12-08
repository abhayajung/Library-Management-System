# Library Management System

# Creating two file to store user information and books information permanently.
import os
 
if not os.path.exists('users.txt'):
    with open('users.txt','w') as f:
        pass
if not os.path.exists('books.txt'):
    with open('books.txt','w') as f:
        pass

def load_user():
    users_dict={}
    try:
        with open ('users.txt','r') as f:
            for line in f:
                line=line.strip()
                if line:
                    username,password=line.split(',')
                    users_dict[username]=password
    except FileNotFoundError:
        print("File not found")
    return users_dict

def load_books():
    books_list=[]
    try:
        with open('books.txt','r') as f:
            for line in f:
                line=line.strip()
                if line:
                    book_id,title,author,quantity=line.split(",")
                    
                    book={
                        'id':book_id,
                        'title':title,
                        'author':author,
                        'quantity':int(quantity)
                    }
                    books_list.append(book)
    except FileNotFoundError:
        print("File not found")
    return books_list

def get_existing_books_id(books_list):
    #Create a set to store all the ids of the books 
    book_ids=set()
    for book in books_list:
        #dictionery
        book_ids.add(book['id'])
    return book_ids

#User Register
def register_user(users_dict):
    print("\n------Register a new user------")
    username=input("Enter the username: ").strip()
    password=input("Enter the password: ").strip()
    if username in users_dict:
        print(f"username alresdy exists!")
        return False
    if not username or not password:
        print("Username and password can not be empty")
        return False
    users_dict[username]=password
    
    with open('users.txt','a') as f:
        f.write(f"{username},{password}\n")
    print("Registration Successfull")
    return True

users_dict=load_user()
# print(users_dict)
register_user(users_dict)

def login_user(users_dict):
    print("\n" \
    "")
    username = input("Enter username:  ").strip()
    password = input("Enter password:  ").strip()

    if username in users_dict and users_dict[username] == password:
        print(f"Wecome! {username.capitalize()}")
        return username
    else:
        print("Invalid Username or Password! ")
        return None
    
login_user(users_dict)
    

### Now books operation start
### Main menu function
def main_menu():
    """Display main menu options"""
    print("="*55)
    print("\n" \
    "Library Management system")
    print("="*55)
    print("1. ADD BOOK")
    print("2. VIEW BOOK")
    print("3. SEARCH")
    print("4. ISSUE")
    print("5. RETURN BOOK")
    print("6. LOGOUT")
    print("="*55)

# main_menu()


# ADD BOOK
def add_book(books_list, book_ids):
    """ADD A NEW BOOK TO THE LIBRARY"""
    print("\n" \
    "------ ADD NEW BOOK -----")
    book_id = input("Enter the book ID: ").strip()

    if book_id in book_ids:
        print("Book id already exists")
        return
    
    title = input("Enter the book title:").strip()
    author = input("Enter the author:  ").strip()
    quantity = int(input("Enter the quantity:  ").strip())

    new_book = {
        "id" : book_id,
        "title" : title,
        "author" : author,
        "quantity" : quantity
    }

    books_list.append(new_book)
    book_ids.add(book_id)

    with open("books.txt", 'a') as f:
        f.write(f"{book_id},{title},{author},{quantity}\n")

    print("Book added successfull")

books_list = load_books()
book_ids = get_existing_books_id(books_list)
# print(books_list)
# print(book_ids)
add_book(books_list, book_ids)

### function to view all the books in the library
def view_books(books_list):
    """Display all the books in the library"""
    print("\n" \
    "------ ALL BOOKs IN LIBRARY -------")
    if not books_list:
        print("No books found in library")
        return
    for book in books_list:
        print(f"{book['id']} | {book['title']} | {book['author']} | {book['quantity']}")

view_books(books_list)
    

def search_books(books_list):
    print("-"*30)
    print("\n----- Search the book  -----")
    search_item = input("Enter the title : ").strip().lower()
    found_item = []
    for book in books_list:
        if search_item in book['title'] or search_item in book['author']:
            found_item.append(book)
    if found_item:
        print(f"Found {len(found_item)} books")
        view_books(found_item)
    else:
        print("No books are available")


### Save books to the files
def save_books(books_list):
    """Write all books back to the books.txt"""
    with open("books.txt" , "w" ) as f:
        for book in books_list:
            f.write(f"{book['book_id']}\t |{book['title']}\t |{book['author']} \t |{book['quantity']}\n")
        

### Issue book --> User le library bata book lanu

def issue_book(books_list):
    book_ids = input("Enter the book id to issue: ").strip()
    for book in books_list:
        if book['book_id'] == book_ids:
            if book['quantity'] > 0 :
                book['quantity'] -= 1
                save_books(books_list)
                print(f"Book {book['title']} issued successfully !! ")
                print(f"Remaning quantity:  {book['quantity']} !! ")
                return
            else:
                print("Out of stock books !!")
                return 

    print("Book id not found")

def return_books(books_list):
    """Return a book to user"""
    book_id = input("Enter the book id to return : ").strip()
    for book in books_list:
        if book_id == book['book_id']:
            book['quantity'] += 1
            save_books(books_list)
            print(f"Book {book['title']} return successfully !! ")
            print(f"Current quantity : {book['quantity']}")
            return 
        
    print("Book id not found")

#### Main function --> Control overall workflow

def main():
    """Main program loop"""
    user_dict = load_user()
    print("-"*50)
    print("Welcome to Library Management System")
    print("-"*50)

    while True:
        print('''
            1.Register
            2.Login
            3.Exit
        ''')
        choice = input("Enter the choice(1,2,3) : ").strip()
        if choice == '1':
            register_user(user_dict)
        elif choice == '2':
            username = login_user(user_dict)
            if username:
                books_list = load_books()
                book_ids = get_existing_books_id(books_list)
                
                while True:
                    main_menu()
                    menu_choice = input("Enter choice(1-6): ").strip()
                    if menu_choice == "1":
                        add_book(books_list,book_ids)
                    elif menu_choice == "2":
                        view_books(books_list)
                    elif menu_choice == "3":
                        search_books(books_list)
                    elif menu_choice == "4":
                        issue_book(books_list)
                    elif menu_choice == "5":
                        return_books(books_list)
                    elif menu_choice == "6":
                        print(f"Bye {username.capitalize()}")
                        break
                    else:
                        print("Invalid choice")
        
        elif choice == '3':
            print("Thank you for using my library management system ")
            break

                    
main()

















