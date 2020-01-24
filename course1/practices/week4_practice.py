#!/usr/bin/env python3.7


def factorial(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result


# recursive practice
''' Base to recursion
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
'''


def recursive_factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def push_recurse(n):
    if n < 1:
        return 0
    return n + push_recurse(n - 1)


print(push_recurse(30))


def counter(start, stop):
    x = start
    if start > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x += 1
    return return_string


print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"


def loop(start, stop, step):
    return_string = ""
    if step == 0:
        if start > stop:
            step = -1
        else:
            step = 1
    if start > stop:
        step = abs(step) * -1
    else:
        step = abs(step)
    for count in range(start, stop, step):
        return_string += str(count) + " "
    return return_string.strip()


print(loop(11, 2, 3))  # Should be 11 8 5
print(loop(1, 5, 0))  # Should be 1 2 3 4
print(loop(-1, -2, 0))  # Should be -1
print(loop(10, 25, -2))  # Should be 10 12 14 16 18 20 22 24
print(loop(1, 1, 1))  # Should be empty
