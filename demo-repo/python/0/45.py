for x in range(1,4):
    line=" "
    for y in range(1,4):
        if (x==2 and y==1) or (x==1 and y==2) or (x==3 and y==2)  or (x==2 and y==3):
            line=line+" "
        else:
            line=line+"*"  
    print(line)            

