
"""
Created on Fri Nov 29 22:15:46 2019

"""

class DonkeyKong:
    
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    
    