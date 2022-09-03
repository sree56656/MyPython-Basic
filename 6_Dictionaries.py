# dictionary{} = 'key':'value' pair
# unordered and can not be sorted

# accessing value with key
# my_dict = {'key1':'value1', 'key2':'value2'}
# print(my_dict['key1'])
# prices = {'apple': 100, "oranges" : 90.8}
# print(prices['apple'])

# dictionary inside dictionary
# d = {'k1':123, 'k2':[0,1,'k',4], 'k3':{'insidekey': 100}}
# print(d['k2'])
# print(d['k2'][2].upper())
# print(d['k3']['insidekey'])

# adding new pair to dictionary and overwriting values
# my_dict = {'k1': 'value1', 'k2': 'value2'}
# my_dict['k3'] = 'value3'
# print(my_dict)
# my_dict['k2'] = 'hundred'
# print(my_dict)

dict1 = {}
for i in range(1, int(input())):
    dict1[i] = i * i

print(dict1)
