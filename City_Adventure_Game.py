# Character class which is representing the basic character in the game    
class Character:
    def __init__(self, name, health, position):
        self.name = name
        self.health = health
        self.position = position
    
    # Method move to update character's position     
    def move(self, new_position):
        self.position = new_position
        print(f"{self.name} moves to position {self.position}")
        
    def display_status(self):
        # Display for the character's current health and position
        print(f"{self.name}: Health: {self.health}, Position: {self.position}")
            
# Vehicle class representing a vehicle in the game
class Vehicle:
    def __init__(self, type, speed, fuel_level):
        self.type = type
        self.speed = speed
        self.fuel_level = fuel_level
        
    def drive(self, distance):
        # Check if the vehicle has enough fuel to drive the given distance
        if self.fuel_level > 0:
            self.fuel_level -= distance * 0.1
            print(f"{self.type} drives for {distance}km. Fuel level: {self.fuel_level:.2f}")
        else:
            print(f"{self.type} has no fuel left")
            
# Class HeroCharacter to specialize Character with extra abilities
class HeroCharacter(Character):
    def __init__(self, name, health, position, ability):
        super().__init__(name, health, position)
        self.ability = ability
        
    # Specialized ability method 
    def use_ability(self):
        print(f"{self.name} uses special ability: {self.ability}")
        
def character_vehicle_interaction(character, vehicle):
    # Interaction between character and vehicle
    print(f"{character.name} is driving {vehicle.type}")
    character.move("inside vehicle")
    vehicle.drive(10)
    character.move("original position")
    print(f"{character.name} gets out of the {vehicle.type}.")
    
# A demo for handling different types of objects using polymorphism concept
def handle_object(obj):
    if isinstance(obj, Character):
        obj.display_status()
    elif isinstance(obj, Vehicle):
        print(f"{obj.type}: Speed = {obj.speed}, Fuel level = {obj.fuel_level}")

import tkinter as tk
from tkinter import messagebox

class GameGUI:
    def __init__(self, master):
        self.master = master
        master.title("City Adventure Game")

        # Character status display
        self.character_label = tk.Label(master, text="")
        self.character_label.pack()

        # Buttons for interactions
        self.move_button = tk.Button(master, text="Move Character", command=self.move_character)
        self.move_button.pack()

        self.interact_button = tk.Button(master, text="Interact with Vehicle", command=self.interact_with_vehicle)
        self.interact_button.pack()

        self.ability_button = tk.Button(master, text="Use Special Ability", command=self.use_special_ability)
        self.ability_button.pack()

        # Initialize character
        self.hero = HeroCharacter(name="Flyman", health=100, position="Start", ability="Flying in space")
        self.car = Vehicle(type="Flying Car", speed=60, fuel_level=100)

        # Display initial status
        self.update_status()

    def update_status(self):
        self.character_label.config(text=f"{self.hero.name}: Health: {self.hero.health}, Position: {self.hero.position}")

    def move_character(self):
        self.hero.move("New Position")
        self.update_status()

    def interact_with_vehicle(self):
        character_vehicle_interaction(self.hero, self.car)
        self.update_status()

    def use_special_ability(self):
        self.hero.use_ability()

# Running the GUI
root = tk.Tk()
game_gui = GameGUI(root)
root.mainloop()
