# dictionary - key value pair

emp_deatils = {"name" : "Raju" , "id" : "007" , "age" : 35}

print(emp_deatils)
print(type(emp_deatils))
print(emp_deatils["name"])
print(emp_deatils.get("name"))

print(emp_deatils["id"])
print(emp_deatils["age"])

emp_deatils["id"] = "123"
print(emp_deatils)