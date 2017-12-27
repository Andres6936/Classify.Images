#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelBotones(wx.Panel):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Obtenemos el padre de la clase.
        self.padre = args[0]

        self.botonPuntos = wx.Button(self, -1, 'Cambiar Puntos')
        self.Bind(wx.EVT_BUTTON, self.OnSetPuntos, self.botonPuntos)

        self.botonColorLinea = wx.Button(self, -1, 'Cambiar Lineas')
        self.Bind(wx.EVT_BUTTON, self.OnSetColorLinea, self.botonColorLinea)

        self.botonColorFondo = wx.Button(self, -1, 'Cambiar Fondo')
        self.Bind(wx.EVT_BUTTON, self.OnSetColorFondo, self.botonColorFondo)

        sizerLayout = wx.BoxSizer(wx.VERTICAL)

        sizerLayout.Add(self.botonPuntos, 0, wx.EXPAND)
        sizerLayout.Add(self.botonColorLinea, 0, wx.EXPAND)
        sizerLayout.Add(self.botonColorFondo, 0, wx.EXPAND)

        self.SetSizer(sizerLayout)
        self.Fit()

    def OnSetPuntos(self):
        pass

    def OnSetColorLinea(self):
        pass

    def OnSetColorFondo(self):
        pass
