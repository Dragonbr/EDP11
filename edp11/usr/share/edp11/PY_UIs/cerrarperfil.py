# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/cerrarperfil.ui'
#
# Created: Sat Nov 12 01:00:47 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogCPerf(object):
    def setupUi(self, DialogCPerf):
        DialogCPerf.setObjectName("DialogCPerf")
        DialogCPerf.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogCPerf.resize(280, 108)
        DialogCPerf.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogCPerf)
        self.buttonBox.setGeometry(QtCore.QRect(50, 60, 180, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(DialogCPerf)
        self.label.setGeometry(QtCore.QRect(20, 20, 244, 20))
        self.label.setObjectName("label")

        self.retranslateUi(DialogCPerf)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogCPerf.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogCPerf.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogCPerf)

    def retranslateUi(self, DialogCPerf):
        DialogCPerf.setWindowTitle(QtGui.QApplication.translate("DialogCPerf", "Cerrar Perfil", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogCPerf", "       ¿Esta seguro de Cerrar Perfil?", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogCPerf = QtGui.QDialog()
    ui = Ui_DialogCPerf()
    ui.setupUi(DialogCPerf)
    DialogCPerf.show()
    sys.exit(app.exec_())

