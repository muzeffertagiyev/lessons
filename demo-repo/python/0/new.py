#listin maxini hesablayan proqram


def find_max(*numbers):
    max=numbers[0]
    for digit in numbers:
        if max<digit:
            max=digit
    return max
print(find_max(5,6,32,4,235,500))        

