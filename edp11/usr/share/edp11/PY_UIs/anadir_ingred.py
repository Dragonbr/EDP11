# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/anadir_ingred.ui'
#
# Created: Thu Jul  5 09:10:21 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_Ingred(object):
    def setupUi(self, Dialog_Ingred):
        Dialog_Ingred.setObjectName(_fromUtf8("Dialog_Ingred"))
        Dialog_Ingred.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_Ingred.resize(480, 450)
        Dialog_Ingred.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Ingred)
        self.buttonBox.setGeometry(QtCore.QRect(274, 408, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog_Ingred)
        self.label.setGeometry(QtCore.QRect(13, 25, 92, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.treeWidget = QtGui.QTreeWidget(Dialog_Ingred)
        self.treeWidget.setGeometry(QtCore.QRect(20, 50, 440, 261))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
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
        self.push_Modificar = QtGui.QPushButton(Dialog_Ingred)
        self.push_Modificar.setGeometry(QtCore.QRect(114, 410, 81, 27))
        self.push_Modificar.setObjectName(_fromUtf8("push_Modificar"))
        self.push_Nuevo = QtGui.QPushButton(Dialog_Ingred)
        self.push_Nuevo.setGeometry(QtCore.QRect(27, 410, 81, 27))
        self.push_Nuevo.setObjectName(_fromUtf8("push_Nuevo"))
        self.label_3 = QtGui.QLabel(Dialog_Ingred)
        self.label_3.setGeometry(QtCore.QRect(13, 370, 67, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.doubleSpin_cant = QtGui.QDoubleSpinBox(Dialog_Ingred)
        self.doubleSpin_cant.setGeometry(QtCore.QRect(100, 365, 65, 27))
        self.doubleSpin_cant.setDecimals(1)
        self.doubleSpin_cant.setMaximum(9999.0)
        self.doubleSpin_cant.setSingleStep(0.1)
        self.doubleSpin_cant.setProperty(_fromUtf8("value"), 0.0)
        self.doubleSpin_cant.setObjectName(_fromUtf8("doubleSpin_cant"))
        self.label_2 = QtGui.QLabel(Dialog_Ingred)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 451, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Dialog_Ingred)
        self.label_4.setGeometry(QtCore.QRect(62, 337, 131, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog_Ingred)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_Ingred.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_Ingred.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Ingred)
        Dialog_Ingred.setTabOrder(self.treeWidget, self.doubleSpin_cant)
        Dialog_Ingred.setTabOrder(self.doubleSpin_cant, self.push_Nuevo)
        Dialog_Ingred.setTabOrder(self.push_Nuevo, self.push_Modificar)
        Dialog_Ingred.setTabOrder(self.push_Modificar, self.buttonBox)

    def retranslateUi(self, Dialog_Ingred):
        Dialog_Ingred.setWindowTitle(QtGui.QApplication.translate("Dialog_Ingred", "Añadir Ingredientes", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_Ingred", "Ingredientes:", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Grasas y Aceites", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Farináceos", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Proteínicos", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(3).setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Lácteos", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(4).setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Frutas y Verduras", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.push_Modificar.setText(QtGui.QApplication.translate("Dialog_Ingred", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.push_Nuevo.setText(QtGui.QApplication.translate("Dialog_Ingred", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_Ingred", "Cantidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_Ingred", "Nota: La cantidad se mide en gramos, milílitros o unidades,", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_Ingred", "según ingrediente.", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_Ingred = QtGui.QDialog()
    ui = Ui_Dialog_Ingred()
    ui.setupUi(Dialog_Ingred)
    Dialog_Ingred.show()
    sys.exit(app.exec_())

