import numpy
import colorama
import os
import msvcrt
from colorama import Style,Back,Fore
import random

estudiantes=numpy.empty([10,8],object)


def printv(texto):
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{texto}{Back.GREEN}{Fore.RESET}{Style.RESET_ALL}{Back.RESET}")


def printr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Back.RED}{Fore.RESET}{Style.RESET_ALL}{Back.RESET}")


def limpiarpantalla():
    printv("<<<PRESIONE UNA TECLA PARA CONTINUAR>>>")
    msvcrt.getch()
    os.system("cls")


def Validarrut(rut):
    for i in range(7):
        if estudiantes[i,0]==rut:
         return i
    else:
        -1




 


def guardar(rut,nombre_alumno,edad,genero,promedio,fecha_matricula,nombre_apoderado):
    if None in (estudiantes):
        if len(rut)<0:
            if len(nombre_alumno)>=2 and (nombre_alumno)<=30:
                if (edad)>=4:
                    for i in range():
                     if estudiantes[i,0] is None:
                      estudiantes[i,0]=rut
                      estudiantes[i,1]=nombre_alumno
                      estudiantes[i,2]=edad
                      estudiantes[i,3]=genero
                      estudiantes[i,4]=promedio
                      estudiantes[i,5]=fecha_matricula
                      estudiantes[i,6]=nombre_apoderado
                      printv(f"Estudiante {i,1} registrado")
                      break
                else:
                   printr("La edad de alumno debe ser mayor o igual a 4")
            else:
               printr("El nombre del alumno debe ser mayor  o igual a 2 y menor o igual a 30")



def listar(rut):
    for i in range(8):
     if estudiantes[i,0] is not None:
      printv(f"{estudiantes[i,0],{estudiantes[i,1]},{estudiantes[i,2]},{estudiantes[i,3]},{estudiantes[i,4]},{estudiantes[i,5]},{estudiantes[i,6]}}")







anotaciones=[]
anotaciones.append("EL ESTUDIANTE AGREDE A COMPAÑERO CON UNA BOTELLA DE CHAMITO")
anotaciones.append("EL ESTUDIANTE ES FELICITADO POR SU AYUDA EN EL DIA DE LAS MADRES")
anotaciones.append("EL ESTUDIANTE INSUALTA A SU PROFESOR DICIENDOLE QUE NO SABE EDUCAR NI A SUS PERROS" )
anotaciones.append("EL ESTUDIANTE PREPARA UN ASADO EN PLENA CLASE")
anotaciones.append("EL ESTUDIANTE SE FELICITA POR SU PARTICIPACION EN CLASES")
anotaciones.append("EL ESTUDIANTE BROMEA CON HUMOR NEGRO EN LA SALA DE CLASES")


notas=[]
notas.append("EL PROMEDI DEL ESTUDIANTE ES DE 7.0")
notas.append("EL PROMEDI DEL ESTUDIANTE ES DE 6.0")
notas.append("EL PROMEDI DEL ESTUDIANTE ES DE 5.0")
notas.append("EL PROMEDI DEL ESTUDIANTE ES DE 4.0")
notas.append("EL PROMEDI DEL ESTUDIANTE ES DE 3.0")
notas.append("EL PROMEDI DEL ESTUDIANTE ES DE 2.0")
notas.append("EL PROMEDI DEL ESTUDIANTE ES DE 5.7")



alumnoregular=[]
alumnoregular.append("EL ESTUDIANTE NO ES ALUMNO REGULAR DEL COLEGIO SAN CHARLIS")
alumnoregular.append("EL ESTUDIANTE NO ES ALUMNO REGULAR DEL COLEGIO SAN CHARLIS")


def notasCertificado(rut):
   posicion=Validarrut(rut)
   printv(f"""
   {Fore.GREEN}
   ----------------------------------------------
            CERTIFICADO DE ANOTACIONES
   -----------------------------------------------         
   RUT:              {estudiantes[posicion,0]}
   NOMBRE ALUMNO:     {estudiantes[posicion,1]}  
   --------------------------------------------------
   ANOTACION 1:              {random.randint(anotaciones[0,6])}
   ANOTACION 2:              {random.randint(anotaciones[0,6])}
   ANOTACION 3:              {random.randint(anotaciones[0,6])}
   ---------------------------------------------------
   {Fore.RESET}""")


def NOTASCertificado(rut):
   posicion=Validarrut(rut)
   printv(f"""
   {Fore.GREEN}
   ----------------------------------------------
            CERTIFICADO DE NOTAS
   -----------------------------------------------         
   RUT:              {estudiantes[posicion,0]}
   NOMBRE ALUMNO:     {estudiantes[posicion,1]}  
   --------------------------------------------------
   NOTA 1:              {random.randint(anotaciones[0,6])}
   NOTA 2:              {random.randint(anotaciones[0,6])}
   NOTA 3:              {random.randint(anotaciones[0,6])}
   ---------------------------------------------------
   {Fore.RESET}""")
   


def aLUMNOREGULARCertificado(rut):
   posicion=Validarrut(rut)<0
   printv(f"""
   {Fore.GREEN}
   ----------------------------------------------
            CERTIFICADO DE ANOTACIONES
   -----------------------------------------------         
   RUT:              {estudiantes[posicion,0]}
   NOMBRE ALUMNO:     {estudiantes[posicion,1]}  
   --------------------------------------------------
   Alumno regular:              {random.randint(alumnoregular[0,2])}
   ---------------------------------------------------
   {Fore.RESET}""")