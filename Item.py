class Inventory(object):
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def add(self,item):
        if self.size == 10:
            print("You can't carry anymore items")
            return
        else:
            item.next = self.head
            self.head = item 
            print("\n" + item.name + "has been added to your inventory")

    def remove(self,item):
        prev = None
        i = self.head
        while i is not None:
            if(i.name == item.name):
                break
            prev = i
            i = i.next
        if i == None:
            print("You do not have that item")
        elif prev == None:
            self.head = i.next 
        else:
            prev.next = i.next
            

                 



class Item(object):
    """Class and subclasses to handle items"""
    def __init__(self,name):
        self.name = name
        self.next = None
    def drop(self,player):
        player.inventory.remove(self)

    
        

class HealthPotion(Item):
    def __init__(self,name):
        self.name = name
        self.used = False
        self.value = 5
    def use(self,player):
        player.health += 5








