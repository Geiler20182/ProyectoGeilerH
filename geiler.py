global lista, becas

lista=[['GEILER', 'HIPIA', 18, 'M', 'GIMNASIO'], ['JULIAN', 'NUÑEZ', 18, 'M', 'COMFANDI'], ['LINA', 'PANTOJA', 13, 'M', 'COMFANDI']]
becas=['geiler','jorge','hola']
estudiantes=['geiler','jorge','hola']
print("===============================")
print("PROGRAMA DE BECAS--AÑO 2018---")
print("===============================","\n")

def main():

    print("1.Registrar Estudiante")
    print("2.Generar Beca")
    print("3.Eliminar beca")
    print("4 Ver estudiantes Registrados")
    print("5.Salir")
    print("--------------------------------")
    opc=int(input("¿Qué opción desea?: "))
    
    if (opc==1):
        registrar()
    elif(opc==2):
        generarBeca()
    elif (opc==3):

        eliminarBeca()
    elif (opc==4):
        print("----------------------------------------------")
        print("...Rregistrado exitosamente.......")
        print("----------------------------------------------")
        print(estudiantes)
        print("----------------------------------------------\n")
        main()
    elif(opc==5):
        exit
def registrar():

    print("------------------------------------------------------------------")
    print("---Apreciado usuario por favor diligencie el siguiente formulario")
    print("------------------------------------------------------------------")
    name=str(input("Nombre: "))
    apellido=str(input("Apellidos: "))
    edad=int(input("Edad: "))
    sexo=str(input("Sexo F/M: "))
    colegio=str(input("Colegio: "))
    lista.extend([[name,apellido,edad,sexo,colegio]])
    estudiantes.append([name])
    print("----------------------------------------------")
    print("...Estudiante registrado exitosamente.......")
    print("----------------------------------------------")
    print("===============================")
    print("-------------MENU--------------")
    print("===============================","\n")
    main()

def generarBeca():
    print("----------------------------------------------")
    name=str(input("Indroce el nombre del estudiante: "))
    print("----------------------------------------------")
    
    i=0
    for x in lista:
        if lista[i][0]==name:
            print("Estudiante encontrado......")
            print("---------------------------------")
            print("Validacion de beca")
            print("---------------------------------")
            distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
            numero_hermanos=int(input("Introduce el nº de hermanos en su nucleo familiar: "))
            salario_familiar=int(input("introduce salario anual bruto:  "))            

            if distancia_escuela>8 and numero_hermanos>2 and salario_familiar<=20000:
                print("tienes derecho a beca\n\n")
                becas.append(lista[i][0])
                
                main()
            else:
                
                print("no tienes derecho a beca\n")
            i+=1
        else:
            i+=1

def eliminarBeca():
    print("----------------------------------------------")
    name=str(input("Introduce el nombre del beneficiario: "))
    print("----------------------------------------------")
    i=0
    for x in range(len(becas)):
        if becas[i]==name:
            print("Usuario encontrado......")
            print("---------------------------------")
            print("Eliminacion de Beca")
            print("---------------------------------")
            print("***Motivo***")
            print("---------------------------------")
            print("1.Bajo rendimiento academico")
            print("2.Abandono de carrera")
            print("3.Otro motivo")
            opc=int(input("Motivo: "))

            if (opc==1):
                print(becas)
                becas.remove(becas[i])
                print("Se elimino",name,"exitosamente")
                print(becas)
                i+=1
                break
            
        else:
            i=i+1
    

main()
