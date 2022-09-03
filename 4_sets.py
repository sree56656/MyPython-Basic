# set() won't allow duplicates

# myset = set()
# print(myset)
# myset.add(1)
# print(myset)
# myset.add(2)
# print(myset)
# myset.add(2)  # adding again won't allow
# print(myset)

# set gives output in sort order without allowing duplicates
mylist = [1, 1, 1, 5, 5, 5, 4, 4, 4, 8, 4, 5, 4, 6]
print(set(mylist))
print(type(set(mylist)))