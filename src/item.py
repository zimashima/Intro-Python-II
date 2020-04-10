from gameobject import GameObject

class Item(GameObject):
    def __init__(self, name, description):
        super().__init__(name)
        self.name = name
        self.description = description
                         
    def on_drop(self):
        print(f'{self.name} has been dropped!')

    def on_take(self):
        print(f'{self.name} has been picked up!')