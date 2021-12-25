def lst(strings):
    empty_lst=[]
    for x in strings:
        if len(x)>5:
            empty_lst.append(x)
    return len(empty_lst)
print(lst(["ferid","muzeffer","imameddin","nicat","azer","huseynaga","amil","tagiyev","emin","perviz"]))   