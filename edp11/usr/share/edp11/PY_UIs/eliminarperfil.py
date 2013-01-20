# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/eliminarperfil.ui'
#
# Created: Sat Nov 12 01:01:38 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogEPerf(object):
    def setupUi(self, DialogEPerf):
        DialogEPerf.setObjectName("DialogEPerf")
        DialogEPerf.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogEPerf.resize(280, 142)
        DialogEPerf.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogEPerf)
        self.buttonBox.setGeometry(QtCore.QRect(52, 100, 176, 30))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(DialogEPerf)
        self.label.setGeometry(QtCore.QRect(34, 20, 212, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(DialogEPerf)
        self.lineEdit.setGeometry(QtCore.QRect(84, 48, 112, 22))
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.label_error = QtGui.QLabel(DialogEPerf)
        self.label_error.setGeometry(QtCore.QRect(63, 76, 154, 17))
        self.label_error.setStyleSheet("color: #ff0000")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")

        self.retranslateUi(DialogEPerf)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogEPerf.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogEPerf.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogEPerf)
        DialogEPerf.setTabOrder(self.lineEdit, self.buttonBox)

    def retranslateUi(self, DialogEPerf):
        DialogEPerf.setWindowTitle(QtGui.QApplication.translate("DialogEPerf", "Eliminar Perfil", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogEPerf", "¿Esta seguro de Eliminar Perfil?", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogEPerf = QtGui.QDialog()
    ui = Ui_DialogEPerf()
    ui.setupUi(DialogEPerf)
    DialogEPerf.show()
    sys.exit(app.exec_())

