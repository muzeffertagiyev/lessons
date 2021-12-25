
#iki dene list oturursen iki dene listde index olaraq yoxlayirsan 
# meselen a=[12,21,21,32] b=[1,23,39,12]


def listler(list1,list2):
    count=0
    for x in range(len(list1)):
        if list1[x]>list2[x]:
        
            count=count+1
    return count
print(listler([3,6,31,24,31,22],[5,1,32,20,30,21]))    



#def listler(list1,list2):
    #count=0
    #for x in range(len(list1)):
        #for y in range(len(list2)):
            #if x==y:
                #if list1[x]>list2[y]:
                    #count=count+1
    #return count
#print(listler([3,6,31,24,31,22],[5,1,32,20,30,21]))                    
                
