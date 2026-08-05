

login = lambda username , userpassword : True if username == "admin" and userpassword == "password" else False

for i in range(0,3):
    uname = input("Enter user name")
    upass = input("enter password")
    if login(uname , upass) == True:
        print("Login success")
        break