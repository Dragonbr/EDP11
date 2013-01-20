# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/nuevoingrediente.ui'
#
# Created: Sat Nov 12 01:03:37 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog_Ingr(object):
    def setupUi(self, Dialog_Ingr):
        Dialog_Ingr.setObjectName("Dialog_Ingr")
        Dialog_Ingr.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_Ingr.resize(407, 269)
        Dialog_Ingr.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Ingr)
        self.buttonBox.setGeometry(QtCore.QRect(10, 220, 391, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(Dialog_Ingr)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 17))
        self.label.setObjectName("label")
        self.lineEdit_nom = QtGui.QLineEdit(Dialog_Ingr)
        self.lineEdit_nom.setGeometry(QtCore.QRect(110, 25, 281, 27))
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.label_2 = QtGui.QLabel(Dialog_Ingr)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 61, 17))
        self.label_2.setObjectName("label_2")
        self.combo_udgr = QtGui.QComboBox(Dialog_Ingr)
        self.combo_udgr.setGeometry(QtCore.QRect(174, 75, 51, 27))
        self.combo_udgr.setObjectName("combo_udgr")
        self.combo_udgr.addItem("")
        self.combo_udgr.addItem("")
        self.combo_udgr.addItem("")
        self.label_3 = QtGui.QLabel(Dialog_Ingr)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 41, 17))
        self.label_3.setObjectName("label_3")
        self.combo_tipo = QtGui.QComboBox(Dialog_Ingr)
        self.combo_tipo.setGeometry(QtCore.QRect(110, 125, 151, 27))
        self.combo_tipo.setObjectName("combo_tipo")
        self.combo_tipo.addItem("")
        self.combo_tipo.addItem("")
        self.combo_tipo.addItem("")
        self.combo_tipo.addItem("")
        self.combo_tipo.addItem("")
        self.label_4 = QtGui.QLabel(Dialog_Ingr)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 36, 17))
        self.label_4.setObjectName("label_4")
        self.double_cal = QtGui.QDoubleSpinBox(Dialog_Ingr)
        self.double_cal.setGeometry(QtCore.QRect(110, 175, 75, 27))
        self.double_cal.setMaximum(999.99)
        self.double_cal.setSingleStep(0.01)
        self.double_cal.setProperty("value", 0.0)
        self.double_cal.setObjectName("double_cal")
        self.lineEdit_udgr = QtGui.QLineEdit(Dialog_Ingr)
        self.lineEdit_udgr.setGeometry(QtCore.QRect(110, 75, 41, 27))
        self.lineEdit_udgr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_udgr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_udgr.setReadOnly(True)
        self.lineEdit_udgr.setObjectName("lineEdit_udgr")

        self.retranslateUi(Dialog_Ingr)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_Ingr.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_Ingr.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Ingr)
        Dialog_Ingr.setTabOrder(self.lineEdit_nom, self.lineEdit_udgr)
        Dialog_Ingr.setTabOrder(self.lineEdit_udgr, self.combo_udgr)
        Dialog_Ingr.setTabOrder(self.combo_udgr, self.combo_tipo)
        Dialog_Ingr.setTabOrder(self.combo_tipo, self.double_cal)
        Dialog_Ingr.setTabOrder(self.double_cal, self.buttonBox)

    def retranslateUi(self, Dialog_Ingr):
        Dialog_Ingr.setWindowTitle(QtGui.QApplication.translate("Dialog_Ingr", "Nuevo Ingrediente", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_Ingr", "Ingrediente:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_Ingr", "Medida:", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_udgr.setItemText(0, QtGui.QApplication.translate("Dialog_Ingr", "ud.", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_udgr.setItemText(1, QtGui.QApplication.translate("Dialog_Ingr", "g.", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_udgr.setItemText(2, QtGui.QApplication.translate("Dialog_Ingr", "ml.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_Ingr", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_tipo.setItemText(0, QtGui.QApplication.translate("Dialog_Ingr", "Grasas y Aceites", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_tipo.setItemText(1, QtGui.QApplication.translate("Dialog_Ingr", "Farináceos", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_tipo.setItemText(2, QtGui.QApplication.translate("Dialog_Ingr", "Proteínicos", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_tipo.setItemText(3, QtGui.QApplication.translate("Dialog_Ingr", "Lácteos", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_tipo.setItemText(4, QtGui.QApplication.translate("Dialog_Ingr", "Frutas y Verduras", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_Ingr", "Cal. :", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_udgr.setText(QtGui.QApplication.translate("Dialog_Ingr", "1", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_Ingr = QtGui.QDialog()
    ui = Ui_Dialog_Ingr()
    ui.setupUi(Dialog_Ingr)
    Dialog_Ingr.show()
    sys.exit(app.exec_())

