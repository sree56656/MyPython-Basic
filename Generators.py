# Decorators : we can return functions and we can have function arguments


# def hero():
#     return "My hero is chiru"
#
#
# def Heroine(some_func):
#     return some_func + ",  My heroine is nana!!!"
#
#
# print(Heroine(hero()))


#  new code

def new_decorartor(original_func: object) -> object:
    def wrap_func():
        print("Before decorator")
        original_func()
        print("After decorator")
    return wrap_func()


@new_decorartor
def func_needs_gen():
    print("func is generated")

new_decorartor(func_needs_gen)
