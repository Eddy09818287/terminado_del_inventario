import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("⚠️ El inventario está vacío. No hay nada para guardar.")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for producto in inventario:
                writer.writerow([
                    producto["nombre"],
                    producto["precio"],
                    producto["cantidad"]
                ])

        print(f"✅ Inventario guardado en: {ruta}")

    except PermissionError:
        print("❌ Error: No tienes permisos para escribir en esa ruta.")
    except Exception as e:
        print(f"❌ Error inesperado al guardar: {e}")
    if not inventario:
        print("⚠️ El inventario está vacío. No hay nada para guardar.")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for producto in inventario:
                writer.writerow([
                    producto["nombre"],
                    producto["precio"],
                    producto["cantidad"]
                ])

        print(f"✅ Inventario guardado en: {ruta}")

    except PermissionError:
        print("❌ Error: No tienes permisos para escribir en esa ruta.")
    except Exception as e:
        print(f"❌ Error inesperado al guardar: {e}")


def cargar_csv(ruta):
    inventario_cargado = []
    filas_invalidas = 0

    try:
        with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            # validar encabezado
            encabezado = next(reader, None)
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("❌ Encabezado inválido. Debe ser: nombre,precio,cantidad")
                return []

            for fila in reader:
                # validar columnas
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    inventario_cargado.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except ValueError:
                    filas_invalidas += 1

        print(f"⚠️ {filas_invalidas} filas inválidas omitidas.")
        return inventario_cargado

    except FileNotFoundError:
        print("❌ Error: Archivo no encontrado.")
    except UnicodeDecodeError:
        print("❌ Error: Problema de codificación del archivo.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

    return []