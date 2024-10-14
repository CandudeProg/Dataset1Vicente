# Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulación del dataset con las columnas relevantes
data = {
    'nivel_educativo_padres': ['Postgrado', 'Secundaria', 'Primaria', 'Postgrado', 'Secundaria'],
    'ingresos_familiares': ['50000', '35000', '80000', '45000', '60000'],
    'horas_estudio': ['4', '2', '5', '3', '6'],
    'Exam_Score': [85, 70, 90, 75, 88],
    'participacion_extracurricular': ['Si', 'No', 'Si', 'No', 'Si']  # Factor hipotético agregado
}

# Crear DataFrame
df = pd.DataFrame(data)

# Convertir 'ingresos_familiares' y 'horas_estudio' a numéricos
df['ingresos_familiares'] = pd.to_numeric(df['ingresos_familiares'], errors='coerce')
df['horas_estudio'] = pd.to_numeric(df['horas_estudio'], errors='coerce')

# Crear columnas dummy para 'nivel_educativo_padres' y 'participacion_extracurricular'
df_dummies = pd.get_dummies(df[['nivel_educativo_padres', 'participacion_extracurricular']], drop_first=True)

# Concatenar las dummies con el DataFrame original
df = pd.concat([df, df_dummies], axis=1)

# ** Gráfico 1: Relación entre el Nivel Educativo de los Padres y la Calificación **
plt.figure(figsize=(8, 6))
sns.boxplot(x='nivel_educativo_padres', y='Exam_Score', data=df, hue='nivel_educativo_padres', palette='Set3', dodge=False)
plt.title('Calificación según Nivel Educativo de los Padres', fontsize=14, fontweight='bold')
plt.xlabel('Nivel Educativo de los Padres')
plt.ylabel('Calificación en el Examen')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ** Gráfico 2: Relación entre el Nivel Educativo de los Padres y la Calificación (Regresión) **
plt.figure(figsize=(8, 6))
sns.regplot(x='ingresos_familiares', y='Exam_Score', data=df, scatter_kws={"s": 100}, line_kws={"color": "red"})
plt.title('Relación entre Ingresos Familiares y Calificación', fontsize=14, fontweight='bold')
plt.xlabel('Ingresos Familiares')
plt.ylabel('Calificación en el Examen')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ** Gráfico 3: Relación entre Horas de Estudio y Calificación **
plt.figure(figsize=(8, 6))
sns.regplot(x='horas_estudio', y='Exam_Score', data=df, scatter_kws={"s": 100}, line_kws={"color": "green"})
plt.title('Relación entre Horas de Estudio y Calificación', fontsize=14, fontweight='bold')
plt.xlabel('Horas de Estudio Diarias')
plt.ylabel('Calificación en el Examen')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ** Gráfico 4: Relación entre Horas de Estudio y Calificación, agrupado por el Nivel Educativo de los Padres **
plt.figure(figsize=(8, 6))
sns.scatterplot(x='horas_estudio', y='Exam_Score', hue='nivel_educativo_padres', data=df, s=100, edgecolor='black')
plt.title('Relación entre Horas de Estudio y Calificación agrupado por Nivel Educativo de los Padres', fontsize=14, fontweight='bold')
plt.xlabel('Horas de Estudio Diarias')
plt.ylabel('Calificación en el Examen')
plt.legend(title='Nivel Educativo de los Padres', fontsize=10, title_fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ** Gráfico 5: Relación entre Participación Extracurricular y Calificación **
plt.figure(figsize=(8, 6))
sns.boxplot(x='participacion_extracurricular_Si', y='Exam_Score', data=df, hue='participacion_extracurricular_Si', palette='Set1', dodge=False)
plt.title('Participación Extracurricular y Calificación', fontsize=14, fontweight='bold')
plt.xlabel('Participación Extracurricular (Sí = 1, No = 0)')
plt.ylabel('Calificación en el Examen')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ** Gráfico 6: Relación entre Ingresos Familiares y Calificación (con Regresión) **
plt.figure(figsize=(8, 6))
sns.regplot(x='ingresos_familiares', y='Exam_Score', data=df, scatter_kws={"s": 100}, line_kws={"color": "blue"})
plt.title('Ingresos Familiares vs Calificación con Regresión', fontsize=14, fontweight='bold')
plt.xlabel('Ingresos Familiares')
plt.ylabel('Calificación en el Examen')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
