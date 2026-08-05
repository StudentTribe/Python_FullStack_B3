
def login(username , userpassword):
    if username == "admin" and userpassword == "password":
        print("login success")
    else:
        print("login failed")

for i in range(0,3):
    uname = input("Enter user name")
    upass = input("enter password")
    print(login(uname , upass))