
import pandas as pd
import matplotlib.pyplot as plt

## Pedro Martinez NC.0093

# 1. Crear diccionario con datos de clases de gimnasio
clases_gimnasio = {
    'id_clase': [101, 102, 103, 104, 105, 106],
    'nombre_clase': ['Spinning', 'Yoga', 'Crossfit', 'Zumba', 'Pilates', 'Boxeo'],
    'instructor': ['Ana', 'Sofia', 'Carlos', 'Laura', 'Maria', 'Pedro'],
    'dia_semana': ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'],
    'horario': ['07:00', '09:00', '18:00', '19:00', '10:00', '11:00'],
    'duracion_minutos': [45, 60, 60, 50, 50, 60],
    'capacidad_maxima': [20, 15, 12, 25, 15, 10],
    'inscritos_promedio': [18, 12, 12, 20, 10, 8],
    'nivel': ['Intermedio', 'Principiante', 'Avanzado', 'Principiante', 'Intermedio', 'Intermedio'],
    'costo_por_clase': [100, 120, 150, 90, 130, 140]
}

print("\n Analisis Exploratorio de Datos EDA")
print("\n Exploratory Data Analysis por ---> Pedro Martinez NC.0093")
print("\n 5. Crear el diccionario con 10 listas y 6 elementos")
# 2. Convertir diccionario a DataFrame
df = pd.DataFrame(clases_gimnasio)

print("\n --- TABLA ORIGINAL DE CLASES DE GIMNASIO ---")
print(df)
# 3. Exportar los datos a CSV
print("\n -+-+-Convertir el DataFrame en archivo CSV-+-+-")

df.to_csv(
    'clases_gimnasio_0093.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\n Archivo CSV creado correctamente")
# 4. Leer el archivo CSV
print("\n +-+- 8. Leer los datos desde el archivo CSV +-+-")
print("clases_gimnasio_0093.csv")

df = pd.read_csv('clases_gimnasio_0093.csv')

print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print("\n -+-+-9. Análisis Exploratorio de Datos (EDA) +-+-+")
# 5. Primeros y últimos registros
print("\n-+-+-+ 1. PRIMEROS REGISTROS (Head):-+-+-+-")
print(df.head(3))

print("\n-+-+-+ 2. ÚLTIMOS REGISTROS (Tail):-+-++-+")
print(df.tail(2))
# 6. Dimensiones y estructura
print("\n-+-+ 6. Dimensiones y estructura -+-+-+")
print(df)

print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)

print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)

print("\n5. TIPOS DE DATOS:\n", df.dtypes)

print("\n6. INFORMACIÓN GENERAL:")
df.info()
# 7. Estadísticas y limpieza

print("\n+-+-+ 7. ESTADÍSTICAS DESCRIPTIVAS: +-+-+-")
print(df.describe())

print("\n+-+-+ 8. VALORES FALTANTES (Nulls): +-+-+-")
print(df.isnull().sum())

print("\n+-+-+ 9. REGISTROS DUPLICADOS: +-+-+-")
print(df.duplicated().sum())

print("\n-+-+- 10. VALORES ÚNICOS POR COLUMNA: +-+-+-")
print(df.nunique())

print("Niveles únicos:", df['nivel'].unique())
print("Días únicos:", df['dia_semana'].unique())
# 8. Análisis específico
print(df)

print("-------------------------------------------------------------------")

print("\n11. CLASES POR NIVEL:")
print(df['nivel'].value_counts())

print("\n12. PROMEDIO DE COSTO POR CLASE: $", df['costo_por_clase'].mean())

print("13. COSTO MÁXIMO: $", df['costo_por_clase'].max())

print("14. COSTO MÍNIMO: $", df['costo_por_clase'].min())
# 9. Ordenamiento, filtrado y agrupación

print("\n 9. Ordenamiento, filtrado y agrupación")

print("\n-+-+-+ 15. CLASES ORDENADAS POR COSTO (Mayor a menor): +-+-+-")
print(df.sort_values(by='costo_por_clase', ascending=False))

print("\n16. CLASES CON COSTO MAYOR A $120:")
filtro = df[df['costo_por_clase'] > 120]
print(filtro)

print("\n17. RESUMEN POR NIVEL:")

resumen = df.groupby('nivel').agg(
    cantidad_clases=('id_clase', 'count'),
    costo_promedio=('costo_por_clase', 'mean'),
    costo_maximo=('costo_por_clase', 'max'),
    inscritos_promedio=('inscritos_promedio', 'mean')
)

print(resumen)
# 18. Gráfica de barras: Clases por nivel
print("\n-+-+18. Gráfica de barras: Clases por nivel+----")

conteo = df['nivel'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Clases por nivel Pedro Martinez 0093')
plt.xlabel('Nivel 0093')
plt.ylabel('Cantidad de clases 0093')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Costos por clase
print("\n19. Gráfica de barras: Costos por clase")

plt.figure(figsize=(8, 5))
plt.bar(df['nombre_clase'], df['costo_por_clase'], color='lightgreen')
plt.title('Costo por clase de gimnasio EDA por Pedro 0093')
plt.xlabel('Nombre de la clase')
plt.ylabel('Costo en pesos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de duración
print("\n20. Histograma: Distribución de duración de clases")

plt.figure(figsize=(8, 5))
plt.hist(df['duracion_minutos'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de duración de clases por Pedro 0093')
plt.xlabel('Duración en minutos')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Duración vs Costo
print("\n21. Gráfica de dispersión: Duración vs Costo")

plt.figure(figsize=(8, 5))
plt.scatter(df['duracion_minutos'], df['costo_por_clase'], color='red', s=100)
plt.title('Relación entre duración y costo Pedro Martinez 0093')
plt.xlabel('Duración en minutos')
plt.ylabel('Costo por clase')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de costos
print("\n22. Diagrama de caja: Distribución de costos")

plt.figure(figsize=(7, 5))
plt.boxplot(
    df['costo_por_clase'],
    patch_artist=True,
    boxprops=dict(facecolor='lightblue')
)
plt.title('Distribución de costos (Boxplot) Pedro 0093')
plt.ylabel('Costo por clase')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
print("\n23. Matriz de correlación")

correlacion = df.corr(numeric_only=True)

print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas por Pedro 0093')
plt.tight_layout()
plt.show()
