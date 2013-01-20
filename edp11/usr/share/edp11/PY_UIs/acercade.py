# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/acercade.ui'
#
# Created: Tue Jul 31 13:53:40 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_Acercade(object):
    def setupUi(self, Dialog_Acercade):
        Dialog_Acercade.setObjectName(_fromUtf8("Dialog_Acercade"))
        Dialog_Acercade.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_Acercade.resize(530, 199)
        Dialog_Acercade.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Acercade)
        self.buttonBox.setGeometry(QtCore.QRect(422, 164, 86, 24))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog_Acercade)
        self.label.setGeometry(QtCore.QRect(60, 30, 411, 26))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog_Acercade)
        self.label_2.setGeometry(QtCore.QRect(237, 60, 56, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog_Acercade)
        self.label_3.setGeometry(QtCore.QRect(227, 100, 76, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog_Acercade)
        self.label_4.setGeometry(QtCore.QRect(218, 120, 94, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_Credit = QtGui.QPushButton(Dialog_Acercade)
        self.pushButton_Credit.setGeometry(QtCore.QRect(20, 165, 72, 24))
        self.pushButton_Credit.setObjectName(_fromUtf8("pushButton_Credit"))
        self.pushButton_Licencia = QtGui.QPushButton(Dialog_Acercade)
        self.pushButton_Licencia.setGeometry(QtCore.QRect(100, 165, 70, 24))
        self.pushButton_Licencia.setObjectName(_fromUtf8("pushButton_Licencia"))

        self.retranslateUi(Dialog_Acercade)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_Acercade.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_Acercade.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Acercade)

    def retranslateUi(self, Dialog_Acercade):
        Dialog_Acercade.setWindowTitle(QtGui.QApplication.translate("Dialog_Acercade", "Acerca de Estudio Dietético Programado 2011", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_Acercade", "Estudio Dietético Programado 2011", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_Acercade", "EDP11", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_Acercade", "Versión 0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_Acercade", "Licencia GPL3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Credit.setText(QtGui.QApplication.translate("Dialog_Acercade", "Créditos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Licencia.setText(QtGui.QApplication.translate("Dialog_Acercade", "Licencia", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_Acercade = QtGui.QDialog()
    ui = Ui_Dialog_Acercade()
    ui.setupUi(Dialog_Acercade)
    Dialog_Acercade.show()
    sys.exit(app.exec_())

