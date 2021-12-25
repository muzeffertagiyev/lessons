list_1=[]

for x in range(1,4):
    list_2=[]
    for y in range(1,4):
        user_eded=int(input("enter a number: "))
        list_2.append(user_eded)
        list_1.append(list_2)
print(list_1)      

for x in range(3):
    line=" "
    for y in range(3):
        line=line+" "+str(list_2[x][y])
    print(line)        