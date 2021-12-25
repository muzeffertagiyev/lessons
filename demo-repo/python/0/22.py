set_1={"ferid","muzeffer","perviz","elvin","nicat"}
set_2={"perviz","elvin","nicat","ferid",1,"test1",8,"imameddin","azer",15,"emil","muzeffer"}

if len(set_1.intersection(set_2))==5:
    print(set_1.union(set_2))
else:
    print(set_2.difference(set_1))

