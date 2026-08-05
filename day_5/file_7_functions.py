
def login(username , userpassword):
    if username == "admin" and userpassword == "password":
        return True
    else:
        return False

for i in range(0,3):
    uname = input("Enter user name")
    upass = input("enter password")
    status = login(uname , upass)
    if status == True:
        print("Login sucess")
break