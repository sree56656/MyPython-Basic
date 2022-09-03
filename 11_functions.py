# return True if any number is even inside  a list      #tuple # list

# return [element for element in lists if element % 2 == 0
def check_even_list(lists):
    for ele in lists:
        if ele % 2 == 0:
            return True
        else:
            pass
    return False


# return even numbers as a list

# even_num = []
#
#
# def check_even(lists):
#     for element in lists:
#         if element % 2 == 0:
#             even_num.append(element)
#         else:
#             pass
#     return even_num
#
#
# # print(check_even_list([1, 3, 7, 9]))
# print(check_even([1, 3, 7, 9, 4, 6]))

# unpacking TUPLE

work_hours = [('abby', 00), ('billy', 4000), ('sam', 500)]


def employee_check(hours):
    emp_name = ""
    no_of_hours = 0
    for name, hrs in hours:
        if hrs > no_of_hours:
            no_of_hours = hrs
            emp_name = name
        else:
            pass

    return emp_name, no_of_hours


print(employee_check(work_hours))