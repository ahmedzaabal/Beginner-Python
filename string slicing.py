# Slicing = creating a substring by extracring elemets from another string
#           indexing[] or slice()
#           [start:stop:step]


name = "Ahmed Adel"

first_name = name[:5]
last_name = name[6:]

funky_name = name[::2]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website1 = "http://facebook.com"
sliced = slice(7, -4)
print(website1[sliced])


website2 = "http://wikipedia.com"
print(website2[sliced])