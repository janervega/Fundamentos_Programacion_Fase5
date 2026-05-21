# -------------------------------------------------------------
# Nombre del estudiante: Janner Jose Vega Torres
# Grupo: 213022_174
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación
# Código Fuente: autoría propia
# -------------------------------------------------------------

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Módulo (función) para determinar la cantidad exacta a pedir para un artículo.
    Lógica de negocio:
    - Si el Stock Actual es menor al Mínimo, se pide la diferencia.
    - Si el Stock Actual es suficiente, se pide cero (0).
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

def auditar_inventario():
    # Matriz con al menos 5 artículos: [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
    inventario = [
        ["A001", "Arroz (Bulto)", 12, 30],
        ["A002", "Azúcar (Bulto)", 8, 20],
        ["A003", "Aceite (Caja)", 15, 10],
        ["A004", "Panela (Caja)", 5, 15],
        ["A005", "Huevos (Cubeta)", 25, 20]
    ]

    print("\n--- REPORTE DE AUDITORÍA DE INVENTARIO ---")
    print("-" * 50)

    # Recorrer cada artículo de la matriz
    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        # Llamar al módulo para calcular la cantidad exacta a pedir
        cantidad_a_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        # Mostrar resultado para cada artículo
        print(f"Artículo: {nombre:<16} | Cantidad a solicitar: {cantidad_a_pedir}")

    print("-" * 50)

# Ejecutar el programa principal
if __name__ == "__main__":
    auditar_inventario()
    
    # Pausa para que no se cierre el programa
    input("\nPresione Enter para salir...")
