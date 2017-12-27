#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from math import sqrt

class Triangulo(object):
    '''
    classdocs
    '''


    def __init__(self, elPunto1, elPunto2, elPunto3, relleno, lineas):
        '''
        Constructor
        '''
        
        self.punto1 = elPunto1
        self.punto2 = elPunto2
        self.punto3 = elPunto3
        
        self.colorRelleno = relleno
        self.colorLineas = lineas
        
    def GetPunto1(self):
        return self.punto1
    
    def GetPunto2(self):
        return self.punto2
    
    def GetPunto3(self):
        return self.punto3
    
    def GetColorRelleno(self):
        return self.colorRelleno
    
    def GetColorLineas(self):
        return self.colorLineas
    
    def GetPerimetro(self):
        return self.GetLado1() + self.GetLado2() + self.GetLado3()
    
    def GetArea(self):
        
        perimetro = self.GetPerimetro()
        s = perimetro / 2
    
        valorLado1 = s - self.GetLado1()
        valorLado2 = s - self.GetLado2()
        valorLado3 = s - self.GetLado3()
        
        area = sqrt(s * valorLado1 * valorLado2 * valorLado3)
        
        return area
        
    def GetAltura(self):
        
        area = self.GetArea()
        base = self.GetLado1()
        altura = (area / base) * 2
        
        return altura
    
    def GetLado1(self):
        
        valorX = pow(self.punto1.GetX() - self.punto2.GetX(), 2)
        valorY = pow(self.punto1.GetY() - self.punto2.GetY(), 2)
        
        distancia = sqrt(valorX + valorY)
        
        return distancia
    
    def GetLado2(self):
        
        valorX = pow(self.punto2.GetX() - self.punto3.GetX(), 2)
        valorY = pow(self.punto2.GetY() - self.punto3.GetY(), 2)
        
        distancia = sqrt(valorX + valorY)
        
        return distancia
    
    def GetLado3(self):
        
        valorX = pow(self.punto3.GetX() - self.punto1.GetX(), 2)
        valorY = pow(self.punto3.GetY() - self.punto1.GetY(), 2)
        
        distancia = sqrt(valorX + valorY)
        
        return distancia
    
    def Metodo1(self):
        return "Respuesta 1"
    
    def Metodo2(self):
        return "Respuesta 2"
