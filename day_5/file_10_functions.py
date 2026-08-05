def form_deatils(name,age,weight):
    return {
        "Name" : name,
        "Age" : age,
        "Weight" : weight
    }

print(form_deatils("Arun", 22, 50))
print(form_deatils(age = 22, weight = 50, name = "Jai"))
