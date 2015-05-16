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

#search through list to find item with name matching value            
def search(list,value):
    i = list.head
    while i is not None:
        if i.name == value:
            return i
        i = i.next
    return None




class Equipment(object):
    """Items that player currently has equipped"""
    def __init__(self,head = None,chest = None, legs = None, feet = None, left_hand = None, right_hand = None):
        self.head = head
        self.chest = chest
        self.legs = legs
        self.feet = feet
        self.left_hand = left_hand
        self.right_hand = right_hand

    def __str__(self):
        print("You are wearing:\n head: %s\n chest: %s\n legs %s\n\nYou are wielding:\n %s left hand: %s\n right hand: %s\n" % (self.head,self.chest,self.legs,self.feet,self.left_hand,self.right_hand))

    def equip(self,item):
        if item is not wearable:
            print("You cannot equip that item.")
        else:
            #TODO implement if item slot is already full
            if item.type == "head":
                self.head = item
            elif item.type == "chest":
                self.chest = item
            elif item.type == "legs":
                self.legs = item
            elif item.type == "feet":
                self.feet = item
            elif item.type == "right hand":
                self.right_hand = item
            elif item.type == "left hand":
                self.left_hand = item


           




class Item(object):
    """Class and subclasses to handle items"""
    def __init__(self,name,canCombine):

        self.name = name
        self.next = None
        self.canCombine = canCombine

    def drop(self,player):
        player.inventory.remove(self)

    def use(self,player):
        print("Item use test Item Class")

    
        

class HealthPotion(Item):
    def __init__(self,name,canCombine):
        self.used = False
        self.value = 5
        super(HealthPotion,self).__init__(self,name,canCombine)
    def use(self,player):
        player.health += 5








