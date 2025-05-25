

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo CSV
file_path = r'c:\Users\corte\Desktop\PYHON BIG DATA\actividad2.csv'
data = pd.read_csv(file_path)

# Mostrar las primeras filas del dataset
print("Primeras filas del dataset:")
print(data.head())

# Verificar información general del dataset
print("\nInformación general del dataset:")
print(data.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(data.describe())

# Clasificar pacientes según las categorías de presión arterial
def clasificar_paciente(row):
    if row['systolic_pressure'] < 70 and row['diastolic_pressure'] < 50:
        return 'Hipotensión'
    elif 70 <= row['systolic_pressure'] < 110 and 50 <= row['diastolic_pressure'] < 70:
        return 'Óptima'
    elif 110 <= row['systolic_pressure'] < 120 and 70 <= row['diastolic_pressure'] < 75:
        return 'Normal'
    elif 120 <= row['systolic_pressure'] < 130 and 75 <= row['diastolic_pressure'] < 80:
        return 'Pre hipertensión'
    elif 130 <= row['systolic_pressure'] < 150 and 80 <= row['diastolic_pressure'] < 90:
        return 'Hipertensión Grado 1'
    elif 150 <= row['systolic_pressure'] < 170 and 90 <= row['diastolic_pressure'] < 100:
        return 'Hipertensión Grado 2'
    elif row['systolic_pressure'] >= 170 or row['diastolic_pressure'] >= 100:
        return 'Hipertensión Grado 3'
    elif row['systolic_pressure'] >= 130 and row['diastolic_pressure'] < 80:
        return 'Hipertensión Solo Sistólica'
    else:
        return 'Sin Clasificar'

data['categoria'] = data.apply(clasificar_paciente, axis=1)

# Mostrar la distribución de categorías
print("\nDistribución de categorías:")
print(data['categoria'].value_counts())

# Visualizar la distribución de categorías
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='categoria', order=data['categoria'].value_counts().index, palette='viridis')
plt.title('Distribución de Categorías de Presión Arterial')
plt.xlabel('Categoría')
plt.ylabel('Cantidad de Pacientes')
plt.xticks(rotation=45)
plt.show()

# Análisis por región
region_summary = data.groupby('department_name')['categoria'].value_counts().unstack().fillna(0)
print("\nResumen por región:")
print(region_summary)

# Visualizar la influencia de la región
plt.figure(figsize=(12, 8))
region_summary.plot(kind='bar', stacked=True, figsize=(15, 8), colormap='viridis')
plt.title('Distribución de Categorías por Región')
plt.xlabel('Región')
plt.ylabel('Cantidad de Pacientes')
plt.legend(title='Categoría', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Histograma de presión arterial sistólica
plt.figure(figsize=(10, 6))
sns.histplot(data['systolic_pressure'], kde=True, color='blue', bins=20)
plt.title('Distribución de la Presión Arterial Sistólica')
plt.xlabel('Presión Sistólica')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de presión arterial diastólica
plt.figure(figsize=(10, 6))
sns.histplot(data['diastolic_pressure'], kde=True, color='green', bins=20)
plt.title('Distribución de la Presión Arterial Diastólica')
plt.xlabel('Presión Diastólica')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de dispersión entre presión sistólica y diastólica
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='systolic_pressure', y='diastolic_pressure', hue='categoria', palette='viridis')
plt.title('Relación entre Presión Sistólica y Diastólica')
plt.xlabel('Presión Sistólica')
plt.ylabel('Presión Diastólica')
plt.legend(title='Categoría', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Boxplot de presión sistólica por categoría
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='categoria', y='systolic_pressure', palette='viridis')
plt.title('Distribución de la Presión Sistólica por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Presión Sistólica')
plt.xticks(rotation=45)
plt.show()

# Boxplot de presión diastólica por categoría
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='categoria', y='diastolic_pressure', palette='viridis')
plt.title('Distribución de la Presión Diastólica por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Presión Diastólica')
plt.xticks(rotation=45)
plt.show()

# Mapa de calor de categorías por región
plt.figure(figsize=(12, 8))
sns.heatmap(region_summary, annot=True, fmt='.0f', cmap='viridis', cbar=True)
plt.title('Mapa de Calor: Categorías por Región')
plt.xlabel('Categoría')
plt.ylabel('Región')
plt.show()