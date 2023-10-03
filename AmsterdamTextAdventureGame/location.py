'''
This file contains the Location class which represents a location in the game.
'''
class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.objects = {}
        self.connections = {}
    def add_connection(self, direction, location):
        self.connections[direction] = location
    def get_next_location(self, direction):
        return self.connections.get(direction)
    def get_object(self, object_name):
        if object_name in self.objects:
            return self.objects.pop(object_name)
        else:
            return None
    def add_object(self, object):
        self.objects[object.name] = object