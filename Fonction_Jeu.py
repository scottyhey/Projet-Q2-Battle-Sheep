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

def look_a_barrier(case_coordonate):
    """Look if a sheep can spawn or move on a case.
    parameters
    -----------
    case_coordonate: The coordonate x and y of the case we wanted to see (tuples)
    return
    -----------
    type: return if there are a sheep, a rock, the limit of the maps or nothing. (str) 
    """
    
    #Faudrait peut être l'améliorer pour choisir de vérifier qu'une condition ou plusieurs en fonction de nos besoins

def get_seed (coordonate):
    """Verify if therer are a seed on the case""" #je crois pas qu'on en as besoin vu qu'on à la fonction look_a_barrier

def growth_grass():
    """Growth all the grass, in fact add 1 to the life_stats"""

def grass_propagation (coordonate):
    """Propage the grass around
    parameters
    ----------
    grass_coordinate : coordonate in x,y of the grass that will grow (tuples)
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """
def delete_emoji (emoji_coordonate):
    """delete the emoji we need 
    parameters
    ----------
    emoji_coordonate: coordonate in x,y of the emoji we want to delete, in fact remplace by a double space (tuples or list depend if the emoji is element of 
    the map or a sheep)
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def attack_sheep(sheep,attack_coordonate):
    """Attack a sheep if he is near enough to be attack
    parameters
    ----------
    sheep : players sheep who attack (bol)      
    attack_coordonate: position in x and y where the sheep attacked is (tuples)
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def move_sheep (old_coordonate,new_coordonate):
    """Move a sheep if he want to move or if i was attack
    parameters
    ----------
    old_coordinate : coordinate in x,y of the sheep where he was (list)
    new_coordinate : coordinate in x,y of the sheep where it will move (list)
    
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def sheep_graze(sheep, grass_coordonate):
     """Graze a grass if the sheep is on this case and the case
    parameters
    ----------
    sheep : player shep (bol)
    grass_coordonate: placement in x and y of the sheep (list)
    return
    ------
    emojii_deleted: coordinate in x and y of the grass that will be eaten (tuples)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def translate_orders (messsage):
    """Translate a string message into a list to be usable for the program
    parameters
    ----------
    message : get the player message (str)
    
    return 
    orders: a list with every separate order. The orders are in the chronologic order (the first one is for the first phase) (list)
    ------

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """
    
map={'rock':{'rock_1':(1,2),'rock_2':(2,5)}}

for rocks in map['rock']:
    my_tuples=map['rock'][rocks]

#get_sheep_life:()
