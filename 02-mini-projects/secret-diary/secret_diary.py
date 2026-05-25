
def create_password():
    user_password = input("enter the password")
    with open ("pass.txt" ,"w") as passwd : 
     passwd.write(user_password)

    print("your password is created successfully")
   
    

def write_secret_note():
    password = input("enter your password ")
    with open ("pass.txt","r") as passwd :
     saved_pass = passwd.read()

    if password == saved_pass:
        note = input(" enter your secret note")
        with open ("data,txt","w") as data :
         data.write(note)

    else :
        print("invalid password")

def read_secret_note():
    password = input("enter your password ")
    with open ("pass.txt","r") as passwd :
      saved_pass = passwd.read()

    if password == saved_pass:
        
        with open ("data,txt","r") as data :
         print(data.read())

    else :
        print("invalid password")



while True:
    
    print(""" 
    1. create a password
    2. write your secret note
    3. read your secret note
    4. exit""")

    c = int(input("enter your choice: "))

    if c == 1:
        create_password()
    elif c == 2:
        write_secret_note()
    elif c == 3:
        read_secret_note()
    elif c == 4:
        break
    else :
        print("invalid Choice")
        


