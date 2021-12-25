# sene list verilir ededlerden ibaret hemin listin icersinde olan cut ededlerin cemini hesablamaq

digits=[5,7,8,10,22,12,15,13,21,24,30,31]

sum=0

for digit in digits:
    if digit%2==0:
        sum=sum+digit

print(sum)
