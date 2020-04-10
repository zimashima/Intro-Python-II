from room import Room
from player import Player
from item import Item

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
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


cat_food = Item('Cat Food', 'Cat food, you idiot')
cat_litter = Item('Cat Litter', 'Cat litter, you idiot')
dog_food = Item('Dog food', 'Dog food, you idiot')


room['outside'].storage.append(cat_litter)
print(room['outside'].storage[0].name)


def command(x):
    global player
    print(f'{player.name} is on the move...')

    if (x == 'n') & (player.current_room.n_to != None):
        player.current_room = player.current_room.n_to
        print(f'{player.name} decided to move north...')
    elif(x =='s') & (player.current_room.s_to != None):
        print(f'{player.name} decided to move south...')
        player.current_room  = player.current_room.s_to
    elif(x =='w') & (player.current_room.w_to != None):
        print(f'{player.name} decided to move west...')
        player.current_room = player.current_room.w_to
    elif(x =='e') & (player.current_room.e_to != None):
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


def check_inventory():
    print(f'Checking {player.name} inventory...')
    print('...')
    if (len(player.inventory) == 0):
        print(f'{player.name} does not have anything because he is just a poor millennial...')
    else:
        print(f'This is what {player.name} has')
        for item in player.inventory:
            print(f'{player.name} has [{item.name}]')

def check_room():
    print(f'{player.name} looks around for somthing in {player.current_room.name}...')
    print('...')
    if (len(player.current_room.storage) == 0):
        print(f'{player.current_room.name} does not have any thing')
    else:
        print(f'This room seem to have something...')
        for item in player.current_room.storage:
            print(f'[{item.name}] is in this room')

def item_action(word):
    action_word = word.split(' ')
    verb = action_word[0]
    item = ' '.join(action_word[1:]).lower()
    if verb == 'drop':
        for i in player.inventory:
            if i.name.lower() == item:
                player.current_room.storage.append(i)
                player.inventory.remove(i)
                i.on_drop()
                break
            else:
                print('{player.name} does not have [{i.name}]')
    elif(verb == 'take'):
        for i in player.current_room.storage:
            if i.name.lower() == item:
                player.inventory.append(i)
                player.current_room.storage.remove(i)
                i.on_take()
                break
            else:
                print('{player.current_room.storage.name} does not have [{i.name}]')
    else:
        print('INCORRECT INPUT')
                

new_player = input('Enter the player name : ')
player = Player(new_player, room['outside'])


run = True

while run == True:
    print('...')
    print(f'{player.name} is now in {player.current_room.name}...')
    print(f'{player.current_room.description}...')
    check_room()
    print(f'What should {player.name} do?')
    print('[GO NORTH] press n')
    print('[GO SOUTH] press s')
    print('[GO EAST] press e')
    print('[GO WEST] press w')
    print('[CHECK INVENTORY] press i')
    print('[DROP AN ITEM] [drop] [item_name]')
    print('[TAKE AN ITEM] [take] [item_name]')
    print('[QUIT THE GAME] press q')
    x = input(f"What should {player.name} do? : ")
    
    if (x == 'q'):
        run = False
    elif (x == 'i'):
        check_inventory()
    elif x in ['n', 's', 'w', 'e']:
        command(x)
    else:
        item_action(x)