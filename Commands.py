#For handling commands from the player
import Rooms
import Player

def processCommand(msg,player):
    cmd, args = msg.split(" ")

    if(cmd == "help"):
        print("\n======Welcome to the Rooms:The RPG Help Section======\n\nCommands you can use are as follows:\nn - head north\nw - head west\ns - head south")
        print("w - head west\nlook - states current room and surroundings\nstatus - states your current status\ninv - takes you to inventory management\nscore - gives current score\nexit - exit the game/n")
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
        print("\n=====%d's Status=====\n\nHealth: %d" % player.health)
    elif(cmd == "exit"):
       player.isAlive = False 
       print("\n=====YOU HAVE FAILED TO ESCAPE=====")
    elif(cmd == "score"):
        print("\n====%s's score====\nEnemies Killed: %d\nDamsels Rescued: %d\nItems Recovered: %d\nTotal Score: %d"%(player.name,player.enemies,player.damsels,player.items,player.get_total_score()))
    elif(cmd == "inv"):
        i = player.inventory.head
        while i is not None:
            print(i.name)
            print("\n=====Inventory Manager=====\n\n")
        while True:
            ans = input("Type 'help' if you would like to see a list of commands for the inventory")
            #exit inventory
            cmd, args = ans.split(" ",1)
            if ans == 'q':
                break
            elif ans == "help":
                print("=====Inventory Help Screen=====\n\nCommands you can use are as follows:\nlist - lists all objects in your inventory\nexamine <object> - gives description of object")
                print("use <object> - uses object for its purpose\ncombine <object1> <object2> - combines 2 objects\ndrop <object> - drops object from your inventory\n")
                print("equip <object> - if object is wearable or wieldable it will be equipped\n\n")
            #TODO write functions for inventory manager
            elif ans == "list":
                i = player.inventory.head
                while i is not None:
                    print(i.name)
            elif ans == "examine":

            elif ans == "use":
                pass
            elif ans == "combine":
                pass
            elif ans == "drop":
                pass
            elif ans == "equip":
                pass
            else:
                i = player.inventory.head
                while i is not None:
                    if(i.name == ans):
                        print(i.description)
                    i = i.next
                else:
                    pass
    else:
        print("\nI don't understand what you are asking. Enter 'help' if you do not know what to do.\n")









    
     #helo   
    


 
