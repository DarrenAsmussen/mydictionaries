import random

# Dictionaries have key value pairs. THe key will be on the left and it is always a string value, annd on the right could be anything else.
# Python is an object orriented language. Objects have attributes that describe the attributes and methods that carry out a function on the attributes.
# JSON file is a way for people to securely exchange information online

phonebook = {}
phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}


"""
print()
print('*****  start section 1 - print dictionary ********')
print()

mydictionary = dict(m=8,n=9)
print (mydictionary)


print(len(phonebook))
print(type(phonebook))



print()
print('*****  end section 1 ********')
print()



print()
print("*****  start section 2 - search dictionary ********")
print()

name = "chris"
# phone = phonebook["Chris"]
# print(phone)
if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")

print()
print("*****  end section 2 ********")
print()


print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)


phonebook["Chris"] = "555-0123"
phonebook["Joe"] = "555-4444"

print(phonebook)


print()
print("*****  end section 3 ********")
print()



print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

print(phonebook)

del phonebook["Chris"]

print(phonebook)


print()
print("*****  end section 4 ********")
print()


print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()

for k in phonebook:
    print(f"the key is {k} and the value is {phonebook[k]}")

for value in phonebook.values():
    print(value)

for key, value in phonebook.items():
    print(f"the kiey is {key} and the value is {value}")

for ph_tuple in phonebook.items():
    print(ph_tuple)

print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - using get and clear ********")
print()

phone = phonebook.get("Chris", "999")
print(phone)

phonebook.clear()
print(phonebook)


print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - using pop method ********")
print()

remove - phonebook.pop ('Chris', 'not found')
print(remove)
print(phonebook)


print()
print("*****  end section 7 ********")
print()


print()
print("*****  start section 8 - using popitem ********")
print()

a = phonebook.popitem()


print(a)
print(phonebook)


print()
print("*****  end section 8 ********")
print()


"""
print()
print("*****  start section 9 - using random and converting to list ********")
print()

phonebook_list = list(phonebook)
print(phonebook_list)
random_key = random.choice(phonebook_list)
print(random_key)
print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))])

print()
print("*****  end section 9 ********")
print()
