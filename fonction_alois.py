# sheep is bol. Players 1 = 0 and player_2 = 1

def get_distance():
    """Get the distance (distane between two entites)"""

def create_map_dictio():
    """create a dictionary with every usefull informations about the map creation from the #map file#

    notes
    -----
    the file should be in ./maps/

    version
    -------
    specification: Heynen Scott-Socrate (v1 20/02/24)
    """

def is_game_over():
    """check if game is over

    returns
    -------
    true if the game is over, false otherwise (bool)

    version
    -------
    specification : Heynen Scott-Socrate (v1 20/02/24)
    """

def display_map(map,player,seed):
    """display the map from the diction
    parameters
    ----------
    
    map : file .bsh (str)
    players : get players spawn poitn (int)
    grass : get the seed pos (int)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """ 

def try_spawn_sheep(sheep):
    """Spawn a sheep if it's needed
    parameters
    ----------
    sheep : player number (bol)
    
    notes
    -----
    if sheep is 0 -> it is player 1 (blue color)
    if sheep is 1 -> it is player 2 (red color)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def look_a_barrier(move_coordinate_x, move_coordinate_y):
    """Look if a sheep can spawn or move on a case.
    parameters
    ----------
    move_coordinate_x : player movement in x (int)
    move_coordinate_y : player movemenet in y (int)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """
    #think about specifiate the type of the thing that obstructs

def get_seed (seed_coordinate_x,seed_coordinate_y):
    """Verify if therer are a seed on the case
    parameters
    ----------
    seed_coordinate_x : coordinate in x of the seed (int)
    seed_coordinate_y : coordinate in y of the seed (int)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def growth_grass():
    """Growth all the grass, in fact add 1 to the life_stats"""

def grass_propagation (grass_coordinate):
    """Propage the grass around
    parameters
    ----------
    grass_coordinate : coordinate in x,y of the grass that will grow (int)
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def delete_emoji (emoji_deleted_x,emoji_deleted_y):
    """delete the emoji we need 
    parameters
    ----------
    emoji_deleted_x : position in x where the emoji is (int)
    emoji_deleted_y : position in y where the emoji is (int)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def attack_sheep(sheep, attack_coordinate_x, attack_coordinate_y):
    """Attack a sheep if he is near enough to be attack
    parameters
    ----------
    sheep : players sheep who attack (bol)
    attack_coordinate_x :  position in x where the sheep 1 is (int)
    attack_coordinate_y :  position in y where the sheep 1 is (int)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def move_sheep (old_coordinate,new_coordinate):
    """Move a sheep if he want to move or if i was attack
    parameters
    ----------
    old_coordinate : coordinate in x,y of the sheep where he was (int)
    new_coordinate : coordinate in x,y of the sheep where it will move (int)
    
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def sheep_graze(sheep, graze_coordinate_x, graze_coordinate_y):
    """Graze a grass if the sheep is on this case and the case
    parameters
    ----------
    sheep : player shep (bol)
    graze_coordinate_x : placement in x the sheep (int)
    graze_coordinate_y : placement in y the sheep (int)

    return
    ------
    emoji_deleted_x : coordinate in x of the grass that will be eaten.
    emoji_deleted_y : coordinate in y of the grass that will be eaten.

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def translate_orders (message):
    """Translate a string message into a list to be usable for the program
    parameters
    ----------
    message : get the player message (str)
    
    return 
    ------

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """
    
map={'rock':{'rock_1':(1,2),'rock_2':(2,5)}}

for rocks in map['rock']:
    my_tuples=map['rock'][rocks]

#get_sheep_life:()
