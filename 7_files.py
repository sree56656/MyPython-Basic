

# opening file
# file = open("myfile.txt", 'r+')
# file.write("this is the fourth line")
# file.seek(0)
# print(file.read())
# file.close()

# opening file and reading
# file = open("D:/text.txt", 'r')  # opening with absolute path
# print(file.readlines()[2])
# for line in file:
#     print(line)
# file.close()

#  another mode of opening
with open("D:/text.txt", 'r+') as file:  # with open automatically closes the file
    print(file.read())
    file.write("\nthis is a fourth line")
    contents = file.read()
    print(contents)




