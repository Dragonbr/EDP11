# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/seleccionarreceta.ui'
#
# Created: Sat Nov 12 01:05:24 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogSelRec(object):
    def setupUi(self, DialogSelRec):
        DialogSelRec.setObjectName("DialogSelRec")
        DialogSelRec.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogSelRec.resize(424, 321)
        DialogSelRec.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogSelRec)
        self.buttonBox.setGeometry(QtCore.QRect(210, 280, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.treeWidget = QtGui.QTreeWidget(DialogSelRec)
        self.treeWidget.setGeometry(QtCore.QRect(20, 20, 381, 231))
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setDefaultSectionSize(189)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(300)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.treeWidget.header().setStretchLastSection(False)

        self.retranslateUi(DialogSelRec)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogSelRec.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogSelRec.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogSelRec)
        DialogSelRec.setTabOrder(self.treeWidget, self.buttonBox)

    def retranslateUi(self, DialogSelRec):
        DialogSelRec.setWindowTitle(QtGui.QApplication.translate("DialogSelRec", "Seleccionar Receta a Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("DialogSelRec", "Receta", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("DialogSelRec", "Calorías", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogSelRec = QtGui.QDialog()
    ui = Ui_DialogSelRec()
    ui.setupUi(DialogSelRec)
    DialogSelRec.show()
    sys.exit(app.exec_())

