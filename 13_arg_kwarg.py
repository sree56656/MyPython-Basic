# *args => returns as Tuple
# we can give as many arguments as we want
#
# def myfunc(*args):
#     print(args)
#     for item in args:
#         print(item)
# #
# #
# myfunc(2, 3, 5, 7)
# myfunc1(2, 3, 5, 7, 8, 9)


# kwargs => returns as dictionary

# def myfunc(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print("My fruit is choice of {}".format(kwargs['fruit']))
#     else:
#         print('i did not find any fruit here')


# myfunc(fruit='apple', veggie = 'noodles')

# args and kwargs at a time

# def myfunc1(*args):
#     return sum(args)
#
# myfunc(2, 3, 5, 7, 8, 9)


# def myfunc(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print("My fruit is choice of {}".format(kwargs['fruit']))
#     else:
#         print('i did not find any fruit here')


# return output as list


# def myfunc2(*args):
#     output = []
#     for ele in args:
#         if ele % 2 == 0:
#             output.append(ele)
#     return output


# myfunc(3, 5, 7, fruit='apple', veggie = 'noodles')
# print(myfunc2(3, 5, 6, 7, 8))


