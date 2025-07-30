"""
Laboratorio 2: Generación de reportes automáticos

Objetivo: Crear un reporte automático con análisis y visualizaciones.

Instrucciones:
1. Usa el archivo del ejercicio anterior.
2. Genera un resumen estadístico y al menos un gráfico de producción.
3. Exporta el reporte en dos de los siguientes formatos: Excel, PDF o HTML.
4. El reporte debe incluir el resumen y el gráfico.
"""

# Tu código aquí 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates  # Importación adicional

# 1. Cargar y limpiar los datos
archivo_entrada = '../datos/datos_produccion_automatizada_grande.csv'
df = pd.read_csv(archivo_entrada)
df = df.drop_duplicates().dropna()
df['fecha'] = pd.to_datetime(df['fecha'])  # Asegurar que la fecha esté en formato datetime

# 2. Resumen estadístico
resumen = df.describe()

# 3. Gráfico de producción
df_filtrado = df[df['fecha'] >= '2022-01-01']  # Filtrar desde 2022

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_filtrado, x='fecha', y='produccion_bpd')
plt.title('Producción a lo largo del tiempo (desde 2022)')
plt.xlabel('Año')
plt.ylabel('Producción (BPD)')

# Mostrar solo los años en el eje X
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator(1))  # Mostrar cada año
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig('../datos/grafico_produccion.png')  # Guardar gráfico
# Mostrar solo los años en el eje X
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator(1))  # Cada 1 años
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig('../datos/grafico_produccion.png')  # Guardar gráfico

# 4. Exportar a Excel
with pd.ExcelWriter('../datos/reporte_produccion.xlsx') as writer:
    df.to_excel(writer, sheet_name='Datos Limpios', index=False)
    resumen.to_excel(writer, sheet_name='Resumen Estadístico')

# 5. Exportar a HTML
html = f"""
<html>
<head><title>Reporte de Producción</title></head>
<body>
<h1>Reporte de Producción</h1>

<h2>Resumen Estadístico</h2>
{resumen.to_html()}

<h2>Gráfico de Producción</h2>
<img src="grafico_produccion.png" width="600">

</body>
</html>
"""

with open('../datos/reporte_produccion.html', 'w') as f:
    f.write(html)

print("✅ Reporte generado en Excel y HTML.")

# 6. Exportar la gráfica en PDF
plt.savefig('../datos/grafico_produccion.pdf')   # Guardar como PDF

print("✅ Reporte generado en Excel, HTML y gráfica exportada a PDF.")