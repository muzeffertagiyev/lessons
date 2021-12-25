digits=[3,5,6,2,1,3,12,11,10,9,10]
empty_lst1=[]
empty_lst2=[]

i=0

while i<len(digits):
    if digits[i]%2==0:
        empty_lst1.append(digits[i])
    else:     
        empty_lst2.append(digits[i])
    i=i+1    
print(len(empty_lst1)*len(empty_lst2))
    

      
       