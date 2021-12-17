
"""
Created on Fri Nov 29 17:24:02 2019


"""
import constants
import random
class princess:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    
class ladders:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    
class floors:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    
class livestitle:
    def __init__(self,x,y,number):
        self.__x=x
        self.__y=y
        self.__number=number
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self,value):
        return self.__number

class socreBox:
    def __init__(self,x,y,point):
        self.__x=x
        self.__y=y
        self.__point=point
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def point(self):
        return self.__point
    @point.setter
    def point(self, value):
        self.__point=value

class barrels:
    def __init__(self,x,y,direction):
        self.__x=x
        self.__y=y
        self.___direction=direction
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def direction(self):
        return self.__direction
    
    def move(self):
        #barrels moving to right and fall
        for r in range(0,3):
            
            if (self.__y==constants.FLOOR_R[r]-12) and self.__x<(constants.WIDTH-constants.FLOOR_X[1]) and self.___direction:
                self.__x+=1
                if (self.__x==constants.LADDER_R[r]) and random.randint(0,100)<=25 and self.___direction:
                    self.__y+=40
                    self.___direction=not self.___direction
                elif (self.__x == constants.WIDTH-constants.FLOOR_X[1]) and (self.__y==constants.FLOOR_R[r]-12):
                    self.__y+=40
                    self.___direction=not self.___direction
         
      
       #barrels moving to left and fall
            elif (self.__y==constants.FLOOR_L[r]-12) and self.__x+8>=constants.FLOOR_X[1] and (not self.___direction):
                self.__x-=1

                if (self.__x==constants.LADDER_L[r]) and random.randint(0,100)<=25 and (not self.___direction):
                    self.__y+=40
                    self.___direction=not self.___direction

                if (self.__x+8 == constants.FLOOR_X[1]-1) and (self.__y==constants.FLOOR_L[r]-12):
                    self.__y+=40
                    self.___direction= not self.___direction


        
    
        
        
    
    
