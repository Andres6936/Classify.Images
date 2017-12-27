#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelTriangulo(wx.Panel):

    def __init__(self, *args, **kwargs):
        """
        Constructor del panel.

        :param args: Lista de argumentos.
        :param kwargs: Diccionario de argumentos.
        """

        # Enviamos todos los parametros a la clase padre.
        super().__init__(*args, **kwargs)

        # Triángulo a dibujar.
        self.triangulo = None

        # Asociamos el método a un evento.
        self.Bind(wx.EVT_PAINT, self.PaintComponent)

        self.SetSize(wx.Size(270, 200))

    def SetTriangulo(self, elTriangulo):

        self.triangulo = elTriangulo

    def PaintComponent(self, event):

        device = wx.PaintDC(self)
        device.SetBackground(wx.Brush(wx.WHITE))
        device.Clear()

        # Obtenemos el color de fondo.
        colorFondo = wx.Colour(self.triangulo.GetColorRelleno().GetRojo(),
                               self.triangulo.GetColorRelleno().GetVerde(),
                               self.triangulo.GetColorRelleno().GetAzul())

        # Obtenemos el color del borde.
        colorLineas = wx.Colour(self.triangulo.GetColorLineas().GetRojo(),
                                self.triangulo.GetColorLineas().GetVerde(),
                                self.triangulo.GetColorLineas().GetRojo())

        # Pinta el fondo.
        device.SetBrush(wx.Brush(colorFondo))

        # Pinta el borde.
        device.SetPen(wx.Pen(colorLineas))

        puntos1 = (int(self.triangulo.GetPunto1().GetX()),
                   int(self.triangulo.GetPunto1().GetY()))

        puntos2 = (int(self.triangulo.GetPunto2().GetX()),
                   int(self.triangulo.GetPunto2().GetY()))

        puntos3 = (int(self.triangulo.GetPunto3().GetX()),
                   int(self.triangulo.GetPunto3().GetY()))

        device.DrawPolygon([puntos1, (puntos2), (puntos3)])