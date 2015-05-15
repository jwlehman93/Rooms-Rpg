#For handling commands from the player
import Rooms
import Player

def processCommand(msg,player):

    if(msg == "help"):
        print("\n======Welcome to the Rooms:The RPG Help Section======\n\nCommands you can use are as follows:\nn - head north\nw - head west\ns - head south")
        print("w - head west\nlook - states current room and surroundings\nstatus - states your current status\ninv - lists your current inventoryscore - gives current score\nexit - exit the game/n")
    elif(msg == "n"):
        player.enterRoom(player.current_room.exits["north"])
    elif(msg == "e"):
        player.enterRoom(player.current_room.exits["east"])
    elif(msg == "s"):
        player.enterRoom(player.current_room.exits["south"])
    elif(msg == "w"):
        player.enterRoom(player.current_room.exits["west"])
    elif(msg == "look"):
        print(player.current_room)
    elif(msg == "exit"):
       player.isAlive = False 
       print("\n=====YOU HAVE FAILED TO ESCAPE=====")
    elif(msg == "score"):
        print("\n====%s's score====\nEnemies Killed: %d\nDamsels Rescued: %d\nItems Recovered: %d\nTotal Score: %d",player.name,player.enemies,player.damsels,player.items,player.get_total_score())
    elif(msg == "inv"):
        for i in player.inventory:
            print(i.name)
        ans = input("If you would like to see the description of an item type in that items name now or enter 'q' to exit.")
        if(ans == 'q'):
            return
        else:
            for i in player.inventory:
                if(i.name == ans):
                    print i.description


        

    else:
        print("\nI don't understand what you are asking. Enter 'help' if you do not know what to do.\n")









    
        
    


 
