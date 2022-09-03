def user_choice():
    choice = "wrong"
    acceptable_range = range(0, 9)
    while choice.isdigit() == False:
        choice = input("Enter a number (0-10) : ")
        if choice.isdigit() == True:

        if choice.isdigit() == False:
            print("that is not a digit!!")
    return int(choice)

print(user_choice())