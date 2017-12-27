#!/usr/bin/env python3
# coding=utf-8
# @Date Created on 21/12/2017
# @author: Joan Andrés

import wx

from Source.Interfaz.InterfazTriangulo import InterfazTriangulo


class ApplicationManager(wx.App):

    def __init__(self, *args, **kwargs):

        # Enviamos todos los parámetros a la clase padre.
        super().__init__(self, *args, **kwargs)

    def OnInit(self):

        self.frame = InterfazTriangulo(parent=None, id=-1, title='Triángulo')
        self.SetTopWindow(self.frame)
        return True
