from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].connections['n'] = room['foyer']
room['foyer'].connections['s']  = room['outside']
room['foyer'].connections['n']  = room['overlook']
room['foyer'].connections['e']  = room['narrow']
room['overlook'].connections['s']  = room['foyer']
room['narrow'].connections['w']  = room['foyer']
room['narrow'].connections['n']  = room['treasure']
room['treasure'].connections['s']  = room['narrow']

my_player = Player("Andronik", room['outside'])
my_room = Room("Andronik", room['outside'])

user_is_playing = True

while user_is_playing:
    
    print("------- NAME -------")
    print(my_player.current_room.name)
    print("--------------------")
    print("\n")
    print("---- INVENTORY ----")
    print(my_room.items)
    print("-------------------")
    
    for line in textwrap.wrap(my_player.current_room.description, 10):
        print(line)
    
    user_input = input("Which direction would you like to go(n/s/e/w): ")
    user_item = input("Enter an item to put into your inventory: ")

    if user_input in ['n','e','s','w']:
        my_player.move(user_input)
        my_room.add(user_item)

    else:
        print("You exited the game. Thanks for playing!")

        user_is_playing = False


