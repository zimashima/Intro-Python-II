class GameObject:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return str(self.__dict__)