# -*- coding: utf-8 -*-
import sys, os
import math
import datetime
import sqlite3 as dbapi

sys.path.append('PY_UIs')
#os.chdir("/usr/share/edp11/")

from edp11 import *
from tabla_niveles import *
from dietista import *
from paciente import *
from receta import *
from ingrediente import *
from GUI import *

def main():
#Declaraciones de la GUI Principal
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedWidth(908)
    MainWindow.setFixedHeight(610)
    MainWindow.show()

#Declaraciones de la accion Abrir Perfil Dietista
    gui = GUI(ui,MainWindow)

#Conexion de accion Abrir Perfil Dietista y GUI Perfil Dietista
    dietista = Dietista(gui)
    dietista.VentanaAbrir()

    gui.conectarAct(ui.actionDietista, dietista.MostrarDietistas)

#Declaraciones de la accion Cerrar Perfil 
    dietista.VentanaCerrar()

#Conexion de accion Cerrar Perfil y GUI Cerrar Perfil
    gui.conectarAct(ui.actionCerrar_Perfil, dietista.WindowCPer.show)
    gui.conectarAcp(dietista.uiCPe.buttonBox, dietista.CerrarPerf)

#Declaraciones de la accion Nuevo Paciente
    paciente = Paciente(gui)
    objetos = Objetos()
    paciente.VentanaNuevo()

#Conexion de accion Nuevo Paciente y GUI Nuevo Paciente  
    gui.conectarAct(ui.actionNuevo_Paciente, paciente.NuevoPaciente)
    gui.conectarAcp(paciente.uiNP.buttonBox, lambda: paciente.MostrarVentana2NPaciente(paciente.uiNP))
    gui.conectarRej(paciente.uiNP2.buttonBox, paciente.WindowNewPac.show)

#Declaraciones de la accion Abrir Paciente
    paciente.VentanaAbrir()

#Conexion de accion Abrir Paciente y GUI Abrir Paciente
    gui.conectarAct(ui.actionAbrir_Paciente, lambda: paciente.AbrirPaciente(ui,dietista))
    gui.conectarAcp(paciente.uiAP.buttonBox, lambda: paciente.MostrarDatosP(ui))

#Declaraciones de la accion Eliminar Paciente
    paciente.VentanaEliminar()
    
#Conexion de accion Eliminar Paciente y GUI Eliminar Paciente
    gui.conectarAct(ui.actionEliminar_Paciente, lambda: paciente.EliminarPaciente(ui,dietista))
    gui.conectarAcp(paciente.uiEP.buttonBox, paciente.DropPaciente)
#Declaraciones de la accion Cerrar Paciente
    paciente.VentanaCerrar()

#Conexion de accion Cerrar Paciente y GUI Cerrar Paciente
    gui.conectarAct(ui.actionCerrar_Paciente, paciente.WindowCPac.show)
    gui.conectarAcp(paciente.uiCP.buttonBox, lambda: paciente.CerrarPaciente(ui,objetos)
)
    gui.conectarAcp(dietista.uiCPe.buttonBox, lambda: paciente.CerrarPaciente(ui,objetos))
    gui.conectarAcp(dietista.uiCPe.buttonBox, gui.QuitarEnabled)

#Declaraciones de la accion Nueva Receta
    receta = Receta()

#Conexion de accion Nueva Receta y GUI Nueva Receta
    receta.VentanaNueva()
    gui.conectarAct(ui.actionNueva_Receta, receta.Nueva_Receta)

#Declaraciones de la accion Modificar Receta
    receta.VentanaModif()

#Conexion de accion Modificar Receta y GUIs Modificar Receta
    gui.conectarAct(ui.actionEditar_Receta, lambda: receta.SeleccionarReceta(dietista))
    gui.conectarAcp(receta.uiSR.buttonBox, lambda: receta.VentanaModificar(dietista))
    gui.conectarRej(receta.uiMR.buttonBox, receta.WindowSelRec.show)
    gui.conectarAcp(dietista.uiCPe.buttonBox, lambda: receta.InicializarTreeWidget(ui))

#Declaraciones de la accion Modificar Receta
    receta.VentanaElim()

#Conexion de accion Eliminar Receta y GUI Eliminar Receta
    gui.conectarAct(ui.actionEliminar_Receta, lambda: receta.listElimReceta(dietista))
    gui.conectarAcp(receta.uiER.buttonBox, lambda: receta.DropReceta(dietista))

#Copia nombre y apellidos en rotulo
    def copiaNA():
        ui.lineEdit.setText(ui.lineEdit_Nom.text()+" "+ui.lineEdit_Apell.text())

    gui.conectarText(ui.lineEdit_Nom, copiaNA)
    gui.conectarText(ui.lineEdit_Apell, copiaNA)

#Calcular IMC a partir de peso / altura^2
    def modificaIMC():
        if ui.doubleSpin_Peso.value() != 0:
            if ui.doubleSpin_Alt.value() != 0:
                imc = ui.doubleSpin_Peso.value() / (math.pow(ui.doubleSpin_Alt.value() / 100,2.0))
                ui.doubleSpin_IMC.setValue(imc)    

    gui.conectarValue(ui.doubleSpin_Peso, modificaIMC)
    gui.conectarValue(ui.doubleSpin_Alt, modificaIMC)
    
#Determinar Grado de obesidad segun IMC
    def dotarGrado():
        if ui.doubleSpin_IMC.value() < 25:
            ui.toolButton_Grado.setText("Ok")
            ui.toolButton_Grado.setStyleSheet("color: #0dc434")
        elif 25 <= ui.doubleSpin_IMC.value() <= 27.99:
            ui.toolButton_Grado.setText("I")
            ui.toolButton_Grado.setStyleSheet("color: #feff0d")
        elif 28 <= ui.doubleSpin_IMC.value() <= 31.99:
            ui.toolButton_Grado.setText("II")
            ui.toolButton_Grado.setStyleSheet("color: #ee9711")
        elif 32 <= ui.doubleSpin_IMC.value() <= 41.99:
            ui.toolButton_Grado.setText("III")
            ui.toolButton_Grado.setStyleSheet("color: #ff0000")
        elif ui.doubleSpin_IMC.value() >= 42:
            ui.toolButton_Grado.setText("IV")
            ui.toolButton_Grado.setStyleSheet("color: #aa0821")

    gui.conectarValue(ui.doubleSpin_IMC, dotarGrado)
    gui.conectarValue(ui.doubleSpin_Peso, dotarGrado)
    gui.conectarValue(ui.doubleSpin_Alt, dotarGrado)

#Declaraciones del toolButton Grado obesidad
    WindowNivel = QtGui.QDialog()
    uiNiv = Ui_DialogNivel()
    uiNiv.setupUi(WindowNivel)

#Conexion de toolButton Grado obesidad y GUI Tabla Niveles
    gui.conectarClic(ui.toolButton_Grado,  WindowNivel.show)
    gui.conectarAcp(uiNiv.pushButton, WindowNivel.accept)

#Calculo edad a partir de fecha
    def calcularEdad(ui):
        hoy = datetime.date.today()
        fechaNac = datetime.date(ui.date_FNac.date().year(), ui.date_FNac.date().month(), ui.date_FNac.date().day())
        cumple = fechaNac.replace(year = hoy.year)
        anio = (hoy.year - fechaNac.year)
        if anio > 0:
            if hoy >= cumple:
                ui.lineEdit_Edad.setText(str(anio))
            elif hoy < cumple:
                ui.lineEdit_Edad.setText(str(anio-1))
        else:
            ui.lineEdit_Edad.setText("0")

    gui.conectar(ui.date_FNac, QtCore.SIGNAL("dateChanged(QDate)"), lambda: calcularEdad(ui))
    gui.conectar(paciente.uiNP.date_FNac, QtCore.SIGNAL("dateChanged(QDate)"), lambda: calcularEdad(paciente.uiNP))
 
#Calculo metabolismo basal
    def calcularMB():
        if ui.combo_FM.currentIndex() == 0:
            mb = 8.7 * ui.doubleSpin_POb.value() + 829
            ui.doubleSpin_MB.setValue(mb)
        elif ui.combo_FM.currentIndex() == 1:
            mb = 11.6 * ui.doubleSpin_POb.value() + 879
            ui.doubleSpin_MB.setValue(mb)

    gui.conectarValue(ui.doubleSpin_POb, calcularMB)
    gui.conectarIndex(ui.combo_FM, calcularMB)

#Incremento segun Actividad
    def modificarMB():
        if ui.combo_FM.currentIndex() == 0: #Mujer
            if ui.combo_Activ.currentIndex() == 0: #Delgada
                incr = 1.56 * ui.doubleSpin_MB.value() 
            elif ui.combo_Activ.currentIndex() == 1:  #Media
                incr =  1.64 * ui.doubleSpin_MB.value()
            elif ui.combo_Activ.currentIndex() == 2:  #Ancha
                incr =  1.82 * ui.doubleSpin_MB.value()
        elif ui.combo_FM.currentIndex() == 1: #Hombre
            if ui.combo_Activ.currentIndex() == 0: #Delgada
                incr = 1.55 * ui.doubleSpin_MB.value()
            elif ui.combo_Activ.currentIndex() == 1: #Media
                incr = 1.78 * ui.doubleSpin_MB.value()
            elif ui.combo_Activ.currentIndex() == 2: #Ancha
                incr = 2.1 * ui.doubleSpin_MB.value()
        ui.doubleSpin_Increm.setValue(incr)

    gui.conectarValue(ui.doubleSpin_MB, modificarMB)
    gui.conectarIndex(ui.combo_Activ, modificarMB)
    gui.conectarIndex(ui.combo_FM, modificarMB)

#Reduccion segun edad
    def reducirMB():
        if "40" <= ui.lineEdit_Edad.text() <= "49":
            red = ui.doubleSpin_Increm.value() * 5 / 100
        elif "50" <= ui.lineEdit_Edad.text() <= "59":
            red = ui.doubleSpin_Increm.value() * 10 / 100
        elif "60" <= ui.lineEdit_Edad.text() <= "69":
            red = ui.doubleSpin_Increm.value() * 20 / 100
        elif ui.lineEdit_Edad.text() > "70":
            red = ui.doubleSpin_Increm.value() * 30 / 100
        else:
            red = 0
        ui.doubleSpin_Reduc.setValue(red)

    gui.conectar(ui.date_FNac, QtCore.SIGNAL("dateChanged(QDate)"), reducirMB)
    gui.conectarValue(ui.doubleSpin_Increm, reducirMB)

#Calculo Energia Total
    def calcularET():
        et = ui.doubleSpin_Increm.value() - ui.doubleSpin_Reduc.value()
        ui.doubleSpin_ET.setValue(et)

    gui.conectarValue(ui.doubleSpin_Increm, calcularET)
    gui.conectarValue(ui.doubleSpin_Reduc, calcularET)

#Calculo rango necesidades energeticas(Glucidica,Lipidica,Proteica) en orden
    def calcularNG():
        inf = ui.doubleSpin_ET.value() * 50 / 100
        sup = ui.doubleSpin_ET.value() * 60 / 100
        rango = str(inf) + " - " + str(sup)
        ui.lineEdit_NG.setText(rango)

    def calcularNL():
        inf = ui.doubleSpin_ET.value() * 30 / 100
        sup = ui.doubleSpin_ET.value() * 35 / 100
        rango = str(inf) + " - " + str(sup)
        ui.lineEdit_NL.setText(rango)

    def calcularNP():
        inf = ui.doubleSpin_ET.value() * 12 / 100
        sup = ui.doubleSpin_ET.value() * 15 / 100
        rango = str(inf) + " - " + str(sup)
        ui.lineEdit_NP.setText(rango)

    gui.conectarValue(ui.doubleSpin_ET, calcularNG)
    gui.conectarValue(ui.doubleSpin_ET, calcularNL)
    gui.conectarValue(ui.doubleSpin_ET, calcularNP)

#Calculo KCal / % segun numero de ingestas
    def repartoingestas():
        if ui.comboBox.currentIndex() == 0: #6 ingestas
            linea1 = linea6 = ui.doubleSpin_ET.value() * 5 / 100
            linea2 = linea4 = ui.doubleSpin_ET.value() * 15 / 100
            linea3 = linea5 = ui.doubleSpin_ET.value() * 30 / 100
            ui.lineEdit_6_1.setText(str(round(linea1,3)))
            ui.lineEdit_6_2.setText(str(round(linea2,3)))
            ui.lineEdit_6_3.setText(str(round(linea3,3)))           
            ui.lineEdit_6_4.setText(str(round(linea4,3)))
            ui.lineEdit_6_5.setText(str(round(linea5,3)))
            ui.lineEdit_6_6.setText(str(round(linea6,3)))
        elif ui.comboBox.currentIndex() == 1: #5 ingestas
            linea1 = ui.doubleSpin_ET.value() * 10 / 100
            linea2 = linea4 = ui.doubleSpin_ET.value() * 15 / 100
            linea3 = linea5 = ui.doubleSpin_ET.value() * 30 / 100
            ui.lineEdit_5_1.setText(str(round(linea1,3)))
            ui.lineEdit_5_2.setText(str(round(linea2,3)))
            ui.lineEdit_5_3.setText(str(round(linea3,3)))           
            ui.lineEdit_5_4.setText(str(round(linea4,3)))
            ui.lineEdit_5_5.setText(str(round(linea5,3)))
        elif ui.comboBox.currentIndex() == 2: #4 ingestas
            linea1 = linea3 = ui.doubleSpin_ET.value() * 15 / 100
            linea2 = linea4 = ui.doubleSpin_ET.value() * 30 / 100
            ui.lineEdit_4_1.setText(str(round(linea1,3)))
            ui.lineEdit_4_2.setText(str(round(linea2,3)))
            ui.lineEdit_4_3.setText(str(round(linea3,3)))           
            ui.lineEdit_4_4.setText(str(round(linea4,3)))
        elif ui.comboBox.currentIndex() == 3: #3 ingestas
            linea1 = ui.doubleSpin_ET.value() * 25 / 100
            linea2 = ui.doubleSpin_ET.value() * 40 / 100
            linea3 = ui.doubleSpin_ET.value() * 35 / 100
            ui.lineEdit_3_1.setText(str(round(linea1,3)))
            ui.lineEdit_3_2.setText(str(round(linea2,3)))
            ui.lineEdit_3_3.setText(str(round(linea3,3)))           

    gui.conectarValue(ui.doubleSpin_ET, repartoingestas)
    gui.conectarIndex(ui.comboBox, repartoingestas)
    
#Calculo de Peso Ideal con BBDD
    def filtrarPI():
        if ui.combo_FM.currentIndex() == 0:
            FM = "F"
        elif ui.combo_FM.currentIndex() == 1:
            FM = "M"
        if ui.combo_Complex.currentIndex() == 0:
            COMP = "Delgada"
        elif ui.combo_Complex.currentIndex() == 1:
            COMP = "Media"
        elif ui.combo_Complex.currentIndex() == 2:
            COMP = "Ancha"
        ALT = str(ui.doubleSpin_Alt.value())
        return (FM,COMP,ALT,)
    
    def mostrarPI():
        valores = filtrarPI()
        #Declaracion y conexion con la bbdd
        bbdd = dbapi.connect('edp11.bd')
        cursor = bbdd.cursor()
        #Consulta a la bbdd y guardado del resultado
        cursor.execute("select pi_peso from Peso_Ideal where pi_fm=? and pi_compl=? and pi_alt=? ", valores)
        row = cursor.fetchone()
        #Establecer valor obtenido en lineedit de peso ideal
        if row != None:
            row = row[0]
            ui.lineEdit_PIdeal.setText(row)
        #Cierre de la bbdd y de la consulta
        cursor.close()
        bbdd.close()

    gui.conectarValue(ui.doubleSpin_Alt, mostrarPI)
    gui.conectarIndex(ui.combo_Complex, mostrarPI)
    gui.conectarIndex(ui.combo_FM, mostrarPI)
    
#Declaracion Registro Dietista
    dietista.VentanaRegistro()
    
#Conexion button Nuevo de abrir perfil dietista y GUI Registro Dietista
    gui.conectarRej(dietista.uiRD.buttonBox, dietista.WindowPDiet.show)
    gui.conectarClic(dietista.uiPD.Button_Nuevo, dietista.Nuevo)
    gui.conectarAcp(dietista.uiRD.buttonBox, dietista.GuardarDietista)

#Declaracion GUI Eliminar Perfil
    dietista.VentanaEliminar()

#Conexion button eliminar de abrir perfil dietista y treeWidget  
    gui.conectarRej(dietista.uiEP.buttonBox, dietista.WindowPDiet.show)
    gui.conectarClic(dietista.uiPD.Button_Elim, dietista.Eliminar)
    gui.conectarAcp(dietista.uiEP.buttonBox, dietista.ElimPerf)

#Declaracion GUI Perfil Dietista Pass
    dietista.VentanaLogin()

#Conexion button Aceptar de Perfil Dietista y GUI Perfil Dietista Pass
    gui.conectarAcp(dietista.uiPD.buttonBox, dietista.AceptarPass)

#Conexion button Cancelar de Perfil Dietista Pass y GUI Perfil Dietista
    gui.conectarRej(dietista.uiPDP.buttonBox, dietista.WindowPDiet.show)

#Comprobacion de Perfil Dietista y password
    gui.conectarAcp(dietista.uiPDP.buttonBox, lambda: dietista.Aceptar(ui))
    gui.conectarAcp(dietista.uiPDP.buttonBox, lambda: receta.MostrarRecetas(dietista,ui))

#Declaraciones de GUI Anadir Ingredientes
    receta.VentanaAnadirIngr()

#Conexion de button Anadir y GUI Anadir Ingredientes
    #Para Nueva Receta
    gui.conectarClic(receta.uiNR.push_Anadir, lambda: receta.MostrarAnadirIngrediente(receta.uiAI, receta.WindowAIngr))

    #Para Modificar Receta
    gui.conectarClic(receta.uiMR.push_Anadir, lambda: receta.MostrarAnadirIngrediente(receta.uiAI, receta.WindowAIngr))

#Declaraciones de GUI Nuevo Ingrediente
    ingrediente = Ingrediente()
    ingrediente.VentanaNuevo()
    ingrediente.VentanaModificar()

#Conexion de button Nuevo de GUI Anadir Ingredientes y GUI Nuevo Ingrediente
    gui.conectarClic(receta.uiAI.push_Nuevo, ingrediente.NuevoIngr)

#Conexion de combo medida de GUI Nuevo Ingrediente y lineEdit ud | gr | ml
    gui.conectarIndex(ingrediente.uiNI.combo_udgr, lambda: ingrediente.Cantidad(ingrediente.uiNI))
    gui.conectarIndex(ingrediente.uiMI.combo_udgr, lambda: ingrediente.Cantidad(ingrediente.uiMI))

#Conexion de buttonBox Aceptar y treeWidget de Anadir Ingrediente con BBDD
    gui.conectarAcp(ingrediente.uiNI.buttonBox, lambda: ingrediente.GuardarIngrediente(receta))
    gui.conectarAcp(ingrediente.uiNI.buttonBox, lambda: ingrediente.RecogerPreferencias(objetos))

#Conexion de button Modificar de GUI Anadir Ingredientes y GUI Nuevo Ingrediente
    gui.conectarClic(receta.uiAI.push_Modificar, lambda: receta.ModificarIngr(ingrediente))
    gui.conectarAcp(ingrediente.uiMI.buttonBox, lambda: ingrediente.ModificarIngrediente(receta))

#Conexion de Aceptar de Añadir Ingrediente y treeWidget de Nueva Receta
    gui.conectarAcp(receta.uiAI.buttonBox, lambda: receta.AgregarIngr(receta.uiNR))

#Conexion de Aceptar de Añadir Ingrediente y treeWidget de Modificar  Receta
    gui.conectarAcp(receta.uiAI.buttonBox, lambda: receta.AgregarIngr(receta.uiMR))

#Conexion de push_Eliminar de GUI Nueva Receta y treeWidget
    gui.conectarClic(receta.uiNR.push_Eliminar, lambda: receta.EliminarIngr(receta.uiNR))

#Conexion de push_Eliminar de GUI Modificar Receta y treeWidget
    gui.conectarClic(receta.uiMR.push_Eliminar, lambda: receta.EliminarIngr(receta.uiMR))

#Conexion de Aceptar de GUI Nueva Receta, bbdd y treeWidget de MainWindow
    gui.conectarAcp(receta.uiNR.buttonBox, lambda: receta.GuardarReceta(receta.uiNR ,dietista))
    #Añadir Receta a treeWidget recetas
    gui.conectarAcp(receta.uiNR.buttonBox, lambda: receta.MostrarRecetas(dietista,ui))

#Conexion de Aceptar de GUI Modificar Receta, bbdd y treeWidget de MainWindow
    gui.conectarAcp(receta.uiMR.buttonBox, lambda: receta.GuardarReceta(receta.uiMR ,dietista))
    #Añadir Receta a treeWidget recetas
    gui.conectarAcp(receta.uiMR.buttonBox, lambda: receta.MostrarRecetas(dietista,ui))
    #Borrar Receta de treeWidget recetas
    gui.conectarAcp(receta.uiER.buttonBox, lambda: receta.MostrarRecetas(dietista,ui))

#Conexion de Rechazar de GUI Modificar Receta y bbdd
    def CancelarModif(receta, dietista):
        receta.GuardarReceta(receta.uiMR, dietista)
        receta.SeleccionarReceta(dietista)

    gui.conectarRej(receta.uiMR.buttonBox, lambda: CancelarModif(receta, dietista))

#Conexion de Aceptar uiNP2 y guardar Paciente
    gui.conectarAcp(paciente.uiNP2.buttonBox, lambda: paciente.GuardarPaciente(dietista))

#Conexion boton Informacion Medica y Ventana Info Med
    paciente.VentanaInfoMed()

    gui.conectarClic(ui.pushButton_InfMed, paciente.AbrirInfoMed)
    gui.conectarClic(ui.toolButton, paciente.AbrirInfoMed)

#Conexion de Anadir Ventana Informacion Medica y dialogo abrir Archivo
    gui.conectarClic(paciente.uiInfoM.pushButton_Anadir, paciente.abrirDialogo)

#Conexion de Eliminar de Ventana Informacion Medica y treeWidget
    gui.conectarClic(paciente.uiInfoM.pushButton_Eliminar, paciente.EliminarAnalitica)

#Conexion boton Ver Analitica de Ventana Informacion Medica y PDF
    gui.conectarClic(paciente.uiInfoM.pushButton, paciente.VerAnalitica)

#Conexion boton añadirEP de Ventana Informacion Medica y Dialogo Enfermedades
    paciente.VentanaEnfermedad()

    gui.conectarClic(paciente.uiInfoM.pushButton_AnadirEP, paciente.MostrarListadoEnf)

#Conexion boton Nuevo de Ventana Enfer y Patologias y Dialogo Agregar Enfermedad
    paciente.VentanaNEnfermedad()

    gui.conectarClic(paciente.uiEnfer.push_Nuevo, paciente.MostrarVentanaNEnfermedad)

#Conexion boton añadirEP de Ventana Informacion Medica y Dialogo Enfermedades
    paciente.VentanaNEnfIngred()

    gui.conectarClic(paciente.uiNEnfer.push_Anadir, lambda: paciente.MostrarVentanaSelEIngr(receta))

#Conexion boton Aceptar Ventana Inf Medica y bbdd por trat farma
    gui.conectarAcp(paciente.uiInfoM.buttonBox, lambda: paciente.GuardarTrat(ui))
    gui.conectarAcp(paciente.uiInfoM.buttonBox, lambda: paciente.ExcluirRecetasEnf(dietista,receta,ui))
    gui.conectarAcp(paciente.uiAP.buttonBox, lambda: paciente.ExcluirRecetasEnf(dietista,receta,ui))

#Conexion de Añadir en tratamiento de apoyo y GUI trat
    paciente.VentanaTrataApoyo()

    gui.conectarClic(ui.pushButton_Anadir, paciente.MostrarVentanaTratApoyo)
    gui.conectarAcp(paciente.uiNTA.buttonBox, lambda: paciente.MostrarTratA(ui))
    gui.conectarClic(ui.pushButton_Elim, lambda: paciente.ElimItem(ui))

#Conexion boton Aceptar de Selec Ingredientes de Enfermedades y Dialogo Nueva Enfermedad
    gui.conectarAcp(paciente.uiNEI.buttonBox, paciente.SeleccionarEnfIngred)

#Conexion boton Eliminar Dialogo Nueva Enfermedad y treeWidget
    gui.conectarClic(paciente.uiNEnfer.push_Elim, lambda: paciente.EliminarIngredEnf(paciente.uiNEnfer))

#Conexion boton Aceptar Dialogo Nueva Enfermedad y Dialogo Enfermedades
    gui.conectarAcp(paciente.uiNEnfer.buttonBox, paciente.CrearEnfermedad)

#Conexion boton Eliminar Dialogo Enfermedades y treeWidget
    gui.conectarClic(paciente.uiEnfer.push_Elim, paciente.ElimEnfBBDD)
    gui.conectarClic(paciente.uiEnfer.push_Elim, lambda: paciente.EliminarIngredEnf(paciente.uiEnfer))

#Conexion boton Aceptar Dialogo Nueva Enfermedad y Dialogo Enfermedades
    gui.conectarAcp(paciente.uiEnfer.buttonBox, paciente.AnadirEnfermedad)

#Conexion boton Eliminar Dialogo Enfermedades y treeWidget
    gui.conectarClic(paciente.uiInfoM.pushButton_EliminarEP, lambda: paciente.EliminarEP(paciente.uiInfoM))

#Conexion de boton Informacion General y Gui ventana Info Gen
    paciente.VentanaInfoGen()

    gui.conectarClic(ui.pushButton_InfG, paciente.MostrarInfoGen)

#Conexion de boton Aceptar de InfoGen y bbdd
    gui.conectarAcp(paciente.uiInfoG.buttonBox, paciente.GuardarInfoG)

#Conexion de boton Diario Dietetico y Gui ventana Diario Dietetico
    paciente.VentanaDiarioD()

    gui.conectarClic(ui.pushButton_DiDiet, paciente.AbrirDiarioDiet)

#Conexion de Anadir Ventana Diario Dietetico y dialogo abrir Archivo
    gui.conectarClic(paciente.uiDiarioD.pushButton_Anadir, paciente.abrirDialogoD)

#Conexion de Eliminar de Ventana Diario Dietetico y treeWidget
    gui.conectarClic(paciente.uiDiarioD.pushButton_Eliminar, paciente.EliminarDiario)

#Conexion boton Ver Analitica de Ventana Diario Dietetico y PDF
    gui.conectarClic(paciente.uiDiarioD.pushButton_Ver, paciente.VerDiario)

#Conexion de boton Recordatorio 24h y Gui ventana Recordatorio
    paciente.VentanaRecordatorio()

    gui.conectarClic(ui.pushButton_Record, paciente.AbrirRecordatorio)

#Conexion de Anadir Ventana Recordatorio y dialogo abrir Archivo
    gui.conectarClic(paciente.uiRecordatorio.pushButton_Anadir, paciente.abrirDialogoR)

#Conexion de Eliminar de Ventana Recordatorio y treeWidget
    gui.conectarClic(paciente.uiRecordatorio.pushButton_Eliminar, paciente.EliminarRecordatorio)

#Conexion boton Ver Analitica de Ventana Recordatorio y PDF
    gui.conectarClic(paciente.uiRecordatorio.pushButton_Ver, paciente.VerRecordatorio)

#Conexion boton Formulario de Ventana Diario Dietetico e imprimir
#Conexion boton Diario Dietetico de Nuevo Paciente e imprimir
    gui.conectarClic(paciente.uiDiarioD.pushButton_Form, paciente.ImprimirDiarioD)
    gui.conectarClic(paciente.uiNP2.pushButton_DiDiet, paciente.ImprimirDiarioD)

#Conexion boton Formulario de Ventana Recordatorio e imprimir
#Conexion boton Recordatorio 24h de Nuevo Paciente e imprimir
    gui.conectarClic(paciente.uiRecordatorio.pushButton_Form, paciente.ImprimirRecordatorio)
    gui.conectarClic(paciente.uiNP2.pushButton_Record, paciente.ImprimirRecordatorio)

#Conexion de boton Cuestionario de Frecuencia de Nuevo Paciente y Gui CuestFrec
#Conexion boton Cuestionario de Frecuencia y Gui Cuestionario de Frecuencia
    paciente.VentanaCuestFrec()

    gui.conectarClic(paciente.uiNP2.pushButton_Cuest, lambda: paciente.AbrirCuestionarioFrec(objetos))
    gui.conectarClic(ui.pushButton_Cuest, lambda: paciente.AbrirCuestionarioFrec(objetos))
    gui.conectarClic(ui.pushButton_Cuest, lambda: paciente.MostrarPreferencias(objetos, ingrediente))

#Conexion de boton Aceptar de Cuestionario de Frecuencia y bbdd
    gui.conectarAcp(paciente.uiCuestFrec.buttonBox, lambda: paciente.GuardarCuestionarioFrec(objetos))

#Conexion de TableWidget segun nº ingestas y lineEdits correspondientes
    gui.conectarClic(ui.push_Kcal_6, lambda: paciente.CalcularKcalDia(ui))
    gui.conectarClic(ui.push_Kcal_5, lambda: paciente.CalcularKcalDia(ui))
    gui.conectarClic(ui.push_Kcal_4, lambda: paciente.CalcularKcalDia(ui))
    gui.conectarClic(ui.push_Kcal_3, lambda: paciente.CalcularKcalDia(ui))

#Conexion de Perdida de materia grasa y perdida de liquidos
    def PMG():
        PL = 100 - ui.doubleSpin_PMG.value()
        ui.doubleSpin_PL.setValue(PL)
    def PL():
        PMG = 100 - ui.doubleSpin_PL.value()
        ui.doubleSpin_PMG.setValue(PMG)

    gui.conectarValue(ui.doubleSpin_PMG, PMG)
    gui.conectarValue(ui.doubleSpin_PL, PL)

#Conexion de Accion Guardar y bbdd
    gui.conectarAct(ui.actionGuardar, lambda: paciente.AccionGuardar(ui))

#Conexion de boton Ver Recetas y Ventana Ver Recetas
    paciente.VentanaVerRecetas()

    gui.conectarClic(ui.push_VerRecetas, paciente.VerRecetas)

#Conexion de boton Ver de Ver Recetas y Visor de Recetas
    gui.conectarClic(paciente.uiVRec.Button_Ver, lambda: paciente.Ver(ui))

#Conexion de boton Utilizar de Ver Recetas y treeWidget de MainWindow
    gui.conectarClic(paciente.uiVRec.Button_Utilizar, lambda: paciente.Utilizar(ui))

#Conexion de Accion Imprimir e imprimir pdf
    gui.conectarAct(ui.actionImprimir, lambda: paciente.Imprimir(ui, dietista))

#Conexion de Acerca de y Ventana de Acerca de
    gui.VentanaAcercade()
    
    gui.conectarAct(ui.actionAcerca_de, gui.WindowAcercade.show)

#Conexion de Manual y Manual de usuario
    gui.conectarAct(ui.actionManual, gui.MostrarManual)

#Conexion de Manual y Manual de usuario
    gui.conectarClic(gui.uiA.pushButton_Licencia, gui.MostrarLicencia)

#Conexion de Creditos y Ventana de Creditos
    gui.VentanaCreditos()
    
    gui.conectarClic(gui.uiA.pushButton_Credit, gui.WindowCreditos.show)

#Cerrar cualquier ventana si se cierra la principal
    def CerrarVentanas():
        QtGui.QApplication.closeAllWindows()

    gui.conectarAct(ui.actionSalir, CerrarVentanas)

#Finalizacion del programa
    sys.exit(app.exec_())    

if __name__ == "__main__":    
    main()
