# listde cut indexli ededlerin cemini tek indexli ededlerin hasilini hesablayan proqram

digits=[5,7,6,10,2]

sum_cut=0
sum_tek=1


for index in range(len(digits)):
    if index%2==0:
        sum_cut=sum_cut+digits[index]
    else:
        sum_tek=sum_tek*digits[index]
print(sum_cut)
print(sum_tek)        
