import Rooms
import Player
import Commands

rooms = RoomList()
room1 = Room("Room 1")
start = Room("Starting Room")
room2 = Room("Room 2")
room3 = Room("Room 3")
room4 = Room("Room 4")
rooms.addRooms(room1)
rooms.addRooms(room2)
rooms.addRooms(room3)
rooms.addRooms(room4)
rooms.addRooms(start)
room1.createExits([room2,room3,start,room4])
start.createExits([room1,None,None,None])
room2.createExits([None,None,None,room1])
room3.createExits([None,None,room1,None])
room4.createExits([None,room4,None,None])
e = rooms.head
while e is not None:
    e.description = "You are in room {}".format(e.name)
    e = e.next
player1 = Player(input("What is your name"))
isPlaying = True
while isPlaying == True:
    player1.receiveMessage(start)
    while player1.isAlive == True:
        Commands.processCommand(player1.requestInput("What would you like to do?"),player1)
    ans = player1.requestInput("Would you like to play again?(Type y or n and press <enter>)")
    while(True):
        if ans == "n":
            isPlaying == False
            break
        elif ans != "y":
            print("Improper input. Please enter y or n and press <enter>.")
        else:
            break
print("Thanks for playing!")
            



            














