uname = input("Enter your username")
upass = input("Enter password")

# Write a logic to compare both user user name & password
# username - admin
# password - password
# if both are correct print login success else print try again

if uname == "admin" and upass == "password":
    print("Login Success")
else:
    print("Login failed")