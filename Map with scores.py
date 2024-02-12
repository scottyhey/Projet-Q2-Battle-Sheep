import blessed

term = blessed.Terminal()

WhX = 60 # taille en x
Why = 40 # taille en y
x=Why 
my_dic={'player_grass1':{(10,2),(15,85),1,2,3,5,7,8,9,4,5,6,2,47,5,7,5,6,5,7},"player_grass2":{(10,2),(15,85),(25,84)}} #dictionnaire d'exemple pour les scores
def count_grass(term):  #fonction pour compter le nombre d'herbe que le joueurs posséde
    count=0
    for i in term:
        count+=1
    return count   
print (term.fullscreen)
print(term.clear) #initialisation du terminal
while Why > 0:
    if Why %2 == 0:
        print((term.peru_on_seagreen(' ')+term.on_darkolivegreen(' '))*int(WhX/2)) #permet d'alterner une case sur deux
    else:
        print((term.on_darkolivegreen(' ')+term.peru_on_seagreen(' '))*int(WhX/2))
    Why -= 1

def show_high_score(Length,Dictonary): #Fonction qui permet d'afficher les scores
    playerscore_1=str(count_grass(Dictonary['player_grass1']))
    playerscore_2=str(count_grass(Dictonary['player_grass2'])) #Récupére les scores pour chaque joueurs
    minus=(len(playerscore_1)) #Permet de trouver la valeur pour centrer le score du joueur 1
    print (term.move_xy(Length-minus,0)+term.blue+playerscore_1)
    print (term.move_xy(0,0)+term.red+playerscore_2)
    print (term.home) #Affiche les scores

show_high_score(WhX,my_dic)
print ("\n"*x+term.white)
str(input("Insert your instructions:")) #Suite dans le code pour pouvoir écrires ces instructions
