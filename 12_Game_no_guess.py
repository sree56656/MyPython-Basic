from random import randint, shuffle

# Shuffle function

# example = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# shuffle(example)
# print(example)
# print(randint(1, 100))


# def shuffle_function(ex):
#     shuffle(ex)
#     return ex
#
#
# res = shuffle_function(example)
# print(res)

# player guess

def player_guess():
    target = ""
    while target not in range(1, 9):
        target = randint(1, 9)
        print("num is generated!! \n its your turn")
    return int(target)


def check_guess(guess1, chance):
    if guess1 == guess:
        print("Congrats!!!!!!!!!! success")
    else:
        print("OOPs!!! wrong guess")


fun1 = player_guess()
guess = 0
while fun1 != guess:
    guess = int(input("enter your guess : "))
    check_guess(fun1, guess)
