# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/nuevopaciente2.ui'
#
# Created: Sat Nov 12 01:04:13 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogNuevoP2(object):
    def setupUi(self, DialogNuevoP2):
        DialogNuevoP2.setObjectName("DialogNuevoP2")
        DialogNuevoP2.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogNuevoP2.resize(640, 402)
        DialogNuevoP2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogNuevoP2)
        self.buttonBox.setGeometry(QtCore.QRect(10, 352, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_cint_cm = QtGui.QLabel(DialogNuevoP2)
        self.label_cint_cm.setGeometry(QtCore.QRect(530, 105, 22, 17))
        self.label_cint_cm.setObjectName("label_cint_cm")
        self.label_cint = QtGui.QLabel(DialogNuevoP2)
        self.label_cint.setGeometry(QtCore.QRect(329, 105, 54, 17))
        self.label_cint.setObjectName("label_cint")
        self.doubleSpin_Cad = QtGui.QDoubleSpinBox(DialogNuevoP2)
        self.doubleSpin_Cad.setGeometry(QtCore.QRect(119, 140, 71, 27))
        self.doubleSpin_Cad.setMaximum(999.99)
        self.doubleSpin_Cad.setSingleStep(0.01)
        self.doubleSpin_Cad.setObjectName("doubleSpin_Cad")
        self.label_cader = QtGui.QLabel(DialogNuevoP2)
        self.label_cader.setGeometry(QtCore.QRect(60, 146, 53, 17))
        self.label_cader.setObjectName("label_cader")
        self.label_pob_kg = QtGui.QLabel(DialogNuevoP2)
        self.label_pob_kg.setGeometry(QtCore.QRect(530, 65, 21, 17))
        self.label_pob_kg.setObjectName("label_pob_kg")
        self.doubleSpin_Cint = QtGui.QDoubleSpinBox(DialogNuevoP2)
        self.doubleSpin_Cint.setGeometry(QtCore.QRect(445, 100, 71, 27))
        self.doubleSpin_Cint.setMaximum(999.99)
        self.doubleSpin_Cint.setSingleStep(0.01)
        self.doubleSpin_Cint.setObjectName("doubleSpin_Cint")
        self.label_complex = QtGui.QLabel(DialogNuevoP2)
        self.label_complex.setGeometry(QtCore.QRect(60, 200, 91, 17))
        self.label_complex.setObjectName("label_complex")
        self.label_peso = QtGui.QLabel(DialogNuevoP2)
        self.label_peso.setGeometry(QtCore.QRect(60, 65, 40, 17))
        self.label_peso.setObjectName("label_peso")
        self.doubleSpin_Peso = QtGui.QDoubleSpinBox(DialogNuevoP2)
        self.doubleSpin_Peso.setGeometry(QtCore.QRect(119, 60, 71, 27))
        self.doubleSpin_Peso.setMaximum(999.99)
        self.doubleSpin_Peso.setSingleStep(0.01)
        self.doubleSpin_Peso.setObjectName("doubleSpin_Peso")
        self.label_tr_cm = QtGui.QLabel(DialogNuevoP2)
        self.label_tr_cm.setGeometry(QtCore.QRect(530, 146, 23, 17))
        self.label_tr_cm.setObjectName("label_tr_cm")
        self.combo_Activ = QtGui.QComboBox(DialogNuevoP2)
        self.combo_Activ.setGeometry(QtCore.QRect(445, 195, 101, 27))
        self.combo_Activ.setObjectName("combo_Activ")
        self.combo_Activ.addItem("")
        self.combo_Activ.addItem("")
        self.combo_Activ.addItem("")
        self.doubleSpin_Tricip = QtGui.QDoubleSpinBox(DialogNuevoP2)
        self.doubleSpin_Tricip.setGeometry(QtCore.QRect(445, 140, 71, 27))
        self.doubleSpin_Tricip.setMaximum(999.99)
        self.doubleSpin_Tricip.setSingleStep(0.01)
        self.doubleSpin_Tricip.setObjectName("doubleSpin_Tricip")
        self.doubleSpin_Alt = QtGui.QDoubleSpinBox(DialogNuevoP2)
        self.doubleSpin_Alt.setGeometry(QtCore.QRect(119, 100, 71, 27))
        self.doubleSpin_Alt.setMaximum(999.99)
        self.doubleSpin_Alt.setSingleStep(0.01)
        self.doubleSpin_Alt.setObjectName("doubleSpin_Alt")
        self.doubleSpin_POb = QtGui.QDoubleSpinBox(DialogNuevoP2)
        self.doubleSpin_POb.setGeometry(QtCore.QRect(445, 60, 71, 27))
        self.doubleSpin_POb.setMaximum(999.99)
        self.doubleSpin_POb.setSingleStep(0.01)
        self.doubleSpin_POb.setObjectName("doubleSpin_POb")
        self.label_altura = QtGui.QLabel(DialogNuevoP2)
        self.label_altura.setGeometry(QtCore.QRect(60, 105, 47, 17))
        self.label_altura.setObjectName("label_altura")
        self.label_pob = QtGui.QLabel(DialogNuevoP2)
        self.label_pob.setGeometry(QtCore.QRect(329, 65, 62, 17))
        self.label_pob.setObjectName("label_pob")
        self.label_peso_kg = QtGui.QLabel(DialogNuevoP2)
        self.label_peso_kg.setGeometry(QtCore.QRect(210, 65, 21, 17))
        self.label_peso_kg.setObjectName("label_peso_kg")
        self.label_tricip = QtGui.QLabel(DialogNuevoP2)
        self.label_tricip.setGeometry(QtCore.QRect(329, 146, 105, 17))
        self.label_tricip.setObjectName("label_tricip")
        self.label_alt_cm = QtGui.QLabel(DialogNuevoP2)
        self.label_alt_cm.setGeometry(QtCore.QRect(210, 105, 22, 17))
        self.label_alt_cm.setObjectName("label_alt_cm")
        self.label_cad_cm = QtGui.QLabel(DialogNuevoP2)
        self.label_cad_cm.setGeometry(QtCore.QRect(210, 146, 22, 17))
        self.label_cad_cm.setObjectName("label_cad_cm")
        self.combo_Complex = QtGui.QComboBox(DialogNuevoP2)
        self.combo_Complex.setGeometry(QtCore.QRect(165, 195, 89, 27))
        self.combo_Complex.setObjectName("combo_Complex")
        self.combo_Complex.addItem("")
        self.combo_Complex.addItem("")
        self.combo_Complex.addItem("")
        self.label_activ = QtGui.QLabel(DialogNuevoP2)
        self.label_activ.setGeometry(QtCore.QRect(330, 200, 69, 17))
        self.label_activ.setObjectName("label_activ")
        self.pushButton_Record = QtGui.QPushButton(DialogNuevoP2)
        self.pushButton_Record.setGeometry(QtCore.QRect(230, 280, 131, 27))
        self.pushButton_Record.setObjectName("pushButton_Record")
        self.pushButton_DiDiet = QtGui.QPushButton(DialogNuevoP2)
        self.pushButton_DiDiet.setGeometry(QtCore.QRect(50, 280, 114, 27))
        self.pushButton_DiDiet.setObjectName("pushButton_DiDiet")
        self.pushButton_Cuest = QtGui.QPushButton(DialogNuevoP2)
        self.pushButton_Cuest.setGeometry(QtCore.QRect(410, 280, 191, 27))
        self.pushButton_Cuest.setObjectName("pushButton_Cuest")

        self.retranslateUi(DialogNuevoP2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogNuevoP2.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogNuevoP2.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNuevoP2)
        DialogNuevoP2.setTabOrder(self.doubleSpin_Peso, self.doubleSpin_POb)
        DialogNuevoP2.setTabOrder(self.doubleSpin_POb, self.doubleSpin_Alt)
        DialogNuevoP2.setTabOrder(self.doubleSpin_Alt, self.doubleSpin_Cint)
        DialogNuevoP2.setTabOrder(self.doubleSpin_Cint, self.doubleSpin_Cad)
        DialogNuevoP2.setTabOrder(self.doubleSpin_Cad, self.doubleSpin_Tricip)
        DialogNuevoP2.setTabOrder(self.doubleSpin_Tricip, self.combo_Complex)
        DialogNuevoP2.setTabOrder(self.combo_Complex, self.combo_Activ)
        DialogNuevoP2.setTabOrder(self.combo_Activ, self.pushButton_DiDiet)
        DialogNuevoP2.setTabOrder(self.pushButton_DiDiet, self.pushButton_Record)
        DialogNuevoP2.setTabOrder(self.pushButton_Record, self.pushButton_Cuest)
        DialogNuevoP2.setTabOrder(self.pushButton_Cuest, self.buttonBox)

    def retranslateUi(self, DialogNuevoP2):
        DialogNuevoP2.setWindowTitle(QtGui.QApplication.translate("DialogNuevoP2", "Nuevo Paciente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cint_cm.setText(QtGui.QApplication.translate("DialogNuevoP2", "cm.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cint.setText(QtGui.QApplication.translate("DialogNuevoP2", "Cintura:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cader.setText(QtGui.QApplication.translate("DialogNuevoP2", "Cadera:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pob_kg.setText(QtGui.QApplication.translate("DialogNuevoP2", "Kg.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_complex.setText(QtGui.QApplication.translate("DialogNuevoP2", "Complexión:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_peso.setText(QtGui.QApplication.translate("DialogNuevoP2", "Peso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tr_cm.setText(QtGui.QApplication.translate("DialogNuevoP2", "cm.", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_Activ.setItemText(0, QtGui.QApplication.translate("DialogNuevoP2", "Ligera", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_Activ.setItemText(1, QtGui.QApplication.translate("DialogNuevoP2", "Moderada", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_Activ.setItemText(2, QtGui.QApplication.translate("DialogNuevoP2", "Intensa", None, QtGui.QApplication.UnicodeUTF8))
        self.label_altura.setText(QtGui.QApplication.translate("DialogNuevoP2", "Altura:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pob.setText(QtGui.QApplication.translate("DialogNuevoP2", "Objetivo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_peso_kg.setText(QtGui.QApplication.translate("DialogNuevoP2", "Kg.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tricip.setText(QtGui.QApplication.translate("DialogNuevoP2", "Pliegue Tricipal:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_alt_cm.setText(QtGui.QApplication.translate("DialogNuevoP2", "cm.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cad_cm.setText(QtGui.QApplication.translate("DialogNuevoP2", "cm.", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_Complex.setItemText(0, QtGui.QApplication.translate("DialogNuevoP2", "Delgada", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_Complex.setItemText(1, QtGui.QApplication.translate("DialogNuevoP2", "Media", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_Complex.setItemText(2, QtGui.QApplication.translate("DialogNuevoP2", "Ancha", None, QtGui.QApplication.UnicodeUTF8))
        self.label_activ.setText(QtGui.QApplication.translate("DialogNuevoP2", "Actividad:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Record.setText(QtGui.QApplication.translate("DialogNuevoP2", "Recordatorio 24 h.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_DiDiet.setText(QtGui.QApplication.translate("DialogNuevoP2", "Diario Dietético", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cuest.setText(QtGui.QApplication.translate("DialogNuevoP2", "Cuestionario de Frecuencia", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogNuevoP2 = QtGui.QDialog()
    ui = Ui_DialogNuevoP2()
    ui.setupUi(DialogNuevoP2)
    DialogNuevoP2.show()
    sys.exit(app.exec_())

