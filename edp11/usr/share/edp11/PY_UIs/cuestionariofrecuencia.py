# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/cuestionariofrecuencia.ui'
#
# Created: Mon Jul 30 12:17:55 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_CuestFrec(object):
    def setupUi(self, Dialog_CuestFrec):
        Dialog_CuestFrec.setObjectName(_fromUtf8("Dialog_CuestFrec"))
        Dialog_CuestFrec.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_CuestFrec.resize(676, 482)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_CuestFrec)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.scrollArea = QtGui.QScrollArea(Dialog_CuestFrec)
        self.scrollArea.setGeometry(QtCore.QRect(2, 2, 671, 431))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -407, 653, 836))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setMinimumSize(QtCore.QSize(630, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 67, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 67, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(390, 20, 67, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(470, 20, 111, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(630, 160))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(230, 20, 67, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(390, 20, 67, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(470, 20, 111, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(310, 20, 67, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.widget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(630, 129))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(230, 20, 67, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(390, 20, 67, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(470, 20, 111, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(310, 20, 67, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.widget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(630, 217))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_16 = QtGui.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(230, 20, 67, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(390, 20, 67, 17))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(470, 20, 111, 17))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(310, 20, 67, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.widget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(630, 127))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_21 = QtGui.QLabel(self.groupBox_5)
        self.label_21.setGeometry(QtCore.QRect(230, 20, 67, 17))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.groupBox_5)
        self.label_22.setGeometry(QtCore.QRect(390, 20, 67, 17))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.groupBox_5)
        self.label_23.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.groupBox_5)
        self.label_24.setGeometry(QtCore.QRect(470, 20, 111, 17))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.groupBox_5)
        self.label_25.setGeometry(QtCore.QRect(310, 20, 67, 17))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.verticalLayout.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog_CuestFrec)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_CuestFrec.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_CuestFrec.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_CuestFrec)
        Dialog_CuestFrec.setTabOrder(self.scrollArea, self.buttonBox)

    def retranslateUi(self, Dialog_CuestFrec):
        Dialog_CuestFrec.setWindowTitle(QtGui.QApplication.translate("Dialog_CuestFrec", "Cuestionario de Frecuencia", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog_CuestFrec", "Grasas y Aceites", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Alimento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Diario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Semanal:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Mensual:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Preferencia(1-5):", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog_CuestFrec", "Farináceos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Diario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Mensual:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Alimento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Preferencia(1-5):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Semanal:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog_CuestFrec", "Proteínicos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Diario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Mensual:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Alimento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Preferencia(1-5):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Semanal:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog_CuestFrec", "Lácteos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Diario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Mensual:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Alimento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Preferencia(1-5):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Semanal:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Dialog_CuestFrec", "Frutas y Verduras", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Diario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Mensual:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Alimento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Preferencia(1-5):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("Dialog_CuestFrec", "Semanal:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_CuestFrec = QtGui.QDialog()
    ui = Ui_Dialog_CuestFrec()
    ui.setupUi(Dialog_CuestFrec)
    Dialog_CuestFrec.show()
    sys.exit(app.exec_())
