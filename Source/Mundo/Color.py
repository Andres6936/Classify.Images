#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

class Color(object):
    '''
    classdocs
    '''

    def __init__(self, elRojo, elVerde, elAzul):
        """
        Constructor
        """
        
        self.rojo = elRojo
        self.verde = elVerde
        self.azul = elAzul
        
    def GetRojo(self):
        return self.rojo
    
    def GetVerde(self):
        return self.verde
    
    def GetAzul(self):
        return self.azul
    
    def SetRojo(self, elRojo):
        self.rojo = elRojo
        
    def SetVerde(self, elVerde):
        self.verde = elVerde
        
    def SetAzul(self, elAzul):
        self.azul = elAzul