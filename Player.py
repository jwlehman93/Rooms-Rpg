import Rooms
import Inventory
class Player(object):
    """Player that traverses rooms"""
    def __init__(self,name):
        self.name = name
        self.current_room = None
        self.isAlive = True
        self.damsels = 0
        self.enemies = 0
        self.items = 0
        self.inventory = Inventory.Inventory()
        self.health = 10
        self.equipment = Inventory.Equipment()
    
    def enterRoom(self,room):
        if room == None:
            print("You cannot go that way")
            return
        print("\nYou have left " +self.current_room.name + " and are now entering " + room.name)
        room.isOccupied = True
        self.current_room.isOccupied = False
        self.current_room = room
        print(self.current_room)

    def getCommand(self):
        com = input("What would you like to do?")
        return com

    def receiveMessage(self,msg):
        print(msg)
    
    def requestInput(self,msg):
        return input(msg)
    
    def get_total_score(self):
        return self.enemies + self.damsels + self.items

    def add_inventory(self,item):
        self.inventory.add(item)



    

    

    

