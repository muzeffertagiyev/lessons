class library:
    pass

class person(library):
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
    def fullname(self):
        return self.name+" "+self.surname+"'s "+"age is "+self.age+"."

class workers(person):
    def __init__(self,name,surname,age,workduration,salary):
        self.workduration=workduration
        self.salary=salary 
        super().__init__(name,surname,age)
        

    def wduration(self):
        return "He/she works here for "+self.workduration+"."    
    def income(self):   
        return   "His/her salary is "+str(self.salary)+"."
    def increasesalary(self,amount):
        self.salary=self.salary + amount
        return  "His/her salary will increase"+" "+str(amount)+""+"azn and will be "+str(self.salary)+"."


#class buyers(person):
   # pass


class books(library):
    def __init__(self,book_name,writer,publishdate,book_number):
        self.book_name=book_name
        self.writer=writer
        self.publishdate=publishdate
        self.book_number=book_number
        
    def book(self):
        return  "   The book  "+self.book_name+" "+"is written by "+self.writer+" "+"and published in "+self.publishdate+"."+"Available numbers:"+str(self.book_number)+"."
    def buy(self,buyername,quantity):
        self.buyername=buyername
        self.book_number=self.book_number-quantity
        return self.buyername+" bought book in quantity of  "+str(quantity)+" from "+self.book_name+" by "+self.writer+" and remained "+str(self.book_number)

class janrs(books):  
    def perspect(self,janr):
        return "The book is in "+janr+" "+"janr."
class history(janrs):
    def hstr(self):
        return"This book is a best seller book in America beetween years 2009 and 2012.It is based on  unsaid true events between World War 2(1939-1945)"
class dedective(janrs):
    def dedec(self):
        return "The book is Agatha Chiristie's best known book.Dedective Erkul Puaro looks for mysterious murderer of owner of Villa Oksford"
class science_finction(janrs):
    def scnfiction(self):
        return "There are some games that inspired by this book.The main character is Artyom who looks for help for their station which faces with outside dangers."

    
    
       
#workers      
ferid=workers("Ferid","Veliyev","23","2 months",1200)
muzeffer=workers("Muzeffer","Tagiyev","22","5 months",1400)
perviz=workers("Perviz","Veliyev","21","1 year",1600)

#books

ww2=history("Greatest events of WW2","Pablo","2005",30)
black_coffee=dedective("The black coffee spot","Agatha Christie","1968",15)
metro2033=science_finction("Metro 2033","Dmirty Glukovsky ","2002",50)

#buyer
buyer1=books("The black coffee spot","Agatha Christie","1968",15)
buyer2=books("Greatest events of WW2","Pablo","2005",30)
buyer3=books("Metro 2033","Dmirty Glukovsky ","2002",50)

print("WORKERs")
print(ferid.fullname(),ferid.wduration(),ferid.income(),ferid.increasesalary(400))
print(muzeffer.fullname(),muzeffer.wduration(),muzeffer.income(),muzeffer.increasesalary(300))
print(perviz.fullname(),perviz.wduration(),perviz.income(),perviz.increasesalary(300))
print(" ")
print("BOOKs")
print(ww2.book(),ww2.perspect("history"),ww2.hstr()) 
print(black_coffee.book(),black_coffee.perspect("Mystery"),black_coffee.dedec())
print(metro2033.book(),metro2033.perspect("Science Finction"),metro2033.scnfiction())
print(" ")
print("BUYERs")
print(buyer1.buy("Nicat",5))
print(buyer2.buy("Azer",3))
print(buyer3.buy("Emil",7))
