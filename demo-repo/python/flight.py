class Flight():

    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]

    def add_passengers(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight=Flight(3)

people=["ferid","nicat","azer","imammeddin"]

for person in people:
    if flight.add_passengers(person):
        print(f"Person in name {person}  was added successfully!")

    else:
        print(f"No space available for {person}")