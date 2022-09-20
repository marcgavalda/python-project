#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame 
from pygame.locals import *
from pygame import mixer
import time
import threading
from IPython.display import clear_output
from PIL import Image


# In[2]:


# define rooms and items room a

# DEFINE ROOMS

game_room = {
    "name": "GAME-ROOM",
    "type": "room",
}

bedroom_1 = {
    "name": "BEDROOM 1",
    "type": "room",
}

bedroom_2 = {
    "name": "BEDROOM 2",
    "type": "room",
}

living_room = {
    "name": "LIVING-ROOM",
    "type": "room",
}

# DEFINE DOORS AND KEYS

door_a = {
    "name": "DOOR A",
    "type": "door",
}

door_b = {
    "name": "DOOR B",
    "type": "door",
}

door_c = {
    "name": "DOOR C",
    "type": "door",
}

door_d = {
    "name": "DOOR D",
    "type": "door",
}

key_a = {
    "name": "KEY for DOOR A",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "KEY for DOOR B",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "KEY for DOOR C",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "KEY for DOOR D",
    "type": "key",
    "target": door_d,
}


# GAME-ROOM ITEMS

couch = {
    "name": "COUCH",
    "type": "furniture",
}

piano = {
    "name": "PIANO",
    "type": "furniture",
}

shelve = {
    "name": "SHELVE",
    "type": "furniture",
}

# BEDROOM 1 ITEMS

queen_bed = {
    "name": "QUEEN BED",
    "type": "furniture",
}

wardrove = {
    "name": "WARDROVE",
    "type": "furniture",
}

# BEDROOM 2 ITEMS

double_bed = {
    "name": "DOUBLE BED",
    "type": "furniture",
}

dresser = {
    "name": "DRESSER",
    "type": "furniture",
}

library = {
    "name": "LIBRARY",
    "type": "furniture",
}

# LIVING ROOM ITEMS

dining_table = {
    "name": "DINING TABLE",
    "type": "furniture",
}

#OUTSIDE 

outside = {
  "name": "outside"
}


all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    
    "PIANO": [key_a],
    "QUEEN BED": [key_b],
    "DOUBLE BED": [key_c],
    "DRESSER": [key_d],
    
    "GAME-ROOM": [couch, piano, shelve, door_a],
    "BEDROOM 1": [queen_bed, wardrove, door_a, door_b, door_c],
    "BEDROOM 2": [double_bed, dresser, library, door_b],
    "LIVING-ROOM": [dining_table, door_c, door_d],
    "outside": [door_d],
    
    "DOOR A": [game_room, bedroom_1],
    "DOOR B": [bedroom_1, bedroom_2],
    "DOOR C": [bedroom_1, living_room],
    "DOOR D": [living_room, outside],  
    
}


# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}


# In[3]:


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    mixer.init()
    mixer.music.load('sample-music.wav')
    mixer.music.play()
    time = threading.Timer(300.0, gameover)
    time.start()
    print('You have 5 minutes to finish the game.\n')
    print("\n")
    print("Welcome", (bcolors.BOLD + player_name.upper()+ bcolors.ENDC), "to the Escape-Room game!!, the adventure is about to begin. You wake up on a couch and find yourself in a strange house with no windows which you have never been to before!. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!. You MUST find each room's way out in the less time possible.")
    print("\n")
    print(bcolors.UNDERLINE + "INSTRUCTIONS" + bcolors.ENDC)
    print("- Each ROOM has a DOOR that only opens with its KEY. The KEY is hide in a room's OBJECT.") 
    print("- Use 'EXPLORE' to know the existing objects and 'EXAMINE' to search for the KEY in that object.")
    print("- Remember!, once you have the KEY, go EXAMINE the DOOR to open it, and do it again in the next room.")
    print("- The basic layout below will get help you to understand your location and the path to follow.")
    print("\n")
    print(bcolors.UNDERLINE + "BASIC LAYOUT:" + bcolors.ENDC, "\n")
    print("             door A               door B            ")
    print("GAME ROOM ---------> BEDROOM 1 <---------> BEDROOM 2")
    print("                       |                            ")
    print("                       | door C                     ")
    print("                       v           door D           ")
    print("                  LIVING ROOM --------------> EXIT  ")
    
    play_room(game_state["current_room"])

def gameover():
    
    clear_output()
    mixer.music.stop()
    print('Your time is up!')
    
def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        mixer.music.stop()
        print("\n")
        print(bcolors.OKGREEN + "CONGRATULATIONS", (bcolors.BOLD + player_name.upper()+ bcolors.ENDC), "!! you escaped, and won the game!" + bcolors.ENDC)
        print(bcolors.HEADER + "CONGRATULATIONS", (bcolors.BOLD + player_name.upper()+ bcolors.ENDC), "!! you escaped, and won the game!" + bcolors.ENDC)
        print(bcolors.OKCYAN + "CONGRATULATIONS", (bcolors.BOLD + player_name.upper()+ bcolors.ENDC), "!! you escaped, and won the game!" + bcolors.ENDC)
        print(bcolors.OKBLUE + "CONGRATULATIONS", (bcolors.BOLD + player_name.upper()+ bcolors.ENDC), "!! you escaped, and won the game!" + bcolors.ENDC)
    else:
        print("\n")
        print(bcolors.BOLD + (bcolors.OKBLUE+ "LOCATION: " + room["name"] + bcolors.ENDC) + bcolors.ENDC)
        intended_action = input("    What would you like to do? Type 'EXPLORE' or 'EXAMINE'? ").strip()
        if intended_action.lower() == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action.lower() == "examine":
            examine_item((input("    What would you like to EXAMINE? ").strip()).upper())
        else:
            print(bcolors.FAIL + "    Not sure what you mean. Type 'EXPLORE' or 'EXAMINE'." + bcolors.ENDC)
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("    You EXPLORED the " + room["name"] + " and found this OBJECTS: " + (bcolors.BOLD + ", ".join(items) + bcolors.ENDC), "\n")

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "    You EXAMINE " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += (bcolors.BOLD + "You unlock the DOOR with a key you have." + bcolors.ENDC)
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += (bcolors.BOLD + "Is locked and you don't have the key, EXPLORE and EXAMINE objects to find it." + bcolors.ENDC)
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += (bcolors.BOLD + (bcolors.OKGREEN + "You find " + item_found["name"] + "!!!!!." + bcolors.ENDC) + bcolors.ENDC)
                else:
                    output += (bcolors.BOLD + "There isn't anything interesting about it, try other object." + bcolors.ENDC)
            print(output)
            break

    if(output is None):
        print(bcolors.FAIL + "    Sorry!, the item you requested is not found in the current room, try EXPLORE if necessary." + bcolors.ENDC)
    
    if(next_room and ((input((bcolors.BOLD + "    Do you want to go change the room? Enter 'YES': " + bcolors.ENDC)).strip()).upper()) == 'YES'):
        play_room(next_room)
    else:
        play_room(current_room)

game_state = INIT_GAME_STATE.copy()

player_name = input("Before starts, can you tell us your name: ")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

start_game()

