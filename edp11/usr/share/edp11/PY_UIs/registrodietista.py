# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/registrodietista.ui'
#
# Created: Sat Nov 12 01:04:50 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog_RegD(object):
    def setupUi(self, Dialog_RegD):
        Dialog_RegD.setObjectName("Dialog_RegD")
        Dialog_RegD.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_RegD.resize(451, 261)
        Dialog_RegD.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_RegD)
        self.buttonBox.setGeometry(QtCore.QRect(250, 220, 181, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_dni = QtGui.QLineEdit(Dialog_RegD)
        self.lineEdit_dni.setGeometry(QtCore.QRect(140, 34, 101, 27))
        self.lineEdit_dni.setObjectName("lineEdit_dni")
        self.lineEdit_nom = QtGui.QLineEdit(Dialog_RegD)
        self.lineEdit_nom.setGeometry(QtCore.QRect(140, 81, 291, 27))
        self.lineEdit_nom.setText("")
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.lineEdit_pass = QtGui.QLineEdit(Dialog_RegD)
        self.lineEdit_pass.setGeometry(QtCore.QRect(140, 130, 141, 27))
        self.lineEdit_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.label = QtGui.QLabel(Dialog_RegD)
        self.label.setGeometry(QtCore.QRect(40, 38, 51, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog_RegD)
        self.label_2.setGeometry(QtCore.QRect(40, 84, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog_RegD)
        self.label_3.setGeometry(QtCore.QRect(40, 134, 91, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit_pass2 = QtGui.QLineEdit(Dialog_RegD)
        self.lineEdit_pass2.setGeometry(QtCore.QRect(140, 180, 141, 27))
        self.lineEdit_pass2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_pass2.setObjectName("lineEdit_pass2")
        self.label_4 = QtGui.QLabel(Dialog_RegD)
        self.label_4.setGeometry(QtCore.QRect(40, 186, 91, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Dialog_RegD)
        self.label_5.setGeometry(QtCore.QRect(40, 171, 47, 17))
        self.label_5.setObjectName("label_5")
        self.label_verif2 = QtGui.QLabel(Dialog_RegD)
        self.label_verif2.setEnabled(True)
        self.label_verif2.setGeometry(QtCore.QRect(300, 150, 121, 17))
        self.label_verif2.setStyleSheet("color: #ff0000")
        self.label_verif2.setText("")
        self.label_verif2.setObjectName("label_verif2")
        self.label_verif3 = QtGui.QLabel(Dialog_RegD)
        self.label_verif3.setGeometry(QtCore.QRect(310, 170, 88, 17))
        self.label_verif3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_verif3.setStyleSheet("color: #ff0000")
        self.label_verif3.setText("")
        self.label_verif3.setObjectName("label_verif3")
        self.label_verif = QtGui.QLabel(Dialog_RegD)
        self.label_verif.setEnabled(True)
        self.label_verif.setGeometry(QtCore.QRect(290, 38, 121, 17))
        self.label_verif.setStyleSheet("color: #ff0000")
        self.label_verif.setText("")
        self.label_verif.setObjectName("label_verif")

        self.retranslateUi(Dialog_RegD)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_RegD.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_RegD.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_RegD)
        Dialog_RegD.setTabOrder(self.lineEdit_dni, self.lineEdit_nom)
        Dialog_RegD.setTabOrder(self.lineEdit_nom, self.lineEdit_pass)
        Dialog_RegD.setTabOrder(self.lineEdit_pass, self.lineEdit_pass2)
        Dialog_RegD.setTabOrder(self.lineEdit_pass2, self.buttonBox)

    def retranslateUi(self, Dialog_RegD):
        Dialog_RegD.setWindowTitle(QtGui.QApplication.translate("Dialog_RegD", "Introducir Datos Dietista", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_RegD", "D.N.I. :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_RegD", "Nombre :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_RegD", "Contraseña :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_RegD", "Contraseña :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog_RegD", "Repita", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_RegD = QtGui.QDialog()
    ui = Ui_Dialog_RegD()
    ui.setupUi(Dialog_RegD)
    Dialog_RegD.show()
    sys.exit(app.exec_())

