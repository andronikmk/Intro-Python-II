from item import Item

class Room:
    def __init__(self, name, description, n_to=None, e_to=None, s_to=None, w_to=None,items=[]):
        self.name = name
        self.description = description
        self.connections = {
            "n":n_to,
            "e":e_to,
            "s":s_to,
            "w":w_to
        }
        self.items = items


    def add(self, item=[]):
        self.items.append(item)
