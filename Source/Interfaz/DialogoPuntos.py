#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class DialogoPuntos(wx.Dialog):

    def __init__(self, *args, **kwargs):

        super(DialogoPuntos, self).__init__(*args, **kwargs)

        # Ventana principal.
        self.padre = args[0]

        self.triangulo = self.padre.GetTriangulo()
