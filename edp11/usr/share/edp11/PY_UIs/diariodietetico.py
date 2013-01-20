# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/diariodietetico.ui'
#
# Created: Tue Apr 24 14:08:32 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog_DDiet(object):
    def setupUi(self, Dialog_DDiet):
        Dialog_DDiet.setObjectName("Dialog_DDiet")
        Dialog_DDiet.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_DDiet.resize(645, 267)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_DDiet)
        self.buttonBox.setGeometry(QtCore.QRect(10, 224, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.treeWidget = QtGui.QTreeWidget(Dialog_DDiet)
        self.treeWidget.setGeometry(QtCore.QRect(150, 30, 461, 131))
        self.treeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(229)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(140)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.treeWidget.header().setStretchLastSection(False)
        self.pushButton_Eliminar = QtGui.QPushButton(Dialog_DDiet)
        self.pushButton_Eliminar.setGeometry(QtCore.QRect(230, 170, 71, 23))
        self.pushButton_Eliminar.setObjectName("pushButton_Eliminar")
        self.pushButton_Anadir = QtGui.QPushButton(Dialog_DDiet)
        self.pushButton_Anadir.setGeometry(QtCore.QRect(150, 170, 61, 23))
        self.pushButton_Anadir.setObjectName("pushButton_Anadir")
        self.label = QtGui.QLabel(Dialog_DDiet)
        self.label.setGeometry(QtCore.QRect(20, 30, 121, 17))
        self.label.setObjectName("label")
        self.pushButton_Ver = QtGui.QPushButton(Dialog_DDiet)
        self.pushButton_Ver.setGeometry(QtCore.QRect(530, 170, 81, 23))
        self.pushButton_Ver.setObjectName("pushButton_Ver")
        self.pushButton_Form = QtGui.QPushButton(Dialog_DDiet)
        self.pushButton_Form.setGeometry(QtCore.QRect(420, 170, 91, 23))
        self.pushButton_Form.setObjectName("pushButton_Form")

        self.retranslateUi(Dialog_DDiet)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_DDiet.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_DDiet.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_DDiet)
        Dialog_DDiet.setTabOrder(self.treeWidget, self.pushButton_Anadir)
        Dialog_DDiet.setTabOrder(self.pushButton_Anadir, self.pushButton_Eliminar)
        Dialog_DDiet.setTabOrder(self.pushButton_Eliminar, self.pushButton_Form)
        Dialog_DDiet.setTabOrder(self.pushButton_Form, self.pushButton_Ver)
        Dialog_DDiet.setTabOrder(self.pushButton_Ver, self.buttonBox)

    def retranslateUi(self, Dialog_DDiet):
        Dialog_DDiet.setWindowTitle(QtGui.QApplication.translate("Dialog_DDiet", "Diario Dietético", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog_DDiet", "Fichero", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("Dialog_DDiet", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Eliminar.setText(QtGui.QApplication.translate("Dialog_DDiet", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Anadir.setText(QtGui.QApplication.translate("Dialog_DDiet", "Añadir", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_DDiet", "Diario Dietético:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Ver.setText(QtGui.QApplication.translate("Dialog_DDiet", "Ver Diario", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Form.setText(QtGui.QApplication.translate("Dialog_DDiet", "Formulario", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_DDiet = QtGui.QDialog()
    ui = Ui_Dialog_DDiet()
    ui.setupUi(Dialog_DDiet)
    Dialog_DDiet.show()
    sys.exit(app.exec_())

