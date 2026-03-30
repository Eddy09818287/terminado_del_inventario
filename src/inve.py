inventario = []
def agregar_producto():
    nombre_producto = input("ingrese nombre del producto:")
# pedir precio con validacion
    i = 0
    while True:
        try:
            precio_producto = float(input("ingrese precio del producto:"))
            if i > precio_producto:
                print("ingrese un valor numerico correcto")
                continue
            break
        except ValueError:
            print("ingrese solo numeros :")
    # pedir la cantidad de producto con validacion
    while True:
        try:
            cantidad_producto = int(input("ingrese la cantidad de su producto:"))
            if i > cantidad_producto:
                print("ingrese un valor numerico correctro ")
                print("ingrese un valor correcto:")
                continue
            break
        except ValueError:
            print("ingrese un valor correcto:")

    
    producto = {
      "nombre" : nombre_producto,
      "precio": precio_producto,
      "cantidad": cantidad_producto,
    }
    inventario.append(producto)
    print("producto agregado correctamente")

    
def mostrar_invenatrio():
    print("---INVENTARIO---")
    if len (inventario) == 0:
        print("inventario esta vacio")
    else:
        for producto in inventario:
            print (f"producto:{producto['nombre']} | precio:{producto['precio']} | cantidad:{producto['cantidad']}" )

def calcular_estadistica():
    if not inventario :
        print("no hay producto para calcular la estadistica")
    for producto in inventario:
        valor_total = sum(producto['precio'] for producto in inventario * producto['cantidad'] for producto in inventario)
        cantidad_total = sum(producto['cantidad'] for producto in inventario)         
        return

    print("-----Estadiaticas del inventario-----")
    print(f"El valor total del inventario es de{valor_total}")
    print (f"la cantidad de producto es {cantidad_total}")

def quitar_producto():
    if not inventario:
        print("El inventario está vacío")
        return
    nombre = input("Ingrese el nombre del producto que quieres remover: ").strip().lower()
    productos_encontrados = [producto for producto in inventario if producto['nombre'].strip().lower() == nombre]
    if not productos_encontrados:
        print("No existe ese producto en el inventario")
        return
    for producto in productos_encontrados:
        inventario.remove(producto)  
        print(f"{producto['nombre']} eliminado del inventario")

def actualizar_productos ():
    print("menu para actualizar productos")
    print("1-actualizar nombre")
    print("2-actualizar precio")
    print("3-actualizar cantidad")
    opcion = input("ingrese una opcion:")

    if not inventario:
        print("no hay productos para actualizar " )
        return
    nombre_actualizar = input("ingrese el producto actulizar:")
    for productos in inventario:
        if productos['nombre'].strip().lower() == nombre_actualizar:
            print("productos encontrados ingrese los nuevos datos")
            if opcion == "1":
                nuevo_nombre = input("ingrese el nuevo nombre:")
                productos["nombre"] = nuevo_nombre
                print("nombre actualizado correctamente")
                return
            if opcion == "2":
                nuevo_precio = float(input("ingrese el nuevo precio:"))
                productos["precio"] = nuevo_precio
                print("precio actualizado correctamente")
                return
            if opcion == "3":                 
                nueva_catidad = int(input("ingrese la nueva cantidad:"))
                productos["cantidad"]= nueva_catidad
                print("cantidad actualizada correctamente")
                return 
def buscar_producto ():
    if not inventario:
        print("no hay producto para buscar")
        return
        
    nombre_buscar = input("ingrese el producto que quieres buscar")
    for producto in inventario:
        if producto ['nombre'].strip().lower() == nombre_buscar:
            print (f"producto:{producto['nombre']} | precio:{producto['precio']} | cantidad:{producto['cantidad']}" )
        return 
    
   