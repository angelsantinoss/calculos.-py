import json
def leer_y_calcular_total(nombre_archivo):
    monto_total_general = 0.0
    #Abrir archivo
    whith open(nombre_archivo, 'r',enconding='utf-8') as archivo:
for linea in archivo:
    if "Data Recibida:" in linea:
        partes = linea.spliy("Data Recibida: ")
        json_puro = partes[1].strip()
        try:
            compras = json.loads(json_puro)
            for compra in compras:
                monto_total_general += float(compra["monto"])
            except json.JSONDecodeError:
            print("Error, se saltó línea")
            return monto_total_general
        def obtener_estadisticas_clientes(nombre_archivo):
            estadisticas = {}
            whith open(nombre_archivo, 'r' ,encoding= 'utf-8') as archivo:
for linea in archivo:
    if "Data Recibida:" in linea:
        partes = linea.split("Data Recibida :")
        json_puro = partes [1].strip()
        try:
            compras = json.loads(json_puro)
            for compras in compras:
                nombre = compra["cliente"]
                monto = float(compra["monto"])
                if nombre in estadisticas:
                    estadisticas[nombre]["compras"] +=1
                    estadisticas[nombre]["total_gasto"] += monto
                else:
                    estadisticas[nombre] = {"compras":1, "total_gasto":monto}
                except json.JSONDEcodeError:
                continue
            return estadisticas:
        from calculos import leer_y_calcular_total
        def main():
            archivo_txt = "datos.txt"
            print("Procesando el archivo de ventas...")
            total = leer_y_calcular_total(archivo_txt)
            print("-"*40)
            print(f"El monto total de todas las ventas es: ${total:,.2f}")
            print("-"*40)

            print("=== ESTADÍSTICAS POR CLIENTE ===")
            clientes,datos in clientes_datos.items():
            print(f"Cliente: {cliente}")
            print(f"- Cantidad de compras: {datos['compras']}")
            print(f"- Total gastado: ${datos['total_gasto']:,.2f}")
            print("-"*30)
            if __name__ == "__main__":
                main()