import openpyxl

FILE_PATH = "backend/productos.xlsx"

def leer_productos_excel():
    """
    Lee los productos desde un archivo Excel y los devuelve como una lista de diccionarios.
    Cada diccionario representa un producto.
    """
    productos = []
    try:
        workbook = openpyxl.load_workbook(FILE_PATH)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if any(row):
                producto = {
                    "Id": row[0],
                    "Nombre": row[1],
                    "Precio": row[2],
                    "Cantidad": row[3]
                }
                productos.append(producto)
        
        return productos

    except FileNotFoundError:
        print(f"Error: El archivo '{FILE_PATH}' no fue encontrado. Asegúrate de que exista.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        return []
