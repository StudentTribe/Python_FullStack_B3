
for i in range(0,3):
    uname = input("Enter your username")
    upass = input("Enter password")
    if uname == "admin" and upass == "password":
        print("Login sucess")
        break
    else:
        print("Try again")



