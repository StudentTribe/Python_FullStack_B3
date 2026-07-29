uname = input("Enter your username")
upass = input("Enter password")

# Write a logic to compare both user user name & password
# username - admin
# password - password
# if both are correct print login success else print try again
# in case credentials are incorrect user should get more chances

while uname != "admin" or upass != "password":
    print("Try again")
    uname = input("Enter your username")
    upass = input("Enter password")
else:
    print("Login Sucess")