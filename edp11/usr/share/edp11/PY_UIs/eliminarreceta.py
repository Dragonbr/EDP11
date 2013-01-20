# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/eliminarreceta.ui'
#
# Created: Sat Nov 12 01:01:58 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogElimR(object):
    def setupUi(self, DialogElimR):
        DialogElimR.setObjectName("DialogElimR")
        DialogElimR.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogElimR.resize(424, 321)
        DialogElimR.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogElimR)
        self.buttonBox.setGeometry(QtCore.QRect(210, 280, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.treeWidget = QtGui.QTreeWidget(DialogElimR)
        self.treeWidget.setGeometry(QtCore.QRect(20, 20, 381, 231))
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setMidLineWidth(1)
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(209)
        self.treeWidget.header().setMinimumSectionSize(170)

        self.retranslateUi(DialogElimR)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogElimR.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogElimR.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogElimR)

    def retranslateUi(self, DialogElimR):
        DialogElimR.setWindowTitle(QtGui.QApplication.translate("DialogElimR", "Eliminar Receta", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("DialogElimR", "Recetas", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogElimR = QtGui.QDialog()
    ui = Ui_DialogElimR()
    ui.setupUi(DialogElimR)
    DialogElimR.show()
    sys.exit(app.exec_())

