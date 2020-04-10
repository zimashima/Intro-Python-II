# Write a class to hold player information, e.g. what room they are in
# currently.

from gameobject import GameObject

class Player(GameObject):
    def __init__(self, name, current_room):
        super().__init__(name)
        self.name = name
        self.current_room = current_room
        self.inventory = []