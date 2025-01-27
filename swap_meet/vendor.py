class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory
        self.inventory = self.inventory if inventory is not None else []

    def add(self, item):

        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory: 
            return False
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        item_by_category = []

        for item in self.inventory:
            if category == item.category:
                item_by_category.append(item)
        return item_by_category
    
    def swap_items(self,other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            self.remove(my_item)
            return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

    def get_best_by_category(self, category):
        
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        return max(category_list, key = lambda item: item.condition)


    def swap_best_by_category(self,other,my_priority,their_priority):

        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        else:
            return self.swap_items(other, my_best, their_best)