# Abrir el archivo

import csv

archivo_nombre = 'febrero.csv'

with open(archivo_nombre, mode='r', encoding='utf-8') as archivo:

    lector = csv.DictReader(archivo)
    
    suma_gastos = 0
    
    for fila in lector:
        if fila['FECHA'] == 'TOTAL':
            continue
            
        monto_limpio = fila['MONTO'].replace('$', '').replace(',', '').strip()
        
        try:
            valor = float(monto_limpio)
            suma_gastos += valor
        except ValueError:
            continue

print(f"--- RESULTADO DEL ANÁLISIS ---")
print(f"Gastos totales de Febrero: ${suma_gastos:.2f}")

presupuesto = 25000000
falta = presupuesto - suma_gastos
print(f"Te faltan ${falta:,.2f} para tu presupuesto de $2.5k")
