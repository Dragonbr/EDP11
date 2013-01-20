# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/perfildietista_pass.ui'
#
# Created: Sat Nov 12 01:04:26 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog_PD_Pass(object):
    def setupUi(self, Dialog_PD_Pass):
        Dialog_PD_Pass.setObjectName("Dialog_PD_Pass")
        Dialog_PD_Pass.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_PD_Pass.resize(316, 177)
        Dialog_PD_Pass.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_PD_Pass)
        self.buttonBox.setGeometry(QtCore.QRect(130, 130, 175, 30))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(Dialog_PD_Pass)
        self.label.setGeometry(QtCore.QRect(20, 45, 101, 17))
        self.label.setObjectName("label")
        self.lineEdit_PD = QtGui.QLineEdit(Dialog_PD_Pass)
        self.lineEdit_PD.setEnabled(True)
        self.lineEdit_PD.setGeometry(QtCore.QRect(130, 40, 161, 27))
        self.lineEdit_PD.setReadOnly(True)
        self.lineEdit_PD.setObjectName("lineEdit_PD")
        self.lineEdit_Pass = QtGui.QLineEdit(Dialog_PD_Pass)
        self.lineEdit_Pass.setGeometry(QtCore.QRect(130, 85, 161, 27))
        self.lineEdit_Pass.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_Pass.setObjectName("lineEdit_Pass")
        self.label_2 = QtGui.QLabel(Dialog_PD_Pass)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 82, 17))
        self.label_2.setObjectName("label_2")
        self.label_error = QtGui.QLabel(Dialog_PD_Pass)
        self.label_error.setGeometry(QtCore.QRect(20, 10, 199, 17))
        self.label_error.setStyleSheet("color: #ff0000")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")

        self.retranslateUi(Dialog_PD_Pass)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_PD_Pass.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_PD_Pass.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_PD_Pass)
        Dialog_PD_Pass.setTabOrder(self.lineEdit_PD, self.lineEdit_Pass)
        Dialog_PD_Pass.setTabOrder(self.lineEdit_Pass, self.buttonBox)

    def retranslateUi(self, Dialog_PD_Pass):
        Dialog_PD_Pass.setWindowTitle(QtGui.QApplication.translate("Dialog_PD_Pass", "Introduzca Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_PD_Pass", "Perfil Dietista:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_PD_Pass", "Contraseña:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_PD_Pass = QtGui.QDialog()
    ui = Ui_Dialog_PD_Pass()
    ui.setupUi(Dialog_PD_Pass)
    Dialog_PD_Pass.show()
    sys.exit(app.exec_())

