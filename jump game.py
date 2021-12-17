import pyxel
import Mario
import constants
import Characters
import donkeykong
import random


def marioMovements(): #making mario move and jump
    if pyxel.btn(pyxel.KEY_RIGHT):
        mario.move2('right')
        if pyxel.btn(pyxel.KEY_SPACE):
            mario.times=pyxel.frame_count
            mario.jump('right')
        
        elif pyxel.frame_count-mario.times==1:
            mario.notJump('right')
            
    elif pyxel.btn(pyxel.KEY_LEFT):
        mario.move2('left')
        if pyxel.btn(pyxel.KEY_SPACE):
            mario.times=pyxel.frame_count
            mario.jump('left')
        
        elif pyxel.frame_count-mario.times==1:
            mario.notJump('left')
            
    elif pyxel.btn(pyxel.KEY_UP) :
        mario.move2('up')
    elif pyxel.btn(pyxel.KEY_DOWN): 
        mario.move2('down')


def barrelManagement():
    if random.randint(1,10)<=5 and len(listBarrels) < 10 and pyxel.frame_count%70==0:

        barrel=Characters.barrels(constants.DONKEY_X+20, constants.BARREL_Y[1], constants.BARREL_DIR)
        listBarrels.append(barrel) #generating barrels

    
    for i in listBarrels:
        i.move() #move barrels
        

        if i.y>constants.HEIGHT or i.x>constants.WIDTH:
            listBarrels.remove(i) #remove barrels when they reach the end
            
        if i.y in range(mario.y,mario.y+10) and i.x in range(mario.x-8,mario.x+8): # mario goes  back to the starting point and loss one live when he hits the barrels
            mario.x=constants.MARIO_X
            mario.y=constants.MARIO_Y
            mario.lives-=1
            
        if i.x in range(mario.x,mario.x+2) and i.y>mario.y+12 and pyxel.frame_count-mario.times<=3:# 100 points obtained by jumping over a barrel
            scorebox.point+=100


        
def update():
    ''' This function is executed every frame. Now it only checks if the user
    pressed Q to finish'''
    global x, y
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
        
    else:
        marioMovements()
        barrelManagement()

        

        
        
def draw():
    ''' This function draws graphics from the image bank'''
    pyxel.cls(0)
    pyxel.blt(donkeyKong.x,donkeyKong.y,0,4,56,44,36,colkey=False)#donkey
    pyxel.blt(princess.x,princess.y,1,4,0,-24,40,colkey=False)#princess
    pyxel.blt(barrel1.x,barrel1.y,0,9,101,13,36,colkey=False)#barrel1
    pyxel.blt(barrel2.x,barrel2.y,0,34,105,16,16,colkey=False) #barrel2
    pyxel.blt(floor1.x,floor1.y,0,0,248,200,8)#first floor
    pyxel.blt(platform.x,platform.y,0,0,248,32,8)#platform for princess
    pyxel.blt(scorebox.x,scorebox.y,0,176,96,48,24, colkey=False)#scorebox
    pyxel.text(livestitle.x[0],livestitle.y[0],"LIVES REMAINING:%i"%mario.lives,10)# tex for showing number of lives
    pyxel.text(constants.SCORE_POINT_X,constants.SCORE_POINT_Y,"%i"%scorebox.point,10) #scorebox
    for j in listLadders: #all the ladders
        pyxel.blt(j.x,j.y,0,0,16,8,16)
    for i in listBarrels: #all the barrels
        pyxel.blt(i.x,i.y,0,34,105,16,16,colkey=False)
    for f in listFloors:# all the floors except the ground floor
        pyxel.blt(f.x,f.y,0,0,248,184,8)
    pyxel.blt(mario.x,mario.y,0,28,32,-16,16, colkey=False) #mario
    if mario.lives<=0: # if lives are all lost, screen goes black and print "YOU"RE DEAD!" 
        pyxel.cls(0)
        pyxel.text(constants.WIDTH/3, constants.HEIGHT/2, "YOU’RE DEAD!", 8)

          
    

listBarrels=[ ]
listLadders=[ ]
listFloors=[ ]
mario=Mario.Mario(constants.MARIO_X,constants.MARIO_Y,constants.LIVES, constants.SALTAR, constants.TIMES) #create object Mario
princess=Characters.princess(constants.PRINCESS_X, constants.PRINCESS_Y)#create object princess
for j in range(0,10):#create objects ladders
    ladder1=Characters.ladders(constants.LADDER_X1[j], constants.LADDER_Y[j])
    listLadders.append(ladder1)
for f in range(0,5):#create objects floors
    floor=Characters.floors(constants.FLOOR_X1[f],constants.FLOOR_Y1[f])
    listFloors.append(floor)
floor1=Characters.floors(constants.FLOOR_X[0],constants.FLOOR_Y[0])#create object the ground floor
platform=Characters.floors(constants.PLATFORM_X, constants.PLATFORM_Y)#create object where the princess stands
livestitle=Characters.livestitle(constants.LIVESTITLE_X,constants.LIVESTITLE_Y, mario.lives)#create object the text of shw=owing the number of lives
scorebox=Characters.socreBox(constants.SCOREBOX_X, constants.SCOREBOX_Y, constants.SCORE_POINT)#create object scorebox
donkeyKong=donkeykong.DonkeyKong(constants.DONKEY_X, constants.DONKEY_Y)#create object donkey kong
barrel1=Characters.barrels(constants.BARREL_X,constants.BARREL_Y[0],constants.BARREL_DIR)#create object the standing barrel
barrel2=Characters.barrels(constants.BARREL_X,constants.BARREL_Y[1], constants.BARREL_DIR)#create object the barrel facing players
CAPTION = "Donkey Kong"
pyxel.init(constants.WIDTH, constants.HEIGHT, caption=CAPTION)


pyxel.load("assets\my_resource.pyxres")

pyxel.run(update,draw)
