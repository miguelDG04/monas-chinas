asientoComun = 60000
espacioParapiernas = 80000
noReclinable = 50000
asientos = [asientoComun,espacioParapiernas,noReclinable]

while True:
    print("(1)Comprar pasajes ")
    print("(2)Ver listado de pasajeros ")
    print("(3)Buscar pasajero ")
    print("(4)Reasignar asiento ")
    print("(5)Mostrar ganancias totales ")
    print("(6)salir ")

    op = int(input("ingrese su opcion: "))

    if op==1:
        pasajes = int(input("cuantos pasajes quiere comprar: "))
        print(f"1.asiento comun ${asientoComun} \n2.espacion para piernas ${espacioParapiernas} \n3.no reclinable ${noReclinable}")
        asientos = int(input("¿que tipo de asiento le gustaria elegir? "))
        nombre = input("ingrese su nombre ")
        apellido = input("ingrese su apellido ")
        rut = input("ingrese su rut ")
        pasajeros = [nombre,apellido,rut]
        print(pasajeros)
        lugarAsiento = int(input("eliga el lugar un lugar disponible "))
        

    elif op==2:
        listadodepasajeros = pasajeros
        print(listadodepasajeros)

    elif op==3:
        print("buscar")

    elif op==4:
        print("reasignar")
    
    elif op==5:
        print("ganancias")

    elif op==6:
        print("termino la compra")
        break
    else:
        print("seleccione una opcion valida")