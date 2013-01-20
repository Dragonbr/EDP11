# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../../../UIs/nuevopaciente1.ui'
#
# Created: Tue Oct 30 10:14:37 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogNuevoP1(object):
    def setupUi(self, DialogNuevoP1):
        DialogNuevoP1.setObjectName(_fromUtf8("DialogNuevoP1"))
        DialogNuevoP1.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogNuevoP1.resize(640, 401)
        DialogNuevoP1.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogNuevoP1)
        self.buttonBox.setGeometry(QtCore.QRect(10, 350, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_sexo = QtGui.QLabel(DialogNuevoP1)
        self.label_sexo.setGeometry(QtCore.QRect(30, 60, 41, 17))
        self.label_sexo.setObjectName(_fromUtf8("label_sexo"))
        self.combo_FM = QtGui.QComboBox(DialogNuevoP1)
        self.combo_FM.setEnabled(True)
        self.combo_FM.setGeometry(QtCore.QRect(150, 60, 51, 21))
        self.combo_FM.setEditable(False)
        self.combo_FM.setObjectName(_fromUtf8("combo_FM"))
        self.combo_FM.addItem(_fromUtf8(""))
        self.combo_FM.addItem(_fromUtf8(""))
        self.label_nom = QtGui.QLabel(DialogNuevoP1)
        self.label_nom.setGeometry(QtCore.QRect(30, 108, 62, 17))
        self.label_nom.setObjectName(_fromUtf8("label_nom"))
        self.label_prof = QtGui.QLabel(DialogNuevoP1)
        self.label_prof.setGeometry(QtCore.QRect(30, 235, 71, 17))
        self.label_prof.setObjectName(_fromUtf8("label_prof"))
        self.label_FNac = QtGui.QLabel(DialogNuevoP1)
        self.label_FNac.setGeometry(QtCore.QRect(30, 150, 118, 16))
        self.label_FNac.setObjectName(_fromUtf8("label_FNac"))
        self.label_dni = QtGui.QLabel(DialogNuevoP1)
        self.label_dni.setGeometry(QtCore.QRect(30, 190, 47, 17))
        self.label_dni.setObjectName(_fromUtf8("label_dni"))
        self.date_FNac = QtGui.QDateEdit(DialogNuevoP1)
        self.date_FNac.setGeometry(QtCore.QRect(150, 145, 115, 27))
        self.date_FNac.setDate(QtCore.QDate(1950, 10, 1))
        self.date_FNac.setCalendarPopup(True)
        self.date_FNac.setObjectName(_fromUtf8("date_FNac"))
        self.lineEdit_Prof = QtGui.QLineEdit(DialogNuevoP1)
        self.lineEdit_Prof.setGeometry(QtCore.QRect(150, 230, 380, 27))
        self.lineEdit_Prof.setObjectName(_fromUtf8("lineEdit_Prof"))
        self.label_tlf = QtGui.QLabel(DialogNuevoP1)
        self.label_tlf.setGeometry(QtCore.QRect(320, 190, 71, 17))
        self.label_tlf.setObjectName(_fromUtf8("label_tlf"))
        self.lineEdit_Apell = QtGui.QLineEdit(DialogNuevoP1)
        self.lineEdit_Apell.setGeometry(QtCore.QRect(400, 104, 211, 27))
        self.lineEdit_Apell.setObjectName(_fromUtf8("lineEdit_Apell"))
        self.lineEdit_Tlf = QtGui.QLineEdit(DialogNuevoP1)
        self.lineEdit_Tlf.setGeometry(QtCore.QRect(400, 185, 113, 27))
        self.lineEdit_Tlf.setObjectName(_fromUtf8("lineEdit_Tlf"))
        self.lineEdit_Dir = QtGui.QLineEdit(DialogNuevoP1)
        self.lineEdit_Dir.setGeometry(QtCore.QRect(150, 275, 380, 27))
        self.lineEdit_Dir.setObjectName(_fromUtf8("lineEdit_Dir"))
        self.label_apell = QtGui.QLabel(DialogNuevoP1)
        self.label_apell.setGeometry(QtCore.QRect(320, 108, 71, 17))
        self.label_apell.setObjectName(_fromUtf8("label_apell"))
        self.lineEdit_Dni = QtGui.QLineEdit(DialogNuevoP1)
        self.lineEdit_Dni.setGeometry(QtCore.QRect(150, 185, 101, 27))
        self.lineEdit_Dni.setObjectName(_fromUtf8("lineEdit_Dni"))
        self.lineEdit_Nom = QtGui.QLineEdit(DialogNuevoP1)
        self.lineEdit_Nom.setGeometry(QtCore.QRect(150, 104, 136, 27))
        self.lineEdit_Nom.setObjectName(_fromUtf8("lineEdit_Nom"))
        self.label_edad = QtGui.QLabel(DialogNuevoP1)
        self.label_edad.setGeometry(QtCore.QRect(320, 150, 41, 17))
        self.label_edad.setObjectName(_fromUtf8("label_edad"))
        self.lineEdit_Edad = QtGui.QLineEdit(DialogNuevoP1)
        self.lineEdit_Edad.setEnabled(True)
        self.lineEdit_Edad.setGeometry(QtCore.QRect(400, 145, 34, 27))
        self.lineEdit_Edad.setReadOnly(True)
        self.lineEdit_Edad.setObjectName(_fromUtf8("lineEdit_Edad"))
        self.label_dir = QtGui.QLabel(DialogNuevoP1)
        self.label_dir.setGeometry(QtCore.QRect(30, 280, 71, 17))
        self.label_dir.setObjectName(_fromUtf8("label_dir"))
        self.label = QtGui.QLabel(DialogNuevoP1)
        self.label.setGeometry(QtCore.QRect(150, 320, 251, 17))
        self.label.setStyleSheet(_fromUtf8("color: #ff0000"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(DialogNuevoP1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogNuevoP1.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogNuevoP1.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNuevoP1)
        DialogNuevoP1.setTabOrder(self.combo_FM, self.lineEdit_Nom)
        DialogNuevoP1.setTabOrder(self.lineEdit_Nom, self.lineEdit_Apell)
        DialogNuevoP1.setTabOrder(self.lineEdit_Apell, self.date_FNac)
        DialogNuevoP1.setTabOrder(self.date_FNac, self.lineEdit_Edad)
        DialogNuevoP1.setTabOrder(self.lineEdit_Edad, self.lineEdit_Dni)
        DialogNuevoP1.setTabOrder(self.lineEdit_Dni, self.lineEdit_Tlf)
        DialogNuevoP1.setTabOrder(self.lineEdit_Tlf, self.lineEdit_Prof)
        DialogNuevoP1.setTabOrder(self.lineEdit_Prof, self.lineEdit_Dir)
        DialogNuevoP1.setTabOrder(self.lineEdit_Dir, self.buttonBox)

    def retranslateUi(self, DialogNuevoP1):
        DialogNuevoP1.setWindowTitle(QtGui.QApplication.translate("DialogNuevoP1", "Nuevo Paciente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sexo.setText(QtGui.QApplication.translate("DialogNuevoP1", "Sexo :", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_FM.setItemText(0, QtGui.QApplication.translate("DialogNuevoP1", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_FM.setItemText(1, QtGui.QApplication.translate("DialogNuevoP1", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.label_nom.setText(QtGui.QApplication.translate("DialogNuevoP1", "Nombre :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_prof.setText(QtGui.QApplication.translate("DialogNuevoP1", "Profesión :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_FNac.setText(QtGui.QApplication.translate("DialogNuevoP1", "Fch. Nacimiento :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_dni.setText(QtGui.QApplication.translate("DialogNuevoP1", "D.N.I. :", None, QtGui.QApplication.UnicodeUTF8))
        self.date_FNac.setDisplayFormat(QtGui.QApplication.translate("DialogNuevoP1", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tlf.setText(QtGui.QApplication.translate("DialogNuevoP1", "Teléfono :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_apell.setText(QtGui.QApplication.translate("DialogNuevoP1", "Apellidos :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_edad.setText(QtGui.QApplication.translate("DialogNuevoP1", "Edad :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_dir.setText(QtGui.QApplication.translate("DialogNuevoP1", "Dirección:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogNuevoP1 = QtGui.QDialog()
    ui = Ui_DialogNuevoP1()
    ui.setupUi(DialogNuevoP1)
    DialogNuevoP1.show()
    sys.exit(app.exec_())

