# sene list verilir eger listdeki elementlerin cemi 20den cox olarsa o zaman loopdan cixmaq 


digits=[3,6,7,9,10,22,11,3]

sum=0

for digit in digits:
    sum=sum+digit
    if sum>20:
        break
print(sum)


