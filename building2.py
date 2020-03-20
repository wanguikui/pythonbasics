class Building(): #A constructor method- a special method that will be called
    # the minute you will create an object/instance
    def __init__(self,name,totalRooms,occupiedRooms,securityGuards):
     #refers to the object that will call your method
                self.buildingName=name
                self.totalRooms=totalRooms
                self.occupiedRooms=occupiedRooms
                self.securityGuards=securityGuards


    def vacant_rooms(self):
        self.vacantRooms=self.totalRooms-self.occupiedRooms
        return self.vacantRooms


    def book_room(self,number):
        self.occupiedRooms+=number
        self.vacantRooms-=number
        return f"There are {self.vacantRooms} Vacant rooms and There are {self.occupiedRooms} Occupied Rooms"








Hazina_Towers = Building("Hazina Towers",150,50,20)

print(Hazina_Towers.buildingName)
print(Hazina_Towers.totalRooms)
print(Hazina_Towers.occupiedRooms)
print(Hazina_Towers.securityGuards)
print(Hazina_Towers.vacant_rooms())
print(Hazina_Towers.book_room(12))


