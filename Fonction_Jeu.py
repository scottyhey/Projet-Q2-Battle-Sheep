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
    specification : Heynen Scott-Socrate (v1 20/02/24)"""


def display_map(map,player,seed):
    """display the map from the diction
    parameters
    ----------
    
    map : dictonary of the map with the size of the map, rocks, player spawn and seeds (dic)
    players : dictonary of the différent sheeps and their ownership (dic)
    grass : dictonary of the grass and their ownership (dic)

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

def look_a_barrier(coordonate):
    """Look if a sheep can spawn or move on a case.
    parameters
    -----------
    coordonate: The coordonate x and y of the case we wanted to see (tuples)
    return
    -----------
    type: return if there are a sheep, a rock, the limit of the maps or nothing. (str) 
    """
    
    #think about specifiate the type of the thing that obstructs

def get_seed (coordonate):
    """Verify if therer are a seed on the case"""

def growth_grass():
    """Growth all the grass, in fact add 1 to the life_stats"""

def grass_propagation (coordonate):
    """Propage the grass around"""

def delete_emoji (coordonate):
    """delete the emoji we need """

def attack_sheep(coordonate):
    """Attack a sheep if he is near enough to be attack"""

def move_sheep (old_coordonate,new_coordonate):
    """Move a sheep if he want to move or if i was attack"""

def sheep_graze(coordonate):
    """Graze a grass if the sheep is on this case and the case"""

def translate_orders (messsage):
    """Translate a string message into a list to be usable for the program"""
    
map={'rock':{'rock_1':(1,2),'rock_2':(2,5)}}

for rocks in map['rock']:
    my_tuples=map['rock'][rocks]

#get_sheep_life:()
