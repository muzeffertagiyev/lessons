digits=[3,42,500,301,405,403,501,3,200]

max=digits[0]
min=digits[0]

for digit in digits:
    if max<digit:
        max=digit
    if min>digit:
        min=digit
print(min*max)        
