'''
This file contains the Game class which represents the text adventure game.
'''
from location import Location
from object import Object
from player import Player
class Game:
    def __init__(self):
        self.locations = {}
        self.player = Player()
    def start(self):
        self.load_locations()
        self.player.current_location = self.locations["start"]
        self.print_location_description()
        while True:
            command = input("Enter a command: ")
            self.process_command(command)
    def load_locations(self):
        # Load all the locations and their descriptions
        self.locations["start"] = Location("Start", "You are at the starting point.")
        self.locations["rijksmuseum"] = Location("Rijksmuseum", "You are at the Rijksmuseum.")
        self.locations["rembrandthuis"] = Location("Rembrandthuis", "You are at the Rembrandthuis.")
        # Add more locations here
        self.locations["start"].add_connection("n", self.locations["rijksmuseum"])
        self.locations["rijksmuseum"].add_connection("s", self.locations["start"])
        self.locations["start"].add_connection("w", self.locations["rembrandthuis"])
        self.locations["rembrandthuis"].add_connection("e", self.locations["start"])
        self.locations["rijksmuseum"].add_object(Object("paintbrush", "A paintbrush."))
    def print_location_description(self):
        print(self.player.current_location.description)
    def process_command(self, command):
        if command.lower() in ["n", "w", "e", "s"]:
            self.move(command.lower())
        elif command.lower().startswith("get"):
            self.get_object(command.lower()[4:].strip())
        elif command.lower().startswith("drop"):
            self.drop_object(command.lower()[5:].strip())
        else:
            print("Invalid command.")
    def move(self, direction):
        next_location = self.player.current_location.get_next_location(direction)
        if next_location:
            self.player.current_location = next_location
            self.print_location_description()
        else:
            print("You cannot move in that direction.")
    def get_object(self, object_name):
        object_found = self.player.current_location.get_object(object_name)
        if object_found:
            self.player.add_object(object_found)
            print(f"You picked up {object_found.name}.")
        else:
            print("Object not found in this location.")
    def drop_object(self, object_name):
        object_found = self.player.get_object(object_name)
        if object_found:
            self.player.current_location.add_object(object_found)
            print(f"You dropped {object_found.name}.")
        else:
            print("You don't have that object.")