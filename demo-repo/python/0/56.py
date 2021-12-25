#listin maxini hesablayan proqram


def find_max(list):
    max=list[0]
    for digit in list:
        if max<digit:
            max=digit
    return max
print(find_max([5,6,32,4,235,500,700]))        

