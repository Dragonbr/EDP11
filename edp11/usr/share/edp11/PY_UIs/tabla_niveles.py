# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/tabla_niveles.ui'
#
# Created: Thu Jun 28 20:20:40 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogNivel(object):
    def setupUi(self, DialogNivel):
        DialogNivel.setObjectName("DialogNivel")
        DialogNivel.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogNivel.resize(408, 215)
        DialogNivel.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton = QtGui.QPushButton(DialogNivel)
        self.pushButton.setGeometry(QtCore.QRect(307, 180, 81, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtGui.QLabel(DialogNivel)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 17))
        self.label.setStyleSheet("color: #07fa0a")
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(DialogNivel)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 331, 17))
        self.label_2.setStyleSheet("color: #eff01b")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(DialogNivel)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 361, 17))
        self.label_3.setStyleSheet("color: #ee9711")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(DialogNivel)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 341, 17))
        self.label_4.setStyleSheet("color: #ff0000")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(DialogNivel)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 294, 17))
        self.label_5.setStyleSheet("color: #aa0821")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(DialogNivel)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), DialogNivel.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogNivel)

    def retranslateUi(self, DialogNivel):
        DialogNivel.setWindowTitle(QtGui.QApplication.translate("DialogNivel", "Tabla de niveles según I.M.C.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("DialogNivel", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogNivel", "Peso Normal:  I.M.C.  <  25", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogNivel", "Grado I (Sobrepeso leve):     25  <=   I.M.C.  <  27,99", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogNivel", "Grado II (Sobrepeso moderado):  28  <=  I.M.C. <  31,99", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogNivel", "Grado III (Sobrepeso grave):   32  <=   I.M.C.  <  41,99", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogNivel", "Grado IV (Obesidad mórbida):  I.M.C.  >=  42", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogNivel = QtGui.QDialog()
    ui = Ui_DialogNivel()
    ui.setupUi(DialogNivel)
    DialogNivel.show()
    sys.exit(app.exec_())

