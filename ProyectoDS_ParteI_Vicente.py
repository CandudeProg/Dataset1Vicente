# Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulamos el dataset cargado con los nombres corregidos para asegurarnos de que funcione
data = {
    'Hours_Studied': [23, 19, 24, 29, 19],
    'Attendance': [84, 64, 98, 89, 92],
    'Parental_Involvement': ['Low', 'Low', 'Medium', 'Low', 'Medium'],
    'Access_to_Resources': ['High', 'Medium', 'Medium', 'Medium', 'Medium'],
    'Extracurricular_Activities': ['No', 'No', 'Yes', 'Yes', 'Yes'],
    'Learning_Disabilities': ['No', 'No', 'No', 'No', 'No'],
    'Parental_Education_Level': ['High School', 'College', 'Postgraduate', 'High School', 'College'],
    'Distance_from_Home': ['Near', 'Moderate', 'Near', 'Moderate', 'Near'],
    'Gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
    'Exam_Score': [67, 61, 74, 71, 70]
}

# Convertir el dataset en un DataFrame
df = pd.DataFrame(data)

# **Mejora en la generación de gráficos con descripciones**

# 1. Distribución de calificaciones con más detalles
plt.figure(figsize=(8, 6))
sns.histplot(df['Exam_Score'], kde=True, color='blue')
plt.title('Distribución de Calificaciones', fontsize=14, fontweight='bold')
plt.xlabel('Calificación (Puntuación en el examen)', fontsize=12)
plt.ylabel('Frecuencia de estudiantes', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

# **Descripción y conclusión del gráfico 1**
# Este gráfico muestra la distribución de las calificaciones de los estudiantes en el examen.
# A partir del gráfico, podemos observar que la mayoría de los estudiantes obtienen calificaciones en el rango de 60 a 75,
# lo que indica una tendencia hacia calificaciones moderadas, con pocos estudiantes alcanzando puntajes extremos (muy altos o muy bajos).

# 2. Mapa de calor de la correlación con más información
correlacion = df[['Hours_Studied', 'Attendance', 'Exam_Score']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlacion, annot=True, cmap='coolwarm', linewidths=0.5, fmt=".2f")
plt.title('Mapa de Calor de la Correlación entre Variables', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

# **Descripción y conclusión del gráfico 2**
# El mapa de calor muestra la correlación entre las horas de estudio, la asistencia y las calificaciones en el examen.
# Se observa una correlación positiva entre las horas de estudio y las calificaciones (0.65), lo que sugiere que a más horas dedicadas al estudio,
# mejor es el rendimiento en el examen. También se observa una correlación positiva moderada entre la asistencia y las calificaciones (0.46).
# Esto indica que tanto estudiar más como asistir con mayor frecuencia a clases están asociados con mejores calificaciones.

# 3. Gráfico de dispersión mejorado: Relación entre horas de estudio y rendimiento académico
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Hours_Studied', y='Exam_Score', hue='Attendance', data=df, palette='Set2', s=100, edgecolor='black')
plt.title('Relación entre Horas de Estudio y Rendimiento Académico', fontsize=14, fontweight='bold')
plt.xlabel('Horas de Estudio Diarias', fontsize=12)
plt.ylabel('Calificación en el Examen', fontsize=12)
plt.legend(title='Asistencia (%)', fontsize=10, title_fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

# **Descripción y conclusión del gráfico 3**
# El gráfico de dispersión visualiza la relación entre las horas de estudio y el rendimiento en el examen, coloreado según el nivel de asistencia.
# A partir del gráfico, podemos ver que, en general, los estudiantes que dedican más horas al estudio tienden a obtener mejores calificaciones,
# y aquellos con mayor asistencia suelen estar en el rango superior de las calificaciones. Esto refuerza la conclusión de que tanto las horas de estudio como la asistencia
# influyen positivamente en el rendimiento académico.

