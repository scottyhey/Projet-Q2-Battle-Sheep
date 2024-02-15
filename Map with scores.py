import blessed,time

term = blessed.Terminal()
print(term.clear)
WhX = 60 # taille en x
Why = 40
x=Why
my_dic={'player_grass1':{(10,2),(15,85),1,2,3,5,7,8,9,4,5,6,2,47,5,7,5,6,5,7},"player_grass2":{(10,2),(15,85),(25,84)}}
def count_grass(term):
    count=0
    for i in term:
        count+=1
    return count
while Why > 0:
    if Why %2 == 0:
        print((term.peru_on_seagreen('  ')+term.on_darkolivegreen('  '))*int(WhX/2))
    else:
        print((term.on_darkolivegreen('  ')+term.peru_on_seagreen('  '))*int(WhX/2))
    Why -= 1

def show_high_score(Length,Dictonary):
    playerscore_1=str(count_grass(Dictonary['player_grass1']))
    playerscore_2=str(count_grass(Dictonary['player_grass2']))
    minus=(len(playerscore_1))
    print (term.move_xy(Length*2-minus,0)+term.blue+playerscore_1)
    print (term.move_xy(0,0)+term.red+playerscore_2)
    print (term.home)

show_high_score(WhX,my_dic)
print (term.move_xy(0,1)+term.peru_on_seagreen+"🐑")
time.sleep(0.5)
print (term.move_xy(0,1)+term.peru_on_seagreen+"  ")
print (term.move_xy(2,2)+term.peru_on_seagreen+"🐑")
time.sleep(0.5)
print (term.move_xy(0,1)+term.peru_on_seagreen+"🌱")
print ("\n"*x+term.white+term.normal)
str(input("Insert your instructions:"))
