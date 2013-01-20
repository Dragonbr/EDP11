# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../../../UIs/nuevareceta.ui'
#
# Created: Mon Oct 29 10:15:51 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogNRec(object):
    def setupUi(self, DialogNRec):
        DialogNRec.setObjectName(_fromUtf8("DialogNRec"))
        DialogNRec.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogNRec.resize(708, 572)
        DialogNRec.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogNRec)
        self.buttonBox.setGeometry(QtCore.QRect(510, 520, 171, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(DialogNRec)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 531, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(DialogNRec)
        self.label.setGeometry(QtCore.QRect(50, 45, 48, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DialogNRec)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 62, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(DialogNRec)
        self.doubleSpinBox.setGeometry(QtCore.QRect(150, 95, 80, 27))
        self.doubleSpinBox.setReadOnly(True)
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.treeWidget = QtGui.QTreeWidget(DialogNRec)
        self.treeWidget.setGeometry(QtCore.QRect(150, 150, 531, 120))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setDefaultSectionSize(175)
        self.treeWidget.header().setMinimumSectionSize(175)
        self.label_3 = QtGui.QLabel(DialogNRec)
        self.label_3.setGeometry(QtCore.QRect(50, 155, 92, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(DialogNRec)
        self.label_4.setGeometry(QtCore.QRect(50, 345, 88, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEdit = QtGui.QTextEdit(DialogNRec)
        self.textEdit.setGeometry(QtCore.QRect(150, 340, 531, 171))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.push_Anadir = QtGui.QPushButton(DialogNRec)
        self.push_Anadir.setGeometry(QtCore.QRect(327, 280, 71, 22))
        self.push_Anadir.setObjectName(_fromUtf8("push_Anadir"))
        self.push_Eliminar = QtGui.QPushButton(DialogNRec)
        self.push_Eliminar.setGeometry(QtCore.QRect(410, 280, 71, 22))
        self.push_Eliminar.setObjectName(_fromUtf8("push_Eliminar"))
        self.label_5 = QtGui.QLabel(DialogNRec)
        self.label_5.setGeometry(QtCore.QRect(330, 100, 71, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBox = QtGui.QComboBox(DialogNRec)
        self.comboBox.setGeometry(QtCore.QRect(420, 95, 131, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_6 = QtGui.QLabel(DialogNRec)
        self.label_6.setGeometry(QtCore.QRect(150, 20, 131, 17))
        self.label_6.setStyleSheet(_fromUtf8("color: #ff0000"))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(DialogNRec)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogNRec.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogNRec.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNRec)
        DialogNRec.setTabOrder(self.lineEdit, self.doubleSpinBox)
        DialogNRec.setTabOrder(self.doubleSpinBox, self.treeWidget)
        DialogNRec.setTabOrder(self.treeWidget, self.push_Anadir)
        DialogNRec.setTabOrder(self.push_Anadir, self.push_Eliminar)
        DialogNRec.setTabOrder(self.push_Eliminar, self.textEdit)
        DialogNRec.setTabOrder(self.textEdit, self.comboBox)
        DialogNRec.setTabOrder(self.comboBox, self.buttonBox)

    def retranslateUi(self, DialogNRec):
        DialogNRec.setWindowTitle(QtGui.QApplication.translate("DialogNRec", "Nueva Receta", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogNRec", "Título:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogNRec", "Calorías:", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("DialogNRec", "Ingrediente", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("DialogNRec", "Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("DialogNRec", "Calorías", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogNRec", "Ingredientes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogNRec", "Preparación:", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Anadir.setText(QtGui.QApplication.translate("DialogNRec", "Añadir", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Eliminar.setText(QtGui.QApplication.translate("DialogNRec", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogNRec", "Categoría:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("DialogNRec", "Desayuno", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("DialogNRec", "Media Mañana", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("DialogNRec", "Almuerzo", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("DialogNRec", "Merienda", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("DialogNRec", "Cena", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("DialogNRec", "Tentempié", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogNRec = QtGui.QDialog()
    ui = Ui_DialogNRec()
    ui.setupUi(DialogNRec)
    DialogNRec.show()
    sys.exit(app.exec_())

