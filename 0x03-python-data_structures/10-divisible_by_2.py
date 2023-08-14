#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Identify elements divisible by 2 in a list."""
    divisibility_flags = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divisibility_flags.append(True)
        else:
            divisibility_flags.append(False)

    return divisibility_flags
