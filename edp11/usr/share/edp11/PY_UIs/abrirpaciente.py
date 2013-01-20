# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/abrirpaciente.ui'
#
# Created: Sat Nov 12 00:59:14 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogAbrirP(object):
    def setupUi(self, DialogAbrirP):
        DialogAbrirP.setObjectName("DialogAbrirP")
        DialogAbrirP.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogAbrirP.resize(424, 321)
        DialogAbrirP.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogAbrirP)
        self.buttonBox.setGeometry(QtCore.QRect(210, 280, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.treeWidget = QtGui.QTreeWidget(DialogAbrirP)
        self.treeWidget.setGeometry(QtCore.QRect(20, 20, 381, 231))
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setMidLineWidth(1)
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(209)
        self.treeWidget.header().setMinimumSectionSize(170)

        self.retranslateUi(DialogAbrirP)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogAbrirP.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogAbrirP.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAbrirP)
        DialogAbrirP.setTabOrder(self.treeWidget, self.buttonBox)

    def retranslateUi(self, DialogAbrirP):
        DialogAbrirP.setWindowTitle(QtGui.QApplication.translate("DialogAbrirP", "Abrir Paciente", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("DialogAbrirP", "Paciente", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("DialogAbrirP", "D.N.I.", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAbrirP = QtGui.QDialog()
    ui = Ui_DialogAbrirP()
    ui.setupUi(DialogAbrirP)
    DialogAbrirP.show()
    sys.exit(app.exec_())

