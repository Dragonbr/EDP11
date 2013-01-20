# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/anadirtratapoyo.ui'
#
# Created: Mon Nov 14 03:16:27 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog_Trat(object):
    def setupUi(self, Dialog_Trat):
        Dialog_Trat.setObjectName("Dialog_Trat")
        Dialog_Trat.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_Trat.resize(501, 225)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Trat)
        self.buttonBox.setGeometry(QtCore.QRect(300, 177, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(Dialog_Trat)
        self.label.setGeometry(QtCore.QRect(15, 35, 91, 17))
        self.label.setObjectName("label")
        self.lineEdit_trat = QtGui.QLineEdit(Dialog_Trat)
        self.lineEdit_trat.setGeometry(QtCore.QRect(130, 30, 351, 27))
        self.lineEdit_trat.setObjectName("lineEdit_trat")
        self.label_2 = QtGui.QLabel(Dialog_Trat)
        self.label_2.setGeometry(QtCore.QRect(15, 87, 74, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_pos = QtGui.QLineEdit(Dialog_Trat)
        self.lineEdit_pos.setGeometry(QtCore.QRect(130, 80, 351, 27))
        self.lineEdit_pos.setObjectName("lineEdit_pos")
        self.label_3 = QtGui.QLabel(Dialog_Trat)
        self.label_3.setGeometry(QtCore.QRect(15, 136, 106, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit_obs = QtGui.QLineEdit(Dialog_Trat)
        self.lineEdit_obs.setGeometry(QtCore.QRect(130, 130, 351, 27))
        self.lineEdit_obs.setObjectName("lineEdit_obs")

        self.retranslateUi(Dialog_Trat)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_Trat.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_Trat.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Trat)
        Dialog_Trat.setTabOrder(self.lineEdit_trat, self.lineEdit_pos)
        Dialog_Trat.setTabOrder(self.lineEdit_pos, self.lineEdit_obs)
        Dialog_Trat.setTabOrder(self.lineEdit_obs, self.buttonBox)

    def retranslateUi(self, Dialog_Trat):
        Dialog_Trat.setWindowTitle(QtGui.QApplication.translate("Dialog_Trat", "Añadir Tratamiento de Apoyo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_Trat", "Tratamiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_Trat", "Posología:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_Trat", "Observaciones:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_Trat = QtGui.QDialog()
    ui = Ui_Dialog_Trat()
    ui.setupUi(Dialog_Trat)
    Dialog_Trat.show()
    sys.exit(app.exec_())

