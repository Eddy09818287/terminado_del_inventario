from src.inve import agregar_producto, mostrar_invenatrio,calcular_estadistica, quitar_producto, actualizar_productos,buscar_producto,inventario
from archivos import guardar_csv, cargar_csv
while True:
    print ("------MENU------")
    print("1-agregar un producto")
    print("2-mostrar el inventario")
    print("3-calculo de la estadistica")
    print("4-quitar un producto")
    print("5-actualizar un producto")
    print("6-buscar un producto")
    print("7-guardar csv")
    print("8-cargar csv")
    print("9-salir")
    opcion = input("ingrese una opcion:")
    if opcion not in [str(i) for i in range(1, 10)]:
        print("Opción inválida, ingrese un número del 1 al 9")
        continue

    if opcion == "1":
            
                agregar_producto()
        
    if opcion == "2":
            mostrar_invenatrio()
        
    if opcion == "3":
            calcular_estadistica()
    if opcion == "4":
            quitar_producto()
    
    if opcion == "5":
           actualizar_productos()
          
    if opcion == "6":
           buscar_producto()

    if opcion == "7":
                  
                ruta = input("Ingrese el nombre del archivo: ")
                guardar_csv(inventario, ruta)
    if opcion == "8":
        ruta = input("Ingrese la ruta del archivo: ")

        nuevo = cargar_csv(ruta)

        if not nuevo:
                continue

        decision = input("¿Sobrescribir inventario actual? (S/N): ").upper()

        if decision == "S":
                inventario = nuevo
                print("✅ Inventario reemplazado")

        else:
                # fusión
                for prod in nuevo:
                 encontrado = False

                for p in inventario:
                        if p["nombre"].strip().lower() == prod["nombre"].strip().lower():
                        
                                p["cantidad"] += prod["cantidad"]

                        if p["precio"] != prod["precio"]:
                                p["precio"] = prod["precio"]

                        encontrado = True
                        break

                if not encontrado:
                        inventario.append(prod)

                print("✅ Inventario fusionado")

        print(f"Productos cargados: {len(nuevo)}")
    elif opcion == "9":
        print("¡Saliendo del programa! ")
        break



    
            