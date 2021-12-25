#list verilir bu listdeki butun ededler iki reqemledi.listdeki butun reqemlerin cemini hesablamaq.


digits=[24,46,33,80,41,50,64,70,48]

sum=0

for digit in digits:
    eded1=digit%10
    eded2=digit//10

    sum=sum+eded1+eded2
    

print(sum)    