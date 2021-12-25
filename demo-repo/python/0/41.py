digits=[3,5,6,2,1,3,12,11,10,9,10,11,20]

i=0
x=0
y=0
while i<len(digits):
    if digits[i]%2==0:
        x=x+1
        
    else:
        y=y+1
        
        
    i=i+1
print(x*y)
     
