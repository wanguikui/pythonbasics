class Building():
    rooms=6
    doors=8
    #lawn=True
    #windows=10
    #garage=True
    #swimmingPool=False
    def open_building(self):
        print(f"{self.name} is now open")

    def close_building(self):
        print(f"{self.name} is now closed")

    def vacant_rooms(self):
        print(self.rooms-self.occupiedRooms)


#creating actual building(s) objects
jamii = Building()
kivuti = Building()
cornerHouse = Building()
kimathi = Building()

#print(jamii)

#print(jamii.rooms)
#print(kivuti.rooms)
#print(cornerHouse.rooms)
cornerHouse = Building()
cornerHouse.name = "Corner House"
cornerHouse.open_building()
cornerHouse.close_building()
print(cornerHouse.name)
cornerHouse.rooms=100
cornerHouse.occupiedRooms=42
cornerHouse.vacant_rooms()
#cornerHouse.unoccupiedRooms=cornerHouse.rooms-cornerHouse.occupiedRooms
#print(cornerHouse.unoccupiedRooms)
print(cornerHouse.rooms)
cornerHouse.security=12
print(cornerHouse.security)
#print(cornerHouse.basement)


kimathi = Building()
kimathi.name="Kimathi House"
kimathi.open_building()
kimathi.close_building()
print(kimathi.name)
kimathi.rooms=150
print(kimathi.rooms)
kimathi.basement=True
print(kimathi.basement)
kimathi.security=8
print(kimathi.security)





























