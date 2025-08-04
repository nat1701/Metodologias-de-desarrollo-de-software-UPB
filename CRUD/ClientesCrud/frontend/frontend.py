from tabulate import tabulate

def mostrar_menu():
    print("\n========= MENÚ DE OPCIONES =========")
    print("1. Mostrar productos")
    print("2. Salir")
    print("====================================")

def mostrar_tabla_productos(productos):
    if not productos:
        print("⚠️ No se encontraron productos.")
        return

    tabla = [[p["Id"], p["Nombre"], p["Precio"], p["Cantidad"]] for p in productos]
    print("\n📦 Productos disponibles:")
    print(tabulate(tabla, headers=["ID", "Nombre", "Precio", "Cantidad"], tablefmt="fancy_grid"))
