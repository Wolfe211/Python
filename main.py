#Kevin Portillo
#A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Entrance': {'East': 'Hallway'},
    'Hallway': {'North': 'Library', 'South': 'Kitchen', 'East': 'Armory', 'Item': 'Fire Potion'},
    'Library': {'East': 'Dragon Room', 'South': 'Hallway','Item': 'Boots'},
    'Kitchen': {'South': 'Hallway', 'East': 'Armory','Item': 'Cake'},
    'Armory': {'West': 'Kitchen', 'North': 'Bedroom', 'Item': 'Sword'},
    'Bedroom': {'West': 'Hallway', 'South': 'Armory','Item': 'Shield'},
    'Dragon Room': {'East': 'Princess Room'},
    'Princess Room': {}
}


## Title of Game

def title():
    print('*********************************************')
    print('*                                           *')
    print('*            THE DRAGONS KEEP               *')
    print('*                                           *')
    print('*********************************************')


location_counter = 0
room_list = []
directions = []
items = []
status = True

#The story of the game
def story(hero, default='Hero'):
    print('Welcome {}'.format(hero, default))
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")

### Gets Room Info
def current_room(location):
    print('----------------------------------')
    print('Location: {}'.format(location))
    print('Your item(s): => {}'. format(items))

#prints out the options the player can move
def movement_options(choice,location):

    if str(room_list[location_counter]) == 'Entrance' or  location == None:
        print()
    elif str(room_list[location_counter]) != 'Entrance':
        if location.get('Item') in items:
            print()
        else:
            print()
            print('You See a {}'.format(location.get('Item')))

    print('Your Options:')
    if str(room_list[location_counter]) == 'Library':
        print('WARNING: Next room (East) is the Dragon. Enter at own risk!')
    for i in choice:
        if i == 'Item':
            pass
        else:
            print('>{} '.format(i), end=' ')
    print('>End')
    print('----------------------------------')

#when this function is called it will end the game
def end_game(finish):
    if finish == 'Finish':
        print("***Congratulations***")
        print('*      You Win!     *')
        print('*  You Defeated The *')
        print('*      DRAGON       *')
        print('*********************')
        print('THANK YOU FOR PLAYING')
        print('*********************')
        global status
        status = False
    elif finish == 'Game Over':
        print('----------------------------------')
        print("OH NO! You became the Dragon's Food")
        print('*NOM NOM*')
        print()
        print("-----GAME OVER----")
        print()
        print('*********************')
        print('THANK YOU FOR PLAYING')
        print('*********************')
        status = False
#checks if the player's options is a valid move
def check_movement(options,user_input):
    global location_counter
    if 'Get ' in user_input:
        if str(rooms.get(room_list[location_counter]).get('Item')).upper() in user_input.upper():
            items.append(str(rooms.get(room_list[location_counter]).get('Item')))
            print('----------------------------------')
            print('>>>You picked up the {}'.format(str(rooms.get(room_list[location_counter]).get('Item'))))
        else:
            print('----------------------------------')
            print('>>>There is nothing to get!')
    elif user_input == 'End':
        return end_game('Finish')
    elif user_input not in ['North', 'South', 'East', 'West']:
        print('Please Enter a valid Command')
    elif user_input not in options:
        print("Can't go there")

        return False
    elif user_input in ['North', 'South', 'East', 'West']:
        for check in options:
            if check == user_input:
                next_room = (rooms[room_list[location_counter]][user_input])
                if next_room == 'Dragon Room':
                    if len(items) < 5:
                        return end_game('Game Over')
                    elif len(items) == 5:
                        return end_game('Finish')
                location_counter = 0
                for check_rooms in room_list:
                    if str(check_rooms) != str(next_room):
                        location_counter += 1
                    elif str(check_rooms) == str(next_room):
                        break


title()
name = input("Hero's Name:")
story(name)

#main game
while status:
    directions = []
    for all_rooms in rooms.keys():
        room_list.append(all_rooms)
    current_room(room_list[location_counter])
    for i in rooms[room_list[location_counter]]:
        if i not in directions:
            directions.append(i)
    movement_options(directions,rooms.get(room_list[location_counter]))
    user = input('>').capitalize()
    check_movement(directions,user)



