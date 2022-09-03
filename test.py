# def makes_twenty(a, b):
#     if a == 20 or b == 20:
#         return True
#     elif a + b == 20:
#         return True
#     else:
#         return False
#
#
# print(makes_twenty(20, 10))
# print(makes_twenty(10, 10))
# print(makes_twenty(30, 10))


#  1st and 4th letter capitalize

# def old_macdonald(word):
#     first_letter = word[0]
#     in_between = word[1:3]
#     fourth_letter = word[3]
#     final = word[4:]
#     return first_letter.upper() + in_between + fourth_letter.upper() + final
#
#
# print(old_macdonald("macdonald"))


# def master_yoda(word):
#     words = word.split(" ")
#     reverse_word = words[::-1]
#     print(" ".join(reverse_word))
#
#
# master_yoda("I am home")


def fizzBuzz(s):
    if s%3 == 0 and s%5 ==0:
        print("FizzBuzz")
    elif s%3 == 0 and s%5 !=0:
        print("Fizz")
    elif s%3 != 0 and s%5 ==0:
        print("Buzz")
    else:
        print("i")

if __name__ == '__main__':
    s = int(input().strip())

    fizzBuzz(s)