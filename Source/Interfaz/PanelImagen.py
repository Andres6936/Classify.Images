#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelImagen(wx.Panel):

    def __init__(self, *args, **kwargs):
        """
        Constructor.

        :param args: Lista de parámetros.
        :param kwargs: Diccionario de parámetros.
        """

        super().__init__(*args, **kwargs)

        self.rutaImagen = 'Data/Titulo.png'

        # Imagen vacia.
        self.imagen = wx.Bitmap(self.rutaImagen, wx.BITMAP_TYPE_PNG)
        # Imagen del Banner.
        self.imagenBanner = wx.StaticBitmap(self, -1)
        # Cargamos la imagen del Banner.
        self.imagenBanner.SetBitmap(self.imagen)

        # Damos forma al panel.
        sizerLayout = wx.BoxSizer(wx.VERTICAL)
        sizerLayout.Add(self.imagenBanner, 0, wx.EXPAND)

        self.SetSizer(sizerLayout)

        self.Layout()
