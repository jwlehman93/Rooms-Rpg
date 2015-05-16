class Room(object):
    """Class that creates room nodes for RoomList"""
    def __init__(self, name, north=None, east=None, west=None,south=None):
        self.name = name
        self.exits = dict()
        self.exits["north"] = north
        self.exits["east"] = east
        self.exits["south"] = south
        self.exits["west"] = west
        self.next = None
        self.description = ""
        self.isOccupied = False

    #exits must be a list of length 4
    def createExits(self,exits):
        self.exits["north"] = exits[0]
        self.exits["east"] = exits[1]
        self.exits["south"] = exits[2]
        self.exits["west"] = exits[3]

    def __str__(self):
        ret = self.description
        exit_desc = "There are exit(s) to the "
        for i in self.exits:
            if self.exits[i] == None:
                continue
            exit_desc += i 
            #TODO eliminate comma after last entry and put and before last entry
            exit_desc += ", "
        ret += exit_desc + "\n"
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
        self.size += 1 

#search through list to find room with matching name
#Return: room or None if room is not found
def search(self,name):
    
    e = self.head
    while e is not None:
        if name == e.name:
            return e
        e = e.next
    return None



     

    