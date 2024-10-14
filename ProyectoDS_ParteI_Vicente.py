import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Cargar datos desde el archivo
file_path = "C:/Users/Usuario/Desktop/Coderhouse Trabajos/Databases Entregas Opciones/StudentPerformanceFactorsUSA.xlsx"
df = pd.read_excel(file_path)

# Convertir algunas columnas a numéricas
df['Family_Income'] = df['Family_Income'].replace({'Low': 1, 'Medium': 2, 'High': 3})

# Definir el directorio de salida
output_directory = "C:/Users/Usuario/Desktop/"

# 1. Mejora visual: radar chart colorido y más legible
def radar_chart():
    radar_data = df[['Family_Income', 'Hours_Studied', 'Exam_Score']].mean()
    categories = ['Family_Income', 'Hours_Studied', 'Exam_Score']

    # Normalización
    radar_data = (radar_data - radar_data.min()) / (radar_data.max() - radar_data.min())

    values = radar_data.values.flatten().tolist()
    values += values[:1]  # Cerrar el gráfico
    categories += categories[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Color de área y líneas
    ax.fill(categories, values, color='lightcoral', alpha=0.4)  # Sombra con alpha
    ax.plot(categories, values, color='darkred', linewidth=3, linestyle='solid')  # Líneas principales

    # Marcadores en los puntos
    ax.scatter(categories, values, color='darkred', s=100, zorder=5)

    # Estilo de los ejes radiales
    ax.spines['polar'].set_visible(True)
    ax.spines['polar'].set_color('darkblue')
    ax.spines['polar'].set_linewidth(2)

    # Etiquetas de las categorías y leyenda
    ax.set_title("Promedio de Ingresos, Horas de Estudio y Calificación", size=16, color='darkblue', weight='bold', pad=20)
    ax.set_yticklabels([])  # Ocultar etiquetas de los valores en los radios
    ax.tick_params(colors='darkblue', labelsize=12)  # Colores de las etiquetas de categorías

    plt.savefig(output_directory + "grafico_promedio_radar.png")
    plt.show()

# Ejecución del gráfico de radar personalizado
radar_chart()

# 2. Gráfico 3D: Ingresos familiares, horas de estudio y calificación
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Family_Income'], df['Hours_Studied'], df['Exam_Score'], c=df['Exam_Score'], cmap='viridis', s=100)

# Personalizaciones del gráfico 3D
ax.set_xlabel('Ingresos Familiares', fontsize=12, color='darkgreen')
ax.set_ylabel('Horas de Estudio', fontsize=12, color='darkgreen')
ax.set_zlabel('Calificación', fontsize=12, color='darkgreen')
ax.set_title('Relación entre Ingresos, Horas de Estudio y Calificación en 3D', size=15, weight='bold')

plt.savefig(output_directory + "grafico_3d_ingresos_horas_calificacion.png")
plt.show()

# 3. Gráfico de barras 3D: Relación entre Ingresos Familiares y Calificación
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Agrupar los datos para obtener el promedio
income_vs_score = df.groupby('Family_Income')['Exam_Score'].mean().reset_index()

# Crear gráfico de barras 3D
ax.bar3d(income_vs_score['Family_Income'], np.zeros_like(income_vs_score['Family_Income']), np.zeros_like(income_vs_score['Exam_Score']),
         0.5, 0.5, income_vs_score['Exam_Score'], color='lightblue', shade=True)

# Personalización del gráfico
ax.set_xlabel('Ingresos Familiares', fontsize=12, color='darkblue')
ax.set_ylabel('Placeholder', fontsize=12, color='darkblue')  # Etiqueta del segundo eje
ax.set_zlabel('Calificación Promedio', fontsize=12, color='darkblue')
ax.set_title('Promedio de Calificación según Ingresos Familiares en 3D', size=15, weight='bold')

plt.savefig(output_directory + "grafico_3d_barras_ingresos_calificacion.png")
plt.show()

# 4. Gráfico 3D: Relación entre Horas de Estudio y Calificación
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Hours_Studied'], df['Exam_Score'], c=df['Exam_Score'], cmap='plasma', s=100)
ax.set_xlabel('Horas de Estudio', fontsize=12, color='darkred')
ax.set_ylabel('Calificación', fontsize=12, color='darkred')
ax.set_title('Relación entre Horas de Estudio y Calificación en 3D', size=15, weight='bold', color='darkred')

plt.savefig(output_directory + "grafico_3d_estudio_calificacion.png")
plt.show()

# 5. Gráfico de dispersión 2D: Participación extracurricular y calificación
plt.figure(figsize=(10, 6))
sns.boxplot(x='Extracurricular_Activities', y='Exam_Score', data=df, hue='Extracurricular_Activities', palette='coolwarm', dodge=False)
plt.title('Participación Extracurricular y Calificación', fontsize=15, color='darkblue')
plt.xlabel('Participación Extracurricular (Sí o No)', fontsize=12, color='darkblue')
plt.ylabel('Calificación en el Examen', fontsize=12, color='darkblue')
plt.legend(title='Participación Extracurricular')
plt.grid(True)

plt.savefig(output_directory + "grafico_participacion_extracurricular.png")
plt.show()

# 6. Gráfico 2D: Relación entre nivel educativo de los padres y calificación (Boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Parental_Education_Level', y='Exam_Score', data=df, hue='Parental_Education_Level', palette='Set2', dodge=False)
plt.title('Calificación según Nivel Educativo de los Padres', fontsize=15, color='darkblue')
plt.xlabel('Nivel Educativo de los Padres', fontsize=12, color='darkblue')
plt.ylabel('Calificación en el Examen', fontsize=12, color='darkblue')
plt.grid(True)

plt.savefig(output_directory + "grafico_boxplot_nivel_educativo_padres.png")
plt.show()

# 7. Gráfico de dispersión 2D agrupado por nivel educativo de los padres
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Hours_Studied', y='Exam_Score', hue='Parental_Education_Level', data=df, s=100, edgecolor='black', palette='Set3')
plt.title('Relación entre Horas de Estudio y Calificación agrupado por Nivel Educativo de los Padres', fontsize=15, color='darkblue')
plt.xlabel('Horas de Estudio Diarias', fontsize=12, color='darkblue')
plt.ylabel('Calificación en el Examen', fontsize=12, color='darkblue')
plt.legend(title='Nivel Educativo de los Padres')
plt.grid(True)

plt.savefig(output_directory + "grafico_scatter_estudio_calificacion.png")
plt.show()

# Verificar datos nulos en el dataset
missing_data = df.isnull().sum()
if missing_data.sum() > 0:
    print("\nDatos nulos encontrados:\n", missing_data)
else:
    print("\nNo se encontraron datos nulos.")
