birthdays=["11.10.2020","12.10.2020",'09.08.2020',"03.05.1997","06.02.1998"]

months={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September",
"10":"October","11":"November","12":"December"
}
counts={"01":0,"02":0,"03":0,"04":0,"05":0,"06":0,"07":0,"08":0,"09":0,
"10":0,"11":0,"12":0}


for birthday in birthdays:
    month=birthday.split(".")[1]
    counts[month]+=1

my_dict={}
for key,value in counts.items():
    
    if value>0:
        my_dict[months[key]]=value

print(my_dict)