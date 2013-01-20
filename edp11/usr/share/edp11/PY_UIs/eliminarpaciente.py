# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/eliminarpaciente.ui'
#
# Created: Sat Nov 12 01:01:24 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogElimP(object):
    def setupUi(self, DialogElimP):
        DialogElimP.setObjectName("DialogElimP")
        DialogElimP.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogElimP.resize(424, 321)
        DialogElimP.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogElimP)
        self.buttonBox.setGeometry(QtCore.QRect(210, 280, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.treeWidget = QtGui.QTreeWidget(DialogElimP)
        self.treeWidget.setGeometry(QtCore.QRect(20, 20, 381, 231))
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setMidLineWidth(1)
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(209)
        self.treeWidget.header().setMinimumSectionSize(170)

        self.retranslateUi(DialogElimP)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogElimP.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogElimP.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogElimP)

    def retranslateUi(self, DialogElimP):
        DialogElimP.setWindowTitle(QtGui.QApplication.translate("DialogElimP", "Eliminar Paciente", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("DialogElimP", "Paciente", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("DialogElimP", "D.N.I.", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogElimP = QtGui.QDialog()
    ui = Ui_DialogElimP()
    ui.setupUi(DialogElimP)
    DialogElimP.show()
    sys.exit(app.exec_())

