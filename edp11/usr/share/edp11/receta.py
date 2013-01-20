# -*- coding: utf-8 -*-
import sys
import sqlite3 as dbapi

sys.path.append('PY_UIs')

from nuevareceta import *
from seleccionarreceta import *
from modificarreceta import *
from eliminarreceta import *
from anadir_ingred import *

class Receta:
    
#Declaraciones de la accion Nueva Receta
    def VentanaNueva(self):
        self.WindowNRec = QtGui.QDialog()
        self.uiNR = Ui_DialogNRec()
        self.uiNR.setupUi(self.WindowNRec)

#Conexion de accion Nueva Receta y GUI Nueva Receta
    def Nueva_Receta(self):
        self.uiNR.lineEdit.clear()
        self.uiNR.treeWidget.clear()
        self.uiNR.textEdit.clear()
        self.uiNR.doubleSpinBox.setValue(0)
        self.uiNR.comboBox.setCurrentIndex(0)
        self.uiNR.label_6.setText("")
        self.WindowNRec.show()

#Declaraciones de la accion Modificar Receta
    def VentanaModif(self):
        self.WindowSelRec = QtGui.QDialog()
        self.uiSR = Ui_DialogSelRec()
        self.uiSR.setupUi(self.WindowSelRec)
        
        self.WindowMRec = QtGui.QDialog()
        self.uiMR = Ui_DialogMRec()
        self.uiMR.setupUi(self.WindowMRec)

#Declaraciones de GUI Anadir Ingredientes
    def VentanaAnadirIngr(self):
        self.WindowAIngr = QtGui.QDialog()
        self.uiAI = Ui_Dialog_Ingred()
        self.uiAI.setupUi(self.WindowAIngr)

#Declaraciones de accion Eliminar Receta
    def VentanaElim(self):
        self.WindowElimR = QtGui.QDialog()
        self.uiER = Ui_DialogElimR()
        self.uiER.setupUi(self.WindowElimR)

#Conexion de button Anadir y GUI Anadir Ingredientes
    def InicializarTreeWidgetI(self, ui):
        ui.treeWidget.clear()
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Grasas y Aceites", None, QtGui.QApplication.UnicodeUTF8))
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Farináceos", None, QtGui.QApplication.UnicodeUTF8))
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(2).setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Proteínicos", None, QtGui.QApplication.UnicodeUTF8))
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(3).setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Lácteos", None, QtGui.QApplication.UnicodeUTF8))
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(4).setText(0, QtGui.QApplication.translate("Dialog_Ingred", "Frutas y Verduras", None, QtGui.QApplication.UnicodeUTF8))

    def MostrarIngred(self, ui, window):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Mostrar registros de la bbdd y mostrar la GUI
        cursor.execute("select i_nombre, i_tipo, i_cant from Ingrediente")
        items = cursor.fetchall()
        index = 0
        self.InicializarTreeWidgetI(ui)
        if items:
            for i in range(len(items)):
                if items[i][1] == "Grasas y Aceites":
                    index = 0
                elif items[i][1] == "Farinaceos":
                    index = 1
                elif items[i][1] == "Proteinicos":
                    index = 2
                elif items[i][1] == "Lacteos":
                    index = 3
                elif items[i][1] == "Frutas y Verduras":
                    index = 4
                item = QtGui.QTreeWidgetItem(ui.treeWidget.topLevelItem(index),0)
                item.setText(0,items[i][0])
                ui.treeWidget.topLevelItem(index).addChild(item)
                ui.treeWidget.topLevelItem(index).sortChildren(0,0)
        I = ui.treeWidget.itemAt(0,0)
        ui.treeWidget.setCurrentItem(I)
        window.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
        
    def MostrarAnadirIngrediente(self, ui, window):
        ui.doubleSpin_cant.setValue(0)
        self.MostrarIngred(ui, window)

#Conexion de Aceptar de Añadir Ingrediente y treeWidget de Nueva Receta
    def AgregarIngr(self, ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Introducir en treeWidget el item
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        N = unicode(self.uiAI.treeWidget.currentItem().text(0))
        cursor.execute("select i_cal, i_cant from Ingrediente where i_nombre=?",(N,))
        res = cursor.fetchone()
        if self.uiAI.doubleSpin_cant.value() != 0:
            cal = self.uiAI.doubleSpin_cant.value() * res[0] / res[1]
            if res[1] == 1:
                medida = str(self.uiAI.doubleSpin_cant.value()) + " uds."
            elif res[1] == 100:
                medida = str(int(self.uiAI.doubleSpin_cant.value())) + " gramos"
            else:
                medida = str(int(self.uiAI.doubleSpin_cant.value())) + " ml."
            item.setText(0,N)
            item.setText(1,medida)
            item.setText(2,str(cal))
            ui.treeWidget.addTopLevelItem(item)
            ui.treeWidget.sortItems(0,0)
            ui.doubleSpinBox.setValue(ui.doubleSpinBox.value() + cal)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de push_Eliminar de GUI Nueva Receta y treeWidget
    def EliminarIngr(self,ui):
        #Eliminacion del item del treeWidget y de la bbdd
        if ui.treeWidget.currentItem():
            item = ui.treeWidget.currentItem()
            column = ui.treeWidget.currentColumn()
            ui.treeWidget.removeItemWidget(item,column)
            valor = ui.doubleSpinBox.value() - float(item.text(2))
            ui.doubleSpinBox.setValue(valor)
        
#Conexion de button Modificar de GUI Anadir Ingredientes y GUI Modificar Ingrediente
    def ParserUnidadIngr(self, udgr):
        if udgr == 1:
            index = 0
        elif udgr == 100:
            index = 1
        elif udgr == 10:
            index = 2
        return index

    def ParserTipoIngr(self, tipo):
        if tipo == "Grasas y Aceites":
            index = 0
        elif tipo == "Farinaceos":
            index = 1
        elif tipo == "Proteinicos":
            index = 2
        elif tipo == "Lacteos":
            index = 3
        elif tipo == "Frutas y Verduras":
            index = 4
        return index

    def ModificarIngr(self, ingrediente):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Mostrar item del treeWidget
        item = self.uiAI.treeWidget.currentItem()
        column = self.uiAI.treeWidget.currentColumn()
        N = unicode(self.uiAI.treeWidget.currentItem().text(0))
        cursor.execute("select * from Ingrediente where i_nombre=?",(N,))
        res = cursor.fetchall()
        ingrediente.uiMI.lineEdit_nom.setText(res[0][1])
        ingrediente.uiMI.double_cal.setValue(res[0][4])
        index_udgr = self.ParserUnidadIngr(res[0][2])
        index_tipo = self.ParserTipoIngr(res[0][3])
        ingrediente.uiMI.combo_udgr.setCurrentIndex(index_udgr)
        ingrediente.uiMI.combo_tipo.setCurrentIndex(index_tipo)
        self.MostrarIngred(self.uiAI, self.WindowAIngr)
        titulo = "Modificar Ingrediente"
        ingrediente.WindowMIngr.setWindowTitle(QtGui.QApplication.translate("MainWindow", titulo, None, QtGui.QApplication.UnicodeUTF8))
        # self.uiAI.treeWidget.setCurrentItem(item)
        ingrediente.WindowMIngr.show()
        ingrediente.EstablecerActual(N)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de Aceptar de GUI Nueva Receta, bbdd y treeWidget de MainWindow
    def ParserComboNR(self,ui):
        tipo = ""
        if ui.comboBox.currentIndex() == 0:
            tipo = "Desayuno"
        elif ui.comboBox.currentIndex() == 1:
            tipo = "Media Manana"
        elif ui.comboBox.currentIndex() == 2:
            tipo = "Almuerzo"
        elif ui.comboBox.currentIndex() == 3:
            tipo = "Merienda"
        elif ui.comboBox.currentIndex() == 4:
            tipo = "Cena"
        elif ui.comboBox.currentIndex() == 5:
            tipo = "Tentempie"
        return tipo

    def GuardarReceta(self, ui, dietista):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Inserccion de Nueva Receta en BBDD
        N = unicode(ui.lineEdit.text())
        C = ui.doubleSpinBox.value()
        CT = self.ParserComboNR(ui)
        P = unicode(ui.textEdit.toPlainText())
        perfil = dietista.ObtenerPerfil()
        cursor.execute("select r_id from Receta where r_nombre=?",(N,))
        existe = cursor.fetchone()
        if existe:
            ui.label_6.setText("La receta ya existe.")
            self.WindowNRec.show()
        else:
            cursor.execute("select max(r_id) from Receta")
            res = cursor.fetchone()
            if res[0] == None:
                NUM = 1
            else:
                NUM = res[0]
                NUM = NUM + 1
            cursor.execute("insert into Receta values (?,?,?,?,?,?)",(NUM,N,C,CT,P,perfil,))
            bbdd.commit()
            #Inserccion de treeWidget de Nueva Receta en Receta_Ingredientes
            I = ui.treeWidget.itemAt(0,0)
            while I:
                ui.treeWidget.setCurrentItem(I)
                NI = unicode(ui.treeWidget.currentItem().text(0))
                CA = unicode(ui.treeWidget.currentItem().text(1))
                CAL = float(ui.treeWidget.currentItem().text(2))
                cursor.execute("select max(ri_id) from Receta_Ingredientes")
                res = cursor.fetchone()
                if res[0] == None:
                    NUM = 1
                else:
                    NUM = res[0]
                    NUM = NUM + 1
                cursor.execute("insert into Receta_Ingredientes values (?,?,?,?,?,?)",(NUM,N,NI,CA,CAL,perfil,))
                I = ui.treeWidget.itemBelow(I)
                bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de accionEditar_Receta y mostrar recetas de un dietista
    def InicializarTreeWidget(self, ui):
        ui.treeWidget.clear()
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "Desayuno", None, QtGui.QApplication.UnicodeUTF8))
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "Media Mañana", None, QtGui.QApplication.UnicodeUTF8))
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(2).setText(0, QtGui.QApplication.translate("MainWindow", "Almuerzo", None, QtGui.QApplication.UnicodeUTF8))
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(3).setText(0, QtGui.QApplication.translate("MainWindow", "Merienda", None, QtGui.QApplication.UnicodeUTF8))
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(4).setText(0, QtGui.QApplication.translate("MainWindow", "Cena", None, QtGui.QApplication.UnicodeUTF8))
        item = QtGui.QTreeWidgetItem(ui.treeWidget,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        ui.treeWidget.addTopLevelItem(item)
        ui.treeWidget.topLevelItem(5).setText(0, QtGui.QApplication.translate("MainWindow", "Tentempié", None, QtGui.QApplication.UnicodeUTF8))

#Mostrar Recetas en treeWidget de MainWindow
    def MostrarRecetas(self,dietista,ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Mostrar registros de la bbdd y mostrar la GUI
        perfil = dietista.ObtenerPerfil()
        cursor.execute("select r_nombre, r_categ, r_cal from Receta where r_ddni=?",(perfil,))
        items = cursor.fetchall()
        index = 0
        self.InicializarTreeWidget(ui)
        if items:
            for i in range(len(items)):
                if items[i][1] == "Desayuno":
                    index = 0
                elif items[i][1] == "Media Manana":
                    index = 1
                elif items[i][1] == "Almuerzo":
                    index = 2
                elif items[i][1] == "Merienda":
                    index = 3
                elif items[i][1] == "Cena":
                    index = 4
                elif items[i][1] == "Tentempie":
                    index = 5
                item = QtGui.QTreeWidgetItem(ui.treeWidget.topLevelItem(index),0)
                item.setText(0,items[i][0])
                item.setText(1,str(items[i][2]))
                ui.treeWidget.topLevelItem(index).addChild(item)
                ui.treeWidget.topLevelItem(index).sortChildren(0,0)
        I = ui.treeWidget.itemAt(0,0)
        ui.treeWidget.setCurrentItem(I)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Mostrar recetas en opcion modificar receta (Seleccionar receta)
    def SeleccionarReceta(self, dietista):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Mostrar recetas en treeWidget de Seleccionar Receta
        perfil = dietista.ObtenerPerfil()
        cursor.execute("select r_nombre, r_categ, r_cal from Receta where r_ddni=?",(perfil,))
        items = cursor.fetchall()
        index = 0
        self.InicializarTreeWidget(self.uiSR)
        if items:
            for i in range(len(items)):
                if items[i][1] == "Desayuno":
                    index = 0
                elif items[i][1] == "Media Manana":
                    index = 1
                elif items[i][1] == "Almuerzo":
                    index = 2
                elif items[i][1] == "Merienda":
                    index = 3
                elif items[i][1] == "Cena":
                    index = 4
                elif items[i][1] == "Tentempie":
                    index = 5
                item = QtGui.QTreeWidgetItem(self.uiSR.treeWidget.topLevelItem(index),0)
                item.setText(0,items[i][0])
                item.setText(1,str(items[i][2]))
                self.uiSR.treeWidget.topLevelItem(index).addChild(item)
                self.uiSR.treeWidget.topLevelItem(index).sortChildren(0,0)
        I = self.uiSR.treeWidget.itemAt(0,0)
        self.uiSR.treeWidget.setCurrentItem(I)
        self.WindowSelRec.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Mostrar recetas en Eliminar Receta
    def listElimReceta(self, dietista):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Mostrar recetas en treeWidget de Seleccionar Receta
        perfil = dietista.ObtenerPerfil()
        cursor.execute("select r_nombre, r_categ from Receta where r_ddni=?",(perfil,))
        items = cursor.fetchall()
        index = 0
        self.InicializarTreeWidget(self.uiER)
        if items:
            for i in range(len(items)):
                if items[i][1] == "Desayuno":
                    index = 0
                elif items[i][1] == "Media Manana":
                    index = 1
                elif items[i][1] == "Almuerzo":
                    index = 2
                elif items[i][1] == "Merienda":
                    index = 3
                elif items[i][1] == "Cena":
                    index = 4
                elif items[i][1] == "Tentempie":
                    index = 5
                item = QtGui.QTreeWidgetItem(self.uiER.treeWidget.topLevelItem(index),0)
                item.setText(0,items[i][0])
                self.uiER.treeWidget.topLevelItem(index).addChild(item)
                self.uiER.treeWidget.topLevelItem(index).sortChildren(0,0)
        I = self.uiER.treeWidget.itemAt(0,0)
        self.uiER.treeWidget.setCurrentItem(I)
        self.WindowElimR.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de Aceptar de Eliminar Receta y bbdd
    def DropReceta(self,dietista):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta de Receta y treeWidget
        perfil = dietista.ObtenerPerfil()
        item_nom = unicode(self.uiER.treeWidget.currentItem().text(0))
        if item_nom != None:
            cursor.execute("delete from Receta where r_nombre=? and r_ddni=?",(item_nom,perfil,))
            cursor.execute("delete from Receta_Ingredientes where ri_nomrec=? and ri_ddni=?",(item_nom,perfil,))
        bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
        
#Conexion de Aceptar de Seleccionar Receta y Ventana Modificar Receta
    def VentanaModificar(self, dietista):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Obtener datos de Receta y mostrar ventana Modificar Receta
        perfil = dietista.ObtenerPerfil()
        self.uiMR.treeWidget.clear()
        self.uiMR.doubleSpinBox.setValue(0)
        R = unicode(self.uiSR.treeWidget.currentItem().text(0))
        cursor.execute("select * from Receta where r_nombre=? and r_ddni=?",(R,perfil,))
        info = cursor.fetchone()
        if info != None:
            id = info[0]
            self.uiMR.lineEdit.setText(info[1])
            self.uiMR.doubleSpinBox.setValue(info[2])
            index = 0
            if info[3] == "Desayuno":
                index = 0
            elif info[3] == "Media Manana":
                index = 1
            elif info[3] == "Almuerzo":
                index = 2
            elif info[3] == "Merienda":
                index = 3
            elif info[3] == "Cena":
                index = 4
            elif info[3] == "Tentempie":
                index = 5
            self.uiMR.comboBox.setCurrentIndex(index)
            self.uiMR.textEdit.setText(info[4])
            cursor.execute("select * from Receta_Ingredientes where ri_nomrec=? and ri_ddni=?",(info[1], perfil,))
            items = cursor.fetchall()
            self.uiMR.doubleSpinBox.setValue(0)
            for i in range(len(items)):
                item = QtGui.QTreeWidgetItem(self.uiMR.treeWidget,0)
                N = items[i][2]
                item.setText(0,N)
                medida = items[i][3]
                item.setText(1,medida)
                cal = items[i][4]
                item.setText(2,str(cal))
                self.uiMR.treeWidget.addTopLevelItem(item)
                self.uiMR.treeWidget.sortItems(0,0)
                self.uiMR.doubleSpinBox.setValue(self.uiMR.doubleSpinBox.value() + cal)
                ri_id = items[i][0]
                #Borrado de los datos en la bbdd para guardarlos posteriormente
                cursor.execute("delete from Receta_Ingredientes where ri_id=?",(ri_id,))
            cursor.execute("delete from Receta where r_id=?",(id,))
            bbdd.commit()
            #Mostrar Ventana Modificar Receta
            self.WindowMRec.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
