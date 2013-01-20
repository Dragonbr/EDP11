# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/eliminaringrediente.ui'
#
# Created: Sat Nov 12 01:01:05 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog_EIngr(object):
    def setupUi(self, Dialog_EIngr):
        Dialog_EIngr.setObjectName("Dialog_EIngr")
        Dialog_EIngr.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_EIngr.resize(300, 108)
        Dialog_EIngr.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_EIngr)
        self.buttonBox.setGeometry(QtCore.QRect(55, 60, 180, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(Dialog_EIngr)
        self.label.setGeometry(QtCore.QRect(25, 20, 250, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_EIngr)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_EIngr.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_EIngr.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_EIngr)

    def retranslateUi(self, Dialog_EIngr):
        Dialog_EIngr.setWindowTitle(QtGui.QApplication.translate("Dialog_EIngr", "Eliminar Ingrediente", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_EIngr", "¿Esta seguro de Eliminar Ingrediente?", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_EIngr = QtGui.QDialog()
    ui = Ui_Dialog_EIngr()
    ui.setupUi(Dialog_EIngr)
    Dialog_EIngr.show()
    sys.exit(app.exec_())

