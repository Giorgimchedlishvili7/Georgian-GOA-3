info = {
    "name" : "Giorgi",
    "date" : "9/12/2014",
    "age" : "11"
}

name_sum = info.get("name")

print (name_sum)

dateofbirth = info["date"]
print(dateofbirth)

age_sum = info.get("age")
print(age_sum)

vaules_all = info.values()
print(vaules_all)

all_keys = info.keys()
print(all_keys)

all_items = info.items()
print(all_items)