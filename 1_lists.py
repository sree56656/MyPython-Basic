# slicing and indexing works similar to string
# list-> can change an element but string can't

# append
# my_list_1 = ["string", "chitti", "swapna", "sree", "snigdha", "super"]
# my_list_1.append("seen")
# popped_item_middle = my_list_1.pop(1) # remove string in middle
# print(my_list_1)
# print(my_list_1[3])
# print(len(my_list))

# pop
# popped_item = my_list_1.pop()
# print(my_list_1)
# print("popped item is {}".format(popped_item))
# popped_item_middle = my_list_1.pop(1) # remove string in middle
# print(my_list_1)

# sort
import collections

new_list = ['a', 'h', 'b', 'p', 'c', 'b']
print(collections.Counter(new_list))
# num_list = [4,1,9,5]
# print(type(num_list))
# num_list.sort()
# print(num_list)
# new_list.sort()
# print(new_list)

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
list1=[]
for i in range(1,int(input())+1):
    list1.append(int(i*i))
new = enumerate(list1, 1)
print(dict(new))


# dictn = zip(new_list, num_list)
# print(dict(dictn))


# reverse
# num_list = [4,1,9,5]
# num_list.reverse()
# print(num_list)






