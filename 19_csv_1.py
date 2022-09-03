import csv

# open the file
data = open('example.csv', encoding='utf-8')

# csv.reader
csv_reader = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_reader)
print(data_lines[0])

# printing in lines and accessing elements
for line in data_lines[:5]:
    print(line[5])

# merging two boxes into one
full_names = []
for line in data_lines:
    full_names.append(line[1] + " " + line[2])
print(full_names)

# writing into file
file_to_output = open("to_save_file.csv", mode='w', newline = '')
csv_writer = csv.writer(file_to_output, delimiter = ",")
csv_writer.writerow(['1', '2', '3'])
csv_writer.writerows([['a', 'b', 'c'], ['x', 'y', 'z']])
file_to_output.close()


