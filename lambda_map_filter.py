# map(function, iterable_list)
#
# def square(num):
#     return num**2
#
#
# mynum = [1, 2, 3, 4, 5]
#
# for item in map(square, mynum):
#     print(item)
# print(list(map(square, mynum)))

# even num printing

# mynum = [1, 2, 3, 4, 5]
#
#
# def check_even(num):
#     return num % 2 == 0
#
#
# print(list(filter(check_even, mynum)))

# ************************************************************
# mynum = [1, 2, 3, 4, 5]
# square = list(map((lambda num: num**2), mynum))
#
# # square = lambda num: num**2
# print(square)
# ************************************************************
# mynum = [1, 2, 3, 4, 5]
# square = list(filter(lambda num: num % 2 == 0, mynum))
# print(square)
# **************************************************************
# names = ['Andy', 'penny', 'sally']
# first = list(map(lambda name: name[0], names))
# print(first)
# ***************************************************************

# Creating an empty dict
dict1 = {}
for i in range(1, int(input())):
    dict1[i] = i * i

print(dict1)
