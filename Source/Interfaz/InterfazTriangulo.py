#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

from Source.Interfaz.PanelInfo import PanelInfo
from Source.Interfaz.PanelImagen import PanelImagen
from Source.Interfaz.PanelBotones import PanelBotones
from Source.Interfaz.PanelOpciones import PanelOpciones
from Source.Interfaz.PanelTriangulo import PanelTriangulo

from Source.Mundo.Triangulo import Triangulo
from Source.Mundo.Punto import Punto
from Source.Mundo.Color import Color


class InterfazTriangulo(wx.Frame):

    def __init__(self, *args, **kw):

        super().__init__(*args, **kw)

        self.SetBackgroundColour('White')

        self.SetTitle("Triángulo")

        self.punto1 = Punto(120, 20)
        self.punto2 = Punto(220, 200)
        self.punto3 = Punto(20, 200)

        self.colorRelleno = Color(0, 0, 170)

        self.colorLineas = Color(0, 0, 0)

        self.triangulo = Triangulo(self.punto1, self.punto2, self.punto3,
                                   self.colorRelleno, self.colorLineas)

        # Construye los paneles.
        self.panelTriangulo = PanelTriangulo(self, -1)
        self.panelOpciones = PanelOpciones(self, -1)
        self.panelBotones = PanelBotones(self, -1)
        self.panelImagen = PanelImagen(self, -1)
        self.panelInfo = PanelInfo(self, -1)

        # Enviamos el triangulo para dibujar.
        self.panelTriangulo.SetTriangulo(self.triangulo)

        # Construye la forma del Frame.
        sizerLayoutRoot = wx.BoxSizer(wx.VERTICAL)

        # Construye Layout con titulos.
        sizerLayoutOpciones = wx.StaticBoxSizer(wx.VERTICAL, self, 'Opciones')
        sizerLayoutBotones = wx.StaticBoxSizer(wx.VERTICAL, self, 'Modificaciones')
        sizerLayoutInfo = wx.StaticBoxSizer(wx.VERTICAL, self, 'Información')

        # Añadimos los paneles a los layout con titulos.
        sizerLayoutOpciones.Add(self.panelOpciones, 0, wx.EXPAND | wx.ALL, 3)
        sizerLayoutBotones.Add(self.panelBotones, 0, wx.EXPAND | wx.ALL, 3)
        sizerLayoutInfo.Add(self.panelInfo, 0, wx.EXPAND | wx.ALL, 3)

        sizerLayoutComdin = wx.BoxSizer(wx.VERTICAL)

        sizerLayoutComdin.Add(sizerLayoutBotones, 1, wx.EXPAND)
        sizerLayoutComdin.Add(sizerLayoutInfo, 1, wx.EXPAND)

        sizerLayoutVertical = wx.BoxSizer(wx.HORIZONTAL)

        sizerLayoutVertical.Add(sizerLayoutComdin, 1, wx.EXPAND)
        sizerLayoutVertical.Add(self.panelTriangulo, 2, wx.EXPAND)

        sizerLayoutRoot.Add(self.panelImagen, 0, wx.EXPAND)
        sizerLayoutRoot.Add(sizerLayoutVertical, 1, wx.EXPAND | wx.ALL, 5)
        sizerLayoutRoot.Add(sizerLayoutOpciones, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizerLayoutRoot)
        self.Fit()

        self.Show(True)

        # Actualizamos la información.
        self.Repintar()

    def GetTriangulo(self):
        """
        Devuelve el triángulo actual.

        :return: Triángulo.
        """

        return self.triangulo

    def SetPuntos(self):
        pass

    def SetColorFondo(self):
        pass

    def SetColorLineas(self):
        pass

    def Repintar(self):

        self.panelInfo.SetInformacion(self.triangulo.GetPerimetro(),
                                      self.triangulo.GetArea(),
                                      self.triangulo.GetAltura())

    def Colineales(self):
        pass

    def reqFuncOpcion1(self):
        pass

    def reqFuncOpcion2(self):
        pass
