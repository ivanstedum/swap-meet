from swap_meet.item import Item
class Clothing(Item):
    # self.category = "Clothing"
    # def __init__(self, category = "Clothing", condition = 0):
    #     self.category = category
    #     self.condition = condition
    def __init__(self, condition = 0):
        super().__init__(category = "Clothing",condition = condition)
    

    def __str__(self):
        return "The finest clothing you could wear."