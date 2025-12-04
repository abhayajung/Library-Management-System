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
                    book_id,title,author,quantity=line.split()
                    
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
register_user(users_dict)