# -*- coding: utf-8 -*-
import sys
import os
import datetime
import popplerqt4
import sqlite3 as dbapi

sys.path.append('PY_UIs')

from nuevopaciente1 import *
from nuevopaciente2 import *
from abrirpaciente import *
from eliminarpaciente import *
from cerrarpaciente import *
from informacionmedica import *
from agregarenfermedad import *
from nuevaenfermedad import *
from enfermedad_ingred import *
from anadirtratapoyo import *
from infogen import *
from diariodietetico import *
from cuestionariofrecuencia import *
from verrecetas import *
from relatorio.templates.opendocument import Template
from GUI import *


class Objetos:
    def __init__(self):
        self.objetosGrupo1 = []
        self.objetosGrupo2 = []
        self.objetosGrupo3 = []
        self.objetosGrupo4 = []
        self.objetosGrupo5 = []

class Paciente:
    def __init__(self,GUI):
        self.perfil = 0
        self.gui = GUI

    def VentanaNuevo(self):
    #Declaraciones de la accion Nuevo Paciente
        self.WindowNewPac = QtGui.QDialog()
        self.uiNP = Ui_DialogNuevoP1()
        self.uiNP.setupUi(self.WindowNewPac)

        self.WindowNewP2 = QtGui.QDialog()
        self.uiNP2 = Ui_DialogNuevoP2()
        self.uiNP2.setupUi(self.WindowNewP2)

    def VentanaAbrir(self):
    #Declaraciones de la accion Abrir Paciente
        self.WindowOpenPac = QtGui.QDialog()
        self.uiAP = Ui_DialogAbrirP()
        self.uiAP.setupUi(self.WindowOpenPac)

    def VentanaEliminar(self):
    #Declaraciones de la accion Eliminar Paciente
        self.WindowSuprPac = QtGui.QDialog()
        self.uiEP = Ui_DialogElimP()
        self.uiEP.setupUi(self.WindowSuprPac)

    def VentanaCerrar(self):
    #Declaraciones de la accion Cerrar Paciente
        self.WindowCPac = QtGui.QDialog()
        self.uiCP = Ui_DialogCPac()
        self.uiCP.setupUi(self.WindowCPac)

    def VentanaInfoMed(self):
    #Declaraciones de clase Informacion Medica de Paciente
        self.WindowInfoMed = QtGui.QDialog()
        self.uiInfoM = Ui_Dialog_InfMed()
        self.uiInfoM.setupUi(self.WindowInfoMed)

    def VentanaEnfermedad(self):
    #Declaraciones de clase Enfermedades y Patologias de Paciente
        self.WindowEnfer = QtGui.QDialog()
        self.uiEnfer = Ui_Dialog_Enf()
        self.uiEnfer.setupUi(self.WindowEnfer)

    def VentanaNEnfermedad(self):
    #Declaraciones de clase Nuevo Enfermedades y Patologias de Paciente
        self.WindowNEnfer = QtGui.QDialog()
        self.uiNEnfer = Ui_Dialog_NEnf()
        self.uiNEnfer.setupUi(self.WindowNEnfer)

    def VentanaNEnfIngred(self):
    #Declaraciones de clase Seleccionar Ingrediente
        self.WindowNEIngred = QtGui.QDialog()
        self.uiNEI = Ui_Dialog_SelIngred()
        self.uiNEI.setupUi(self.WindowNEIngred)

    def VentanaTrataApoyo(self):
    #Declaraciones de clase Nuevo Tratamiento de Apoyo
        self.WindowNTratA = QtGui.QDialog()
        self.uiNTA = Ui_Dialog_Trat()
        self.uiNTA.setupUi(self.WindowNTratA)

    def VentanaInfoGen(self):
    #Declaraciones de clase Informacion General
        self.WindowInfoGen = QtGui.QDialog()
        self.uiInfoG = Ui_Dialog_InfoGen()
        self.uiInfoG.setupUi(self.WindowInfoGen)

    def VentanaDiarioD(self):
    #Declaraciones de clase Diario Dietetico
        self.WindowDiarioD = QtGui.QDialog()
        self.uiDiarioD = Ui_Dialog_DDiet()
        self.uiDiarioD.setupUi(self.WindowDiarioD)

    def VentanaRecordatorio(self):
    #Declaraciones de clase Recordatorio
        self.WindowRecordatorio = QtGui.QDialog()
        self.uiRecordatorio = Ui_Dialog_DDiet()
        self.uiRecordatorio.setupUi(self.WindowRecordatorio)
    
    def VentanaCuestFrec(self):
    #Declaraciones de clase Cuestionario de Frecuencia
        self.WindowCuestFrec = QtGui.QDialog()
        self.uiCuestFrec = Ui_Dialog_CuestFrec()
        self.uiCuestFrec.setupUi(self.WindowCuestFrec)

    def VentanaVerRecetas(self):
    #Declaraciones de clase Ver Recetas
        self.WindowVRec = QtGui.QDialog()
        self.uiVRec = Ui_DialogVRec()
        self.uiVRec.setupUi(self.WindowVRec)

#Conexion accion Nuevo Paciente y Ventana Nuevo Paciente
    def NuevoPaciente(self):
        self.uiNP.combo_FM.setCurrentIndex(0)
        self.uiNP.lineEdit_Nom.setText("")
        self.uiNP.lineEdit_Apell.setText("")
        date = QtCore.QDate(1950,10,3)
        self.uiNP.date_FNac.setDate(date)
        self.uiNP.lineEdit_Edad.setText("")
        self.uiNP.lineEdit_Dni.setText("")
        self.uiNP.lineEdit_Tlf.setText("")
        self.uiNP.lineEdit_Prof.setText("")
        self.uiNP.lineEdit_Dir.setText("")
        self.uiNP.label.setText("")
        self.WindowNewPac.show()

#Conexion boton Aceptar 1ºVentana Nuevo Paciente y coger perfil
    def MostrarVentana2NPaciente(self,ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        cursor.execute("select p_id from Paciente where p_dni=?",(unicode(ui.lineEdit_Dni.text()),))
        existe = cursor.fetchone()
        if not(ui.lineEdit_Nom.text()) or not(ui.lineEdit_Apell.text()) or not(ui.lineEdit_Dni.text()) or not(ui.lineEdit_Tlf.text()) or not(ui.lineEdit_Dir.text()) or not(ui.lineEdit_Prof.text()):
            ui.label.setText("Todos los campos son obligatorios.")
            self.WindowNewPac.show()
        elif existe:
            ui.label.setText("El paciente con dicho DNI ya existe.")
            self.WindowNewPac.show()
        else:

            cursor.execute("select max(p_id) from Paciente")
            res = cursor.fetchone()
            if res[0] == None:
                NUM = 1
            else:
                NUM = res[0]
                NUM = NUM + 1

            self.perfil = NUM
            self.WindowNewP2.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion boton Aceptar 2ºVentana Nuevo Paciente y guardar en bbdd
    def GuardarPaciente(self, dietista):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Inserccion en la bbdd
        FM = unicode("F")
        if self.uiNP.combo_FM.currentIndex() == 1:
            FM = unicode("M")
        N = unicode(self.uiNP.lineEdit_Nom.text())
        A = unicode(self.uiNP.lineEdit_Apell.text())
        D = unicode(self.uiNP.date_FNac.date().toString("dd/MM/yyyy"))
        DNI = unicode(self.uiNP.lineEdit_Dni.text())
        T = int(self.uiNP.lineEdit_Tlf.text())
        P = unicode(self.uiNP.lineEdit_Prof.text())
        DIR = unicode(self.uiNP.lineEdit_Dir.text())
        perfil = dietista.ObtenerPerfil()
        cursor.execute("select max(p_id) from Paciente")
        res = cursor.fetchone()
        if res[0] == None:
            NUM = 1
        else:
            NUM = res[0]
            NUM = NUM + 1
        valores = (NUM, FM, DNI, N, A, D, T, P, DIR, perfil,)
        cursor.execute("insert into Paciente values (?,?,?,?,?,?,?,?,?,?)",valores)
        cursor.execute("select max(an_id) from Antrop_Nec")
        res = cursor.fetchone()
        if res[0] == None:
            NUMAN = 1
        else:
            NUMAN = res[0]
            NUMAN = NUMAN + 1
        P = self.uiNP2.doubleSpin_Peso.value()
        A = self.uiNP2.doubleSpin_Alt.value()
        IMC = 0
        OBJ = self.uiNP2.doubleSpin_POb.value()
        CA = self.uiNP2.doubleSpin_Cad.value()
        CI = self.uiNP2.doubleSpin_Cint.value()
        PT = self.uiNP2.doubleSpin_Tricip.value()
        COM = "Delgada"
        if self.uiNP2.combo_Complex.currentIndex() == 1:
            COM = "Media"
        elif self.uiNP2.combo_Complex.currentIndex() == 2:
            COM = "Ancha"
        PPAC = 0
        MB = 0
        AC = "Ligera"
        if self.uiNP2.combo_Activ.currentIndex() == 1:
            AC = "Moderada"
        elif self.uiNP2.combo_Activ.currentIndex() == 2:
            AC = "Intensa"
        ET = 0
        NING = 6
        PMAT = 0
        INFO_TRAT = ""
        perfilP = NUM
        valores = (NUMAN, P, A, IMC, OBJ, CA, CI, PT, COM, PPAC, MB, AC, ET, NING, PMAT, INFO_TRAT, perfilP,)
        cursor.execute("insert into Antrop_Nec values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",valores)
        valores = (NUM, "","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",perfilP,)
        cursor.execute("insert into Info_General values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",valores)
        bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion accion Abrir Paciente y Ventana Abrir Paciente
    def AbrirPaciente(self,ui,dietista):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        #Para que funcione office desde el principio
        os.system("soffice -headless -accept=\"socket,port=8100;urp;\"")

        perfil = dietista.ObtenerPerfil()
        self.uiAP.treeWidget.clear()
        cursor.execute("select p_dni, p_nombre, p_apell from Paciente where p_ddni=?",(perfil,))
        items = cursor.fetchall()
        if items:
            for i in range(len(items)):
                item = QtGui.QTreeWidgetItem(self.uiAP.treeWidget,0)
                nomapell = items[i][1] + " " + items[i][2]
                item.setText(0,nomapell)
                item.setText(1,items[i][0])
                self.uiAP.treeWidget.addTopLevelItem(item)
        self.uiAP.treeWidget.sortItems(0,0)
        I = self.uiAP.treeWidget.itemAt(0,0)
        self.uiAP.treeWidget.setCurrentItem(I)
        self.WindowOpenPac.show()

        dietista.IniciaTabla(ui)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
        
#Conexion boton Aceptar Abrir Paciente, boton Aceptar de Ventana Abrir Paciente y establecer datos en MainWindow
    def MostrarDatosP(self, ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Mostrar datos en MainWindow
        if self.uiAP.treeWidget.currentItem():
            dni = unicode(self.uiAP.treeWidget.currentItem().text(1))
            cursor.execute("select * from Paciente where p_dni=?",(dni,))
            res = cursor.fetchone()
            self.perfil = res[0]
            if res[1] == "F":
                ui.combo_FM.setCurrentIndex(0)
            else:
                ui.combo_FM.setCurrentIndex(1)
            ui.lineEdit_Dni.setText(res[2])
            ui.lineEdit_Nom.setText(res[3])
            ui.lineEdit_Apell.setText(res[4])
            date = QtCore.QDate.fromString(res[5],"dd/MM/yyyy")
            ui.date_FNac.setDate(date)
            ui.lineEdit_Tlf.setText(unicode(res[6]))
            ui.lineEdit_Prof.setText(res[7])
            ui.lineEdit_Dir.setText(res[8])
            cursor.execute("select * from Antrop_Nec where an_pid=?",(self.perfil,))
            datos = cursor.fetchone()
            ui.doubleSpin_Peso.setValue(datos[1])
            ui.doubleSpin_Alt.setValue(datos[2])
            ui.doubleSpin_POb.setValue(datos[4])
            ui.doubleSpin_Cad.setValue(datos[5])
            ui.doubleSpin_Cint.setValue(datos[6])
            ui.doubleSpin_Tricip.setValue(datos[7])
            if datos[8] == "Delgada":
                ui.combo_Complex.setCurrentIndex(0)
            elif datos[8] == "Media":
                ui.combo_Complex.setCurrentIndex(1)
            elif datos[8] == "Ancha":
                ui.combo_Complex.setCurrentIndex(2)
            ui.doubleSpin_PPac.setValue(datos[9])
            if datos[11] == "Ligera":
                ui.combo_Activ.setCurrentIndex(0)
            elif datos[11] == "Moderada":
                ui.combo_Activ.setCurrentIndex(1)
            elif datos[11] == "Intensa":
                ui.combo_Activ.setCurrentIndex(2)
            if datos[13] == 6:
                ui.comboBox.setCurrentIndex(0)
            elif datos[13] == 5:
                ui.comboBox.setCurrentIndex(1)
            elif datos[13] == 4:
                ui.comboBox.setCurrentIndex(2)
            elif datos[13] == 3:
                ui.comboBox.setCurrentIndex(3)
            ui.doubleSpin_PMG.setValue(datos[14])
            self.gui.QuitarEnabledP()
            if datos[15] != "":
                ui.toolButton.setStyleSheet("color: red")

            self.uiInfoM.textEdit.setText(datos[15])
            ui.toolButton.setEnabled(True)
            ui.tabWidget.setEnabled(True)
            ui.combo_FM.setEnabled(True)
            ui.lineEdit_Edad.setEnabled(True)
            ui.stackedWidget.setEnabled(True)
            ui.label_6_1.setEnabled(True)
            ui.lineEdit_6_1.setEnabled(True)
            ui.lineEdit_6_2.setEnabled(True)
            ui.lineEdit_6_3.setEnabled(True)
            ui.lineEdit_6_4.setEnabled(True)
            ui.lineEdit_6_5.setEnabled(True)
            ui.lineEdit_6_6.setEnabled(True)
            ui.lineEdit_6_7.setEnabled(True)
            ui.lineEdit_6_8.setEnabled(True)
            ui.lineEdit_6_9.setEnabled(True)
            ui.lineEdit_6_10.setEnabled(True)
            ui.lineEdit_6_11.setEnabled(True)
            ui.lineEdit_6_12.setEnabled(True)
            ui.lineEdit_6_13.setEnabled(True)

            cursor.execute("select * from Trat_Apoyo where ta_pid=?",(self.perfil,))
            res = cursor.fetchall()
            if res != "":
                for i in range(len(res)):
                    item = QtGui.QTreeWidgetItem(ui.treeWidget_tratam,0)
                    item.setText(0,unicode(res[i][1]))
                    item.setText(1,unicode(res[i][2]))
                    item.setText(2,unicode(res[i][3]))
                    item.setText(3,unicode(res[i][4]))
                ui.treeWidget_tratam.sortItems(0,0)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
        
#Conexion accion Cerrar Paciente y boton Aceptar de Ventana Cerrar Paciente
    def CerrarPaciente(self,ui,objetos):
        self.perfil = 0
        ui.combo_FM.setCurrentIndex(0)
        ui.lineEdit_Dni.clear()
        ui.lineEdit_Nom.clear()
        ui.lineEdit_Apell.clear()
        date = QtCore.QDate.fromString("03/10/1950","dd/MM/yyyy")
        ui.date_FNac.setDate(date)
        ui.lineEdit_Edad.clear()
        ui.lineEdit_Tlf.clear()
        ui.lineEdit_Prof.clear()
        ui.lineEdit_Dir.clear()
        ui.doubleSpin_Peso.setValue(0.0)
        ui.doubleSpin_Alt.setValue(0)
        ui.doubleSpin_IMC.setValue(0.0)
        ui.doubleSpin_POb.setValue(0.0)
        ui.doubleSpin_Cad.setValue(0.0)
        ui.doubleSpin_Cint.setValue(0.0)
        ui.doubleSpin_Tricip.setValue(0.0)
        ui.combo_Complex.setCurrentIndex(0)
        ui.combo_Activ.setCurrentIndex(0)
        ui.lineEdit_PIdeal.clear()
        ui.doubleSpin_PPac.setValue(0.0)
        ui.doubleSpin_PMG.setValue(0.0)
        ui.doubleSpin_PL.setValue(0.0)
        ui.doubleSpin_MB.setValue(0.0)
        ui.doubleSpin_Increm.setValue(0.0)
        ui.doubleSpin_Reduc.setValue(0.0)
        ui.doubleSpin_ET.setValue(0.0)
        ui.lineEdit_NG.clear()
        ui.lineEdit_NL.clear()
        ui.lineEdit_NP.clear()
        ui.treeWidget_tratam.clear()
        ui.comboBox.setCurrentIndex(0)
        ui.lineEdit_3.clear()
        ui.lineEdit_4.clear()
        self.gui.PonerEnabledP()
        self.uiInfoM.textEdit.clear() 
        self.uiInfoM.treeWidgetEP.clear()
        self.ClearInfoG()
        self.ClearCuestFrec(objetos)
        ui.toolButton.setStyleSheet("color: grey")
        ui.toolButton.setEnabled(False)
        ui.tabWidget.setEnabled(False)
        ui.stackedWidget.setEnabled(False)
        ui.tabWidget.setCurrentIndex(0)

        ui.lineEdit_6_7.setText("")
        ui.lineEdit_6_8.setText("")
        ui.lineEdit_6_9.setText("")
        ui.lineEdit_6_10.setText("")
        ui.lineEdit_6_11.setText("")
        ui.lineEdit_6_12.setText("")
        ui.lineEdit_6_13.setText("")
        ui.lineEdit_5_6.setText("")
        ui.lineEdit_5_7.setText("")
        ui.lineEdit_5_8.setText("")
        ui.lineEdit_5_9.setText("")
        ui.lineEdit_5_10.setText("")
        ui.lineEdit_5_11.setText("")
        ui.lineEdit_5_12.setText("")
        ui.lineEdit_4_5.setText("")
        ui.lineEdit_4_6.setText("")
        ui.lineEdit_4_7.setText("")
        ui.lineEdit_4_8.setText("")
        ui.lineEdit_4_9.setText("")
        ui.lineEdit_4_10.setText("")
        ui.lineEdit_4_11.setText("")
        ui.lineEdit_3_4.setText("")
        ui.lineEdit_3_5.setText("")
        ui.lineEdit_3_6.setText("")
        ui.lineEdit_3_7.setText("")
        ui.lineEdit_3_8.setText("")
        ui.lineEdit_3_9.setText("")
        ui.lineEdit_3_10.setText("")

        ui.tableWidget_5.clearContents()
        ui.tableWidget_4.clearContents()
        ui.tableWidget_3.clearContents()
        ui.tableWidget_2.clearContents()

#Conexion accion Eliminar Paciente y Ventana Eliminar Paciente
    def EliminarPaciente(self,ui,dietista):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        perfil = dietista.ObtenerPerfil()
        self.uiEP.treeWidget.clear()
        cursor.execute("select p_dni, p_nombre, p_apell from Paciente where p_ddni=?",(perfil,))
        items = cursor.fetchall()
        if items:
            for i in range(len(items)):
                item = QtGui.QTreeWidgetItem(self.uiEP.treeWidget,0)
                nomapell = items[i][1] + " " + items[i][2]
                item.setText(0,nomapell)
                item.setText(1,items[i][0])
                self.uiEP.treeWidget.addTopLevelItem(item)
        self.uiEP.treeWidget.sortItems(0,0)
        I = self.uiEP.treeWidget.itemAt(0,0)
        self.uiEP.treeWidget.setCurrentItem(I)
        self.WindowSuprPac.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion boton Aceptar de Eliminar Paciente y bbdd
    def DropPaciente(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        item = self.uiEP.treeWidget.currentItem()
        column = self.uiEP.treeWidget.currentColumn()
        D = str(self.uiEP.treeWidget.currentItem().text(1))
        cursor.execute("select p_id from Paciente where p_dni=?",(D,))
        id = cursor.fetchone()[0]
        cursor.execute("delete from Antrop_Nec where an_pid=?",(id,))
        cursor.execute("delete from Diario_Diet where dd_pid=?",(id,))
        cursor.execute("delete from Enf_Paciente where epp_pid=?",(id,))
        cursor.execute("delete from Info_General where ig_pid=?",(id,))
        cursor.execute("delete from Paciente where p_dni=?",(D,))
        cursor.execute("delete from Preferencia where pr_pid=?",(id,))
        cursor.execute("delete from Recordatorio where rd_pid=?",(id,))
        cursor.execute("delete from Semanario where s_pid=?",(id,))
        cursor.execute("delete from Trat_Apoyo where ta_pid=?",(id,))
        bbdd.commit()
        self.uiEP.treeWidget.removeItemWidget(item,column)
        self.WindowSuprPac.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Mostrar widget Analisis en Ventana Info Medica
    def MostrarAnalisis(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        perfil = self.perfil
        self.uiInfoM.treeWidget.clear()
        cursor.execute("select a_nombre, a_fch from Analisis where a_pid=?",(perfil,))
        items = cursor.fetchall()
        if items:
            for i in range(len(items)):
                item = QtGui.QTreeWidgetItem(self.uiInfoM.treeWidget,0)
                nombre = items[i][0]
                item.setText(0,nombre)
                item.setText(1,items[i][1])
                self.uiInfoM.treeWidget.addTopLevelItem(item)
        self.uiInfoM.treeWidget.sortItems(0,0)
        I = self.uiInfoM.treeWidget.itemAt(0,0)
        self.uiInfoM.treeWidget.setCurrentItem(I)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Mostrar widget Enfermedades y Patologias en Ventana Info Medica
    def MostrarEnfPaciente(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        self.uiInfoM.treeWidgetEP.clear()
        perfil = self.perfil
        cursor.execute("select epp_epid from Enf_Paciente where epp_pid=?",(perfil,))
        items = cursor.fetchall()
        if items:
            for i in range(len(items)):
                item = QtGui.QTreeWidgetItem(self.uiInfoM.treeWidgetEP,0)
                EPID = items[i][0]
                cursor.execute("select ep_nombre from Enfermedad where ep_id=?",(EPID,))
                res = cursor.fetchone()[0]
                item.setText(0,res)
                self.uiInfoM.treeWidgetEP.addTopLevelItem(item)
        self.uiInfoM.treeWidgetEP.sortItems(0,0)
        I = self.uiInfoM.treeWidgetEP.itemAt(0,0)
        self.uiInfoM.treeWidgetEP.setCurrentItem(I)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion boton Informacion Medica y Ventana Info Med
    def AbrirInfoMed(self):
        self.WindowInfoMed.show()
        self.MostrarAnalisis()
        self.MostrarEnfPaciente()

#Conexion de Anadir Ventana Informacion Medica y dialogo abrir Archivo
    def abrirDialogo(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        abrir = QtGui.QFileDialog()
        ruta = abrir.getOpenFileName(self.WindowInfoMed,"Seleccionar PDF","/home","PDF Files (*.pdf)")
        nombrefile = ruta.split("/")[-1]
        if ruta != "":
            item = QtGui.QTreeWidgetItem(self.uiInfoM.treeWidget,0)
            item.setText(0,nombrefile)
            hoy = datetime.date.today().strftime("%d/%m/%Y")
            item.setText(1,unicode(hoy))
            self.uiInfoM.treeWidget.addTopLevelItem(item)
            self.uiInfoM.treeWidget.sortItems(0,0)
            I = self.uiInfoM.treeWidget.itemAt(0,0)
            self.uiInfoM.treeWidget.setCurrentItem(I)
            perfil = self.perfil
            cursor.execute("select max(a_id) from Analisis")
            res = cursor.fetchone()
            if res[0] == None:
                NUM = 1
            else:
                NUM = res[0]
                NUM = NUM + 1
            valores = (NUM, unicode(ruta), unicode(nombrefile), hoy, perfil,)
            cursor.execute("insert into Analisis values (?,?,?,?,?)",valores)
            bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de Eliminar de Ventana Informacion Medica y treeWidget
    def EliminarAnalitica(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        item = self.uiInfoM.treeWidget.currentItem()
        column = self.uiInfoM.treeWidget.currentColumn()
        if item:
            nombre = item.text(0)
            self.uiInfoM.treeWidget.removeItemWidget(item,column)
            valores = (unicode(nombre), self.perfil,)
            cursor.execute("delete from Analisis where a_nombre=? and a_pid=?", valores)
            bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de Ver Analitica de Ventana Inf Medica y abrir pdf
    def VerAnalitica(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        item = self.uiInfoM.treeWidget.currentItem()
        if item:
            nombre = unicode(item.text(0))
            cursor.execute("select a_ruta from Analisis where a_nombre=?",(nombre,))
            ruta = cursor.fetchone()[0]
            file = "file://" + ruta
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(unicode(file)))
        # , QtCore.QUrl.TolerantMode)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de campo trat farmacologico de Ventana Inf Medica y bbdd
    def GuardarTrat(self, ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        perfil = self.perfil
        FTRAT = unicode(self.uiInfoM.textEdit.toPlainText())
        cursor.execute("select an_infotrat from Antrop_Nec where an_pid=?",(perfil,))
        res = cursor.fetchall()[0][0]
        if res:
            antiguo = res
        else:
            antiguo = ""
        sqliteorden = "update Antrop_Nec set an_infotrat=\"" + FTRAT + "\" where an_infotrat=\"" + antiguo + "\" and an_pid=\"" + unicode(perfil) + "\""
        cursor.execute(sqliteorden)
        bbdd.commit()
        if FTRAT != "":
            ui.toolButton.setStyleSheet("color: red")
        else:
            ui.toolButton.setStyleSheet("color: black")

        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de añadir tratamiento de apoyo y ventana
    def MostrarVentanaTratApoyo(self):
        self.uiNTA.lineEdit_trat.clear()
        self.uiNTA.lineEdit_pos.clear()
        self.uiNTA.lineEdit_obs.clear()
        self.WindowNTratA.show()

#Conexion de GUI Nuevo Tratamiento de Apoyo y treeWidget Trat Apoyo
    def MostrarTratA(self,ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        cursor.execute("select max(ta_id) from Trat_Apoyo")
        res = cursor.fetchone()
        if res[0] == None:
            TAID = 1
        else:
            TAID = res[0] + 1
        trat = self.uiNTA.lineEdit_trat.text()
        pos = self.uiNTA.lineEdit_pos.text()
        obs = self.uiNTA.lineEdit_obs.text()
        hoy = datetime.date.today().strftime("%d/%m/%Y")
        item = QtGui.QTreeWidgetItem(ui.treeWidget_tratam,0)
        item.setText(0,unicode(hoy))
        item.setText(1,unicode(trat))
        item.setText(2,unicode(pos))
        item.setText(3,unicode(obs))
        ui.treeWidget_tratam.addTopLevelItem(item)
        ui.treeWidget_tratam.sortItems(0,0)
        I = ui.treeWidget_tratam.itemAt(0,0)
        ui.treeWidget_tratam.setCurrentItem(I)
        valores = (TAID,hoy,unicode(trat),unicode(pos),unicode(obs),self.perfil,)
        cursor.execute("insert into Trat_Apoyo values (?,?,?,?,?,?)",valores)
        bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
        
#Conexion de treeWidget Trat Apoyo y button Eliminar
    def ElimItem(self,ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        I = ui.treeWidget_tratam.currentItem()
        column = ui.treeWidget_tratam.currentColumn()
        if I:
            TAID = unicode(I.text(1))
            cursor.execute("select ta_id from Trat_Apoyo where ta_trat=? and ta_pid=?",(TAID,self.perfil,))
            res = cursor.fetchone()[0]
            cursor.execute("delete from Trat_Apoyo where ta_id=?",(res,))
            ui.treeWidget_tratam.removeItemWidget(I,column)

        bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion boton añadirEP de Ventana Informacion Medica y Dialogo Enfermedades
    def MostrarVentanaSelEIngr(self, receta):
        receta.MostrarIngred(self.uiNEI, self.WindowNEIngred)
        self.WindowNEIngred.show()

#Conexion boton Nuevo de dialogo Enfermedades y dialogo Nueva Enfermedad
    def MostrarVentanaNEnfermedad(self):
        self.uiNEnfer.lineEdit_Nom.clear()
        self.uiNEnfer.treeWidget.clear()
        self.WindowNEnfer.show()

#Conexion boton Aceptar de Selec Ingredientes de Enfermedades y Dialogo Nueva Enfermedad
    def SeleccionarEnfIngred(self):
        I = self.uiNEI.treeWidget.currentItem()
        column = self.uiNEI.treeWidget.currentColumn()
        if I:
            item = QtGui.QTreeWidgetItem(self.uiNEnfer.treeWidget,0)
            item.setText(0,I.text(0))
            self.uiNEnfer.treeWidget.addTopLevelItem(item)
            self.uiNEnfer.treeWidget.sortItems(0,0)

#Conexion boton Eliminar Dialogo Nueva Enfermedad y treeWidget
#Conexion boton Eliminar Dialogo Enfermedades y treeWidget
    def EliminarIngredEnf(self,ui):
        I = ui.treeWidget.currentItem()
        column = ui.treeWidget.currentColumn()
        if I:
            ui.treeWidget.removeItemWidget(I,column)

    def ElimEnfBBDD(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        I = self.uiEnfer.treeWidget.currentItem()
        if I:
            ENF = unicode(I.text(0))
            cursor.execute("select ep_id from Enfermedad where ep_nombre=?",(ENF,))
            EPID = cursor.fetchone()[0]
            cursor.execute("delete from Enfermedad where ep_id=?",(EPID,))
            cursor.execute("delete from Enf_Paciente where epp_epid=?",(EPID,))
            bbdd.commit()
        self.MostrarEnfPaciente()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()            

#Conexion boton Aceptar de Nueva Enfermedad y dialogo Enfermedades
    def CrearEnfermedad(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        item = QtGui.QTreeWidgetItem(self.uiEnfer.treeWidget,0)
        NOM = self.uiNEnfer.lineEdit_Nom.text()
        item.setText(0,NOM)
        cursor.execute("select max(ep_id) from Enfermedad")
        res = cursor.fetchone()
        if res[0] == None:
            NUM = 1
        else:
            NUM = res[0]
            NUM = NUM + 1
        valores = (NUM, unicode(NOM),)
        cursor.execute("insert into Enfermedad values (?,?)",valores)
        bbdd.commit()
        #Inserccion de treeWidget de Nueva Receta en Receta_Ingredientes
        I = self.uiNEnfer.treeWidget.itemAt(0,0)
        while I:
            self.uiNEnfer.treeWidget.setCurrentItem(I)
            ING = unicode(self.uiNEnfer.treeWidget.currentItem().text(0))
            cursor.execute("select i_id from Ingrediente where i_nombre=?", (ING,))
            I_ID = cursor.fetchone()[0]
            cursor.execute("select max(ei_id) from Enf_Ingred")
            res = cursor.fetchone()
            if res[0] == None:
                NUM_EI = 1
            else:
                NUM_EI = res[0]
                NUM_EI = NUM_EI + 1
            cursor.execute("insert into Enf_Ingred values (?,?,?)",(NUM_EI,NUM,I_ID,))
            I = self.uiNEnfer.treeWidget.itemBelow(I)
        bbdd.commit()
        self.uiEnfer.treeWidget.addTopLevelItem(item)
        self.uiEnfer.treeWidget.sortItems(0,0)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
        
#Conexion boton Aceptar de Enfermedad y dialogo Enfermedades de InfoMed
    def AnadirEnfermedad(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        I = self.uiEnfer.treeWidget.currentItem()
        column = self.uiEnfer.treeWidget.currentColumn()
        perfil = self.perfil
        cursor.execute("select max(epp_id) from Enf_Paciente")
        res = cursor.fetchone()
        if res[0] == None:
            NUM = 1
        else:
            NUM = res[0]
            NUM = NUM + 1
        if I:
            item = QtGui.QTreeWidgetItem(self.uiInfoM.treeWidgetEP,0)
            ENF = unicode(I.text(0))
            item.setText(0,ENF)
            cursor.execute("select ep_id from Enfermedad where ep_nombre=?",(ENF,))
            res = cursor.fetchone()
            valores = (NUM,perfil,res[0],)
            cursor.execute("insert into Enf_Paciente values (?,?,?)", valores)
            bbdd.commit()
            self.uiInfoM.treeWidgetEP.addTopLevelItem(item)
            self.uiInfoM.treeWidgetEP.sortItems(0,0)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion boton Eliminar Dialogo InfoM de Enfermedades y treeWidgetEP
    def EliminarEP(self,ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        I = ui.treeWidgetEP.currentItem()
        column = ui.treeWidgetEP.currentColumn()
        perfil = self.perfil
        if I:
            ui.treeWidgetEP.removeItemWidget(I,column)
            nombre = unicode(I.text(0))
            cursor.execute("select ep_id from Enfermedad where ep_nombre=?",(nombre,))
            res = cursor.fetchone()
            if res[0]:
                EPID = res[0]
                cursor.execute("delete from Enf_Paciente where epp_pid=? and epp_epid=?",(perfil,EPID,))
            bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion boton añadirEP de Ventana Informacion Medica y Dialogo Enfermedades
    def MostrarListadoEnf(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        self.uiEnfer.treeWidget.clear()
        cursor.execute("select ep_nombre from Enfermedad")
        items = cursor.fetchall()
        if items:
            for i in range(len(items)):
                item = QtGui.QTreeWidgetItem(self.uiEnfer.treeWidget,0)
                nombre = items[i][0]
                item.setText(0,nombre)
                self.uiEnfer.treeWidget.addTopLevelItem(item)
        self.uiEnfer.treeWidget.sortItems(0,0)
        I = self.uiEnfer.treeWidget.itemAt(0,0)
        self.uiEnfer.treeWidget.setCurrentItem(I)
        self.WindowEnfer.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de boton Aceptar de InfoTrat y filtrado de recetas
    def ExcluirRecetasEnf(self,dietista,receta,ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        receta.MostrarRecetas(dietista,ui)
        perfil = self.perfil
        dietist = dietista.ObtenerPerfil()
        cursor.execute("select epp_epid from Enf_Paciente where epp_pid=?",(perfil,))
        items = cursor.fetchall()
        if items:
            for i in range(len(items)):
                nombre = items[i][0]
                cursor.execute("select ei_iid from Enf_Ingred where ei_epid=?",(nombre,))
                ingreds = cursor.fetchall()
                if ingreds:
                    for j in range(len(ingreds)):
                        ingr_id = ingreds[j][0]
                        cursor.execute("select i_nombre from Ingrediente where i_id=?",(ingr_id,))
                        ingr = cursor.fetchone()[0]
                        cursor.execute("select ri_nomrec from Receta_Ingredientes where ri_ddni=? and ri_nomingr=?",(dietist,ingr,))
                        rcts = cursor.fetchall()
                        if rcts:
                            for k in range(len(rcts)):
                                rct = rcts[k][0]
                                if rct:
                                    I = ui.treeWidget.itemAt(0,0)
                                    column = ui.treeWidget.currentColumn()
                                    while I:
                                        nhijos = I.childCount() -1
                                        while nhijos != -1:
                                            if I.child(nhijos).text(0) == rct:
                                                ui.treeWidget.removeItemWidget(I.child(nhijos),column)
                                            nhijos = nhijos-1
                                        I = ui.treeWidget.itemBelow(I)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
        
#Conexion de boton Aceptar de InfoGen y bbdd
    def GuardarInfoG(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta y modificacion en la bbdd
        perfil = self.perfil
        cursor.execute("select ig_id from Info_General where ig_pid=?",(perfil,))
        res = cursor.fetchone()[0]
        tabla_0 = self.uiInfoG.tableWidget.item(0,0).text()
        tabla_1 = self.uiInfoG.tableWidget.item(1,0).text()
        tabla_2 = self.uiInfoG.tableWidget.item(2,0).text()
        tabla_3 = self.uiInfoG.tableWidget.item(3,0).text()

        tabla2_0 = self.uiInfoG.tableWidget_2.item(0,0).text()
        tabla2_1 = self.uiInfoG.tableWidget_2.item(1,0).text()
        tabla2_2 = self.uiInfoG.tableWidget_2.item(2,0).text()
        tabla2_3 = self.uiInfoG.tableWidget_2.item(3,0).text()

        tabla3_0 = self.uiInfoG.tableWidget_3.item(0,0).text()
        tabla3_1 = self.uiInfoG.tableWidget_3.item(1,0).text()
        tabla3_2 = self.uiInfoG.tableWidget_3.item(2,0).text()

        tabla4_0 = self.uiInfoG.tableWidget_4.item(0,0).text()
        tabla4_1 = self.uiInfoG.tableWidget_4.item(1,0).text()
        tabla4_2 = self.uiInfoG.tableWidget_4.item(2,0).text()
        tabla4_3 = self.uiInfoG.tableWidget_4.item(3,0).text()
        tabla4_4 = self.uiInfoG.tableWidget_4.item(4,0).text()
        tabla4_5 = self.uiInfoG.tableWidget_4.item(5,0).text()

        tabla5_0 = self.uiInfoG.tableWidget_5.item(0,0).text()
        tabla5_1 = self.uiInfoG.tableWidget_5.item(1,0).text()
        tabla5_2 = self.uiInfoG.tableWidget_5.item(2,0).text()

        tabla6_0 = self.uiInfoG.tableWidget_6.item(0,0).text()
        tabla6_1 = self.uiInfoG.tableWidget_6.item(1,0).text()

        tabla7_0 = self.uiInfoG.tableWidget_7.item(0,0).text()
        tabla7_1 = self.uiInfoG.tableWidget_7.item(1,0).text()
        tabla7_2 = self.uiInfoG.tableWidget_7.item(2,0).text()

        tabla8_0 = self.uiInfoG.tableWidget_8.item(0,0).text()
        tabla8_1 = self.uiInfoG.tableWidget_8.item(1,0).text()
        tabla8_2 = self.uiInfoG.tableWidget_8.item(2,0).text()

        tabla9_0 = self.uiInfoG.tableWidget_9.item(0,0).text()
        tabla9_1 = self.uiInfoG.tableWidget_9.item(1,0).text()
        tabla9_2 = self.uiInfoG.tableWidget_9.item(2,0).text()
        tabla9_2 = self.uiInfoG.tableWidget_9.item(3,0).text()

        tabla10_0 = self.uiInfoG.tableWidget_10.item(0,0).text()
        tabla10_1 = self.uiInfoG.tableWidget_10.item(1,0).text()
        tabla10_2 = self.uiInfoG.tableWidget_10.item(2,0).text()

        tabla11_0 = self.uiInfoG.tableWidget_11.item(0,0).text()
        tabla11_1 = self.uiInfoG.tableWidget_11.item(1,0).text()

        tabla12_0 = self.uiInfoG.tableWidget_12.item(0,0).text()
        tabla12_1 = self.uiInfoG.tableWidget_12.item(1,0).text()
        tabla12_1 = self.uiInfoG.tableWidget_12.item(2,0).text()
        
        valores = (res,unicode(tabla_0),unicode(tabla_1),unicode(tabla_2),unicode(tabla_3),unicode(tabla2_0),unicode(tabla2_1),unicode(tabla2_2),unicode(tabla2_3),unicode(tabla3_0),unicode(tabla3_1),unicode(tabla3_2),unicode(tabla4_0),unicode(tabla4_1),unicode(tabla4_2),unicode(tabla4_3),unicode(tabla4_4),unicode(tabla4_5),unicode(tabla5_0),unicode(tabla5_1),unicode(tabla5_2),unicode(tabla6_0),unicode(tabla6_1),unicode(tabla7_0),unicode(tabla7_1),unicode(tabla7_2),unicode(tabla8_0),unicode(tabla8_1),unicode(tabla8_2),unicode(tabla9_0),unicode(tabla9_1),unicode(tabla9_2),unicode(tabla9_2),unicode(tabla10_0),unicode(tabla10_1),unicode(tabla10_2),unicode(tabla11_0),unicode(tabla11_1),unicode(tabla12_0),unicode(tabla12_1),unicode(tabla12_1),perfil,)

        cursor.execute("delete from Info_General where ig_id=?",(res,))
        cursor.execute("insert into Info_General values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",valores)
        # self.uiInfoG.tableWidget.item(3,0).setText(hola)
        bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de accion Cerrar Paciente y clear de Ventana Info_General
    def ClearInfoG(self):
        self.uiInfoG.tableWidget.item(0,0).setText("")
        self.uiInfoG.tableWidget.item(1,0).setText("")
        self.uiInfoG.tableWidget.item(2,0).setText("")
        self.uiInfoG.tableWidget.item(3,0).setText("")
        self.uiInfoG.tableWidget_2.item(0,0).setText("")
        self.uiInfoG.tableWidget_2.item(1,0).setText("")
        self.uiInfoG.tableWidget_2.item(2,0).setText("")
        self.uiInfoG.tableWidget_2.item(3,0).setText("")
        self.uiInfoG.tableWidget_3.item(0,0).setText("")
        self.uiInfoG.tableWidget_3.item(1,0).setText("")
        self.uiInfoG.tableWidget_3.item(2,0).setText("")
        self.uiInfoG.tableWidget_4.item(0,0).setText("")
        self.uiInfoG.tableWidget_4.item(1,0).setText("")
        self.uiInfoG.tableWidget_4.item(2,0).setText("")
        self.uiInfoG.tableWidget_4.item(3,0).setText("")
        self.uiInfoG.tableWidget_4.item(4,0).setText("")
        self.uiInfoG.tableWidget_4.item(5,0).setText("")
        self.uiInfoG.tableWidget_5.item(0,0).setText("")
        self.uiInfoG.tableWidget_5.item(1,0).setText("")
        self.uiInfoG.tableWidget_5.item(2,0).setText("")
        self.uiInfoG.tableWidget_6.item(0,0).setText("")
        self.uiInfoG.tableWidget_6.item(1,0).setText("")
        self.uiInfoG.tableWidget_7.item(0,0).setText("")
        self.uiInfoG.tableWidget_7.item(1,0).setText("")
        self.uiInfoG.tableWidget_7.item(2,0).setText("")
        self.uiInfoG.tableWidget_8.item(0,0).setText("")
        self.uiInfoG.tableWidget_8.item(1,0).setText("")
        self.uiInfoG.tableWidget_8.item(2,0).setText("")
        self.uiInfoG.tableWidget_9.item(0,0).setText("")
        self.uiInfoG.tableWidget_9.item(1,0).setText("")
        self.uiInfoG.tableWidget_9.item(2,0).setText("")
        self.uiInfoG.tableWidget_9.item(3,0).setText("")
        self.uiInfoG.tableWidget_10.item(0,0).setText("")
        self.uiInfoG.tableWidget_10.item(1,0).setText("")
        self.uiInfoG.tableWidget_10.item(2,0).setText("")
        self.uiInfoG.tableWidget_11.item(0,0).setText("")
        self.uiInfoG.tableWidget_11.item(1,0).setText("")
        self.uiInfoG.tableWidget_12.item(0,0).setText("")
        self.uiInfoG.tableWidget_12.item(1,0).setText("")
        self.uiInfoG.tableWidget_12.item(2,0).setText("")

#Conexion de boton Informacion General de mainWindow y Ventana Info General
    def MostrarInfoGen(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        self.ClearInfoG()
        perfil = self.perfil
        cursor.execute("select * from Info_General where ig_pid=?",(perfil,))
        items = cursor.fetchall()
        if items:
            self.uiInfoG.tableWidget.item(0,0).setText(items[0][1])
            self.uiInfoG.tableWidget.item(1,0).setText(items[0][2])
            self.uiInfoG.tableWidget.item(2,0).setText(items[0][3])
            self.uiInfoG.tableWidget.item(3,0).setText(items[0][4])
            self.uiInfoG.tableWidget_2.item(0,0).setText(items[0][5])
            self.uiInfoG.tableWidget_2.item(1,0).setText(items[0][6])
            self.uiInfoG.tableWidget_2.item(2,0).setText(items[0][7])
            self.uiInfoG.tableWidget_2.item(3,0).setText(items[0][8])
            self.uiInfoG.tableWidget_3.item(0,0).setText(items[0][9])
            self.uiInfoG.tableWidget_3.item(1,0).setText(items[0][10])
            self.uiInfoG.tableWidget_3.item(2,0).setText(items[0][11])
            self.uiInfoG.tableWidget_4.item(0,0).setText(items[0][12])
            self.uiInfoG.tableWidget_4.item(1,0).setText(items[0][13])
            self.uiInfoG.tableWidget_4.item(2,0).setText(items[0][14])
            self.uiInfoG.tableWidget_4.item(3,0).setText(items[0][15])
            self.uiInfoG.tableWidget_4.item(4,0).setText(items[0][16])
            self.uiInfoG.tableWidget_4.item(5,0).setText(items[0][17])
            self.uiInfoG.tableWidget_5.item(0,0).setText(items[0][18])
            self.uiInfoG.tableWidget_5.item(1,0).setText(items[0][19])
            self.uiInfoG.tableWidget_5.item(2,0).setText(items[0][20])
            self.uiInfoG.tableWidget_6.item(0,0).setText(items[0][21])
            self.uiInfoG.tableWidget_6.item(1,0).setText(items[0][22])
            self.uiInfoG.tableWidget_7.item(0,0).setText(items[0][23])
            self.uiInfoG.tableWidget_7.item(1,0).setText(items[0][24])
            self.uiInfoG.tableWidget_7.item(2,0).setText(items[0][25])
            self.uiInfoG.tableWidget_8.item(0,0).setText(items[0][26])
            self.uiInfoG.tableWidget_8.item(1,0).setText(items[0][27])
            self.uiInfoG.tableWidget_8.item(2,0).setText(items[0][28])
            self.uiInfoG.tableWidget_9.item(0,0).setText(items[0][29])
            self.uiInfoG.tableWidget_9.item(1,0).setText(items[0][30])
            self.uiInfoG.tableWidget_9.item(2,0).setText(items[0][31])
            self.uiInfoG.tableWidget_9.item(3,0).setText(items[0][32])
            self.uiInfoG.tableWidget_10.item(0,0).setText(items[0][33])
            self.uiInfoG.tableWidget_10.item(1,0).setText(items[0][34])
            self.uiInfoG.tableWidget_10.item(2,0).setText(items[0][35])
            self.uiInfoG.tableWidget_11.item(0,0).setText(items[0][36])
            self.uiInfoG.tableWidget_11.item(1,0).setText(items[0][37])
            self.uiInfoG.tableWidget_12.item(0,0).setText(items[0][38])
            self.uiInfoG.tableWidget_12.item(1,0).setText(items[0][39])
            self.uiInfoG.tableWidget_12.item(2,0).setText(items[0][40])
            
        self.WindowInfoGen.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Mostrar widget Diario Dietetico en Ventana Diario Dietetico
    def MostrarDiario(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        perfil = self.perfil
        self.uiDiarioD.treeWidget.clear()
        cursor.execute("select dd_nombre, dd_fch from Diario_Diet where dd_pid=?",(perfil,))
        items = cursor.fetchall()
        if items:
            for i in range(len(items)):
                item = QtGui.QTreeWidgetItem(self.uiDiarioD.treeWidget,0)
                nombre = items[i][0]
                item.setText(0,nombre)
                item.setText(1,items[i][1])
                self.uiDiarioD.treeWidget.addTopLevelItem(item)
        self.uiDiarioD.treeWidget.sortItems(0,0)
        I = self.uiDiarioD.treeWidget.itemAt(0,0)
        self.uiDiarioD.treeWidget.setCurrentItem(I)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion boton Diario Dietetico y Ventana Diario Diet
    def AbrirDiarioDiet(self):
        self.WindowDiarioD.show()
        self.MostrarDiario()

#Conexion de Anadir Ventana Diario Dietetico y dialogo abrir Archivo
    def abrirDialogoD(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        abrir = QtGui.QFileDialog()
        ruta = abrir.getOpenFileName(self.WindowDiarioD,"Seleccionar PDF","/home","PDF Files (*.pdf)")
        nombrefile = ruta.split("/")[-1]
        if ruta != "":
            item = QtGui.QTreeWidgetItem(self.uiDiarioD.treeWidget,0)
            item.setText(0,nombrefile)
            hoy = datetime.date.today().strftime("%d/%m/%Y")
            item.setText(1,unicode(hoy))
            self.uiDiarioD.treeWidget.addTopLevelItem(item)
            self.uiDiarioD.treeWidget.sortItems(0,0)
            I = self.uiDiarioD.treeWidget.itemAt(0,0)
            self.uiDiarioD.treeWidget.setCurrentItem(I)
            perfil = self.perfil
            cursor.execute("select max(dd_id) from Diario_Diet")
            res = cursor.fetchone()
            if res[0] == None:
                NUM = 1
            else:
                NUM = res[0]
                NUM = NUM + 1
            valores = (NUM, unicode(ruta), unicode(nombrefile), hoy, perfil,)
            cursor.execute("insert into Diario_Diet values (?,?,?,?,?)",valores)
            bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de Eliminar de Ventana Diario Dietetico y treeWidget
    def EliminarDiario(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        item = self.uiDiarioD.treeWidget.currentItem()
        column = self.uiDiarioD.treeWidget.currentColumn()
        if item:
            nombre = item.text(0)
            self.uiDiarioD.treeWidget.removeItemWidget(item,column)
            valores = (unicode(nombre), self.perfil,)
            cursor.execute("delete from Diario_Diet where dd_nombre=? and dd_pid=?", valores)
            bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de Ver Diario de Ventana Diario Dietetico y abrir pdf
    def VerDiario(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        item = self.uiDiarioD.treeWidget.currentItem()
        if item:
            nombre = unicode(item.text(0))
            cursor.execute("select dd_ruta from Diario_Diet where dd_nombre=?",(nombre,))
            ruta = cursor.fetchone()[0]
            file = "file://" + ruta
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(unicode(file)))
        # , QtCore.QUrl.TolerantMode)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Mostrar widget Recordatorio en Ventana Recordatorio
    def MostrarRecordatorio(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        perfil = self.perfil
        self.uiRecordatorio.treeWidget.clear()
        cursor.execute("select rd_nombre, rd_fch from Recordatorio where rd_pid=?",(perfil,))
        items = cursor.fetchall()
        if items:
            for i in range(len(items)):
                item = QtGui.QTreeWidgetItem(self.uiRecordatorio.treeWidget,0)
                nombre = items[i][0]
                item.setText(0,nombre)
                item.setText(1,items[i][1])
                self.uiRecordatorio.treeWidget.addTopLevelItem(item)
        self.uiRecordatorio.treeWidget.sortItems(0,0)
        I = self.uiRecordatorio.treeWidget.itemAt(0,0)
        self.uiRecordatorio.treeWidget.setCurrentItem(I)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion boton Recordatorio 24h y Ventana Recordatorio
    def AbrirRecordatorio(self):
        self.uiRecordatorio.label.setText("Recordatorio 24h.:")
        self.uiRecordatorio.pushButton_Ver.setText("Ver Recordatorio")
        self.uiRecordatorio.pushButton_Ver.setGeometry(QtCore.QRect(480, 170, 131, 23))
        self.uiRecordatorio.pushButton_Form.setGeometry(QtCore.QRect(370, 170, 91, 23))
        self.WindowRecordatorio.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Recordatorio 24 h.", None, QtGui.QApplication.UnicodeUTF8))
        self.WindowRecordatorio.show()
        self.MostrarRecordatorio()

#Conexion de Anadir Ventana Recordatorio y dialogo abrir Archivo
    def abrirDialogoR(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        abrir = QtGui.QFileDialog()
        ruta = abrir.getOpenFileName(self.WindowRecordatorio,"Seleccionar PDF","/home","PDF Files (*.pdf)")
        nombrefile = ruta.split("/")[-1]
        if ruta != "":
            item = QtGui.QTreeWidgetItem(self.uiRecordatorio.treeWidget,0)
            item.setText(0,nombrefile)
            hoy = datetime.date.today().strftime("%d/%m/%Y")
            item.setText(1,unicode(hoy))
            self.uiRecordatorio.treeWidget.addTopLevelItem(item)
            self.uiRecordatorio.treeWidget.sortItems(0,0)
            I = self.uiRecordatorio.treeWidget.itemAt(0,0)
            self.uiRecordatorio.treeWidget.setCurrentItem(I)
            perfil = self.perfil
            cursor.execute("select max(rd_id) from Recordatorio")
            res = cursor.fetchone()
            if res[0] == None:
                NUM = 1
            else:
                NUM = res[0]
                NUM = NUM + 1
            valores = (NUM, unicode(ruta), unicode(nombrefile), hoy, perfil,)
            cursor.execute("insert into Recordatorio values (?,?,?,?,?)",valores)
            bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de Eliminar de Ventana Recordatorio y treeWidget
    def EliminarRecordatorio(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        item = self.uiRecordatorio.treeWidget.currentItem()
        column = self.uiRecordatorio.treeWidget.currentColumn()
        if item:
            nombre = item.text(0)
            self.uiRecordatorio.treeWidget.removeItemWidget(item,column)
            valores = (unicode(nombre), self.perfil,)
            cursor.execute("delete from Recordatorio where rd_nombre=? and rd_pid=?", valores)
            bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de Ver Recordatorio de Ventana Recordatorio y abrir pdf
    def VerRecordatorio(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        item = self.uiRecordatorio.treeWidget.currentItem()
        if item:
            nombre = unicode(item.text(0))
            cursor.execute("select rd_ruta from Recordatorio where rd_nombre=?",(nombre,))
            ruta = cursor.fetchone()[0]
            file = "file://" + ruta
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(unicode(file)))
        # , QtCore.QUrl.TolerantMode)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de Formulario de Ventana Recordatorio e imprimir pdf
    def ImprimirRecordatorio(self):
        #Utilizamos poppler, puesto que qt no soporta nativamente pdf
        ruta = os.getcwd()
        ruta = ruta + "/Docu/recordatorio.pdf"
        printer = QtGui.QPrinter()
        dialog = QtGui.QPrintDialog(printer)
        document = popplerqt4.Poppler.Document.load(ruta)

        if (dialog.exec_() == 1):
            painter = QtGui.QPainter(printer)
            npage = 0
            while npage < 2: 
                img = document.page(npage).renderToImage(100,100)
                painter.drawImage(QtCore.QPoint(0,0),img)
                if npage < 1:
                    printer.newPage()
                npage = npage + 1
            painter.end()

#Conexion de Formulario de Ventana Diario Dietetico e imprimir pdf
    def ImprimirDiarioD(self):
        #Utilizamos poppler, puesto que qt no soporta nativamente pdf
        ruta = os.getcwd()
        ruta = ruta + "/Docu/diario_dietetico.pdf"
        printer = QtGui.QPrinter()
        dialog = QtGui.QPrintDialog(printer)
        document = popplerqt4.Poppler.Document.load(ruta)

        if (dialog.exec_() == 1):
            painter = QtGui.QPainter(printer)
            npage = 0
            while npage < 7: 
                img = document.page(npage).renderToImage(100,100)
                painter.drawImage(QtCore.QPoint(0,0),img)
                if npage < 6:
                    printer.newPage()
                npage = npage + 1
            painter.end()


#Conexion de Cerrar Paciente y borrar datos Cuestionario de Frecuencia
    def ClearCuestFrec(self,objetos):
        objetos.objetosGrupo1 = []
        objetos.objetosGrupo2 = []
        objetos.objetosGrupo3 = []
        objetos.objetosGrupo4 = []
        objetos.objetosGrupo5 = []

#Conexion de boton Cuestionario de Frecuencia y Ventana Cuestionario de Frec
    def MostrarPreferencias(self, objetos, ingrediente):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta de la bbdd
        cursor.execute("select * from Preferencia where pr_pid=?",(self.perfil,))
        res = cursor.fetchall()
        if res:
            j = 0
            k = 0
            z = 0
            tipo = "Grasas y Aceites"
            cursor.execute("select count(i_id) from Ingrediente where i_tipo=?",(tipo,))
            contador1 = cursor.fetchone()[0]
            for i in range(contador1):
                #Para Grupo1 - Grasas y Aceites
                if j < len(objetos.objetosGrupo1):
                    cursor.execute("select i_nombre from Ingrediente where i_id=?",(res[i][1],))
                    result = cursor.fetchone()
                    if result != None:
                        if unicode(result[0]) == unicode(objetos.objetosGrupo1[j].text()):
                            objetos.objetosGrupo1[j+1].setText(unicode(res[k][z+2]))
                            objetos.objetosGrupo1[j+2].setText(unicode(res[k][z+3]))
                            objetos.objetosGrupo1[j+3].setText(unicode(res[k][z+4]))
                            if res[k][z+5] == 1:
                                objetos.objetosGrupo1[j+4].setChecked(True)
                            elif res[k][z+5] == 2:
                                objetos.objetosGrupo1[j+5].setChecked(True)
                            elif res[k][z+5] == 3:
                                objetos.objetosGrupo1[j+6].setChecked(True)
                            elif res[k][z+5] == 4:
                                objetos.objetosGrupo1[j+7].setChecked(True)
                            elif res[k][z+5] == 5:
                                objetos.objetosGrupo1[j+8].setChecked(True)
                
                    j += 9
                    k += 1
                    z = 0
            #------------------------------------------------------------
            #Para Grupo2 - Farinaceos
            j = 0
            cont = contador1 
            k = cont
            z = 0
            tipo = "Farinaceos"
            cursor.execute("select count(i_id) from Ingrediente where i_tipo=?",(tipo,))
            contador2 = cursor.fetchone()[0]
            for i in range(contador2):
                if j < len(objetos.objetosGrupo2):
                    cursor.execute("select i_nombre from Ingrediente where i_id=?",(res[i+cont][1],))
                    result = cursor.fetchone()
                    if result != None:
                        if unicode(result[0]) == unicode(objetos.objetosGrupo2[j].text()):
                            objetos.objetosGrupo2[j+1].setText(unicode(res[k][z+2]))
                            objetos.objetosGrupo2[j+2].setText(unicode(res[k][z+3]))
                            objetos.objetosGrupo2[j+3].setText(unicode(res[k][z+4]))
                            if res[k][z+5] == 1:
                                objetos.objetosGrupo2[j+4].setChecked(True)
                            elif res[k][z+5] == 2:
                                objetos.objetosGrupo2[j+5].setChecked(True)
                            elif res[k][z+5] == 3:
                                objetos.objetosGrupo2[j+6].setChecked(True)
                            elif res[k][z+5] == 4:
                                objetos.objetosGrupo2[j+7].setChecked(True)
                            elif res[k][z+5] == 5:
                                objetos.objetosGrupo2[j+8].setChecked(True)
                
                    j += 9
                    k += 1
                    z = 0
            #--------------------------------------------------------
            #Para Grupo3 - Proteinicos
            j = 0
            cont = contador1+contador2 
            k = cont
            z = 0
            tipo = "Proteinicos"
            cursor.execute("select count(i_id) from Ingrediente where i_tipo=?",(tipo,))
            contador3 = cursor.fetchone()[0]
            for i in range(contador3):
                if j < len(objetos.objetosGrupo3):
                    cursor.execute("select i_nombre from Ingrediente where i_id=?",(res[i+cont][1],))
                    result = cursor.fetchone()
                    if result != None:
                        if unicode(result[0]) == unicode(objetos.objetosGrupo3[j].text()):
                            objetos.objetosGrupo3[j+1].setText(unicode(res[k][z+2]))
                            objetos.objetosGrupo3[j+2].setText(unicode(res[k][z+3]))
                            objetos.objetosGrupo3[j+3].setText(unicode(res[k][z+4]))
                            if res[k][z+5] == 1:
                                objetos.objetosGrupo3[j+4].setChecked(True)
                            elif res[k][z+5] == 2:
                                objetos.objetosGrupo3[j+5].setChecked(True)
                            elif res[k][z+5] == 3:
                                objetos.objetosGrupo3[j+6].setChecked(True)
                            elif res[k][z+5] == 4:
                                objetos.objetosGrupo3[j+7].setChecked(True)
                            elif res[k][z+5] == 5:
                                objetos.objetosGrupo3[j+8].setChecked(True)
                
                    j += 9
                    k += 1
                    z = 0
            #-------------------------------------------------------
            # #Para Grupo4 - Lacteos
            j = 0
            cont = contador1+contador2+contador3 
            k = cont
            z = 0
            tipo = "Lacteos"
            cursor.execute("select count(i_id) from Ingrediente where i_tipo=?",(tipo,))
            contador4 = cursor.fetchone()[0]
            for i in range(contador4):
                if j < len(objetos.objetosGrupo4):
                    cursor.execute("select i_nombre from Ingrediente where i_id=?",(res[i+cont][1],))
                    result = cursor.fetchone()
                    if result != None:
                        if unicode(result[0]) == unicode(objetos.objetosGrupo4[j].text()):
                            objetos.objetosGrupo4[j+1].setText(unicode(res[k][z+2]))
                            objetos.objetosGrupo4[j+2].setText(unicode(res[k][z+3]))
                            objetos.objetosGrupo4[j+3].setText(unicode(res[k][z+4]))
                            if res[k][z+5] == 1:
                                objetos.objetosGrupo4[j+4].setChecked(True)
                            elif res[k][z+5] == 2:
                                objetos.objetosGrupo4[j+5].setChecked(True)
                            elif res[k][z+5] == 3:
                                objetos.objetosGrupo4[j+6].setChecked(True)
                            elif res[k][z+5] == 4:
                                objetos.objetosGrupo4[j+7].setChecked(True)
                            elif res[k][z+5] == 5:
                                objetos.objetosGrupo4[j+8].setChecked(True)
                
                    j += 9
                    k += 1
                    z = 0
            #-----------------------------------------------------------
            #Para Grupo5 - Frutas y Verduras
            j = 0
            cont = contador1+contador2+contador3+contador4 
            k = cont
            z = 0
            tipo = "Frutas y Verduras"
            cursor.execute("select count(i_id) from Ingrediente where i_tipo=?",(tipo,))
            contador5 = cursor.fetchone()[0]
            for i in range(contador5):
                if j < len(objetos.objetosGrupo5):
                    cursor.execute("select i_nombre from Ingrediente where i_id=?",(res[i+cont][1],))
                    result = cursor.fetchone()
                    if result != None:
                        if unicode(result[0]) == unicode(objetos.objetosGrupo5[j].text()):
                            objetos.objetosGrupo5[j+1].setText(unicode(res[k][z+2]))
                            objetos.objetosGrupo5[j+2].setText(unicode(res[k][z+3]))
                            objetos.objetosGrupo5[j+3].setText(unicode(res[k][z+4]))
                            if res[k][z+5] == 1:
                                objetos.objetosGrupo5[j+4].setChecked(True)
                            elif res[k][z+5] == 2:
                                objetos.objetosGrupo5[j+5].setChecked(True)
                            elif res[k][z+5] == 3:
                                objetos.objetosGrupo5[j+6].setChecked(True)
                            elif res[k][z+5] == 4:
                                objetos.objetosGrupo5[j+7].setChecked(True)
                            elif res[k][z+5] == 5:
                                objetos.objetosGrupo5[j+8].setChecked(True)
                            
                    j += 9
                    k += 1
                    z = 0

            #-----------------------------------------------------------
        #Para copiar datos de ingrediente lista si ha añadido ingrediente nuevo
        else:
            for i in range(len(ingrediente.lista)):
                if ingrediente.lista[i][5] == self.perfil:
                    for j in range(len(objetos.objetosGrupo1)-8):
                        cursor.execute("select i_nombre from Ingrediente where i_id=?",(ingrediente.lista[i][0],))
                        result = cursor.fetchone() 
                        if result != None:
                            if unicode(result[0]) == unicode(objetos.objetosGrupo1[j].text()):
                                objetos.objetosGrupo1[j+1].setText(unicode(ingrediente.lista[i][1]))
                                objetos.objetosGrupo1[j+2].setText(unicode(ingrediente.lista[i][2]))
                                objetos.objetosGrupo1[j+3].setText(unicode(ingrediente.lista[i][3]))
                                if ingrediente.lista[i][4] == 1:
                                    objetos.objetosGrupo1[j+4].setChecked(True)
                                elif ingrediente.lista[i][4] == 2:
                                    objetos.objetosGrupo1[j+5].setChecked(True)
                                elif ingrediente.lista[i][4] == 3:
                                    objetos.objetosGrupo1[j+6].setChecked(True)
                                elif ingrediente.lista[i][4] == 4:
                                    objetos.objetosGrupo1[j+7].setChecked(True)
                                elif ingrediente.lista[i][4] == 5:
                                    objetos.objetosGrupo1[j+8].setChecked(True)
                    for j in range(len(objetos.objetosGrupo2)-8):
                        cursor.execute("select i_nombre from Ingrediente where i_id=?",(ingrediente.lista[i][0],))
                        result = cursor.fetchone()
                        if result != None:
                            if unicode(result[0]) == unicode(objetos.objetosGrupo2[j].text()):
                                objetos.objetosGrupo2[j+1].setText(unicode(ingrediente.lista[i][1]))
                                objetos.objetosGrupo2[j+2].setText(unicode(ingrediente.lista[i][2]))
                                objetos.objetosGrupo2[j+3].setText(unicode(ingrediente.lista[i][3]))
                                if ingrediente.lista[i][4] == 1:
                                    objetos.objetosGrupo2[j+4].setChecked(True)
                                elif ingrediente.lista[i][4] == 2:
                                    objetos.objetosGrupo2[j+5].setChecked(True)
                                elif ingrediente.lista[i][4] == 3:
                                    objetos.objetosGrupo2[j+6].setChecked(True)
                                elif ingrediente.lista[i][4] == 4:
                                    objetos.objetosGrupo2[j+7].setChecked(True)
                                elif ingrediente.lista[i][4] == 5:
                                    objetos.objetosGrupo2[j+8].setChecked(True)
                    for j in range(len(objetos.objetosGrupo3)-8):
                        cursor.execute("select i_nombre from Ingrediente where i_id=?",(ingrediente.lista[i][0],))
                        result = cursor.fetchone()
                        if result != None:
                            if unicode(result[0]) == unicode(objetos.objetosGrupo3[j].text()):
                                objetos.objetosGrupo3[j+1].setText(unicode(ingrediente.lista[i][1]))
                                objetos.objetosGrupo3[j+2].setText(unicode(ingrediente.lista[i][2]))
                                objetos.objetosGrupo3[j+3].setText(unicode(ingrediente.lista[i][3]))
                                if ingrediente.lista[i][4] == 1:
                                    objetos.objetosGrupo3[j+4].setChecked(True)
                                elif ingrediente.lista[i][4] == 2:
                                    objetos.objetosGrupo3[j+5].setChecked(True)
                                elif ingrediente.lista[i][4] == 3:
                                    objetos.objetosGrupo3[j+6].setChecked(True)
                                elif ingrediente.lista[i][4] == 4:
                                    objetos.objetosGrupo3[j+7].setChecked(True)
                                elif ingrediente.lista[i][4] == 5:
                                    objetos.objetosGrupo3[j+8].setChecked(True)
                    for j in range(len(objetos.objetosGrupo4)-8):
                        cursor.execute("select i_nombre from Ingrediente where i_id=?",(ingrediente.lista[i][0],))
                        result = cursor.fetchone()
                        if result != None:
                            if unicode(result[0]) == unicode(objetos.objetosGrupo4[j].text()):
                                objetos.objetosGrupo4[j+1].setText(unicode(ingrediente.lista[i][1]))
                                objetos.objetosGrupo4[j+2].setText(unicode(ingrediente.lista[i][2]))
                                objetos.objetosGrupo4[j+3].setText(unicode(ingrediente.lista[i][3]))
                                if ingrediente.lista[i][4] == 1:
                                    objetos.objetosGrupo4[j+4].setChecked(True)
                                elif ingrediente.lista[i][4] == 2:
                                    objetos.objetosGrupo4[j+5].setChecked(True)
                                elif ingrediente.lista[i][4] == 3:
                                    objetos.objetosGrupo4[j+6].setChecked(True)
                                elif ingrediente.lista[i][4] == 4:
                                    objetos.objetosGrupo4[j+7].setChecked(True)
                                elif ingrediente.lista[i][4] == 5:
                                    objetos.objetosGrupo4[j+8].setChecked(True)
                    for j in range(len(objetos.objetosGrupo5)-8):
                        cursor.execute("select i_nombre from Ingrediente where i_id=?",(ingrediente.lista[i][0],))
                        result = cursor.fetchone()
                        if result != None:
                            if unicode(result[0]) == unicode(objetos.objetosGrupo5[j].text()):
                                objetos.objetosGrupo5[j+1].setText(unicode(ingrediente.lista[i][1]))
                                objetos.objetosGrupo5[j+2].setText(unicode(ingrediente.lista[i][2]))
                                objetos.objetosGrupo5[j+3].setText(unicode(ingrediente.lista[i][3]))
                                if ingrediente.lista[i][4] == 1:
                                    objetos.objetosGrupo5[j+4].setChecked(True)
                                elif ingrediente.lista[i][4] == 2:
                                    objetos.objetosGrupo5[j+5].setChecked(True)
                                elif ingrediente.lista[i][4] == 3:
                                    objetos.objetosGrupo5[j+6].setChecked(True)
                                elif ingrediente.lista[i][4] == 4:
                                    objetos.objetosGrupo5[j+7].setChecked(True)
                                elif ingrediente.lista[i][4] == 5:
                                    objetos.objetosGrupo5[j+8].setChecked(True)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()


    def AbrirCuestionarioFrec(self,objetos):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd

        #Consulta para Grasas y Aceites ---------------------------------------
        tipo = "Grasas y Aceites"
        cursor.execute("select i_nombre from Ingrediente where i_tipo=?",(tipo,))
        items = cursor.fetchall()
        j = 40
        z = 40 + (len(items) * 30)
        self.uiCuestFrec.groupBox.setMinimumSize(QtCore.QSize(630, z))
        for i in range(len(items)):

            self.uiCuestFrec.lineEdit = QtGui.QLineEdit(self.uiCuestFrec.groupBox)
            self.uiCuestFrec.lineEdit.setGeometry(QtCore.QRect(20, j, 191, 27))
            self.uiCuestFrec.lineEdit.setReadOnly(True)
            self.uiCuestFrec.lineEdit.setObjectName("lineEdit")
            self.uiCuestFrec.lineEdit.setText(items[i][0])
            objetos.objetosGrupo1.append(self.uiCuestFrec.lineEdit)
            self.uiCuestFrec.lineEdit_2 = QtGui.QLineEdit(self.uiCuestFrec.groupBox)
            self.uiCuestFrec.lineEdit_2.setGeometry(QtCore.QRect(230, j, 51, 27))
            self.uiCuestFrec.lineEdit_2.setObjectName("lineEdit_2")
            objetos.objetosGrupo1.append(self.uiCuestFrec.lineEdit_2)
            self.uiCuestFrec.lineEdit_3 = QtGui.QLineEdit(self.uiCuestFrec.groupBox)
            self.uiCuestFrec.lineEdit_3.setGeometry(QtCore.QRect(310, j, 51, 27))
            self.uiCuestFrec.lineEdit_3.setObjectName("lineEdit_3")
            objetos.objetosGrupo1.append(self.uiCuestFrec.lineEdit_3)
            self.uiCuestFrec.lineEdit_4 = QtGui.QLineEdit(self.uiCuestFrec.groupBox)
            self.uiCuestFrec.lineEdit_4.setGeometry(QtCore.QRect(390, j, 51, 27))
            self.uiCuestFrec.lineEdit_4.setObjectName("lineEdit_4")
            objetos.objetosGrupo1.append(self.uiCuestFrec.lineEdit_4)
            self.uiCuestFrec.buttonGroup = QtGui.QButtonGroup(self.uiCuestFrec.groupBox)
            self.uiCuestFrec.buttonGroup.setObjectName("buttonGroup"+"_"+str(i))


            self.uiCuestFrec.radioButton = QtGui.QRadioButton(self.uiCuestFrec.groupBox)
            self.uiCuestFrec.radioButton.setGeometry(QtCore.QRect(470, j, 21, 22))
            self.uiCuestFrec.radioButton.setText("")
            self.uiCuestFrec.radioButton.setObjectName("radioButton")
            objetos.objetosGrupo1.append(self.uiCuestFrec.radioButton)
            self.uiCuestFrec.radioButton_2 = QtGui.QRadioButton(self.uiCuestFrec.groupBox)
            self.uiCuestFrec.radioButton_2.setGeometry(QtCore.QRect(490, j, 21, 22))
            self.uiCuestFrec.radioButton_2.setText("")
            self.uiCuestFrec.radioButton_2.setObjectName("radioButton_2")
            objetos.objetosGrupo1.append(self.uiCuestFrec.radioButton_2)
            self.uiCuestFrec.radioButton_3 = QtGui.QRadioButton(self.uiCuestFrec.groupBox)
            self.uiCuestFrec.radioButton_3.setGeometry(QtCore.QRect(510, j, 21, 22))
            self.uiCuestFrec.radioButton_3.setText("")
            self.uiCuestFrec.radioButton_3.setObjectName("radioButton_3")
            objetos.objetosGrupo1.append(self.uiCuestFrec.radioButton_3)
            self.uiCuestFrec.radioButton_4 = QtGui.QRadioButton(self.uiCuestFrec.groupBox)
            self.uiCuestFrec.radioButton_4.setGeometry(QtCore.QRect(530, j, 21, 22))
            self.uiCuestFrec.radioButton_4.setText("")
            self.uiCuestFrec.radioButton_4.setObjectName("radioButton_4")
            objetos.objetosGrupo1.append(self.uiCuestFrec.radioButton_4)
            self.uiCuestFrec.radioButton_5 = QtGui.QRadioButton(self.uiCuestFrec.groupBox)
            self.uiCuestFrec.radioButton_5.setGeometry(QtCore.QRect(550, j, 21, 22))
            self.uiCuestFrec.radioButton_5.setText("")
            self.uiCuestFrec.radioButton_5.setObjectName("radioButton_5")
            objetos.objetosGrupo1.append(self.uiCuestFrec.radioButton_5)
            j = j+30
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_2)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_3)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_4)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_5)
        #--------------------------------------------------------------------
        #Consulta para Farinaceos --------------------------------------------
        tipo = "Farinaceos"
        cursor.execute("select i_nombre from Ingrediente where i_tipo=?",(tipo,))
        items = cursor.fetchall()
        j = 40
        z = 40 + (len(items) * 30)
        self.uiCuestFrec.groupBox_2.setMinimumSize(QtCore.QSize(630, z))
        for i in range(len(items)):

            self.uiCuestFrec.lineEdit = QtGui.QLineEdit(self.uiCuestFrec.groupBox_2)
            self.uiCuestFrec.lineEdit.setGeometry(QtCore.QRect(20, j, 191, 27))
            self.uiCuestFrec.lineEdit.setReadOnly(True)
            self.uiCuestFrec.lineEdit.setObjectName("lineEdit")
            self.uiCuestFrec.lineEdit.setText(items[i][0])
            objetos.objetosGrupo2.append(self.uiCuestFrec.lineEdit)
            self.uiCuestFrec.lineEdit_2 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_2)
            self.uiCuestFrec.lineEdit_2.setGeometry(QtCore.QRect(230, j, 51, 27))
            self.uiCuestFrec.lineEdit_2.setObjectName("lineEdit_2")
            objetos.objetosGrupo2.append(self.uiCuestFrec.lineEdit_2)
            self.uiCuestFrec.lineEdit_3 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_2)
            self.uiCuestFrec.lineEdit_3.setGeometry(QtCore.QRect(310, j, 51, 27))
            self.uiCuestFrec.lineEdit_3.setObjectName("lineEdit_3")
            objetos.objetosGrupo2.append(self.uiCuestFrec.lineEdit_3)
            self.uiCuestFrec.lineEdit_4 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_2)
            self.uiCuestFrec.lineEdit_4.setGeometry(QtCore.QRect(390, j, 51, 27))
            self.uiCuestFrec.lineEdit_4.setObjectName("lineEdit_4")
            objetos.objetosGrupo2.append(self.uiCuestFrec.lineEdit_4)
            self.uiCuestFrec.buttonGroup = QtGui.QButtonGroup(self.uiCuestFrec.groupBox_2)
            self.uiCuestFrec.buttonGroup.setObjectName("buttonGroup"+"_"+str(i))
            self.uiCuestFrec.radioButton = QtGui.QRadioButton(self.uiCuestFrec.groupBox_2)
            self.uiCuestFrec.radioButton.setGeometry(QtCore.QRect(470, j, 21, 22))
            self.uiCuestFrec.radioButton.setText("")
            self.uiCuestFrec.radioButton.setObjectName("radioButton")
            objetos.objetosGrupo2.append(self.uiCuestFrec.radioButton)
            self.uiCuestFrec.radioButton_2 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_2)
            self.uiCuestFrec.radioButton_2.setGeometry(QtCore.QRect(490, j, 21, 22))
            self.uiCuestFrec.radioButton_2.setText("")
            self.uiCuestFrec.radioButton_2.setObjectName("radioButton_2")
            objetos.objetosGrupo2.append(self.uiCuestFrec.radioButton_2)
            self.uiCuestFrec.radioButton_3 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_2)
            self.uiCuestFrec.radioButton_3.setGeometry(QtCore.QRect(510, j, 21, 22))
            self.uiCuestFrec.radioButton_3.setText("")
            self.uiCuestFrec.radioButton_3.setObjectName("radioButton_3")
            objetos.objetosGrupo2.append(self.uiCuestFrec.radioButton_3)
            self.uiCuestFrec.radioButton_4 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_2)
            self.uiCuestFrec.radioButton_4.setGeometry(QtCore.QRect(530, j, 21, 22))
            self.uiCuestFrec.radioButton_4.setText("")
            self.uiCuestFrec.radioButton_4.setObjectName("radioButton_4")
            objetos.objetosGrupo2.append(self.uiCuestFrec.radioButton_4)
            self.uiCuestFrec.radioButton_5 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_2)
            self.uiCuestFrec.radioButton_5.setGeometry(QtCore.QRect(550, j, 21, 22))
            self.uiCuestFrec.radioButton_5.setText("")
            self.uiCuestFrec.radioButton_5.setObjectName("radioButton_5")
            objetos.objetosGrupo2.append(self.uiCuestFrec.radioButton_5)
            j = j+30
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_2)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_3)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_4)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_5)
        #-----------------------------------------------------------------
        #Consulta para Proteinicos
        tipo = "Proteinicos"
        cursor.execute("select i_nombre from Ingrediente where i_tipo=?",(tipo,))
        items = cursor.fetchall()
        j = 40
        z = 40 + (len(items) * 30)
        self.uiCuestFrec.groupBox_3.setMinimumSize(QtCore.QSize(630, z))
        for i in range(len(items)):

            self.uiCuestFrec.lineEdit = QtGui.QLineEdit(self.uiCuestFrec.groupBox_3)
            self.uiCuestFrec.lineEdit.setGeometry(QtCore.QRect(20, j, 191, 27))
            self.uiCuestFrec.lineEdit.setReadOnly(True)
            self.uiCuestFrec.lineEdit.setObjectName("lineEdit")
            self.uiCuestFrec.lineEdit.setText(items[i][0])
            objetos.objetosGrupo3.append(self.uiCuestFrec.lineEdit)
            self.uiCuestFrec.lineEdit_2 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_3)
            self.uiCuestFrec.lineEdit_2.setGeometry(QtCore.QRect(230, j, 51, 27))
            self.uiCuestFrec.lineEdit_2.setObjectName("lineEdit_2")
            objetos.objetosGrupo3.append(self.uiCuestFrec.lineEdit_2)
            self.uiCuestFrec.lineEdit_3 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_3)
            self.uiCuestFrec.lineEdit_3.setGeometry(QtCore.QRect(310, j, 51, 27))
            self.uiCuestFrec.lineEdit_3.setObjectName("lineEdit_3")
            objetos.objetosGrupo3.append(self.uiCuestFrec.lineEdit_3)
            self.uiCuestFrec.lineEdit_4 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_3)
            self.uiCuestFrec.lineEdit_4.setGeometry(QtCore.QRect(390, j, 51, 27))
            self.uiCuestFrec.lineEdit_4.setObjectName("lineEdit_4")
            objetos.objetosGrupo3.append(self.uiCuestFrec.lineEdit_4)
            self.uiCuestFrec.buttonGroup = QtGui.QButtonGroup(self.uiCuestFrec.groupBox_3)
            self.uiCuestFrec.buttonGroup.setObjectName("buttonGroup"+"_"+str(i))
            self.uiCuestFrec.radioButton = QtGui.QRadioButton(self.uiCuestFrec.groupBox_3)
            self.uiCuestFrec.radioButton.setGeometry(QtCore.QRect(470, j, 21, 22))
            self.uiCuestFrec.radioButton.setText("")
            self.uiCuestFrec.radioButton.setObjectName("radioButton")
            objetos.objetosGrupo3.append(self.uiCuestFrec.radioButton)
            self.uiCuestFrec.radioButton_2 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_3)
            self.uiCuestFrec.radioButton_2.setGeometry(QtCore.QRect(490, j, 21, 22))
            self.uiCuestFrec.radioButton_2.setText("")
            self.uiCuestFrec.radioButton_2.setObjectName("radioButton_2")
            objetos.objetosGrupo3.append(self.uiCuestFrec.radioButton_2)
            self.uiCuestFrec.radioButton_3 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_3)
            self.uiCuestFrec.radioButton_3.setGeometry(QtCore.QRect(510, j, 21, 22))
            self.uiCuestFrec.radioButton_3.setText("")
            self.uiCuestFrec.radioButton_3.setObjectName("radioButton_3")
            objetos.objetosGrupo3.append(self.uiCuestFrec.radioButton_3)
            self.uiCuestFrec.radioButton_4 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_3)
            self.uiCuestFrec.radioButton_4.setGeometry(QtCore.QRect(530, j, 21, 22))
            self.uiCuestFrec.radioButton_4.setText("")
            self.uiCuestFrec.radioButton_4.setObjectName("radioButton_4")
            objetos.objetosGrupo3.append(self.uiCuestFrec.radioButton_4)
            self.uiCuestFrec.radioButton_5 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_3)
            self.uiCuestFrec.radioButton_5.setGeometry(QtCore.QRect(550, j, 21, 22))
            self.uiCuestFrec.radioButton_5.setText("")
            self.uiCuestFrec.radioButton_5.setObjectName("radioButton_5")
            objetos.objetosGrupo3.append(self.uiCuestFrec.radioButton_5)
            j = j+30
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_2)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_3)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_4)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_5)
        #-----------------------------------------------------------------
        #Consulta para Lacteos
        tipo = "Lacteos"
        cursor.execute("select i_nombre from Ingrediente where i_tipo=?",(tipo,))
        items = cursor.fetchall()
        j = 40
        z = 40 + (len(items) * 30)
        self.uiCuestFrec.groupBox_4.setMinimumSize(QtCore.QSize(630, z))
        for i in range(len(items)):

            self.uiCuestFrec.lineEdit = QtGui.QLineEdit(self.uiCuestFrec.groupBox_4)
            self.uiCuestFrec.lineEdit.setGeometry(QtCore.QRect(20, j, 191, 27))
            self.uiCuestFrec.lineEdit.setReadOnly(True)
            self.uiCuestFrec.lineEdit.setObjectName("lineEdit")
            self.uiCuestFrec.lineEdit.setText(items[i][0])
            objetos.objetosGrupo4.append(self.uiCuestFrec.lineEdit)
            self.uiCuestFrec.lineEdit_2 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_4)
            self.uiCuestFrec.lineEdit_2.setGeometry(QtCore.QRect(230, j, 51, 27))
            self.uiCuestFrec.lineEdit_2.setObjectName("lineEdit_2")
            objetos.objetosGrupo4.append(self.uiCuestFrec.lineEdit_2)
            self.uiCuestFrec.lineEdit_3 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_4)
            self.uiCuestFrec.lineEdit_3.setGeometry(QtCore.QRect(310, j, 51, 27))
            self.uiCuestFrec.lineEdit_3.setObjectName("lineEdit_3")
            objetos.objetosGrupo4.append(self.uiCuestFrec.lineEdit_3)
            self.uiCuestFrec.lineEdit_4 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_4)
            self.uiCuestFrec.lineEdit_4.setGeometry(QtCore.QRect(390, j, 51, 27))
            self.uiCuestFrec.lineEdit_4.setObjectName("lineEdit_4")
            objetos.objetosGrupo4.append(self.uiCuestFrec.lineEdit_4)
            self.uiCuestFrec.buttonGroup = QtGui.QButtonGroup(self.uiCuestFrec.groupBox_4)
            self.uiCuestFrec.buttonGroup.setObjectName("buttonGroup"+"_"+str(i))
            self.uiCuestFrec.radioButton = QtGui.QRadioButton(self.uiCuestFrec.groupBox_4)
            self.uiCuestFrec.radioButton.setGeometry(QtCore.QRect(470, j, 21, 22))
            self.uiCuestFrec.radioButton.setText("")
            self.uiCuestFrec.radioButton.setObjectName("radioButton")
            objetos.objetosGrupo4.append(self.uiCuestFrec.radioButton)
            self.uiCuestFrec.radioButton_2 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_4)
            self.uiCuestFrec.radioButton_2.setGeometry(QtCore.QRect(490, j, 21, 22))
            self.uiCuestFrec.radioButton_2.setText("")
            self.uiCuestFrec.radioButton_2.setObjectName("radioButton_2")
            objetos.objetosGrupo4.append(self.uiCuestFrec.radioButton_2)
            self.uiCuestFrec.radioButton_3 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_4)
            self.uiCuestFrec.radioButton_3.setGeometry(QtCore.QRect(510, j, 21, 22))
            self.uiCuestFrec.radioButton_3.setText("")
            self.uiCuestFrec.radioButton_3.setObjectName("radioButton_3")
            objetos.objetosGrupo4.append(self.uiCuestFrec.radioButton_3)
            self.uiCuestFrec.radioButton_4 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_4)
            self.uiCuestFrec.radioButton_4.setGeometry(QtCore.QRect(530, j, 21, 22))
            self.uiCuestFrec.radioButton_4.setText("")
            self.uiCuestFrec.radioButton_4.setObjectName("radioButton_4")
            objetos.objetosGrupo4.append(self.uiCuestFrec.radioButton_4)
            self.uiCuestFrec.radioButton_5 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_4)
            self.uiCuestFrec.radioButton_5.setGeometry(QtCore.QRect(550, j, 21, 22))
            self.uiCuestFrec.radioButton_5.setText("")
            self.uiCuestFrec.radioButton_5.setObjectName("radioButton_5")
            objetos.objetosGrupo4.append(self.uiCuestFrec.radioButton_5)
            j = j+30
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_2)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_3)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_4)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_5)
        #-----------------------------------------------------------------
        #Consulta para Frutas y Verduras
        tipo = "Frutas y Verduras"
        cursor.execute("select i_nombre from Ingrediente where i_tipo=?",(tipo,))
        items = cursor.fetchall()
        j = 40
        z = 40 + (len(items) * 30)
        self.uiCuestFrec.groupBox_5.setMinimumSize(QtCore.QSize(630, z))
        for i in range(len(items)):

            self.uiCuestFrec.lineEdit = QtGui.QLineEdit(self.uiCuestFrec.groupBox_5)
            self.uiCuestFrec.lineEdit.setGeometry(QtCore.QRect(20, j, 191, 27))
            self.uiCuestFrec.lineEdit.setReadOnly(True)
            self.uiCuestFrec.lineEdit.setObjectName("lineEdit")
            self.uiCuestFrec.lineEdit.setText(items[i][0])
            objetos.objetosGrupo5.append(self.uiCuestFrec.lineEdit)
            self.uiCuestFrec.lineEdit_2 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_5)
            self.uiCuestFrec.lineEdit_2.setGeometry(QtCore.QRect(230, j, 51, 27))
            self.uiCuestFrec.lineEdit_2.setObjectName("lineEdit_2")
            objetos.objetosGrupo5.append(self.uiCuestFrec.lineEdit_2)
            self.uiCuestFrec.lineEdit_3 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_5)
            self.uiCuestFrec.lineEdit_3.setGeometry(QtCore.QRect(310, j, 51, 27))
            self.uiCuestFrec.lineEdit_3.setObjectName("lineEdit_3")
            objetos.objetosGrupo5.append(self.uiCuestFrec.lineEdit_3)
            self.uiCuestFrec.lineEdit_4 = QtGui.QLineEdit(self.uiCuestFrec.groupBox_5)
            self.uiCuestFrec.lineEdit_4.setGeometry(QtCore.QRect(390, j, 51, 27))
            self.uiCuestFrec.lineEdit_4.setObjectName("lineEdit_4")
            objetos.objetosGrupo5.append(self.uiCuestFrec.lineEdit_4)
            self.uiCuestFrec.buttonGroup = QtGui.QButtonGroup(self.uiCuestFrec.groupBox_5)
            self.uiCuestFrec.buttonGroup.setObjectName("buttonGroup"+"_"+str(i))
            self.uiCuestFrec.radioButton = QtGui.QRadioButton(self.uiCuestFrec.groupBox_5)
            self.uiCuestFrec.radioButton.setGeometry(QtCore.QRect(470, j, 21, 22))
            self.uiCuestFrec.radioButton.setText("")
            self.uiCuestFrec.radioButton.setObjectName("radioButton")
            objetos.objetosGrupo5.append(self.uiCuestFrec.radioButton)
            self.uiCuestFrec.radioButton_2 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_5)
            self.uiCuestFrec.radioButton_2.setGeometry(QtCore.QRect(490, j, 21, 22))
            self.uiCuestFrec.radioButton_2.setText("")
            self.uiCuestFrec.radioButton_2.setObjectName("radioButton_2")
            objetos.objetosGrupo5.append(self.uiCuestFrec.radioButton_2)
            self.uiCuestFrec.radioButton_3 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_5)
            self.uiCuestFrec.radioButton_3.setGeometry(QtCore.QRect(510, j, 21, 22))
            self.uiCuestFrec.radioButton_3.setText("")
            self.uiCuestFrec.radioButton_3.setObjectName("radioButton_3")
            objetos.objetosGrupo5.append(self.uiCuestFrec.radioButton_3)
            self.uiCuestFrec.radioButton_4 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_5)
            self.uiCuestFrec.radioButton_4.setGeometry(QtCore.QRect(530, j, 21, 22))
            self.uiCuestFrec.radioButton_4.setText("")
            self.uiCuestFrec.radioButton_4.setObjectName("radioButton_4")
            objetos.objetosGrupo5.append(self.uiCuestFrec.radioButton_4)
            self.uiCuestFrec.radioButton_5 = QtGui.QRadioButton(self.uiCuestFrec.groupBox_5)
            self.uiCuestFrec.radioButton_5.setGeometry(QtCore.QRect(550, j, 21, 22))
            self.uiCuestFrec.radioButton_5.setText("")
            self.uiCuestFrec.radioButton_5.setObjectName("radioButton_5")
            objetos.objetosGrupo5.append(self.uiCuestFrec.radioButton_5)
            j = j+30
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_2)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_3)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_4)
            self.uiCuestFrec.buttonGroup.addButton(self.uiCuestFrec.radioButton_5)
        #-----------------------------------------------------------------
        self.WindowCuestFrec.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()        

#Conexion de boton Aceptar de Cuestionario de Frecuencia y bbdd
    def GuardarCuestionarioFrec(self,objetos):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta y Modificacion en la bbdd

        #Guardar datos para Grasas y Aceites
        j=0
        k=0
        for i in range(len(objetos.objetosGrupo1)):
            if j < len(objetos.objetosGrupo1):
                cursor.execute("select max(pr_id) from Preferencia")
                res = cursor.fetchone()
                if res[0] == None:
                    PR_ID = 1
                else:
                    PR_ID = res[0]
                    PR_ID += 1

                i_nombre = unicode(objetos.objetosGrupo1[j].text())
                cursor.execute("select i_id from Ingrediente where i_nombre=?",(i_nombre,))
                res = cursor.fetchone()
                PR_IID = res[0]
                
                cursor.execute("select pr_id from Preferencia where pr_iid=? and pr_pid=?",(PR_IID, self.perfil))
                res = cursor.fetchone()

                if res != None:
                    PR_ID = res[0]
                    cursor.execute("delete from Preferencia where pr_id=?",(PR_ID,))
                PR_D = unicode(objetos.objetosGrupo1[j+1].text())
                PR_S = unicode(objetos.objetosGrupo1[j+2].text())
                PR_M = unicode(objetos.objetosGrupo1[j+3].text())

                PR_NPR = 0
                if objetos.objetosGrupo1[j+4].isChecked():
                    PR_NPR = 1
                elif objetos.objetosGrupo1[j+5].isChecked():
                    PR_NPR = 2
                elif objetos.objetosGrupo1[j+6].isChecked():
                    PR_NPR = 3
                elif objetos.objetosGrupo1[j+7].isChecked():
                    PR_NPR = 4
                elif objetos.objetosGrupo1[j+8].isChecked():
                    PR_NPR = 5

                j=j+9

                valores = (PR_ID, PR_IID, PR_D, PR_S, PR_M, PR_NPR, self.perfil,)
                cursor.execute("insert into Preferencia values (?,?,?,?,?,?,?)",valores)
        #--------------------------------------------------------------------

        #Guardar datos para Farinaceos
        j=0
        k=0
        for i in range(len(objetos.objetosGrupo2)):
            if j < len(objetos.objetosGrupo2):
                cursor.execute("select max(pr_id) from Preferencia")
                res = cursor.fetchone()
                if res[0] == None:
                    PR_ID = 1
                else:
                    PR_ID = res[0]
                    PR_ID += 1

                i_nombre = unicode(objetos.objetosGrupo2[j].text())
                cursor.execute("select i_id from Ingrediente where i_nombre=?",(i_nombre,))
                res = cursor.fetchone()
                PR_IID = res[0]
                
                cursor.execute("select pr_id from Preferencia where pr_iid=? and pr_pid=?",(PR_IID, self.perfil))
                res = cursor.fetchone()
                if res != None:
                    PR_ID = res[0]
                    cursor.execute("delete from Preferencia where pr_id=?",(PR_ID,))
                PR_D = unicode(objetos.objetosGrupo2[j+1].text())
                PR_S = unicode(objetos.objetosGrupo2[j+2].text())
                PR_M = unicode(objetos.objetosGrupo2[j+3].text())

                PR_NPR = 0
                if objetos.objetosGrupo2[j+4].isChecked():
                    PR_NPR = 1
                elif objetos.objetosGrupo2[j+5].isChecked():
                    PR_NPR = 2
                elif objetos.objetosGrupo2[j+6].isChecked():
                    PR_NPR = 3
                elif objetos.objetosGrupo2[j+7].isChecked():
                    PR_NPR = 4
                elif objetos.objetosGrupo2[j+8].isChecked():
                    PR_NPR = 5

                j=j+9

                valores = (PR_ID, PR_IID, PR_D, PR_S, PR_M, PR_NPR, self.perfil,)
                cursor.execute("insert into Preferencia values (?,?,?,?,?,?,?)",valores)
        #--------------------------------------------------------------------

        #Guardar datos para Proteinicos
        j=0
        k=0
        for i in range(len(objetos.objetosGrupo3)):
            if j < len(objetos.objetosGrupo3):
                cursor.execute("select max(pr_id) from Preferencia")
                res = cursor.fetchone()
                if res[0] == None:
                    PR_ID = 1
                else:
                    PR_ID = res[0]
                    PR_ID += 1

                i_nombre = unicode(objetos.objetosGrupo3[j].text())
                cursor.execute("select i_id from Ingrediente where i_nombre=?",(i_nombre,))
                res = cursor.fetchone()
                PR_IID = res[0]
                
                cursor.execute("select pr_id from Preferencia where pr_iid=? and pr_pid=?",(PR_IID, self.perfil))
                res = cursor.fetchone()
                if res != None:
                    PR_ID = res[0]
                    cursor.execute("delete from Preferencia where pr_id=?",(PR_ID,))
                PR_D = unicode(objetos.objetosGrupo3[j+1].text())
                PR_S = unicode(objetos.objetosGrupo3[j+2].text())
                PR_M = unicode(objetos.objetosGrupo3[j+3].text())

                PR_NPR = 0
                if objetos.objetosGrupo3[j+4].isChecked():
                    PR_NPR = 1
                elif objetos.objetosGrupo3[j+5].isChecked():
                    PR_NPR = 2
                elif objetos.objetosGrupo3[j+6].isChecked():
                    PR_NPR = 3
                elif objetos.objetosGrupo3[j+7].isChecked():
                    PR_NPR = 4
                elif objetos.objetosGrupo3[j+8].isChecked():
                    PR_NPR = 5

                j=j+9

                valores = (PR_ID, PR_IID, PR_D, PR_S, PR_M, PR_NPR, self.perfil,)
                cursor.execute("insert into Preferencia values (?,?,?,?,?,?,?)",valores)
        #--------------------------------------------------------------------

        #Guardar datos para Lacteos
        j=0
        k=0
        for i in range(len(objetos.objetosGrupo4)):
            if j < len(objetos.objetosGrupo4):
                cursor.execute("select max(pr_id) from Preferencia")
                res = cursor.fetchone()
                if res[0] == None:
                    PR_ID = 1
                else:
                    PR_ID = res[0]
                    PR_ID += 1

                i_nombre = unicode(objetos.objetosGrupo4[j].text())
                cursor.execute("select i_id from Ingrediente where i_nombre=?",(i_nombre,))
                res = cursor.fetchone()
                PR_IID = res[0]
                
                cursor.execute("select pr_id from Preferencia where pr_iid=? and pr_pid=?",(PR_IID, self.perfil))
                res = cursor.fetchone()
                if res != None:
                    PR_ID = res[0]
                    cursor.execute("delete from Preferencia where pr_id=?",(PR_ID,))
                PR_D = unicode(objetos.objetosGrupo4[j+1].text())
                PR_S = unicode(objetos.objetosGrupo4[j+2].text())
                PR_M = unicode(objetos.objetosGrupo4[j+3].text())

                PR_NPR = 0
                if objetos.objetosGrupo4[j+4].isChecked():
                    PR_NPR = 1
                elif objetos.objetosGrupo4[j+5].isChecked():
                    PR_NPR = 2
                elif objetos.objetosGrupo4[j+6].isChecked():
                    PR_NPR = 3
                elif objetos.objetosGrupo4[j+7].isChecked():
                    PR_NPR = 4
                elif objetos.objetosGrupo4[j+8].isChecked():
                    PR_NPR = 5

                j=j+9

                valores = (PR_ID, PR_IID, PR_D, PR_S, PR_M, PR_NPR, self.perfil,)
                cursor.execute("insert into Preferencia values (?,?,?,?,?,?,?)",valores)

        #--------------------------------------------------------------------

        #Guardar datos para Frutas y Verduras
        j=0
        k=0
        for i in range(len(objetos.objetosGrupo5)):
            if j < len(objetos.objetosGrupo5):
                cursor.execute("select max(pr_id) from Preferencia")
                res = cursor.fetchone()
                if res[0] == None:
                    PR_ID = 1
                else:
                    PR_ID = res[0]
                    PR_ID += 1

                i_nombre = unicode(objetos.objetosGrupo5[j].text())
                cursor.execute("select i_id from Ingrediente where i_nombre=?",(i_nombre,))
                res = cursor.fetchone()
                PR_IID = res[0]
                
                cursor.execute("select pr_id from Preferencia where pr_iid=? and pr_pid=?",(PR_IID, self.perfil,))
                res = cursor.fetchone()
                if res != None:
                    PR_ID = res[0]
                    cursor.execute("delete from Preferencia where pr_id=?",(PR_ID,))
                PR_D = unicode(objetos.objetosGrupo5[j+1].text())
                PR_S = unicode(objetos.objetosGrupo5[j+2].text())
                PR_M = unicode(objetos.objetosGrupo5[j+3].text())

                PR_NPR = 0
                if objetos.objetosGrupo5[j+4].isChecked():
                    PR_NPR = 1
                elif objetos.objetosGrupo5[j+5].isChecked():
                    PR_NPR = 2
                elif objetos.objetosGrupo5[j+6].isChecked():
                    PR_NPR = 3
                elif objetos.objetosGrupo5[j+7].isChecked():
                    PR_NPR = 4
                elif objetos.objetosGrupo5[j+8].isChecked():
                    PR_NPR = 5

                j=j+9

                valores = (PR_ID, PR_IID, PR_D, PR_S, PR_M, PR_NPR, self.perfil,)
                cursor.execute("insert into Preferencia values (?,?,?,?,?,?,?)",valores)
        #--------------------------------------------------------------------

        bbdd.commit()
        self.ClearCuestFrec(objetos)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de TableWidget segun nº ingestas y lineEdits correspondientes
    def CalcularKcalDia(self,ui):
        if ui.comboBox.currentIndex() == 0: #Para 6 ingestas
            kcal1 = 0
            if ui.tableWidget_5.item(0,0).text() != "":
                kcal1 = ui.tableWidget_5.item(0,0).cal
            if ui.tableWidget_5.item(1,0).text() != "":
                kcal1 += ui.tableWidget_5.item(1,0).cal
            if ui.tableWidget_5.item(2,0).text() != "":
                kcal1 += ui.tableWidget_5.item(2,0).cal
            if ui.tableWidget_5.item(3,0).text() != "":
                kcal1 += ui.tableWidget_5.item(3,0).cal
            if ui.tableWidget_5.item(4,0).text() != "":
                kcal1 += ui.tableWidget_5.item(4,0).cal
            if ui.tableWidget_5.item(5,0).text() != "":
                kcal1 += ui.tableWidget_5.item(5,0).cal
            ui.lineEdit_6_7.setText(str(kcal1))
            if ui.doubleSpin_ET.value() >= kcal1:
                ui.lineEdit_6_7.setStyleSheet("color: green")
            else:
                ui.lineEdit_6_7.setStyleSheet("color: red")
            kcal2 = 0
            if ui.tableWidget_5.item(0,1).text() != "":
                kcal2 = ui.tableWidget_5.item(0,1).cal
            if ui.tableWidget_5.item(1,1).text() != "":
                kcal2 += ui.tableWidget_5.item(1,1).cal
            if ui.tableWidget_5.item(2,1).text() != "":
                kcal2 += ui.tableWidget_5.item(2,1).cal
            if ui.tableWidget_5.item(3,1).text() != "":
                kcal2 += ui.tableWidget_5.item(3,1).cal
            if ui.tableWidget_5.item(4,1).text() != "":
                kcal2 += ui.tableWidget_5.item(4,1).cal
            if ui.tableWidget_5.item(5,1).text() != "":
                kcal2 += ui.tableWidget_5.item(5,1).cal
            ui.lineEdit_6_8.setText(str(kcal2))
            if ui.doubleSpin_ET.value() >= kcal2:
                ui.lineEdit_6_8.setStyleSheet("color: green")
            else:
                ui.lineEdit_6_8.setStyleSheet("color: red")
            kcal3 = 0
            if ui.tableWidget_5.item(0,2).text() != "":
                kcal3 = ui.tableWidget_5.item(0,2).cal
            if ui.tableWidget_5.item(1,2).text() != "":
                kcal3 += ui.tableWidget_5.item(1,2).cal
            if ui.tableWidget_5.item(2,2).text() != "":
                kcal3 += ui.tableWidget_5.item(2,2).cal
            if ui.tableWidget_5.item(3,2).text() != "":
                kcal3 += ui.tableWidget_5.item(3,2).cal
            if ui.tableWidget_5.item(4,2).text() != "":
                kcal3 += ui.tableWidget_5.item(4,2).cal
            if ui.tableWidget_5.item(5,2).text() != "":
                kcal3 += ui.tableWidget_5.item(5,2).cal
            ui.lineEdit_6_9.setText(str(kcal3))
            if ui.doubleSpin_ET.value() >= kcal3:
                ui.lineEdit_6_9.setStyleSheet("color: green")
            else:
                ui.lineEdit_6_9.setStyleSheet("color: red")
            kcal4 = 0
            if ui.tableWidget_5.item(0,3).text() != "":
                kcal4 = ui.tableWidget_5.item(0,3).cal
            if ui.tableWidget_5.item(1,3).text() != "":
                kcal4 += ui.tableWidget_5.item(1,3).cal
            if ui.tableWidget_5.item(2,3).text() != "":
                kcal4 += ui.tableWidget_5.item(2,3).cal
            if ui.tableWidget_5.item(3,3).text() != "":
                kcal4 += ui.tableWidget_5.item(3,3).cal
            if ui.tableWidget_5.item(4,3).text() != "":
                kcal4 += ui.tableWidget_5.item(4,3).cal
            if ui.tableWidget_5.item(5,3).text() != "":
                kcal4 += ui.tableWidget_5.item(5,3).cal
            ui.lineEdit_6_10.setText(str(kcal4))
            if ui.doubleSpin_ET.value() >= kcal4:
                ui.lineEdit_6_10.setStyleSheet("color: green")
            else:
                ui.lineEdit_6_10.setStyleSheet("color: red")
            kcal5 = 0
            if ui.tableWidget_5.item(0,4).text() != "":
                kcal5 = ui.tableWidget_5.item(0,4).cal
            if ui.tableWidget_5.item(1,4).text() != "":
                kcal5 += ui.tableWidget_5.item(1,4).cal
            if ui.tableWidget_5.item(2,4).text() != "":
                kcal5 += ui.tableWidget_5.item(2,4).cal
            if ui.tableWidget_5.item(3,4).text() != "":
                kcal5 += ui.tableWidget_5.item(3,4).cal
            if ui.tableWidget_5.item(4,4).text() != "":
                kcal5 += ui.tableWidget_5.item(4,4).cal
            if ui.tableWidget_5.item(5,4).text() != "":
                kcal5 += ui.tableWidget_5.item(5,4).cal
            ui.lineEdit_6_11.setText(str(kcal5))
            if ui.doubleSpin_ET.value() >= kcal5:
                ui.lineEdit_6_11.setStyleSheet("color: green")
            else:
                ui.lineEdit_6_11.setStyleSheet("color: red")
            kcal6 = 0
            if ui.tableWidget_5.item(0,5).text() != "":
                kcal6 = ui.tableWidget_5.item(0,5).cal
            if ui.tableWidget_5.item(1,5).text() != "":
                kcal6 += ui.tableWidget_5.item(1,5).cal
            if ui.tableWidget_5.item(2,5).text() != "":
                kcal6 += ui.tableWidget_5.item(2,5).cal
            if ui.tableWidget_5.item(3,5).text() != "":
                kcal6 += ui.tableWidget_5.item(3,5).cal
            if ui.tableWidget_5.item(4,5).text() != "":
                kcal6 += ui.tableWidget_5.item(4,5).cal
            if ui.tableWidget_5.item(5,5).text() != "":
                kcal6 += ui.tableWidget_5.item(5,5).cal
            ui.lineEdit_6_12.setText(str(kcal6))
            if ui.doubleSpin_ET.value() >= kcal6:
                ui.lineEdit_6_12.setStyleSheet("color: green")
            else:
                ui.lineEdit_6_12.setStyleSheet("color: red")
            kcal7 = 0
            if ui.tableWidget_5.item(0,6).text() != "":
                kcal7 = ui.tableWidget_5.item(0,6).cal
            if ui.tableWidget_5.item(1,6).text() != "":
                kcal7 += ui.tableWidget_5.item(1,6).cal
            if ui.tableWidget_5.item(2,6).text() != "":
                kcal7 += ui.tableWidget_5.item(2,6).cal
            if ui.tableWidget_5.item(3,6).text() != "":
                kcal7 += ui.tableWidget_5.item(3,6).cal
            if ui.tableWidget_5.item(4,6).text() != "":
                kcal7 += ui.tableWidget_5.item(4,6).cal
            if ui.tableWidget_5.item(5,6).text() != "":
                kcal7 += ui.tableWidget_5.item(5,6).cal
            ui.lineEdit_6_13.setText(str(kcal7))
            if ui.doubleSpin_ET.value() >= kcal7:
                ui.lineEdit_6_13.setStyleSheet("color: green")
            else:
                ui.lineEdit_6_13.setStyleSheet("color: red")

        elif ui.comboBox.currentIndex() == 1: #Para 5 ingestas
            kcal1 = 0
            if ui.tableWidget_4.item(0,0).text() != "":
                kcal1 = ui.tableWidget_4.item(0,0).cal
            if ui.tableWidget_4.item(1,0).text() != "":
                kcal1 += ui.tableWidget_4.item(1,0).cal
            if ui.tableWidget_4.item(2,0).text() != "":
                kcal1 += ui.tableWidget_4.item(2,0).cal
            if ui.tableWidget_4.item(3,0).text() != "":
                kcal1 += ui.tableWidget_4.item(3,0).cal
            if ui.tableWidget_4.item(4,0).text() != "":
                kcal1 += ui.tableWidget_4.item(4,0).cal
            ui.lineEdit_5_6.setText(str(kcal1))
            if ui.doubleSpin_ET.value() >= kcal1:
                ui.lineEdit_5_6.setStyleSheet("color: green")
            else:
                ui.lineEdit_5_6.setStyleSheet("color: red")
            kcal2 = 0
            if ui.tableWidget_4.item(0,1).text() != "":
                kcal2 = ui.tableWidget_4.item(0,1).cal
            if ui.tableWidget_4.item(1,1).text() != "":
                kcal2 += ui.tableWidget_4.item(1,1).cal
            if ui.tableWidget_4.item(2,1).text() != "":
                kcal2 += ui.tableWidget_4.item(2,1).cal
            if ui.tableWidget_4.item(3,1).text() != "":
                kcal2 += ui.tableWidget_4.item(3,1).cal
            if ui.tableWidget_4.item(4,1).text() != "":
                kcal2 += ui.tableWidget_4.item(4,1).cal
            ui.lineEdit_5_7.setText(str(kcal2))
            if ui.doubleSpin_ET.value() >= kcal2:
                ui.lineEdit_5_7.setStyleSheet("color: green")
            else:
                ui.lineEdit_5_7.setStyleSheet("color: red")
            kcal3 = 0
            if ui.tableWidget_4.item(0,2).text() != "":
                kcal3 = ui.tableWidget_4.item(0,2).cal
            if ui.tableWidget_4.item(1,2).text() != "":
                kcal3 += ui.tableWidget_4.item(1,2).cal
            if ui.tableWidget_4.item(2,2).text() != "":
                kcal3 += ui.tableWidget_4.item(2,2).cal
            if ui.tableWidget_4.item(3,2).text() != "":
                kcal3 += ui.tableWidget_4.item(3,2).cal
            if ui.tableWidget_4.item(4,2).text() != "":
                kcal3 += ui.tableWidget_4.item(4,2).cal
            ui.lineEdit_5_8.setText(str(kcal3))
            if ui.doubleSpin_ET.value() >= kcal3:
                ui.lineEdit_5_8.setStyleSheet("color: green")
            else:
                ui.lineEdit_5_8.setStyleSheet("color: red")
            kcal4 = 0
            if ui.tableWidget_4.item(0,3).text() != "":
                kcal4 = ui.tableWidget_4.item(0,3).cal
            if ui.tableWidget_4.item(1,3).text() != "":
                kcal4 += ui.tableWidget_4.item(1,3).cal
            if ui.tableWidget_4.item(2,3).text() != "":
                kcal4 += ui.tableWidget_4.item(2,3).cal
            if ui.tableWidget_4.item(3,3).text() != "":
                kcal4 += ui.tableWidget_4.item(3,3).cal
            if ui.tableWidget_4.item(4,3).text() != "":
                kcal4 += ui.tableWidget_4.item(4,3).cal
            ui.lineEdit_5_9.setText(str(kcal4))
            if ui.doubleSpin_ET.value() >= kcal4:
                ui.lineEdit_5_9.setStyleSheet("color: green")
            else:
                ui.lineEdit_5_9.setStyleSheet("color: red")
            kcal5 = 0
            if ui.tableWidget_4.item(0,4).text() != "":
                kcal5 = ui.tableWidget_4.item(0,4).cal
            if ui.tableWidget_4.item(1,4).text() != "":
                kcal5 += ui.tableWidget_4.item(1,4).cal
            if ui.tableWidget_4.item(2,4).text() != "":
                kcal5 += ui.tableWidget_4.item(2,4).cal
            if ui.tableWidget_4.item(3,4).text() != "":
                kcal5 += ui.tableWidget_4.item(3,4).cal
            if ui.tableWidget_4.item(4,4).text() != "":
                kcal5 += ui.tableWidget_4.item(4,4).cal
            ui.lineEdit_5_10.setText(str(kcal5))
            if ui.doubleSpin_ET.value() >= kcal5:
                ui.lineEdit_5_10.setStyleSheet("color: green")
            else:
                ui.lineEdit_5_10.setStyleSheet("color: red")
            kcal6 = 0
            if ui.tableWidget_4.item(0,5).text() != "":
                kcal6 = ui.tableWidget_4.item(0,5).cal
            if ui.tableWidget_4.item(1,5).text() != "":
                kcal6 += ui.tableWidget_4.item(1,5).cal
            if ui.tableWidget_4.item(2,5).text() != "":
                kcal6 += ui.tableWidget_4.item(2,5).cal
            if ui.tableWidget_4.item(3,5).text() != "":
                kcal6 += ui.tableWidget_4.item(3,5).cal
            if ui.tableWidget_4.item(4,5).text() != "":
                kcal6 += ui.tableWidget_4.item(4,5).cal
            ui.lineEdit_5_11.setText(str(kcal6))
            if ui.doubleSpin_ET.value() >= kcal6:
                ui.lineEdit_5_11.setStyleSheet("color: green")
            else:
                ui.lineEdit_5_11.setStyleSheet("color: red")
            kcal7 = 0
            if ui.tableWidget_4.item(0,6).text() != "":
                kcal7 = ui.tableWidget_4.item(0,6).cal
            if ui.tableWidget_4.item(1,6).text() != "":
                kcal7 += ui.tableWidget_4.item(1,6).cal
            if ui.tableWidget_4.item(2,6).text() != "":
                kcal7 += ui.tableWidget_4.item(2,6).cal
            if ui.tableWidget_4.item(3,6).text() != "":
                kcal7 += ui.tableWidget_4.item(3,6).cal
            if ui.tableWidget_4.item(4,6).text() != "":
                kcal7 += ui.tableWidget_4.item(4,6).cal
            ui.lineEdit_5_12.setText(str(kcal7))
            if ui.doubleSpin_ET.value() >= kcal7:
                ui.lineEdit_5_12.setStyleSheet("color: green")
            else:
                ui.lineEdit_5_12.setStyleSheet("color: red")

        elif ui.comboBox.currentIndex() == 2: #Para 4 ingestas
            kcal1 = 0
            if ui.tableWidget_3.item(0,0).text() != "":
                kcal1 = ui.tableWidget_3.item(0,0).cal
            if ui.tableWidget_3.item(1,0).text() != "":
                kcal1 += ui.tableWidget_3.item(1,0).cal
            if ui.tableWidget_3.item(2,0).text() != "":
                kcal1 += ui.tableWidget_3.item(2,0).cal
            if ui.tableWidget_3.item(3,0).text() != "":
                kcal1 += ui.tableWidget_3.item(3,0).cal
            ui.lineEdit_4_5.setText(str(kcal1))
            if ui.doubleSpin_ET.value() >= kcal1:
                ui.lineEdit_4_5.setStyleSheet("color: green")
            else:
                ui.lineEdit_4_5.setStyleSheet("color: red")
            kcal2 = 0
            if ui.tableWidget_3.item(0,1).text() != "":
                kcal2 = ui.tableWidget_3.item(0,1).cal
            if ui.tableWidget_3.item(1,1).text() != "":
                kcal2 += ui.tableWidget_3.item(1,1).cal
            if ui.tableWidget_3.item(2,1).text() != "":
                kcal2 += ui.tableWidget_3.item(2,1).cal
            if ui.tableWidget_3.item(3,1).text() != "":
                kcal2 += ui.tableWidget_3.item(3,1).cal
            ui.lineEdit_4_6.setText(str(kcal2))
            if ui.doubleSpin_ET.value() >= kcal2:
                ui.lineEdit_4_6.setStyleSheet("color: green")
            else:
                ui.lineEdit_4_6.setStyleSheet("color: red")
            kcal3 = 0
            if ui.tableWidget_3.item(0,2).text() != "":
                kcal3 = ui.tableWidget_3.item(0,2).cal
            if ui.tableWidget_3.item(1,2).text() != "":
                kcal3 += ui.tableWidget_3.item(1,2).cal
            if ui.tableWidget_3.item(2,2).text() != "":
                kcal3 += ui.tableWidget_3.item(2,2).cal
            if ui.tableWidget_3.item(3,2).text() != "":
                kcal3 += ui.tableWidget_3.item(3,2).cal
            ui.lineEdit_4_7.setText(str(kcal3))
            if ui.doubleSpin_ET.value() >= kcal3:
                ui.lineEdit_4_7.setStyleSheet("color: green")
            else:
                ui.lineEdit_4_7.setStyleSheet("color: red")
            kcal4 = 0
            if ui.tableWidget_3.item(0,3).text() != "":
                kcal4 = ui.tableWidget_3.item(0,3).cal
            if ui.tableWidget_3.item(1,3).text() != "":
                kcal4 += ui.tableWidget_3.item(1,3).cal
            if ui.tableWidget_3.item(2,3).text() != "":
                kcal4 += ui.tableWidget_3.item(2,3).cal
            if ui.tableWidget_3.item(3,3).text() != "":
                kcal4 += ui.tableWidget_3.item(3,3).cal
            ui.lineEdit_4_8.setText(str(kcal4))
            if ui.doubleSpin_ET.value() >= kcal4:
                ui.lineEdit_4_8.setStyleSheet("color: green")
            else:
                ui.lineEdit_4_8.setStyleSheet("color: red")
            kcal5 = 0
            if ui.tableWidget_3.item(0,4).text() != "":
                kcal5 = ui.tableWidget_3.item(0,4).cal
            if ui.tableWidget_3.item(1,4).text() != "":
                kcal5 += ui.tableWidget_3.item(1,4).cal
            if ui.tableWidget_3.item(2,4).text() != "":
                kcal5 += ui.tableWidget_3.item(2,4).cal
            if ui.tableWidget_3.item(3,4).text() != "":
                kcal5 += ui.tableWidget_3.item(3,4).cal
            ui.lineEdit_4_9.setText(str(kcal5))
            if ui.doubleSpin_ET.value() >= kcal5:
                ui.lineEdit_4_9.setStyleSheet("color: green")
            else:
                ui.lineEdit_4_9.setStyleSheet("color: red")
            kcal6 = 0
            if ui.tableWidget_3.item(0,5).text() != "":
                kcal6 = ui.tableWidget_3.item(0,5).cal
            if ui.tableWidget_3.item(1,5).text() != "":
                kcal6 += ui.tableWidget_3.item(1,5).cal
            if ui.tableWidget_3.item(2,5).text() != "":
                kcal6 += ui.tableWidget_3.item(2,5).cal
            if ui.tableWidget_3.item(3,5).text() != "":
                kcal6 += ui.tableWidget_3.item(3,5).cal
            ui.lineEdit_4_10.setText(str(kcal6))
            if ui.doubleSpin_ET.value() >= kcal6:
                ui.lineEdit_4_10.setStyleSheet("color: green")
            else:
                ui.lineEdit_4_10.setStyleSheet("color: red")
            kcal7 = 0
            if ui.tableWidget_3.item(0,6).text() != "":
                kcal7 = ui.tableWidget_3.item(0,6).cal
            if ui.tableWidget_3.item(1,6).text() != "":
                kcal7 += ui.tableWidget_3.item(1,6).cal
            if ui.tableWidget_3.item(2,6).text() != "":
                kcal7 += ui.tableWidget_3.item(2,6).cal
            if ui.tableWidget_3.item(3,6).text() != "":
                kcal7 += ui.tableWidget_3.item(3,6).cal
            ui.lineEdit_4_11.setText(str(kcal7))
            if ui.doubleSpin_ET.value() >= kcal7:
                ui.lineEdit_4_11.setStyleSheet("color: green")
            else:
                ui.lineEdit_4_11.setStyleSheet("color: red")

        elif ui.comboBox.currentIndex() == 3: #Para 3 ingestas
            kcal1 = 0
            if ui.tableWidget_2.item(0,0).text() != "":
                kcal1 = ui.tableWidget_2.item(0,0).cal
            if ui.tableWidget_2.item(1,0).text() != "":
                kcal1 += ui.tableWidget_2.item(1,0).cal
            if ui.tableWidget_2.item(2,0).text() != "":
                kcal1 += ui.tableWidget_2.item(2,0).cal
            ui.lineEdit_3_4.setText(str(kcal1))
            if ui.doubleSpin_ET.value() >= kcal1:
                ui.lineEdit_3_4.setStyleSheet("color: green")
            else:
                ui.lineEdit_3_4.setStyleSheet("color: red")
            kcal2 = 0
            if ui.tableWidget_2.item(0,1).text() != "":
                kcal2 = ui.tableWidget_2.item(0,1).cal
            if ui.tableWidget_2.item(1,1).text() != "":
                kcal2 += ui.tableWidget_2.item(1,1).cal
            if ui.tableWidget_2.item(2,1).text() != "":
                kcal2 += ui.tableWidget_2.item(2,1).cal
            ui.lineEdit_3_5.setText(str(kcal2))
            if ui.doubleSpin_ET.value() >= kcal2:
                ui.lineEdit_3_5.setStyleSheet("color: green")
            else:
                ui.lineEdit_3_5.setStyleSheet("color: red")
            kcal3 = 0
            if ui.tableWidget_2.item(0,2).text() != "":
                kcal3 = ui.tableWidget_2.item(0,2).cal
            if ui.tableWidget_2.item(1,2).text() != "":
                kcal3 += ui.tableWidget_2.item(1,2).cal
            if ui.tableWidget_2.item(2,2).text() != "":
                kcal3 += ui.tableWidget_2.item(2,2).cal
            ui.lineEdit_3_6.setText(str(kcal3))
            if ui.doubleSpin_ET.value() >= kcal3:
                ui.lineEdit_3_6.setStyleSheet("color: green")
            else:
                ui.lineEdit_3_6.setStyleSheet("color: red")
            kcal4 = 0
            if ui.tableWidget_2.item(0,3).text() != "":
                kcal4 = ui.tableWidget_2.item(0,3).cal
            if ui.tableWidget_2.item(1,3).text() != "":
                kcal4 += ui.tableWidget_2.item(1,3).cal
            if ui.tableWidget_2.item(2,3).text() != "":
                kcal4 += ui.tableWidget_2.item(2,3).cal
            ui.lineEdit_3_7.setText(str(kcal4))
            if ui.doubleSpin_ET.value() >= kcal4:
                ui.lineEdit_3_7.setStyleSheet("color: green")
            else:
                ui.lineEdit_3_7.setStyleSheet("color: red")
            kcal5 = 0
            if ui.tableWidget_2.item(0,4).text() != "":
                kcal5 = ui.tableWidget_2.item(0,4).cal
            if ui.tableWidget_2.item(1,4).text() != "":
                kcal5 += ui.tableWidget_2.item(1,4).cal
            if ui.tableWidget_2.item(2,4).text() != "":
                kcal5 += ui.tableWidget_2.item(2,4).cal
            ui.lineEdit_3_8.setText(str(kcal5))
            if ui.doubleSpin_ET.value() >= kcal5:
                ui.lineEdit_3_8.setStyleSheet("color: green")
            else:
                ui.lineEdit_3_8.setStyleSheet("color: red")
            kcal6 = 0
            if ui.tableWidget_2.item(0,5).text() != "":
                kcal6 = ui.tableWidget_2.item(0,5).cal
            if ui.tableWidget_2.item(1,5).text() != "":
                kcal6 += ui.tableWidget_2.item(1,5).cal
            if ui.tableWidget_2.item(2,5).text() != "":
                kcal6 += ui.tableWidget_2.item(2,5).cal
            ui.lineEdit_3_9.setText(str(kcal6))
            if ui.doubleSpin_ET.value() >= kcal6:
                ui.lineEdit_3_9.setStyleSheet("color: green")
            else:
                ui.lineEdit_3_9.setStyleSheet("color: red")
            kcal7 = 0
            if ui.tableWidget_2.item(0,6).text() != "":
                kcal7 = ui.tableWidget_2.item(0,6).cal
            if ui.tableWidget_2.item(1,6).text() != "":
                kcal7 += ui.tableWidget_2.item(1,6).cal
            if ui.tableWidget_2.item(2,6).text() != "":
                kcal7 += ui.tableWidget_2.item(2,6).cal
            ui.lineEdit_3_10.setText(str(kcal7))
            if ui.doubleSpin_ET.value() >= kcal7:
                ui.lineEdit_3_10.setStyleSheet("color: green")
            else:
                ui.lineEdit_3_10.setStyleSheet("color: red")

#Conexion entre Accion Guardar y bbdd
    def AccionGuardar(self,ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Modificacion en la bbdd
        if ui.combo_FM.currentIndex() == 0:
            FM = "F"
        else:
            FM = "M"
        N = ui.lineEdit_Nom.text()
        AP = ui.lineEdit_Apell.text()
        D = ui.date_FNac.date().toString("dd/MM/yyyy")
        DNI = ui.lineEdit_Dni.text()
        DIR = ui.lineEdit_Dir.text()
        TLF = ui.lineEdit_Tlf.text()
        PROF = ui.lineEdit_Prof.text()
        cursor.execute("select p_ddni from Paciente where p_id=?",(self.perfil,))
        DDNI = cursor.fetchone()[0]
        cursor.execute("delete from Paciente where p_id=?",(self.perfil,))
        valores = (self.perfil, unicode(FM), unicode(DNI), unicode(N), unicode(AP), unicode(D), unicode(TLF), unicode(PROF), unicode(DIR), DDNI)
        cursor.execute("insert into Paciente values (?,?,?,?,?,?,?,?,?,?)",valores)

        PS = ui.doubleSpin_Peso.value()
        ALT = ui.doubleSpin_Alt.value()
        IMC = ui.doubleSpin_IMC.value()
        POB = ui.doubleSpin_POb.value()
        CAD = ui.doubleSpin_Cad.value()
        CINT = ui.doubleSpin_Cint.value()
        PT = ui.doubleSpin_Tricip.value()
        if ui.combo_Complex.currentIndex() == 0:
            COMPL = "Delgada"
        elif ui.combo_Complex.currentIndex() == 1:
            COMPL = "Media"
        else:
            COMPL = "Ancha"
        PPAC = ui.doubleSpin_PPac.value()
        MB = ui.doubleSpin_MB.value()
        if ui.combo_Activ.currentIndex() == 0:
            ACT = "Ligera"
        elif ui.combo_Activ.currentIndex() == 1:
            ACT = "Moderada"
        else:
            ACT = "Intensa"
        ET = ui.doubleSpin_ET.value()
        PMG = ui.doubleSpin_PMG.value()
        if ui.comboBox.currentIndex() == 0:
            NUMING = 6
            table = ui.tableWidget_5
        elif ui.comboBox.currentIndex() == 1:
            NUMING = 5
            table = ui.tableWidget_4
        elif ui.comboBox.currentIndex() == 2:
            NUMING = 4
            table = ui.tableWidget_3
        elif ui.comboBox.currentIndex() == 3:
            NUMING = 3
            table = ui.tableWidget_2

        cursor.execute("select an_id, an_infotrat from Antrop_Nec where an_pid=?",(self.perfil,))
        res = cursor.fetchone()
        ANID = res[0]
        ANINFO = res[1]
        cursor.execute("delete from Antrop_Nec where an_id=?",(ANID,))
        valores2 = (ANID,unicode(PS),unicode(ALT),unicode(IMC),unicode(POB),unicode(CAD),unicode(CINT),unicode(PT),COMPL,unicode(PPAC),unicode(MB),ACT,unicode(ET),unicode(NUMING),unicode(PMG),unicode(ANINFO),self.perfil,)
        cursor.execute("insert into Antrop_Nec values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",valores2)

        L1 = ""
        L2 = ""
        L3 = ""
        L4 = ""
        L5 = ""
        L6 = ""
        M1 = ""
        M2 = ""
        M3 = ""
        M4 = ""
        M5 = ""
        M6 = ""
        X1 = ""
        X2 = ""
        X3 = ""
        X4 = ""
        X5 = ""
        X6 = ""
        J1 = ""
        J2 = ""
        J3 = ""
        J4 = ""
        J5 = ""
        J6 = ""
        V1 = ""
        V2 = ""
        V3 = ""
        V4 = ""
        V5 = ""
        V6 = ""
        S1 = ""
        S2 = ""
        S3 = ""
        S4 = ""
        S5 = ""
        S6 = ""
        D1 = ""
        D2 = ""
        D3 = ""
        D4 = ""
        D5 = ""
        D6 = ""
        SUM1 = ""
        SUM2 = ""
        SUM3 = ""
        SUM4 = ""
        SUM5 = ""
        SUM6 = ""
        SUM7 = ""

        if NUMING == 6:
            if table.item(0,0).text():
                L1 = table.item(0,0).text()
                L2 = table.item(1,0).text()
                L3 = table.item(2,0).text()
                L4 = table.item(3,0).text()
                L5 = table.item(4,0).text()
                L6 = table.item(5,0).text()
                M1 = table.item(0,1).text()
                M2 = table.item(1,1).text()
                M3 = table.item(2,1).text()
                M4 = table.item(3,1).text()
                M5 = table.item(4,1).text()
                M6 = table.item(5,1).text()
                X1 = table.item(0,2).text()
                X2 = table.item(1,2).text()
                X3 = table.item(2,2).text()
                X4 = table.item(3,2).text()
                X5 = table.item(4,2).text()
                X6 = table.item(5,2).text()
                J1 = table.item(0,3).text()
                J2 = table.item(1,3).text()
                J3 = table.item(2,3).text()
                J4 = table.item(3,3).text()
                J5 = table.item(4,3).text()
                J6 = table.item(5,3).text()
                V1 = table.item(0,4).text()
                V2 = table.item(1,4).text()
                V3 = table.item(2,4).text()
                V4 = table.item(3,4).text()
                V5 = table.item(4,4).text()
                V6 = table.item(5,4).text()
                S1 = table.item(0,5).text()
                S2 = table.item(1,5).text()
                S3 = table.item(2,5).text()
                S4 = table.item(3,5).text()
                S5 = table.item(4,5).text()
                S6 = table.item(5,5).text()
                D1 = table.item(0,6).text()
                D2 = table.item(1,6).text()
                D3 = table.item(2,6).text()
                D4 = table.item(3,6).text()
                D5 = table.item(4,6).text()
                D6 = table.item(5,6).text()
                SUM1 = ui.lineEdit_6_7.text()
                SUM2 = ui.lineEdit_6_8.text()
                SUM3 = ui.lineEdit_6_9.text()
                SUM4 = ui.lineEdit_6_10.text()
                SUM5 = ui.lineEdit_6_11.text()
                SUM6 = ui.lineEdit_6_12.text()
                SUM7 = ui.lineEdit_6_13.text()
                
        elif NUMING == 5:
            if table.item(0,0).text():
                L1 = table.item(0,0).text()
            	L2 = table.item(1,0).text()
            	L3 = table.item(2,0).text()
            	L4 = table.item(3,0).text()
            	L5 = table.item(4,0).text()
            	L6 = ""
            	M1 = table.item(0,1).text()
            	M2 = table.item(1,1).text()
            	M3 = table.item(2,1).text()
            	M4 = table.item(3,1).text()
            	M5 = table.item(4,1).text()
            	M6 = ""
            	X1 = table.item(0,2).text()
            	X2 = table.item(1,2).text()
            	X3 = table.item(2,2).text()
            	X4 = table.item(3,2).text()
            	X5 = table.item(4,2).text()
            	X6 = ""
            	J1 = table.item(0,3).text()
            	J2 = table.item(1,3).text()
            	J3 = table.item(2,3).text()
            	J4 = table.item(3,3).text()
            	J5 = table.item(4,3).text()
            	J6 = ""
            	V1 = table.item(0,4).text()
            	V2 = table.item(1,4).text()
            	V3 = table.item(2,4).text()
            	V4 = table.item(3,4).text()
            	V5 = table.item(4,4).text()
            	V6 = ""
            	S1 = table.item(0,5).text()
            	S2 = table.item(1,5).text()
            	S3 = table.item(2,5).text()
            	S4 = table.item(3,5).text()
            	S5 = table.item(4,5).text()
            	S6 = ""
            	D1 = table.item(0,6).text()
            	D2 = table.item(1,6).text()
            	D3 = table.item(2,6).text()
            	D4 = table.item(3,6).text()
            	D5 = table.item(4,6).text()
            	D6 = ""
            	SUM1 = ui.lineEdit_5_6.text()
            	SUM2 = ui.lineEdit_5_7.text()
            	SUM3 = ui.lineEdit_5_8.text()
            	SUM4 = ui.lineEdit_5_9.text()
            	SUM5 = ui.lineEdit_5_10.text()
            	SUM6 = ui.lineEdit_5_11.text()
            	SUM7 = ui.lineEdit_5_12.text()

        elif NUMING == 4:
            if table.item(0,0).text():
            	L1 = table.item(0,0).text()
            	L2 = ""
            	L3 = table.item(1,0).text()
            	L4 = table.item(2,0).text()
            	L5 = table.item(3,0).text()
            	L6 = ""
            	M1 = table.item(0,1).text()
            	M2 = ""
            	M3 = table.item(1,1).text()
            	M4 = table.item(2,1).text()
            	M5 = table.item(3,1).text()
            	M6 = ""
            	X1 = table.item(0,2).text()
            	X2 = ""
            	X3 = table.item(1,2).text()
            	X4 = table.item(2,2).text()
            	X5 = table.item(3,2).text()
            	X6 = ""
            	J1 = table.item(0,3).text()
            	J2 = ""
            	J3 = table.item(1,3).text()
            	J4 = table.item(2,3).text()
            	J5 = table.item(3,3).text()
            	J6 = ""
            	V1 = table.item(0,4).text()
            	V2 = ""
            	V3 = table.item(1,4).text()
            	V4 = table.item(2,4).text()
            	V5 = table.item(3,4).text()
            	V6 = ""
            	S1 = table.item(0,5).text()
            	S2 = ""
            	S3 = table.item(1,5).text()
            	S4 = table.item(2,5).text()
            	S5 = table.item(3,5).text()
            	S6 = ""
            	D1 = table.item(0,6).text()
            	D2 = ""
            	D3 = table.item(1,6).text()
            	D4 = table.item(2,6).text()
            	D5 = table.item(3,6).text()
            	D6 = ""
            	SUM1 = ui.lineEdit_4_5.text()
            	SUM2 = ui.lineEdit_4_6.text()
            	SUM3 = ui.lineEdit_4_7.text()
            	SUM4 = ui.lineEdit_4_8.text()
            	SUM5 = ui.lineEdit_4_9.text()
            	SUM6 = ui.lineEdit_4_10.text()
            	SUM7 = ui.lineEdit_4_11.text()

        elif NUMING == 3:
            if table.item(0,0).text():
            	L1 = table.item(0,0).text()
            	L2 = ""
            	L3 = table.item(1,0).text()
            	L4 = ""
            	L5 = table.item(2,0).text()
            	L6 = ""
            	M1 = table.item(0,1).text()
            	M2 = ""
            	M3 = table.item(1,1).text()
            	M4 = ""
            	M5 = table.item(2,1).text()
            	M6 = ""
            	X1 = table.item(0,2).text()
            	X2 = ""
            	X3 = table.item(1,2).text()
            	X4 = ""
            	X5 = table.item(2,2).text()
            	X6 = ""
            	J1 = table.item(0,3).text()
            	J2 = ""
            	J3 = table.item(1,3).text()
            	J4 = ""
            	J5 = table.item(2,3).text()
            	J6 = ""
            	V1 = table.item(0,4).text()
            	V2 = ""
            	V3 = table.item(1,4).text()
            	V4 = ""
            	V5 = table.item(2,4).text()
            	V6 = ""
            	S1 = table.item(0,5).text()
            	S2 = ""
            	S3 = table.item(1,5).text()
            	S4 = ""
            	S5 = table.item(2,5).text()
            	S6 = ""
            	D1 = table.item(0,6).text()
            	D2 = ""
            	D3 = table.item(1,6).text()
            	D4 = ""
            	D5 = table.item(2,6).text()
            	D6 = ""
            	SUM1 = ui.lineEdit_3_4.text()
            	SUM2 = ui.lineEdit_3_5.text()
            	SUM3 = ui.lineEdit_3_6.text()
            	SUM4 = ui.lineEdit_3_7.text()
            	SUM5 = ui.lineEdit_3_8.text()
            	SUM6 = ui.lineEdit_3_9.text()
            	SUM7 = ui.lineEdit_3_10.text()

        cursor.execute("select max(s_id) from Semanario")
        res = cursor.fetchone()
        if res[0] == None:
            SID = 1
        else:
            SID = res[0]+1
        
        SFCH = datetime.date.today().strftime("%d/%m/%Y")
        KCAL = ui.doubleSpin_ET.value()
        
        valores = (SID, unicode(L1), unicode(L2), unicode(L3), unicode(L4), unicode(L5), unicode(L6), unicode(M1), unicode(M2), unicode(M3), unicode(M4), unicode(M5), unicode(M6), unicode(X1), unicode(X2), unicode(X3), unicode(X4), unicode(X5), unicode(X6), unicode(J1), unicode(J2), unicode(J3), unicode(J4), unicode(J5), unicode(J6), unicode(V1), unicode(V2), unicode(V3), unicode(V4), unicode(V5), unicode(V6), unicode(S1), unicode(S2), unicode(S3), unicode(S4), unicode(S5), unicode(S6), unicode(D1), unicode(D2), unicode(D3), unicode(D4), unicode(D5), unicode(D6), unicode(SUM1), unicode(SUM2), unicode(SUM3), unicode(SUM4), unicode(SUM5), unicode(SUM6), unicode(SUM7), unicode(SFCH) , unicode(KCAL), unicode(NUMING), unicode(self.perfil),)
        cursor.execute("insert into Semanario values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",valores)

        bbdd.commit()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
        
#Conexion de boton Ver Recetas y Ventana Ver Recetas
    def VerRecetas(self):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        self.uiVRec.treeWidget.clear()
        cursor.execute("select s_fch, s_numing, s_kcal from Semanario where s_pid=?", (self.perfil,))
        items = cursor.fetchall()
        if items:
            for i in range(len(items)):
                item = QtGui.QTreeWidgetItem(self.uiVRec.treeWidget,0)
                item.setText(0,items[i][0])
                item.setText(1,unicode(items[i][1]))
                item.setText(2,unicode(items[i][2]))
                self.uiVRec.treeWidget.addTopLevelItem(item)
            self.uiVRec.treeWidget.sortItems(0,0)
            self.uiVRec.treeWidget.setCurrentItem(item)
        self.WindowVRec.show()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
        
#Conexion de boton Ver de Ver Recetas y Visor de Recetas
    def to_pdf(self, file_path, is_last=True):
        os.system("soffice -headless -accept=\"socket,port=8100;urp;\"")
        new_file_path = file_path.replace('.odt', '.pdf')
        DocumentConverter().convert(file_path, new_file_path)
        return new_file_path

    def Ver(self, ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        os.system("rm Docu/receta*.* 2> /dev/null")
        class Invoice(dict):
            pass 

        I = self.uiVRec.treeWidget.currentItem()
        cursor.execute("select * from Semanario where s_pid=? and s_fch=?",(self.perfil, unicode(I.text(0)),))
        res = cursor.fetchall()
        L1 = res[0][1]
        L2 = res[0][2]
        L3 = res[0][3]
        L4 = res[0][4]
        L5 = res[0][5]
        L6 = res[0][6]
        M1 = res[0][7]
        M2 = res[0][8]
        M3 = res[0][9]
        M4 = res[0][10]
        M5 = res[0][11]
        M6 = res[0][12]
        X1 = res[0][13]
        X2 = res[0][14]
        X3 = res[0][15]
        X4 = res[0][16]
        X5 = res[0][17]
        X6 = res[0][18]
        J1 = res[0][19]
        J2 = res[0][20]
        J3 = res[0][21]
        J4 = res[0][22]
        J5 = res[0][23]
        J6 = res[0][24]
        V1 = res[0][25]
        V2 = res[0][26]
        V3 = res[0][27]
        V4 = res[0][28]
        V5 = res[0][29]
        V6 = res[0][30]
        S1 = res[0][31]
        S2 = res[0][32]
        S3 = res[0][33]
        S4 = res[0][34]
        S5 = res[0][35]
        S6 = res[0][36]
        D1 = res[0][37]
        D2 = res[0][38]
        D3 = res[0][39]
        D4 = res[0][40]
        D5 = res[0][41]
        D6 = res[0][42]

        if I.text(1) == "3":
            datos = \
                Invoice(customer={'name': ui.lineEdit.text(),
                                  'kcal': I.text(2)},
                        lines=[{'item': {'name': 'Desayuno',
                                         'l': L1,
                                         'm': M1,
                                         'x': X1,
                                         'j': J1,
                                         'v': V1,
                                         's': S1,
                                         'd': D1},},
                               {'item': {'name': 'Almuerzo',
                                         'l': L3,
                                         'm': M3,
                                         'x': X3,
                                         'j': J3,
                                         'v': V3,
                                         's': S3,
                                         'd': D3},},
                               {'item': {'name': 'Cena',
                                         'l': L5,
                                         'm': M5,
                                         'x': X5,
                                         'j': J5,
                                         'v': V5,
                                         's': S5,
                                         'd': D5},},
                               ],
                        id= I.text(0),
                        status='late')

        elif I.text(1) == "4":
            datos = \
                Invoice(customer={'name': ui.lineEdit.text(),
                                  'kcal': I.text(2)},
                        lines=[{'item': {'name': 'Desayuno',
                                         'l': L1,
                                         'm': M1,
                                         'x': X1,
                                         'j': J1,
                                         'v': V1,
                                         's': S1,
                                         'd': D1},},
                               {'item': {'name': 'Almuerzo',
                                         'l': L3,
                                         'm': M3,
                                         'x': X3,
                                         'j': J3,
                                         'v': V3,
                                         's': S3,
                                         'd': D3},},
                               {'item': {'name': 'Merienda',
                                         'l': L4,
                                         'm': M4,
                                         'x': X4,
                                         'j': J4,
                                         'v': V4,
                                         's': S4,
                                         'd': D4},},
                               {'item': {'name': 'Cena',
                                         'l': L5,
                                         'm': M5,
                                         'x': X5,
                                         'j': J5,
                                         'v': V5,
                                         's': S5,
                                         'd': D5},},
                               ],
                        id= I.text(0),
                        status='late')
        elif I.text(1) == "5":
            datos = \
                Invoice(customer={'name': ui.lineEdit.text(),
                                  'kcal': I.text(2)},
                        lines=[{'item': {'name': 'Desayuno',
                                         'l': L1,
                                         'm': M1,
                                         'x': X1,
                                         'j': J1,
                                         'v': V1,
                                         's': S1,
                                         'd': D1},},
                               {'item': {'name': u'Media Ma\xf1ana',
                                         'l': L2,
                                         'm': M2,
                                         'x': X2,
                                         'j': J2,
                                         'v': V2,
                                         's': S2,
                                         'd': D2},},
                               {'item': {'name': 'Almuerzo',
                                         'l': L3,
                                         'm': M3,
                                         'x': X3,
                                         'j': J3,
                                         'v': V3,
                                         's': S3,
                                         'd': D3},},
                               {'item': {'name': 'Merienda',
                                         'l': L4,
                                         'm': M4,
                                         'x': X4,
                                         'j': J4,
                                         'v': V4,
                                         's': S4,
                                         'd': D4},},
                               {'item': {'name': 'Cena',
                                         'l': L5,
                                         'm': M5,
                                         'x': X5,
                                         'j': J5,
                                         'v': V5,
                                         's': S5,
                                         'd': D5},},
                               ],
                        id= I.text(0),
                        status='late')

        elif I.text(1) == "6":
            datos = \
                Invoice(customer={'name': ui.lineEdit.text(),
                                  'kcal': I.text(2)},
                        lines=[{'item': {'name': 'Desayuno',
                                         'l': L1,
                                         'm': M1,
                                         'x': X1,
                                         'j': J1,
                                         'v': V1,
                                         's': S1,
                                         'd': D1},},
                               {'item': {'name': u'Media Ma\xf1ana',
                                         'l': L2,
                                         'm': M2,
                                         'x': X2,
                                         'j': J2,
                                         'v': V2,
                                         's': S2,
                                         'd': D2},},
                               {'item': {'name': 'Almuerzo',
                                         'l': L3,
                                         'm': M3,
                                         'x': X3,
                                         'j': J3,
                                         'v': V3,
                                         's': S3,
                                         'd': D3},},
                               {'item': {'name': 'Merienda',
                                         'l': L4,
                                         'm': M4,
                                         'x': X4,
                                         'j': J4,
                                         'v': V4,
                                         's': S4,
                                         'd': D4},},
                               {'item': {'name': 'Cena',
                                         'l': L5,
                                         'm': M5,
                                         'x': X5,
                                         'j': J5,
                                         'v': V5,
                                         's': S5,
                                         'd': D5},},
                               {'item': {'name': u'Tentempi\xe9',
                                         'l': L6,
                                         'm': M6,
                                         'x': X6,
                                         'j': J6,
                                         'v': V6,
                                         's': S6,
                                         'd': D6},},
                             ],
                        id= I.text(0),
                        status='late')

        basic = Template(source=None, filepath='Docu/basic.odt')
        basic_generated = basic.generate(o=datos).render()
        file('Docu/receta.odt', 'wb').write(basic_generated.getvalue())
        filePDF = self.to_pdf('Docu/receta.odt')
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(filePDF))
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de boton Utilizar de Ver Recetas y treeWidget de MainWindow
    def Utilizar(self, ui):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        item = self.uiVRec.treeWidget.currentItem()
        fecha = item.text(0)
        cursor.execute("select * from Semanario where s_fch=? and s_pid=?",(unicode(fecha),self.perfil,))
        res = cursor.fetchone()
        if res[52] == 3:
            ui.comboBox.setCurrentIndex(3)
            table = ui.tableWidget_2
            L1 = res[1].split(", ")
            cal = 0
            for i in range(len(L1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,0).setText(res[1])
            table.item(0,0).cal = cal
            L3 = res[3].split(", ")
            cal = 0
            for i in range(len(L3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,0).setText(res[3])
            table.item(1,0).cal = cal
            L5 = res[5].split(", ")
            cal = 0
            for i in range(len(L5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,0).setText(res[5])
            table.item(2,0).cal = cal
            M1 = res[7].split(", ")
            cal = 0
            for i in range(len(M1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,1).setText(res[7])
            table.item(0,1).cal = cal
            M3 = res[9].split(", ")
            cal = 0
            for i in range(len(M3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,1).setText(res[9])
            table.item(1,1).cal = cal
            M5 = res[11].split(", ")
            cal = 0
            for i in range(len(M5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,1).setText(res[11])
            table.item(2,1).cal = cal
            X1 = res[13].split(", ")
            cal = 0
            for i in range(len(X1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,2).setText(res[13])
            table.item(0,2).cal = cal
            X3 = res[15].split(", ")
            cal = 0
            for i in range(len(X3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,2).setText(res[15])
            table.item(1,2).cal = cal
            X5 = res[17].split(", ")
            cal = 0
            for i in range(len(X5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,2).setText(res[17])
            table.item(2,2).cal = cal
            J1 = res[19].split(", ")
            cal = 0
            for i in range(len(J1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,3).setText(res[19])
            table.item(0,3).cal = cal
            J3 = res[21].split(", ")
            cal = 0
            for i in range(len(J3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,3).setText(res[21])
            table.item(1,3).cal = cal
            J5 = res[23].split(", ")
            cal = 0
            for i in range(len(J5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,3).setText(res[23])
            table.item(2,3).cal = cal
            V1 = res[25].split(", ")
            cal = 0
            for i in range(len(V1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,4).setText(res[25])
            table.item(0,4).cal = cal
            V3 = res[27].split(", ")
            cal = 0
            for i in range(len(V3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,4).setText(res[27])
            table.item(1,4).cal = cal
            V5 = res[29].split(", ")
            cal = 0
            for i in range(len(V5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,4).setText(res[29])
            table.item(2,4).cal = cal
            S1 = res[31].split(", ")
            cal = 0
            for i in range(len(S1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,5).setText(res[31])
            table.item(0,5).cal = cal
            S3 = res[33].split(", ")
            cal = 0
            for i in range(len(S3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,5).setText(res[33])
            table.item(1,5).cal = cal
            S5 = res[35].split(", ")
            cal = 0
            for i in range(len(S5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,5).setText(res[35])
            table.item(2,5).cal = cal
            D1 = res[37].split(", ")
            cal = 0
            for i in range(len(D1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,6).setText(res[37])
            table.item(0,6).cal = cal
            D3 = res[39].split(", ")
            cal = 0
            for i in range(len(D3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,6).setText(res[39])
            table.item(1,6).cal = cal
            D5 = res[41].split(", ")
            cal = 0
            for i in range(len(D5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,6).setText(res[41])
            table.item(2,6).cal = cal

        elif res[52] == 4:
            ui.comboBox.setCurrentIndex(2)
            table = ui.tableWidget_3
            L1 = res[1].split(", ")
            cal = 0
            for i in range(len(L1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,0).setText(res[1])
            table.item(0,0).cal = cal
            L3 = res[3].split(", ")
            cal = 0
            for i in range(len(L3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,0).setText(res[3])
            table.item(1,0).cal = cal
            L4 = res[4].split(", ")
            cal = 0
            for i in range(len(L4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,0).setText(res[4])
            table.item(2,0).cal = cal
            L5 = res[5].split(",")
            cal = 0
            for i in range(len(L5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,0).setText(res[5])
            table.item(3,0).cal = cal
            M1 = res[7].split(", ")
            cal = 0
            for i in range(len(M1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,1).setText(res[7])
            table.item(0,1).cal = cal
            M3 = res[9].split(", ")
            cal = 0
            for i in range(len(M3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,1).setText(res[9])
            table.item(1,1).cal = cal
            M4 = res[10].split(", ")
            cal = 0
            for i in range(len(M4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,1).setText(res[10])
            table.item(2,1).cal = cal
            M5 = res[11].split(", ")
            cal = 0
            for i in range(len(M5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,1).setText(res[11])
            table.item(3,1).cal = cal
            X1 = res[13].split(", ")
            cal = 0
            for i in range(len(X1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,2).setText(res[13])
            table.item(0,2).cal = cal
            X3 = res[15].split(", ")
            cal = 0
            for i in range(len(X3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,2).setText(res[15])
            table.item(1,2).cal = cal
            X4 = res[16].split(", ")
            cal = 0
            for i in range(len(X4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,2).setText(res[16])
            table.item(2,2).cal = cal
            X5 = res[17].split(", ")
            cal = 0
            for i in range(len(X5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,2).setText(res[17])
            table.item(3,2).cal = cal
            J1 = res[19].split(", ")
            cal = 0
            for i in range(len(J1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,3).setText(res[19])
            table.item(0,3).cal = cal
            J3 = res[21].split(", ")
            cal = 0
            for i in range(len(J3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,3).setText(res[21])
            table.item(1,3).cal = cal
            J4 = res[22].split(", ")
            cal = 0
            for i in range(len(J4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,3).setText(res[22])
            table.item(2,3).cal = cal
            J5 = res[23].split(", ")
            cal = 0
            for i in range(len(J5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,3).setText(res[23])
            table.item(3,3).cal = cal
            V1 = res[25].split(", ")
            cal = 0
            for i in range(len(V1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,4).setText(res[25])
            table.item(0,4).cal = cal
            V3 = res[27].split(", ")
            cal = 0
            for i in range(len(V3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,4).setText(res[27])
            table.item(1,4).cal = cal
            V4 = res[28].split(", ")
            cal = 0
            for i in range(len(V4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,4).setText(res[28])
            table.item(2,4).cal = cal
            V5 = res[29].split(", ")
            cal = 0
            for i in range(len(V5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,4).setText(res[29])
            table.item(3,4).cal = cal
            S1 = res[31].split(", ")
            cal = 0
            for i in range(len(S1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,5).setText(res[31])
            table.item(0,5).cal = cal
            S3 = res[33].split(", ")
            cal = 0
            for i in range(len(S3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,5).setText(res[33])
            table.item(1,5).cal = cal
            S4 = res[34].split(", ")
            cal = 0
            for i in range(len(S4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,5).setText(res[34])
            table.item(2,5).cal = cal
            S5 = res[35].split(", ")
            cal = 0
            for i in range(len(S5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,5).setText(res[35])
            table.item(3,5).cal = cal
            D1 = res[37].split(", ")
            cal = 0
            for i in range(len(D1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,6).setText(res[37])
            table.item(0,6).cal = cal
            D3 = res[39].split(", ")
            cal = 0
            for i in range(len(D3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,6).setText(res[39])
            table.item(1,6).cal = cal
            D4 = res[40].split(", ")
            cal = 0
            for i in range(len(D4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,6).setText(res[40])
            table.item(2,6).cal = cal
            D5 = res[41].split(", ")
            cal = 0
            for i in range(len(D5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,6).setText(res[41])
            table.item(3,6).cal = cal

        elif res[52] == 5:
            ui.comboBox.setCurrentIndex(1)
            table = ui.tableWidget_4
            L1 = res[1].split(", ")
            cal = 0
            for i in range(len(L1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,0).setText(res[1])
            table.item(0,0).cal = cal
            L2 = res[2].split(", ")
            cal = 0
            for i in range(len(L2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,0).setText(res[2])
            table.item(1,0).cal = cal
            L3 = res[3].split(", ")
            cal = 0
            for i in range(len(L3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,0).setText(res[3])
            table.item(2,0).cal = cal
            L4 = res[4].split(", ")
            cal = 0
            for i in range(len(L4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,0).setText(res[4])
            table.item(3,0).cal = cal
            L5 = res[5].split(", ")
            cal = 0
            for i in range(len(L5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,0).setText(res[5])
            table.item(4,0).cal = cal
            M1 = res[7].split(", ")
            cal = 0
            for i in range(len(M1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,1).setText(res[7])
            table.item(0,1).cal = cal
            M2 = res[8].split(", ")
            cal = 0
            for i in range(len(M2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,1).setText(res[8])
            table.item(1,1).cal = cal
            M3 = res[9].split(", ")
            cal = 0
            for i in range(len(M3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,1).setText(res[9])
            table.item(2,1).cal = cal
            M4 = res[10].split(", ")
            cal = 0
            for i in range(len(M4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,1).setText(res[10])
            table.item(3,1).cal = cal
            M5 = res[11].split(", ")
            cal = 0
            for i in range(len(M5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,1).setText(res[11])
            table.item(4,1).cal = cal
            X1 = res[13].split(", ")
            cal = 0
            for i in range(len(X1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,2).setText(res[13])
            table.item(0,2).cal = cal
            X2 = res[14].split(", ")
            cal = 0
            for i in range(len(X2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,2).setText(res[14])
            table.item(1,2).cal = cal
            X3 = res[15].split(", ")
            cal = 0
            for i in range(len(X3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,2).setText(res[15])
            table.item(2,2).cal = cal
            X4 = res[16].split(", ")
            cal = 0
            for i in range(len(X4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,2).setText(res[16])
            table.item(3,2).cal = cal
            X5 = res[17].split(", ")
            cal = 0
            for i in range(len(X5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,2).setText(res[17])
            table.item(4,2).cal = cal
            J1 = res[19].split(", ")
            cal = 0
            for i in range(len(J1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,3).setText(res[19])
            table.item(0,3).cal = cal
            J2 = res[20].split(", ")
            cal = 0
            for i in range(len(J2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,3).setText(res[20])
            table.item(1,3).cal = cal
            J3 = res[21].split(", ")
            cal = 0
            for i in range(len(J3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,3).setText(res[21])
            table.item(2,3).cal = cal
            J4 = res[22].split(", ")
            cal = 0
            for i in range(len(J4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,3).setText(res[22])
            table.item(3,3).cal = cal
            J5 = res[23].split(", ")
            cal = 0
            for i in range(len(J5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,3).setText(res[23])
            table.item(4,3).cal = cal
            V1 = res[25].split(", ")
            cal = 0
            for i in range(len(V1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,4).setText(res[25])
            table.item(0,4).cal = cal
            V2 = res[26].split(", ")
            cal = 0
            for i in range(len(V2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,4).setText(res[26])
            table.item(1,4).cal = cal
            V3 = res[27].split(", ")
            cal = 0
            for i in range(len(V3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,4).setText(res[27])
            table.item(2,4).cal = cal
            V4 = res[28].split(", ")
            cal = 0
            for i in range(len(V4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,4).setText(res[28])
            table.item(3,4).cal = cal
            V5 = res[29].split(", ")
            cal = 0
            for i in range(len(V5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,4).setText(res[29])
            table.item(4,4).cal = cal
            S1 = res[31].split(", ")
            cal = 0
            for i in range(len(S1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,5).setText(res[31])
            table.item(0,5).cal = cal
            S2 = res[32].split(", ")
            cal = 0
            for i in range(len(S2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,5).setText(res[32])
            table.item(1,5).cal = cal
            S3 = res[33].split(", ")
            cal = 0
            for i in range(len(S3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,5).setText(res[33])
            table.item(2,5).cal = cal
            S4 = res[34].split(", ")
            cal = 0
            for i in range(len(S4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,5).setText(res[34])
            table.item(3,5).cal = cal
            S5 = res[35].split(", ")
            cal = 0
            for i in range(len(S5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,5).setText(res[35])
            table.item(4,5).cal = cal
            D1 = res[37].split(", ")
            cal = 0
            for i in range(len(D1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,6).setText(res[37])
            table.item(0,6).cal = cal
            D2 = res[38].split(", ")
            cal = 0
            for i in range(len(D2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,6).setText(res[38])
            table.item(1,6).cal = cal
            D3 = res[39].split(", ")
            cal = 0
            for i in range(len(D3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,6).setText(res[39])
            table.item(2,6).cal = cal
            D4 = res[40].split(", ")
            cal = 0
            for i in range(len(D4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,6).setText(res[40])
            table.item(3,6).cal = cal
            D5 = res[41].split(", ")
            cal = 0
            for i in range(len(D5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,6).setText(res[41])
            table.item(4,6).cal = cal

        elif res[52] == 6:
            ui.comboBox.setCurrentIndex(0)
            table = ui.tableWidget_5
            L1 = res[1].split(", ")
            cal = 0
            for i in range(len(L1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,0).setText(res[1])
            table.item(0,0).cal = cal
            L2 = res[2].split(", ")
            cal = 0
            for i in range(len(L2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,0).setText(res[2])
            table.item(1,0).cal = cal
            L3 = res[3].split(", ")
            cal = 0
            for i in range(len(L3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,0).setText(res[3])
            table.item(2,0).cal = cal
            L4 = res[4].split(", ")
            cal = 0
            for i in range(len(L4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,0).setText(res[4])
            table.item(3,0).cal = cal
            L5 = res[5].split(", ")
            cal = 0
            for i in range(len(L5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,0).setText(res[5])
            table.item(4,0).cal = cal
            L6 = res[6].split(", ")
            cal = 0
            for i in range(len(L6)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(L6[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(5,0).setText(res[6])
            table.item(5,0).cal = cal
            M1 = res[7].split(", ")
            cal = 0
            for i in range(len(M1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,1).setText(res[7])
            table.item(0,1).cal = cal
            M2 = res[8].split(", ")
            cal = 0
            for i in range(len(M2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,1).setText(res[8])
            table.item(1,1).cal = cal
            M3 = res[9].split(", ")
            cal = 0
            for i in range(len(M3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,1).setText(res[9])
            table.item(2,1).cal = cal
            M4 = res[10].split(", ")
            cal = 0
            for i in range(len(M4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,1).setText(res[10])
            table.item(3,1).cal = cal
            M5 = res[11].split(", ")
            cal = 0
            for i in range(len(M5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,1).setText(res[11])
            table.item(4,1).cal = cal
            M6 = res[12].split(", ")
            cal = 0
            for i in range(len(M6)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(M6[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(5,1).setText(res[1])
            table.item(5,1).cal = cal
            X1 = res[13].split(", ")
            cal = 0
            for i in range(len(X1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,2).setText(res[13])
            table.item(0,2).cal = cal
            X2 = res[14].split(", ")
            cal = 0
            for i in range(len(X2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,2).setText(res[14])
            table.item(1,2).cal = cal
            X3 = res[15].split(", ")
            cal = 0
            for i in range(len(X3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,2).setText(res[15])
            table.item(2,2).cal = cal
            X4 = res[16].split(", ")
            cal = 0
            for i in range(len(X4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,2).setText(res[16])
            table.item(3,2).cal = cal
            X5 = res[17].split(", ")
            cal = 0
            for i in range(len(X5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,2).setText(res[17])
            table.item(4,2).cal = cal
            X6 = res[18].split(", ")
            cal = 0
            for i in range(len(X6)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(X6[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(5,2).setText(res[18])
            table.item(5,2).cal = cal
            J1 = res[19].split(", ")
            cal = 0
            for i in range(len(J1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,3).setText(res[19])
            table.item(0,3).cal = cal
            J2 = res[20].split(", ")
            cal = 0
            for i in range(len(J2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,3).setText(res[20])
            table.item(1,3).cal = cal
            J3 = res[21].split(", ")
            cal = 0
            for i in range(len(J3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,3).setText(res[21])
            table.item(2,3).cal = cal
            J4 = res[22].split(", ")
            cal = 0
            for i in range(len(J4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,3).setText(res[22])
            table.item(3,3).cal = cal
            J5 = res[23].split(", ")
            cal = 0
            for i in range(len(J5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,3).setText(res[23])
            table.item(4,3).cal = cal
            J6 = res[24].split(", ")
            cal = 0
            for i in range(len(J6)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(J6[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(5,3).setText(res[24])
            table.item(5,3).cal = cal
            V1 = res[25].split(", ")
            cal = 0
            for i in range(len(V1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,4).setText(res[25])
            table.item(0,4).cal = cal
            V2 = res[26].split(", ")
            cal = 0
            for i in range(len(V2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,4).setText(res[26])
            table.item(1,4).cal = cal
            V3 = res[27].split(", ")
            cal = 0
            for i in range(len(V3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,4).setText(res[27])
            table.item(2,4).cal = cal
            V4 = res[28].split(", ")
            cal = 0
            for i in range(len(V4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,4).setText(res[28])
            table.item(3,4).cal = cal
            V5 = res[29].split(", ")
            cal = 0
            for i in range(len(V5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,4).setText(res[29])
            table.item(4,4).cal = cal
            V6 = res[30].split(", ")
            cal = 0
            for i in range(len(V6)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(V6[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(5,4).setText(res[30])
            table.item(5,4).cal = cal
            S1 = res[31].split(", ")
            cal = 0
            for i in range(len(S1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,5).setText(res[31])
            table.item(0,5).cal = cal
            S2 = res[32].split(", ")
            cal = 0
            for i in range(len(S2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,5).setText(res[32])
            table.item(1,5).cal = cal
            S3 = res[33].split(", ")
            cal = 0
            for i in range(len(S3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,5).setText(res[33])
            table.item(2,5).cal = cal
            S4 = res[34].split(", ")
            cal = 0
            for i in range(len(S4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,5).setText(res[34])
            table.item(3,5).cal = cal
            S5 = res[35].split(", ")
            cal = 0
            for i in range(len(S5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,5).setText(res[35])
            table.item(4,5).cal = cal
            S6 = res[36].split(", ")
            cal = 0
            for i in range(len(S6)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(S6[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(5,5).setText(res[36])
            table.item(5,5).cal = cal
            D1 = res[37].split(", ")
            cal = 0
            for i in range(len(D1)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D1[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(0,6).setText(res[37])
            table.item(0,6).cal = cal
            D2 = res[38].split(", ")
            cal = 0
            for i in range(len(D2)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D2[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(1,6).setText(res[38])
            table.item(1,6).cal = cal
            D3 = res[39].split(", ")
            cal = 0
            for i in range(len(D3)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D3[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(2,6).setText(res[39])
            table.item(2,6).cal = cal
            D4 = res[40].split(", ")
            cal = 0
            for i in range(len(D4)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D4[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(3,6).setText(res[40])
            table.item(3,6).cal = cal
            D5 = res[41].split(", ")
            cal = 0
            for i in range(len(D5)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D5[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(4,6).setText(res[41])
            table.item(4,6).cal = cal
            D6 = res[42].split(", ")
            cal = 0
            for i in range(len(D6)):
                cursor.execute("select r_cal from Receta where r_nombre=?",(D6[i],))
                kres = cursor.fetchone()
                if kres != None:
                    cal += kres[0]
            table.item(5,6).setText(res[42])
            table.item(5,6).cal = cal

        self.WindowVRec.close()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

#Conexion de Accion Imprimir e imprimir pdf
    def Imprimir(self, ui, dietista):
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta en la bbdd
        #Utilizamos poppler, puesto que qt no soporta nativamente pdf
        
        dperfil = dietista.ObtenerPerfil()

        class Invoice(dict):
            pass 

        cursor.execute("select max(s_id) from Semanario where s_pid=?",(self.perfil,))
        sid = cursor.fetchone()
        if sid != None:
            cursor.execute("select s_fch from Semanario where s_id=? order by s_fch limit 1",(sid[0],))
            fchd = cursor.fetchone()
            if fchd != None:
                fch = fchd[0]
                cursor.execute("select * from Semanario where s_id=?",(sid[0],))
                res = cursor.fetchall()
                L1 = res[0][1]
                L2 = res[0][2]
                L3 = res[0][3]
                L4 = res[0][4]
                L5 = res[0][5]
                L6 = res[0][6]
                M1 = res[0][7]
                M2 = res[0][8]
                M3 = res[0][9]
                M4 = res[0][10]
                M5 = res[0][11]
                M6 = res[0][12]
                X1 = res[0][13]
                X2 = res[0][14]
                X3 = res[0][15]
                X4 = res[0][16]
                X5 = res[0][17]
                X6 = res[0][18]
                J1 = res[0][19]
                J2 = res[0][20]
                J3 = res[0][21]
                J4 = res[0][22]
                J5 = res[0][23]
                J6 = res[0][24]
                V1 = res[0][25]
                V2 = res[0][26]
                V3 = res[0][27]
                V4 = res[0][28]
                V5 = res[0][29]
                V6 = res[0][30]
                S1 = res[0][31]
                S2 = res[0][32]
                S3 = res[0][33]
                S4 = res[0][34]
                S5 = res[0][35]
                S6 = res[0][36]
                D1 = res[0][37]
                D2 = res[0][38]
                D3 = res[0][39]
                D4 = res[0][40]
                D5 = res[0][41]
                D6 = res[0][42]
            
                L1s = res[0][1].split(', ')
                L2s = res[0][2].split(', ')
                L3s = res[0][3].split(', ')
                L4s = res[0][4].split(', ')
                L5s = res[0][5].split(', ')
                L6s = res[0][6].split(', ')
                M1s = res[0][7].split(', ')
                M2s = res[0][8].split(', ')
                M3s = res[0][9].split(', ')
                M4s = res[0][10].split(', ')
                M5s = res[0][11].split(', ')
                M6s = res[0][12].split(', ')
                X1s = res[0][13].split(', ')
                X2s = res[0][14].split(', ')
                X3s = res[0][15].split(', ')
                X4s = res[0][16].split(', ')
                X5s = res[0][17].split(', ')
                X6s = res[0][18].split(', ')
                J1s = res[0][19].split(', ')
                J2s = res[0][20].split(', ')
                J3s = res[0][21].split(', ')
                J4s = res[0][22].split(', ')
                J5s = res[0][23].split(', ')
                J6s = res[0][24].split(', ')
                V1s = res[0][25].split(', ')
                V2s = res[0][26].split(', ')
                V3s = res[0][27].split(', ')
                V4s = res[0][28].split(', ')
                V5s = res[0][29].split(', ')
                V6s = res[0][30].split(', ')
                S1s = res[0][31].split(', ')
                S2s = res[0][32].split(', ')
                S3s = res[0][33].split(', ')
                S4s = res[0][34].split(', ')
                S5s = res[0][35].split(', ')
                S6s = res[0][36].split(', ')
                D1s = res[0][37].split(', ')
                D2s = res[0][38].split(', ')
                D3s = res[0][39].split(', ')
                D4s = res[0][40].split(', ')
                D5s = res[0][41].split(', ')
                D6s = res[0][42].split(', ')

                items = []
                if res[0][52] == 3:
                    data = dict(customer={'name': ui.lineEdit.text(),
                                          'kcal': res[0][51]},
                                lines=[{'item': {'name': 'Desayuno',
                                                 'l': L1,
                                                 'm': M1,
                                                 'x': X1,
                                                 'j': J1,
                                                 'v': V1,
                                                 's': S1,
                                                 'd': D1},},
                                       {'item': {'name': 'Almuerzo',
                                                 'l': L3,
                                                 'm': M3,
                                                 'x': X3,
                                                 'j': J3,
                                                 'v': V3,
                                                 's': S3,
                                                 'd': D3},},
                                       {'item': {'name': 'Cena',
                                                 'l': L5,
                                                 'm': M5,
                                                 'x': X5,
                                                 'j': J5,
                                                 'v': V5,
                                                 's': S5,
                                                 'd': D5},},
                                       ])
                    
                    for i in range(len(L1s)):
                        items.append(L1s[i])
                    for i in range(len(L3s)):
                        items.append(L3s[i])
                    for i in range(len(L5s)):
                        items.append(L5s[i])
                    for i in range(len(M1s)):
                        items.append(M1s[i])
                    for i in range(len(M3s)):
                        items.append(M3s[i])
                    for i in range(len(M5s)):
                        items.append(M5s[i])
                    for i in range(len(X1s)):
                        items.append(X1s[i])
                    for i in range(len(X3s)):
                        items.append(X3s[i])
                    for i in range(len(X5s)):
                        items.append(X5s[i])
                    for i in range(len(J1s)):
                        items.append(J1s[i])
                    for i in range(len(J3s)):
                        items.append(J3s[i])
                    for i in range(len(J5s)):
                        items.append(J5s[i])
                    for i in range(len(V1s)):
                        items.append(V1s[i])
                    for i in range(len(V3s)):
                        items.append(V3s[i])
                    for i in range(len(V5s)):
                        items.append(V5s[i])
                    for i in range(len(S1s)):
                        items.append(S1s[i])
                    for i in range(len(S3s)):
                        items.append(S3s[i])
                    for i in range(len(S5s)):
                        items.append(S5s[i])
                    for i in range(len(D1s)):
                        items.append(D1s[i])
                    for i in range(len(D3s)):
                        items.append(D3s[i])
                    for i in range(len(D5s)):
                        items.append(D5s[i])

                    lista = sorted(set(items))

                elif res[0][52] == 4:
                    data = dict(customer={'name': ui.lineEdit.text(),
                                          'kcal': res[0][51]},
                                lines=[{'item': {'name': 'Desayuno',
                                                 'l': L1,
                                                 'm': M1,
                                                 'x': X1,
                                                 'j': J1,
                                                 'v': V1,
                                                 's': S1,
                                                 'd': D1},},
                                       {'item': {'name': 'Almuerzo',
                                                 'l': L3,
                                                 'm': M3,
                                                 'x': X3,
                                                 'j': J3,
                                                 'v': V3,
                                                 's': S3,
                                                 'd': D3},},
                                       {'item': {'name': 'Merienda',
                                                 'l': L4,
                                                 'm': M4,
                                                 'x': X4,
                                                 'j': J4,
                                                 'v': V4,
                                                 's': S4,
                                                 'd': D4},},
                                       {'item': {'name': 'Cena',
                                                 'l': L5,
                                                 'm': M5,
                                                 'x': X5,
                                                 'j': J5,
                                                 'v': V5,
                                                 's': S5,
                                                 'd': D5},},
                                       ])
                
                    for i in range(len(L1s)):
                        items.append(L1s[i])
                    for i in range(len(L3s)):
                        items.append(L3s[i])
                    for i in range(len(L4s)):
                        items.append(L4s[i])
                    for i in range(len(L5s)):
                        items.append(L5s[i])
                    for i in range(len(M1s)):
                        items.append(M1s[i])
                    for i in range(len(M3s)):
                        items.append(M3s[i])
                    for i in range(len(M4s)):
                        items.append(M4s[i])
                    for i in range(len(M5s)):
                        items.append(M5s[i])
                    for i in range(len(X1s)):
                        items.append(X1s[i])
                    for i in range(len(X3s)):
                        items.append(X3s[i])
                    for i in range(len(X4s)):
                        items.append(X4s[i])
                    for i in range(len(X5s)):
                        items.append(X5s[i])
                    for i in range(len(J1s)):
                        items.append(J1s[i])
                    for i in range(len(J3s)):
                        items.append(J3s[i])
                    for i in range(len(J4s)):
                        items.append(J4s[i])
                    for i in range(len(J5s)):
                        items.append(J5s[i])
                    for i in range(len(V1s)):
                        items.append(V1s[i])
                    for i in range(len(V3s)):
                        items.append(V3s[i])
                    for i in range(len(V4s)):
                        items.append(V4s[i])
                    for i in range(len(V5s)):
                        items.append(V5s[i])
                    for i in range(len(S1s)):
                        items.append(S1s[i])
                    for i in range(len(S3s)):
                        items.append(S3s[i])
                    for i in range(len(S4s)):
                        items.append(S4s[i])
                    for i in range(len(S5s)):
                        items.append(S5s[i])
                    for i in range(len(D1s)):
                        items.append(D1s[i])
                    for i in range(len(D3s)):
                        items.append(D3s[i])
                    for i in range(len(D4s)):
                        items.append(D4s[i])
                    for i in range(len(D5s)):
                        items.append(D5s[i])

                    lista = sorted(set(items))

                elif res[0][52] == 5:
                    data = dict(customer={'name': ui.lineEdit.text(),
                                          'kcal': res[0][51]},
                                lines=[{'item': {'name': 'Desayuno',
                                                 'l': L1,
                                                 'm': M1,
                                                 'x': X1,
                                                 'j': J1,
                                                 'v': V1,
                                                 's': S1,
                                                 'd': D1},},
                                       {'item': {'name': u'Media Ma\xf1ana',
                                                 'l': L2,
                                                 'm': M2,
                                                 'x': X2,
                                                 'j': J2,
                                                 'v': V2,
                                                 's': S2,
                                                 'd': D2},},
                                       {'item': {'name': 'Almuerzo',
                                                 'l': L3,
                                                 'm': M3,
                                                 'x': X3,
                                                 'j': J3,
                                                 'v': V3,
                                                 's': S3,
                                                 'd': D3},},
                                       {'item': {'name': 'Merienda',
                                                 'l': L4,
                                                 'm': M4,
                                                 'x': X4,
                                                 'j': J4,
                                                 'v': V4,
                                                 's': S4,
                                                 'd': D4},},
                                       {'item': {'name': 'Cena',
                                                 'l': L5,
                                                 'm': M5,
                                                 'x': X5,
                                                 'j': J5,
                                                 'v': V5,
                                                 's': S5,
                                                 'd': D5},},
                                       ])
                
                    for i in range(len(L1s)):
                        items.append(L1s[i])
                    for i in range(len(L2s)):
                        items.append(L2s[i])
                    for i in range(len(L3s)):
                        items.append(L3s[i])
                    for i in range(len(L4s)):
                        items.append(L4s[i])
                    for i in range(len(L5s)):
                        items.append(L5s[i])
                    for i in range(len(M1s)):
                        items.append(M1s[i])
                    for i in range(len(M2s)):
                        items.append(M2s[i])
                    for i in range(len(M3s)):
                        items.append(M3s[i])
                    for i in range(len(M4s)):
                        items.append(M4s[i])
                    for i in range(len(M5s)):
                        items.append(M5s[i])
                    for i in range(len(X1s)):
                        items.append(X1s[i])
                    for i in range(len(X2s)):
                        items.append(X2s[i])
                    for i in range(len(X3s)):
                        items.append(X3s[i])
                    for i in range(len(X4s)):
                        items.append(X4s[i])
                    for i in range(len(X5s)):
                        items.append(X5s[i])
                    for i in range(len(J1s)):
                        items.append(J1s[i])
                    for i in range(len(J2s)):
                        items.append(J2s[i])
                    for i in range(len(J3s)):
                        items.append(J3s[i])
                    for i in range(len(J4s)):
                        items.append(J4s[i])
                    for i in range(len(J5s)):
                        items.append(J5s[i])
                    for i in range(len(V1s)):
                        items.append(V1s[i])
                    for i in range(len(V2s)):
                        items.append(V2s[i])
                    for i in range(len(V3s)):
                        items.append(V3s[i])
                    for i in range(len(V4s)):
                        items.append(V4s[i])
                    for i in range(len(V5s)):
                        items.append(V5s[i])
                    for i in range(len(S1s)):
                        items.append(S1s[i])
                    for i in range(len(S3s)):
                        items.append(S3s[i])
                    for i in range(len(S4s)):
                        items.append(S4s[i])
                    for i in range(len(S5s)):
                        items.append(S5s[i])
                    for i in range(len(D1s)):
                        items.append(D1s[i])
                    for i in range(len(D2s)):
                        items.append(D2s[i])
                    for i in range(len(D3s)):
                        items.append(D3s[i])
                    for i in range(len(D4s)):
                        items.append(D4s[i])
                    for i in range(len(D5s)):
                        items.append(D5s[i])

                    lista = sorted(set(items))

                elif res[0][52] == 6:
                    data = dict(customer={'name': ui.lineEdit.text(),
                                          'kcal': res[0][51]},
                                lines=[{'item': {'name': 'Desayuno',
                                                 'l': L1,
                                                 'm': M1,
                                                 'x': X1,
                                                 'j': J1,
                                                 'v': V1,
                                                 's': S1,
                                                 'd': D1},},
                                       {'item': {'name': u'Media Ma\xf1ana',
                                                 'l': L2,
                                                 'm': M2,
                                                 'x': X2,
                                                 'j': J2,
                                                 'v': V2,
                                                 's': S2,
                                                 'd': D2},},
                                       {'item': {'name': 'Almuerzo',
                                                 'l': L3,
                                                 'm': M3,
                                                 'x': X3,
                                                 'j': J3,
                                                 'v': V3,
                                                 's': S3,
                                                 'd': D3},},
                                       {'item': {'name': 'Merienda',
                                                 'l': L4,
                                                 'm': M4,
                                                 'x': X4,
                                                 'j': J4,
                                                 'v': V4,
                                                 's': S4,
                                                 'd': D4},},
                                       {'item': {'name': 'Cena',
                                                 'l': L5,
                                                 'm': M5,
                                                 'x': X5,
                                                 'j': J5,
                                                 'v': V5,
                                                 's': S5,
                                                 'd': D5},},
                                       {'item': {'name': u'Tentempi\xe9',
                                                 'l': L6,
                                                 'm': M6,
                                                 'x': X6,
                                                 'j': J6,
                                                 'v': V6,
                                                 's': S6,
                                                 'd': D6},},
                                       ])
                
                    for i in range(len(L1s)):
                        items.append(L1s[i])
                    for i in range(len(L2s)):
                        items.append(L2s[i])
                    for i in range(len(L3s)):
                        items.append(L3s[i])
                    for i in range(len(L4s)):
                        items.append(L4s[i])
                    for i in range(len(L5s)):
                        items.append(L5s[i])
                    for i in range(len(L6s)):
                        items.append(L6s[i])
                    for i in range(len(M1s)):
                        items.append(M1s[i])
                    for i in range(len(M2s)):
                        items.append(M2s[i])
                    for i in range(len(M3s)):
                        items.append(M3s[i])
                    for i in range(len(M4s)):
                        items.append(M4s[i])
                    for i in range(len(M5s)):
                        items.append(M5s[i])
                    for i in range(len(M6s)):
                        items.append(M6s[i])
                    for i in range(len(X1s)):
                        items.append(X1s[i])
                    for i in range(len(X2s)):
                        items.append(X2s[i])
                    for i in range(len(X3s)):
                        items.append(X3s[i])
                    for i in range(len(X4s)):
                        items.append(X4s[i])
                    for i in range(len(X5s)):
                        items.append(X5s[i])
                    for i in range(len(X6s)):
                        items.append(X6s[i])
                    for i in range(len(J1s)):
                        items.append(J1s[i])
                    for i in range(len(J2s)):
                        items.append(J2s[i])
                    for i in range(len(J3s)):
                        items.append(J3s[i])
                    for i in range(len(J4s)):
                        items.append(J4s[i])
                    for i in range(len(J5s)):
                        items.append(J5s[i])
                    for i in range(len(J6s)):
                        items.append(J6s[i])
                    for i in range(len(V1s)):
                        items.append(V1s[i])
                    for i in range(len(V2s)):
                        items.append(V2s[i])
                    for i in range(len(V3s)):
                        items.append(V3s[i])
                    for i in range(len(V4s)):
                        items.append(V4s[i])
                    for i in range(len(V5s)):
                        items.append(V5s[i])
                    for i in range(len(V6s)):
                        items.append(V6s[i])
                    for i in range(len(S1s)):
                        items.append(S1s[i])
                    for i in range(len(S3s)):
                        items.append(S3s[i])
                    for i in range(len(S4s)):
                        items.append(S4s[i])
                    for i in range(len(S5s)):
                        items.append(S5s[i])
                    for i in range(len(S6s)):
                        items.append(S6s[i])
                    for i in range(len(D1s)):
                        items.append(D1s[i])
                    for i in range(len(D2s)):
                        items.append(D2s[i])
                    for i in range(len(D3s)):
                        items.append(D3s[i])
                    for i in range(len(D4s)):
                        items.append(D4s[i])
                    for i in range(len(D5s)):
                        items.append(D5s[i])
                    for i in range(len(D6s)):
                        items.append(D6s[i])

                    lista = sorted(set(items))


                recetas = []
                nomprep_recs = []
                for i in lista:
                    cursor.execute("select * from Receta_Ingredientes where ri_nomrec=? and ri_ddni=?",(i,dperfil,))
                    ingrs = cursor.fetchall()
                    cursor.execute("select r_prep from Receta where r_nombre=? and r_ddni=?",(i,dperfil,))
                    resprep = cursor.fetchone()
                    if resprep != None:
                        prep = resprep[0]
                    else:
                        prep = ""
                    if res != None:
                        rece = []
                        for j in range(len(ingrs)):
                            rec = {'elemento':{'ingr': ingrs[j][2],'cant': ingrs[j][3],}}
                            rece.append(rec)
                            
                        nomprep_rec = {'item': {'name': i+':',
                                                'ingreds': rece,
                                                'prep': prep},}
                        
                        nomprep_recs.append(nomprep_rec)
                        data['nomprep_recs'] = nomprep_recs
                        data['id']= fch

                    datos = \
                        Invoice(dict(data))
            
                basic = Template(source=None, filepath='Docu/basicweek.odt')
                basic_generated = basic.generate(o=datos).render()
                file('Docu/semanario.odt', 'wb').write(basic_generated.getvalue())
                filePDF = self.to_pdf('Docu/semanario.odt')
                
                ruta = os.getcwd()
                ruta = ruta + "/Docu/semanario.pdf"
                printer = QtGui.QPrinter()
                dialog = QtGui.QPrintDialog(printer)
                document = popplerqt4.Poppler.Document.load(ruta)
            
                if (dialog.exec_() == 1):
                    painter = QtGui.QPainter(printer)
                    npage = 0
                    while npage < document.numPages(): 
                        img = document.page(npage).renderToImage(100,100)
                        painter.drawImage(QtCore.QPoint(0,0),img)
                        if npage < document.numPages()-1:
                            printer.newPage()
                        npage = npage + 1
                    painter.end()
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()
