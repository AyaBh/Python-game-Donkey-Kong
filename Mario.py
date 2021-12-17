
"""
Created on Mon Nov 18 16:17:10 2019

"""
import constants
class Mario:
    
    def __init__(self,x,y,lives,saltando, times):
        self.__x=x
        self.__y=y
        self.__lives=lives
        self.__saltando=saltando
        self.__times=times
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,value):
        self.__x=value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,value):
        self.__y=value
    @property
    def lives(self):
        return self.__lives
    @lives.setter
    def lives(self,value):
        self.__lives=value
    @property
    def saltando(self):
        return self.__saltando
    @property
    def times(self):
        return self.__times
    @times.setter
    def times(self,value):
        self.__times=value
        
    
    def jump(self, direction):# allows mario jump
        if direction=='right':
            if 0<self.__x<constants.WIDTH-26 and not self.__saltando:
                self.__x+=11
                self.__y-=11
                self.__saltando= not self.__saltando
    
 
        elif direction=='left':
            if 10<self.__x<constants.WIDTH-26 and not self.__saltando:
                self.__x-=11
                self.__y-=11
                self.__saltando= not self.__saltando
        


        
    def notJump(self, direction): #allows mario falls back to the floor after jumping
        if direction=='right':
            if self.__saltando:
                self.__x+=11
                self.__y+=11
                self.__saltando= not self.__saltando
            
        elif direction=='left':
            if self.__saltando:
                self.__x-=11
                self.__y+=11
                self.__saltando= not self.__saltando
                

    
    def move2(self,direction):

            if direction=='right' and self.__x<=constants.WIDTH-15:
                self.__x+=1 #mario moves to the right by 1
                for r in range(0,5): # if mario is inbetween the ladders, he doesn't move to the left or the right
                    if self.__x in range(constants.coor_x[r],constants.COOR_X[r]) and self.__y in range(constants.COOR_Y[r],constants.coor_y[r]):
                        self.__x+=0
                    for c in range(0,3):#mario falls from the gaps
                        if self.__x>constants.GAP1[c] and self.__y in range(constants.COOR_Y[c], constants.coor_y[c]):
                            self.__y+=40
                            
            elif direction=='left' and self.__x>=1:
                self.__x-=1#mario moves to the left by 1
                for p in range(0,5):# if mario is inbetween the ladders, he doesn't move to the left or the right
                    if self.__x in range(constants.coor_x[p],constants.COOR_X[p]) and self.__y in range(constants.COOR_Y[p],constants.coor_y[p]):
                        self.__x+=0
                    for i in range(0,2):#mario falls from the gaps
                        if self.__x<constants.GAP2[i] and self.__y in range(constants.COOR_Y[i+3], constants.coor_y[i+3]):
                            self.__y+=40
            elif direction=='up' and self.__x > 5:
                for j in range(0,5):#mario can go up on the ladders
                    if self.__x in range(constants.coor_up_x[j], constants.COOR_UP_X[j]) and self.__y in range(constants.COOR_UP_Y[j], constants.coor_up_y[j]):
                        self.__y-=1
                        
            elif direction=='down' and self.__x<constants.HEIGHT-22:
                for q in range(0,4):#mario can go down on the ladders
                    if (self.__x in range(constants.coor_down_x[q],constants.COOR_DOWN_X[q]) and self.__y in range(constants.COOR_DOWN_Y[q],constants.coor_down_y[q])) or self.__x in range(constants.coor_down_x1, constants.COOR_DOWN_X1):
                        self.__y+=1
   

    
    
        
    
    
    