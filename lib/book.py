#!/usr/bin/env python3
# the title and page_count
class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            self._title = new_title    

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, new_page_count):
        if isinstance(new_page_count, int):
            self._page_count = new_page_count
            return self._page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")