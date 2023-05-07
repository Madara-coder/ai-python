# Using of the dictionaries in python

customer = {
    "name": "Debrath Sharma",
    "age": 19,
    "is_verified": True
}

print(customer)

print(customer["name"])

print(customer.get("age"))# helps to get the key from the dictionary named customer


customer["name"] = "Esdeath Sharma"
print(customer.get("name"))

customer["birthdate"] = "Jan 1 2002"
print(customer.get("birthdate"))