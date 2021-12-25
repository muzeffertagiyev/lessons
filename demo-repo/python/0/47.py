diaqonal1=0
diaqonal2=0

for x in range(1,4):
     for y in range(1,4):
          if x==y:
               diaqonal1=diaqonal1+x
          if x==(4-y):
               diaqonal2=diaqonal2+x     
print(diaqonal1*diaqonal2)               






#lst=[[3,5,6],
     #[4,7,8],
     #[5,7,9]]


#a=lst[0][0]+lst[1][1]+lst[2][2]
#b=lst[0][2]+lst[1][1]+lst[2][0]
#print(a*b)
