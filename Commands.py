#For handling commands from the player
import Rooms
import Player

def processCommand(msg,player):
    cmd, args = msg.split(" ")

    if(cmd == "help"):
        print("\n======Welcome to the Rooms:The RPG Help Section======\n\nCommands you can use are as follows:\nn - head north\nw - head west\ns - head south")
        print("w - head west\nlook - states current room and surroundings\nstatus - states your current status\ninv - lists your current inventoryscore - gives current score\nexit - exit the game/n")
    elif(cmd == "n"):
        player.enterRoom(player.current_room.exits["north"])
    elif(cmd == "e"):
        player.enterRoom(player.current_room.exits["east"])
    elif(cmd == "s"):
        player.enterRoom(player.current_room.exits["south"])
    elif(cmd == "w"):
        player.enterRoom(player.current_room.exits["west"])
    elif(cmd == "look"):
        print(player.current_room)
    elif(cmd == "status"):
        print("\n=====%d's Status=====\nHealth: %d" % player.health)
    elif(cmd == "exit"):
       player.isAlive = False 
       print("\n=====YOU HAVE FAILED TO ESCAPE=====")
    elif(cmd == "score"):
        print("\n====%s's score====\nEnemies Killed: %d\nDamsels Rescued: %d\nItems Recovered: %d\nTotal Score: %d"%(player.name,player.enemies,player.damsels,player.items,player.get_total_score()))
    elif(cmd == "inv"):
        i = player.inventory.head
        while i is not None:
            print(i.name)
        ans = input("\nIf you would like to see the description of an item type in that items name now or enter 'q' to exit. Type 'help' if you would like to see a list of commands for the inventory")
        #exit inventory
        if ans == 'q':
            return
        else:
            i = player.inventory.head
            while i is not None:
                if(i.name == ans):
                    print(i.description)
                i = i.next
            else
        elif ans == "help":

    else:
        print("\nI don't understand what you are asking. Enter 'help' if you do not know what to do.\n")









    
     #helo   
    


 
