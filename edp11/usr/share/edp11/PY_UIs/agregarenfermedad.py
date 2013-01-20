# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/agregarenfermedad.ui'
#
# Created: Sat Nov 12 01:00:05 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog_Enf(object):
    def setupUi(self, Dialog_Enf):
        Dialog_Enf.setObjectName("Dialog_Enf")
        Dialog_Enf.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_Enf.resize(380, 353)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Enf)
        self.buttonBox.setGeometry(QtCore.QRect(190, 312, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.treeWidget = QtGui.QTreeWidget(Dialog_Enf)
        self.treeWidget.setGeometry(QtCore.QRect(20, 35, 341, 241))
        self.treeWidget.setObjectName("treeWidget")
        self.push_Nuevo = QtGui.QPushButton(Dialog_Enf)
        self.push_Nuevo.setGeometry(QtCore.QRect(20, 278, 61, 23))
        self.push_Nuevo.setObjectName("push_Nuevo")
        self.push_Elim = QtGui.QPushButton(Dialog_Enf)
        self.push_Elim.setGeometry(QtCore.QRect(90, 278, 71, 23))
        self.push_Elim.setObjectName("push_Elim")
        self.label = QtGui.QLabel(Dialog_Enf)
        self.label.setGeometry(QtCore.QRect(20, 15, 171, 17))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_Enf)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_Enf.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_Enf.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Enf)

    def retranslateUi(self, Dialog_Enf):
        Dialog_Enf.setWindowTitle(QtGui.QApplication.translate("Dialog_Enf", "Enfermedades y Patologías", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog_Enf", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Nuevo.setText(QtGui.QApplication.translate("Dialog_Enf", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Elim.setText(QtGui.QApplication.translate("Dialog_Enf", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_Enf", "Enfermedad o Patología:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_Enf = QtGui.QDialog()
    ui = Ui_Dialog_Enf()
    ui.setupUi(Dialog_Enf)
    Dialog_Enf.show()
    sys.exit(app.exec_())

