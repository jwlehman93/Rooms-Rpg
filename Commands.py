#For handling commands from the player
import Rooms
import Player

def processCommand(msg,player):

    if(msg == "help"):
        print("======Welcome to the Rooms:The RPG Help Section======\n\nCommands you can use are as follows:\nn - head north\nw - head west\ns - head south")
        print("w - head west\nlook - states current room and surroundings\nexit - exit the game")
    elif(msg == "n"):
        player.enterRoom(player.current_room.north)
    elif(msg == "e"):
        player.enterRoom(player.current_room.east)
    elif(msg == "s"):
        player.enterRoom(player.current_room.south)
    elif(msg == "w"):
        player.enterRoom(player.current_room.west)
    elif(msg == "look"):
        print(player.current_room)
    elif(msg == "exit"):
       player.isAlive = False 
       print("You have failed to escape")








    
        
    




