directions = ["north","east","south","west"]
class Room(object):
    """Class that creates room nodes for RoomList"""
    isOccupied = False
    def __init__(self, name, north=None, east=None, west=None,south=None):
        self.name = name
        self.west = west
        self.east = east
        self.north = north
        self.south = south
        #exits list must always be in format [n,e,s,w]
        self.exits = [north,east,south,west]
        self.next = None
        self.description = ""
    #exits must be a list of length 4
    def createExits(self,exits):
        if len(exits)!=4:
            return None
        for i in exits:
            self.exits[i] = exits[i]

    def __str__(self):
        ret = self.description
        exit_desc = "\nThere are exit(s) to the "
        for i in exits:
            if exits[i] == None:
                continue
            exit_desc += directions[i] 
            if exits[i]!=self.west:
                exit_desc += ", "
        ret += exits_desc + "\n"
        return ret
         

class RoomList(object):
    """Singly Linked List of rooms"""
    size = 0
    def __init__(self,head=None):
        self.head = head
    def addRoom(self,room):
        if not self.head:
            self.head = room
        else:
            room.next = self.head
            self.head = room    
        size += 1 

#search through list to find room with matching name
#Return: room or None if room is not found
def search(self,name):
    
    e = self.head
    while e is not None:
        if name == e.name:
            return e
        e = e.next
    return None



     

    