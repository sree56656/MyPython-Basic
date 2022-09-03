# Tuple() is similar to list
# difference => it is immutable (cannot change)

# Assigning and accessing
# t = (1, 2, 1,  3, 'hero')
# print(type(t))
# print(t[4])

# count => no of times appeared
t = ('a', 'b', 'c', 'b')
print(t.count('b'))
print(t.index('b'))  # gives first appeared
# t[0] = 'j' # cannot modify values inside tuple
