mylist = []
mystring = "Hello"

# for letter in mystring:
#     mylist.append(letter)
# print(mylist)
#
# mylist = [letter for letter in mystring]
# print(mylist)
#
# num_list = [num for num in range(1, 9)]
# print(num_list)
#
# num_list1 = [num for num in range(1, 11) if num % 2 == 0]
# print(num_list1)
#
# celcius = [0, 10, 20, 34.5]
# farengeit = [(9/5 * temp + 32) for temp in celcius]
# print(farengeit)

# st = 'Print only the words that start with s in this sentence'
# list = st.split(" ")
# for element in list:
#     if element[0] == 's':
#         print(element)

#  print all even numbers between 0 to 10
# for i in range(1,11):
#     if i%2 == 0:
#         print(i)

# list of all numbers b/w 1 and 50 that are divisible by 3
# num_list = [n for n in range(1, 50) if (n % 3 == 0)]
# print(num_list)


# print range of num b/w 1 and 100, if num/3 ==0 print Fizz if num/5 == 0 print Buzz if num/3 and num/5 ==0 print FizzBuzz
# mylist = []
# for i in range(1,101):
#     if i % 3 == 0:
#         if (i % 3 == 0) and (i % 5 == 0):
#             mylist.append("FizzBuzz")
#         else:
#             mylist.append('Fizz')
#     elif i % 5 == 0:
#         mylist.append('Buzz')
#     else:
#         mylist.append(i)
#
# print(mylist)


# st = 'Print only the words that start with s in this sentence'
# st_list = st.rsplit(" ")
# print(st_list)
# new_list = []
# for word in st_list:
#     if len(word) % 2 == 0:
#         new_list.append("even!")
#     else:
#         new_list.append(word)
#
# print(word)