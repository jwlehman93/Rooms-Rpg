import Rooms
import Player
import Commands
import Inventory

rooms = Rooms.RoomList()
room1 = Rooms.Room("Room 1")
start = Rooms.Room("Starting Room")
room2 = Rooms.Room("Room 2")
room3 = Rooms.Room("Room 3")
room4 = Rooms.Room("Room 4")
rooms.addRoom(room1)
rooms.addRoom(room2)
rooms.addRoom(room3)
rooms.addRoom(room4)
rooms.addRoom(start)
room1.createExits([room2,room3,start,room4])
start.createExits([room1,None,None,None])
room2.createExits([None,None,room1,None])
room3.createExits([None,None,None,room1])
room4.createExits([None,room1,None,None])
e = rooms.head
while e is not None:
    e.description = "\nYou are in room {}\n".format(e.name)
    e = e.next
player1 = Player.Player(input("What is your name?\n"))
isPlaying = True
while isPlaying == True:
    player1.receiveMessage(start)
    player1.current_room = start
    while player1.isAlive == True:
        Commands.processCommand(player1.requestInput("What would you like to do?\n"),player1)
    ans = player1.requestInput("Would you like to play again?(Type y or n and press <enter>)\n")
    while True:
        if ans == "n":
            isPlaying = False
            break
        elif ans != "y":
            print("Improper input. Please enter y or n and press <enter>.")
        else:
            break
print("Thanks for playing!")
            



            














