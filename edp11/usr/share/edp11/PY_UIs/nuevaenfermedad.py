# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/nuevaenfermedad.ui'
#
# Created: Sat Nov 12 01:03:08 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog_NEnf(object):
    def setupUi(self, Dialog_NEnf):
        Dialog_NEnf.setObjectName("Dialog_NEnf")
        Dialog_NEnf.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_NEnf.resize(408, 320)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_NEnf)
        self.buttonBox.setGeometry(QtCore.QRect(240, 280, 161, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(Dialog_NEnf)
        self.label.setGeometry(QtCore.QRect(20, 40, 67, 17))
        self.label.setObjectName("label")
        self.lineEdit_Nom = QtGui.QLineEdit(Dialog_NEnf)
        self.lineEdit_Nom.setGeometry(QtCore.QRect(100, 35, 288, 27))
        self.lineEdit_Nom.setObjectName("lineEdit_Nom")
        self.treeWidget = QtGui.QTreeWidget(Dialog_NEnf)
        self.treeWidget.setGeometry(QtCore.QRect(100, 70, 288, 171))
        self.treeWidget.setObjectName("treeWidget")
        self.label_2 = QtGui.QLabel(Dialog_NEnf)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 72, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog_NEnf)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 67, 17))
        self.label_3.setObjectName("label_3")
        self.push_Elim = QtGui.QPushButton(Dialog_NEnf)
        self.push_Elim.setGeometry(QtCore.QRect(170, 245, 71, 23))
        self.push_Elim.setObjectName("push_Elim")
        self.push_Anadir = QtGui.QPushButton(Dialog_NEnf)
        self.push_Anadir.setGeometry(QtCore.QRect(100, 245, 61, 23))
        self.push_Anadir.setObjectName("push_Anadir")

        self.retranslateUi(Dialog_NEnf)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_NEnf.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_NEnf.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_NEnf)
        Dialog_NEnf.setTabOrder(self.lineEdit_Nom, self.treeWidget)
        Dialog_NEnf.setTabOrder(self.treeWidget, self.push_Anadir)
        Dialog_NEnf.setTabOrder(self.push_Anadir, self.push_Elim)
        Dialog_NEnf.setTabOrder(self.push_Elim, self.buttonBox)

    def retranslateUi(self, Dialog_NEnf):
        Dialog_NEnf.setWindowTitle(QtGui.QApplication.translate("Dialog_NEnf", "Nueva Enfermedad o Patología", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_NEnf", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog_NEnf", "Ingrediente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_NEnf", "Alimentos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_NEnf", "a evitar:", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Elim.setText(QtGui.QApplication.translate("Dialog_NEnf", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Anadir.setText(QtGui.QApplication.translate("Dialog_NEnf", "Añadir", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_NEnf = QtGui.QDialog()
    ui = Ui_Dialog_NEnf()
    ui.setupUi(Dialog_NEnf)
    Dialog_NEnf.show()
    sys.exit(app.exec_())

