# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/abrirperfildiet.ui'
#
# Created: Sat Nov 12 00:59:30 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogDiet(object):
    def setupUi(self, DialogDiet):
        DialogDiet.setObjectName("DialogDiet")
        DialogDiet.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogDiet.resize(424, 316)
        DialogDiet.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogDiet)
        self.buttonBox.setGeometry(QtCore.QRect(210, 280, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Button_Nuevo = QtGui.QPushButton(DialogDiet)
        self.Button_Nuevo.setGeometry(QtCore.QRect(29, 283, 83, 25))
        self.Button_Nuevo.setObjectName("Button_Nuevo")
        self.Button_Elim = QtGui.QPushButton(DialogDiet)
        self.Button_Elim.setGeometry(QtCore.QRect(123, 283, 83, 25))
        self.Button_Elim.setObjectName("Button_Elim")
        self.treeWidget = QtGui.QTreeWidget(DialogDiet)
        self.treeWidget.setGeometry(QtCore.QRect(20, 20, 381, 231))
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setMidLineWidth(1)
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(209)
        self.treeWidget.header().setMinimumSectionSize(170)

        self.retranslateUi(DialogDiet)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogDiet.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogDiet.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogDiet)
        DialogDiet.setTabOrder(self.treeWidget, self.Button_Nuevo)
        DialogDiet.setTabOrder(self.Button_Nuevo, self.Button_Elim)
        DialogDiet.setTabOrder(self.Button_Elim, self.buttonBox)

    def retranslateUi(self, DialogDiet):
        DialogDiet.setWindowTitle(QtGui.QApplication.translate("DialogDiet", "Abrir Perfil Dietista", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_Nuevo.setText(QtGui.QApplication.translate("DialogDiet", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_Elim.setText(QtGui.QApplication.translate("DialogDiet", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("DialogDiet", "Dietista", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("DialogDiet", "D.N.I.", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogDiet = QtGui.QDialog()
    ui = Ui_DialogDiet()
    ui.setupUi(DialogDiet)
    DialogDiet.show()
    sys.exit(app.exec_())

