from room import Room
from player import Player

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

    'beach': Room("Beach", "It's a beach")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].e_to = room['beach']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Joe Exotic', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def command(x):
    global player
    print(f'{player.name} is on the move...')

    if (x == 'n') & (player.current_room.n_to != None):
        player.current_room = player.current_room.n_to
        print(f'{player.name} decided to move north...')
    elif(x =='s') & (player.current_room.n_to != None):
        print(f'{player.name} decided to move south...')
        player.current_room  = player.current_room.s_to
    elif(x =='w') & (player.current_room.n_to != None):
        print(f'{player.name} decided to move west...')
        player.current_room = player.current_room.w_to
    elif(x =='e') & (player.current_room.n_to != None):
        print(f'{player.name} decided to move east...')
        player.current_room = player.current_room.e_to
    elif (x not in ['n', 's', 'w', 'e']):
        print('*******')
        print('WRONG INPUT')
        print('PLEASE TRY AGAIN')
        print('*******')
    else:
        print('*******')
        print('YOU SHALL NOT PASS')
        print('*******')

run = True

while run == True:
    print(f'{player.name} is now in {player.current_room.name}...')
    print(f'{player.current_room.description}...')
    x = input("Where would you like to go next? (n/e/w/s/q) : ")
    if (x == 'q'):
        run = False
    else:
        command(x)