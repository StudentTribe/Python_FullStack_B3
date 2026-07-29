#Logical operator

# age of a person is more then 18 or not 
# height is more then 70 or not

age = 19
height = 65

print(age > 18 and height > 70)     #True  and  False => False
print(age < 18 and height < 70)     #False  and  True => False
print(age < 18 and height > 70)     #False  and  False => False
print(age > 18 and height < 70)     #True  and  True => True

print("======================================================================")

print(age > 18 or height > 70)     #True  and  False => True
print(age < 18 or height < 70)     #False  and  True => True
print(age < 18 or height > 70)     #False  and  False => False
print(age > 18 or height < 70)     #True  and  True => True