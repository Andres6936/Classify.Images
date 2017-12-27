#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelOpciones(wx.Panel):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Obtenemos el padre de la clase.
        self.principal = args[0]

        self.botonOpcion1 = wx.Button(self, -1, 'Opción 1')
        self.Bind(wx.EVT_BUTTON, self.OnOpcion1, self.botonOpcion1)

        self.botonOpcion2 = wx.Button(self, -1, 'Opción 2')
        self.Bind(wx.EVT_BUTTON, self.OnOpcion2, self.botonOpcion2)

        sizerLayout = wx.BoxSizer(wx.HORIZONTAL)

        sizerLayout.Add(self.botonOpcion1, 1, wx.EXPAND)
        sizerLayout.Add(self.botonOpcion2, 1, wx.EXPAND)

        self.SetSizer(sizerLayout)
        self.Fit()

    def OnOpcion1(self):

        self.principal.reqFuncOpcion1()

    def OnOpcion2(self):

        self.principal.reqFuncOpcion2()
