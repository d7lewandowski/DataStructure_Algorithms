def is_valid(combination):

    diff = 0

    for par in combination:
        if par == '(':
            diff += 1 
        else:
            if diff == 0:
                return False
            else:
                diff -= 1
    
    return diff == 0 

# print(is_valid("((())))"))

assert False == is_valid("((())))")
assert True == is_valid("((()))")

