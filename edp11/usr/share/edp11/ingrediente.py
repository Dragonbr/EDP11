# -*- coding: utf-8 -*-
import sys
import sqlite3 as dbapi

sys.path.append('PY_UIs')

from receta import *
from nuevoingrediente import *

class Ingrediente():
    def __init__(self):
        self.actual = ""
        self.lista = []

    def EstablecerActual(self,nombre):
        self.actual = nombre

#Declaraciones de GUI Nuevo Ingrediente
    def VentanaNuevo(self):
        self.WindowNIngr = QtGui.QDialog()
        self.uiNI = Ui_Dialog_Ingr()
        self.uiNI.setupUi(self.WindowNIngr)

#Declaraciones de GUI Modificar Ingrediente
    def VentanaModificar(self):
        self.WindowMIngr = QtGui.QDialog()
        self.uiMI = Ui_Dialog_Ingr()
        self.uiMI.setupUi(self.WindowMIngr)

#Conexion de button Nuevo de GUI Anadir Ingredientes y GUI Nuevo Ingrediente
    def NuevoIngr(self):
        self.uiNI.lineEdit_nom.clear()
        self.uiNI.double_cal.setValue(0)
        self.uiNI.combo_udgr.setCurrentIndex(0)
        self.uiNI.combo_tipo.setCurrentIndex(0)
        self.WindowNIngr.show()

#Conexion de button Aceptar de GUI Modificar Ingredientes y BBDD
    def ModificarIngrediente(self, receta):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion del item del treeWidget y de la bbdd
        N = self.actual
        cursor.execute("select i_id from Ingrediente where i_nombre=?",(N,))
        res = cursor.fetchone()
        IID = res[0]
        cursor.execute("delete from Ingrediente where i_id=?",(IID,))
        NOM = unicode(self.uiMI.lineEdit_nom.text())
        C = unicode(self.uiMI.lineEdit_udgr.text())
        T = self.ParserComboI(self.uiMI)
        CA = self.uiMI.double_cal.value()
        cursor.execute("insert into Ingrediente values (?,?,?,?,?)",(IID,NOM,C,T,CA,))
        cursor.execute("select * from Receta_Ingredientes where ri_nomingr=?",(N,))
        items = cursor.fetchall()
        if items:
            for i in range(len(items)):
                RID = items[i][0]
                RNOM = items[i][1]
                # RING = items[i][2]
                RCANT = items[i][3]
                # RCAL = items[i][4]
                RDDNI = items[i][5]
                cursor.execute("delete from Receta_Ingredientes where ri_id=?",(RID,))          
                if  C == "1":
                    CANT =  RCANT.split(" ")[0] + " uds."
                elif C == "100":
                    CANT = RCANT.split(" ")[0] + " gramos"
                else:
                    CANT = RCANT.split(" ")[0] + " ml."
                RCAL = float(RCANT.split(" ")[0]) * CA / float(C)
                cursor.execute("insert into Receta_Ingredientes values (?,?,?,?,?,?)",(RID,RNOM,NOM,CANT,RCAL,RDDNI,))
        bbdd.commit()
        receta.MostrarAnadirIngrediente(receta.uiAI, receta.WindowAIngr)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de combo medida de GUI Nuevo Ingrediente y lineEdit ud | gr
    def Cantidad(self, ui):
        if ui.combo_udgr.currentIndex() == 0:
            ui.lineEdit_udgr.setText("1")
        elif ui.combo_udgr.currentIndex() == 1:
            ui.lineEdit_udgr.setText("100")
        elif ui.combo_udgr.currentIndex() == 2:
            ui.lineEdit_udgr.setText("10")

#Conexion de buttonBox Aceptar y treeWidget de Anadir Ingrediente con BBDD
    def ParserComboI(self, ui):
        tipo = ""
        if ui.combo_tipo.currentIndex() == 0:
            tipo = "Grasas y Aceites"
        elif ui.combo_tipo.currentIndex() == 1:
            tipo = "Farinaceos"
        elif ui.combo_tipo.currentIndex() == 2:
            tipo = "Proteinicos"
        elif ui.combo_tipo.currentIndex() == 3:
            tipo = "Lacteos"
        elif ui.combo_tipo.currentIndex() == 4:
            tipo = "Frutas y Verduras"
        return tipo

    def RecogerPreferencias(self,objetos):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta y modificacion en la bbdd
        cursor.execute("select pr_iid, pr_d, pr_s, pr_m, pr_npr, pr_pid from Preferencia")
        res = cursor.fetchall()
        lista = []
        if res:
            for i in range(len(res)):
                item = [res[i][0],res[i][1],res[i][2],res[i][3],res[i][4],res[i][5]]
                lista.append(item)
        self.lista = lista
        cursor.execute("delete from Preferencia")
        objetos.objetosGrupo1 = []
        objetos.objetosGrupo2 = []
        objetos.objetosGrupo3 = []
        objetos.objetosGrupo4 = []
        objetos.objetosGrupo5 = []

        bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()


    def GuardarIngrediente(self, receta):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Introducir en treeWidget el item
        numtipo = self.uiNI.combo_tipo.currentIndex()
        item = QtGui.QTreeWidgetItem(receta.uiAI.treeWidget.topLevelItem(numtipo),0)
        item.setText(0, self.uiNI.lineEdit_nom.text())
        receta.uiAI.treeWidget.topLevelItem(numtipo).addChild(item)
        receta.uiAI.treeWidget.topLevelItem(numtipo).sortChildren(0,0)
        #Inserccion en la bbdd
        cursor.execute("select max(i_id) from Ingrediente")
        res = cursor.fetchone()
        if res[0] == None:
            NUM = 1
        else:
            NUM = res[0]
            NUM = NUM + 1
        N = unicode(self.uiNI.lineEdit_nom.text())
        C = unicode(self.uiNI.lineEdit_udgr.text())
        T = self.ParserComboI(self.uiNI)
        CA = self.uiNI.double_cal.value()
        cursor.execute("insert into Ingrediente values (?,?,?,?,?)",(NUM,N,C,T,CA,))
        bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
