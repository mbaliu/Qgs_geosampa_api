# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SP_CroquiFiscalDialog
                                 A QGIS plugin
 Baixa o croqui fiscal do site da prefeitura
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-04-10
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Marcelo Baliú Fiamenghi
        email                : ma.baliu@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'croqui_fiscal_dialog_base.ui'))


class SP_CroquiFiscalDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SP_CroquiFiscalDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)


    # Choose the destination directory
    def diretorio(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(parent=None, caption=QtWidgets.QApplication.translate("selecione a pasta de destino", "Selecione o diretorio ..."), directory=rQtCore.QDir.currentPath())
        # filename = QtWidgets.QFileDialog.getExistingDirectory(parent=None, caption=QtWidgets.QApplication.translate("select destination", "Select directory to Fling from..."), directory=QtCore.QDir.currentPath())
        if filename:
            self._diretorio.setText(filename)