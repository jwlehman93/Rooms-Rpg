import Rooms
class Player(object):
    """Player that traverses rooms"""
    isAlive = True
    def __init__(self,name):
        self.name = name
        self.current_room = None
    
    def enterRoom(self,room):
        if room == None:
            print("You cannot go that way")
            return
        print("You have left " +current_room.name + " and are now entering " + room.name)
        room.isOccupied = True
        self.current_room.isOccupied = False
        self.current_room = room
        print current_room

    def getCommand(self):
        com = input("What would you like to do?")
        return com

    def receiveMessage(self,msg):
        print(msg)
    
    def requestInput(self,msg):
        return input(msg)
    

