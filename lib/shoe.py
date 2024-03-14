#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if isinstance(new_size, int):
            self._size = new_size
            return self._size
        else:
            print("size must be an integer")
       
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
        # return self._condition
        # if cobble.has_been_called:
    #         
# my_shoe = Shoe(brand="Nike", size=9, condition="New")
        

        