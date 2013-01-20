# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/creditos.ui'
#
# Created: Thu Aug  2 12:26:25 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_Creditos(object):
    def setupUi(self, Dialog_Creditos):
        Dialog_Creditos.setObjectName(_fromUtf8("Dialog_Creditos"))
        Dialog_Creditos.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_Creditos.resize(416, 137)
        Dialog_Creditos.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Creditos)
        self.buttonBox.setGeometry(QtCore.QRect(317, 100, 86, 24))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog_Creditos)
        self.label.setGeometry(QtCore.QRect(60, 20, 44, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog_Creditos)
        self.label_2.setGeometry(QtCore.QRect(125, 20, 201, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog_Creditos)
        self.label_3.setGeometry(QtCore.QRect(44, 60, 62, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog_Creditos)
        self.label_4.setGeometry(QtCore.QRect(125, 60, 231, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog_Creditos)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_Creditos.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_Creditos.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Creditos)

    def retranslateUi(self, Dialog_Creditos):
        Dialog_Creditos.setWindowTitle(QtGui.QApplication.translate("Dialog_Creditos", "Créditos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_Creditos", "Autor: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_Creditos", "Manuel González Pérez", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_Creditos", "Soporte:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_Creditos", "gonzalezperezmanuel@gmail.com", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_Creditos = QtGui.QDialog()
    ui = Ui_Dialog_Creditos()
    ui.setupUi(Dialog_Creditos)
    Dialog_Creditos.show()
    sys.exit(app.exec_())

