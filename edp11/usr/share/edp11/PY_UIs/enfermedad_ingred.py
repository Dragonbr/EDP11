# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/enfermedad_ingred.ui'
#
# Created: Sat Nov 12 01:02:15 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog_SelIngred(object):
    def setupUi(self, Dialog_SelIngred):
        Dialog_SelIngred.setObjectName("Dialog_SelIngred")
        Dialog_SelIngred.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_SelIngred.resize(480, 361)
        Dialog_SelIngred.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_SelIngred)
        self.buttonBox.setGeometry(QtCore.QRect(293, 322, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(Dialog_SelIngred)
        self.label.setGeometry(QtCore.QRect(13, 25, 92, 17))
        self.label.setObjectName("label")
        self.treeWidget = QtGui.QTreeWidget(Dialog_SelIngred)
        self.treeWidget.setGeometry(QtCore.QRect(20, 50, 440, 261))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

        self.retranslateUi(Dialog_SelIngred)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog_SelIngred.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog_SelIngred.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_SelIngred)
        Dialog_SelIngred.setTabOrder(self.treeWidget, self.buttonBox)

    def retranslateUi(self, Dialog_SelIngred):
        Dialog_SelIngred.setWindowTitle(QtGui.QApplication.translate("Dialog_SelIngred", "Seleccionar Ingredientes", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_SelIngred", "Ingredientes:", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog_SelIngred", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("Dialog_SelIngred", "Grasas y Aceites", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("Dialog_SelIngred", "Farináceos", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).setText(0, QtGui.QApplication.translate("Dialog_SelIngred", "Proteínicos", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(3).setText(0, QtGui.QApplication.translate("Dialog_SelIngred", "Lácteos", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(4).setText(0, QtGui.QApplication.translate("Dialog_SelIngred", "Frutas y Verduras", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_SelIngred = QtGui.QDialog()
    ui = Ui_Dialog_SelIngred()
    ui.setupUi(Dialog_SelIngred)
    Dialog_SelIngred.show()
    sys.exit(app.exec_())

