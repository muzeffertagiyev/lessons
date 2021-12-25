

def ededler(a):
    lst=[]
    for x in a:
        if x%2==0:
           lst.append(x)

    return lst        


            
print(ededler([3,5,6,2,7,8,10,15,21]))  
print(ededler([3,5,62,1,23,22,4241,24]))          