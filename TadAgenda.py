"""TAD AGENDA"""
from TadPaciente import *
from TadCita import *

"""ATRIBUTOS:"""
# cita: Cita

def crearAgenda():
    #retorna agenda vacia
    
    agenda=[]
    return agenda

def existeCita(agenda,cita):
    #retorna verdadero si existe la cita en la agenda
    
    return cita in agenda

def agregarCita(agenda, cita):
    #agrega tipo Cita en Agenda
    
    agenda.append(cita)

def eliminarCita(agenda):
    #eliminar tipo Cita en Agenda
    agenda.pop()
    
def eliminarCitaPorOS(agenda, obraSocial):
    #eliminar tipo Cita en Agenda por obra social

    agenda.remove(obraSocial)

"""def listarCitas(agenda):
    #retorna listado de citas de la agenda
    
    return agenda"""

def tamanioAgenda(agenda): 
    #retorna cantidad de citas que posee la agenda

    return len(agenda)

def modificarAgenda(agenda, fechaActual, fechaDestino):
    #modificar todas las citas con fechaActual a fechaDestino 

    for cita in agenda: 
        if(verFecha(cita)==fechaActual):
            modFecha(cita, fechaDestino)