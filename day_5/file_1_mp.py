menu = {
    "chai": 10, 
    "samosa": 15, 
    "coffee": 20,
    "lassi" : 25
    }

order = ["chai", "chai", "samosa" , "lassi"]

total = 0

for item in order:
    #print(item , menu[item])
    total = total + menu[item]

print("Total: Rs", total , "Total orderd items-" , len(order))           # 35

for item,price in menu.items():
    print(item , "-" , price)

# 1. Add lassi at Rs 25 to the menu, and order one.
# 2. Also print how many items were ordered, using len(order).
# 3. Print each item with its price on its own line, using the for loop and the menu.