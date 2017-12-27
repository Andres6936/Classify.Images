#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

class Punto(object):
    '''
    classdocs
    '''


    def __init__(self, x_coord, y_coord):
        '''
        Constructor
        '''
        
        self.x = x_coord
        self.y = y_coord
        
    def GetX(self):
        return self.x
    
    def GetY(self):
        return self.y
    
    def SetX(self, x_coord):
        self.x = x_coord
        
    def SetY(self, y_coord):
        self.y = y_coord