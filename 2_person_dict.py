person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
print("children"[1])
# print out the name of the cat


# iterate through all children and print out each child
for children in person:
    print(f"")

# print out the pets in this formate:
# type of pet: dog name of pet: Fido
