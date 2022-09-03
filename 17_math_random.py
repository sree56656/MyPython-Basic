import math
import random
import pdb
import re
# import Numpy

# value = 6.55
# print(math.floor(value))
# print(math.ceil(value))
# print(round(value))
# print(math.pi)
# print(math.log(math.e))
#
# print(random.randint(10, 50))
#
# random.seed(3)
# print(random.randint(10, 50))

text = 'the agent phone number is 408-444-1234. phone call soon!'
print('phone' in text)
# pattern = 'number is'
# print(re.search(pattern, text))
# print(re.search(pattern, text).span())
# print(re.search(pattern, text).start())

# for match in re.finditer('phone', text):
#     print(match.group())

pattern = re.search(r'(\d{3})-(\d{3})-(\d{4})', text)
print(pattern.group())
print(re.compile(pattern.group(1)))

