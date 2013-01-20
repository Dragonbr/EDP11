# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/cerrarpaciente.ui'
#
# Created: Sat Nov 12 01:00:32 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogCPac(object):
    def setupUi(self, DialogCPac):
        DialogCPac.setObjectName("DialogCPac")
        DialogCPac.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogCPac.resize(280, 108)
        DialogCPac.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogCPac)
        self.buttonBox.setGeometry(QtCore.QRect(50, 60, 180, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(DialogCPac)
        self.label.setGeometry(QtCore.QRect(30, 20, 220, 20))
        self.label.setObjectName("label")

        self.retranslateUi(DialogCPac)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogCPac.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogCPac.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogCPac)

    def retranslateUi(self, DialogCPac):
        DialogCPac.setWindowTitle(QtGui.QApplication.translate("DialogCPac", "Cerrar Paciente", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogCPac", "¿Esta seguro de Cerrar Paciente?", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogCPac = QtGui.QDialog()
    ui = Ui_DialogCPac()
    ui.setupUi(DialogCPac)
    DialogCPac.show()
    sys.exit(app.exec_())

