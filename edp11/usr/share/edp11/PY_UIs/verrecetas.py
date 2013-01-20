# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/verrecetas.ui'
#
# Created: Thu Jun 28 20:14:30 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogVRec(object):
    def setupUi(self, DialogVRec):
        DialogVRec.setObjectName("DialogVRec")
        DialogVRec.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogVRec.resize(424, 316)
        DialogVRec.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(DialogVRec)
        self.buttonBox.setGeometry(QtCore.QRect(305, 280, 86, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.Button_Utilizar = QtGui.QPushButton(DialogVRec)
        self.Button_Utilizar.setGeometry(QtCore.QRect(29, 283, 83, 25))
        self.Button_Utilizar.setObjectName("Button_Utilizar")
        self.Button_Ver = QtGui.QPushButton(DialogVRec)
        self.Button_Ver.setGeometry(QtCore.QRect(172, 283, 83, 25))
        self.Button_Ver.setObjectName("Button_Ver")
        self.treeWidget = QtGui.QTreeWidget(DialogVRec)
        self.treeWidget.setGeometry(QtCore.QRect(20, 20, 381, 231))
        self.treeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setMidLineWidth(1)
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(104)
        self.treeWidget.header().setMinimumSectionSize(140)

        self.retranslateUi(DialogVRec)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogVRec.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogVRec.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogVRec)
        DialogVRec.setTabOrder(self.treeWidget, self.Button_Utilizar)
        DialogVRec.setTabOrder(self.Button_Utilizar, self.Button_Ver)
        DialogVRec.setTabOrder(self.Button_Ver, self.buttonBox)

    def retranslateUi(self, DialogVRec):
        DialogVRec.setWindowTitle(QtGui.QApplication.translate("DialogVRec", "Ver Recetas", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_Utilizar.setText(QtGui.QApplication.translate("DialogVRec", "Utilizar", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_Ver.setText(QtGui.QApplication.translate("DialogVRec", "Ver", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("DialogVRec", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("DialogVRec", "Nº Ingestas", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("DialogVRec", "KCal.", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogVRec = QtGui.QDialog()
    ui = Ui_DialogVRec()
    ui.setupUi(DialogVRec)
    DialogVRec.show()
    sys.exit(app.exec_())

