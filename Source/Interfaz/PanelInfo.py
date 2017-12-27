#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelInfo (wx.Panel):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.etiquetaPerimetro = wx.StaticText(self, -1, 'Perímetro')

        self.etiquetaArea = wx.StaticText(self, -1, 'Área')

        self.etiquetaAltura = wx.StaticText(self, -1, 'Altura')

        sizerLayout = wx.BoxSizer(wx.VERTICAL)

        sizerLayout.Add(self.etiquetaPerimetro, 0, wx.EXPAND)
        sizerLayout.Add(self.etiquetaArea, 0, wx.EXPAND)
        sizerLayout.Add(self.etiquetaAltura, 0, wx.EXPAND)

        self.SetSizer(sizerLayout)
        self.Fit()

    def SetInformacion(self, perimetro, area, altura):

        self.etiquetaPerimetro.SetLabelText("Perímetro: {0:.2f} px".format(perimetro))
        self.etiquetaArea.SetLabelText("Área: {0:.2f} px".format(area))
        self.etiquetaAltura.SetLabelText("Altura: {0:.2f} px".format(altura))