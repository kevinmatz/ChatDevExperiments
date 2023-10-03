'''
This file contains the Player class which represents the player in the game.
'''
class Player:
    def __init__(self):
        self.current_location = None
        self.objects = []
    def add_object(self, object):
        self.objects.append(object)
    def get_object(self, object_name):
        for obj in self.objects:
            if obj.name == object_name:
                self.objects.remove(obj)
                return obj
        return None