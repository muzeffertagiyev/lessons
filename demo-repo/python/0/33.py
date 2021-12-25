names1=["nicat","ferid","elvin","perviz","imameddin","cavad","vusal","huseynaga"]
names2=["vusal","tural","abbas","azer","nicat","ferid","huseynaga","orxan"]
names=[]
for x in names1:
    for y in names2:
        if x==y:            
            names.append(y)
print(names)          
