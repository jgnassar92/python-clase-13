"""
Laboratorio 1: Automatización de tareas de análisis

Objetivo: Automatizar la limpieza y análisis básico del dataset de producción.

Instrucciones:
1. Carga el archivo '../datos/datos_produccion_automatizada_grande.csv' en un DataFrame.
2. Elimina duplicados y valores nulos.
3. Calcula el total de producción y el promedio de presión.
4. Guarda el DataFrame limpio en '../datos/datos_produccion_automatizada_grande_limpio.csv'.
5. Imprime los resultados del análisis.
"""

# Tu código aquí 
import pandas as pd

# 1. Cargar el archivo CSV en un DataFrame
ruta_entrada = '../datos/datos_produccion_automatizada_grande.csv'
df = pd.read_csv(ruta_entrada)

# 2. Eliminar duplicados y valores nulos
df = df.drop_duplicates()
df = df.dropna()

# 3. Calcular el total de producción y el promedio de presión
# Suponiendo que las columnas relevantes se llaman 'producción' y 'presión'
total_produccion = df['produccion_bpd'].sum()
promedio_presion = df['presion_psi'].mean()

# 4. Guardar el DataFrame limpio en un nuevo archivo
ruta_salida = '../datos/datos_produccion_automatizada_grande_limpio.csv'
df.to_csv(ruta_salida, index=False)

# 5. Imprimir los resultados del análisis
print(f"Total de producción: {total_produccion}")
print(f"Promedio de presión: {promedio_presion:.2f}")