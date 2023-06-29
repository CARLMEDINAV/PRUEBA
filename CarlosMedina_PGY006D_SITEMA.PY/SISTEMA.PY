import funciones as fu


while True:
    fu.limpiarpantalla()
    fu.printv("""
    -------------------------------------
               SAN CHARLIS
    --------------------------------------
    1) GUARDAR
    2) BUSCAR
    3) Certificados
    4) SALIR""")
    opcion=int(input("INGRESE UNA OPCION :"))
    if  opcion==0:
        fu.printv("ADIOS")
    elif opcion==1:
        rut=input("INGRESE RUT DEL ESTUDIANTE SIN GUION : ")
        nombre_alumno=input("INGRESE EL NOMBRE COMPLETO DEL ESTUDIANTE :")
        edad=int(input("INGRESE LA EDAD DEL ALUMNO : "))
        genero=input("INGRESE EL GENERO DL ALUMNO : ")
        promedio=input("INGRESE EL PROMEDIO DEL ALUMNO : ")
        fecha_matricula=(input("INGRESE LA FECHA DE LA MATRICULA(SEPARELO CON UN GUION -) : "))
        nombre_apoderado=input("INGRESE EL NOMBRE DEL APODERADO : ")
        fu.guardar(rut,nombre_alumno,edad,genero,promedio,fecha_matricula,nombre_apoderado)
    elif opcion==2:
        fu.listar(rut)
    elif opcion==3:
        fu.printv("""1) CERTIFICADO ANOTACIONES
                  2) CERTIFICADO REGULAR
                  3) CERTIFICADO NOTAS
        """)
    CERTIFICADO=int(input("INGRESE EL NUMERO DE CERTIFICADO QUE DESEA"))
    if CERTIFICADO==1:
     fu.anotacionesCertificado(rut)
    elif CERTIFICADO==2:
        fu.NOTASCertificado(rut)
    elif CERTIFICADO==3:
        fu.aLUMNOREGULARCertificado(rut)