# e-commerce - 110011
# WAP to ask for pincode - if the pincode is not 110011
# ask for the pincode once again saying we don't deliver at given location

pincode = input("Enter your pincode to deliver the product")

while pincode != "110011":
    print("We are currently not delivering in that location, Try again")
    pincode = input("Enter your pincode to deliver the product")
else:
    print("Product will be delivered in 2 days")