from collections import OrderedDict
"""
Was gonna implement my own using a dict to to store keys and
my own doubly linked list to do the ordering. I'm not 100% sure about the complexity
of the OrderedDict, but it should be O(1) for get and set. 
"""

class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")
        self.limit = limit
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return None
        self.data.move_to_end(key)    # end is most recent
        return self.data[key]

    def set(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.limit:
            self.data.popitem(last=False)