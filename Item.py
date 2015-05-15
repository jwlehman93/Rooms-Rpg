class Inventory(object):
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def add(self,item):
       item.next = self.head
       self.head = item 



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








