# Series: Estructura de una dimensión.
# DataFrame: Estructura de dos dimensiones (tablas).
# Panel: Estructura de tres dimensiones (cubos).

import pandas as pd
import numpy as np
s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')
print(s, '\n')

t = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(t,'\n')

print(t.size) # s.size : Devuelve el número de elementos de la serie s.
print(t.index) # s.index : Devuelve una lista con los nombres de las filas del DataFrame s.
print(t.dtype, '\n') # s.dtype : Devuelve el tipo de datos de los elementos de la serie s.

print(t[0]) # s[i] : Devuelve el elemento que ocupa la posición i+1 en la serie s.
print(t['Economía']) # s[nombres]: Devuelve otra serie con los elementos con los nombres de la lista nombres en el índice.
print(t[['Matemáticas', 'Programación']], '\n') # s[nombres] : Devuelve otra serie con los elementos correspondientes a los nombres indicadas en la lista nombres en el índice.

x = pd.Series([1,1,1,1,2,2,2,3,3,4])
print(x.count()) # Devuelve el número de elementos que no son nulos ni NaN en la serie s.
print(x.sum(), '\n') # Devuelve la suma de los datos de la serie s cuando los datos son de un tipo numérico, o la concatenación de ellos cuando son del tipo cadena str.
print(x.cumsum(), '\n') # Devuelve una serie con la suma acumulada de los datos de la serie s cuando los datos son de un tipo numérico.
print(x.value_counts(), '\n') #  Devuelve una serie con la frecuencia (número de repeticiones) de cada valor de la serie s.
print(x.min()) # Devuelve el menor de los datos de la serie s.
print(x.max(), '\n') # Devuelve el menor de los datos de la serie s.
print(x.mean(), '\n') # Devuelve la media de los datos de la serie s cuando los datos son de un tipo numérico.
print(x.std(), '\n') # Devuelve la desviación típica de los datos de la serie s cuando los datos son de un tipo numérico.
print(x.describe(), '\n') # Devuelve una serie con un resumen descriptivo que incluye el número de datos, su suma, el mínimo, el máximo, la media, la desviación típica y los cuartiles.

y = pd.Series([1, 2, 3, 4])
print(y*2, '\n')

    # y.apply(funcion)
from math import log
print(y.apply(log), '\n')

    # y[condicion]
print(y[y < 3], '\n')

print(t.sort_values(ascending=True))    # ascending = True -> creciente
print(t.sort_index(ascending=False), '\n')  # ascending = True -> decreciente

l = pd.Series(['a', 'b', None, 'c', np.NaN, 'd'])
print(l.dropna(), '\n') # Elimina los datos desconocidos o nulos de la serie s.

# CREACION DE UN DATAFRAME A PARTIR DE UN DICCIONARIO DE LISTAS
    # DataFrame(data=diccionarios, index=filas, columns=columnas, dtype=tipos)
datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'], 
        'edad':[18, 22, 20, 21],
        'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
        'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']}
df = pd.DataFrame(datos)
print(df, '\n')

# CREACION DE UN DATAFRAME A PARTIR DE UNA LISTA DE LISTAS
    # DataFrame(data=listas, index=filas, columns=columnas, dtype=tipos)
df2 = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
print(df2, '\n')

# CREACION DE UN DATAFRAME A PARTIR DE UNA LISTA DE DICCIONARIOS
    # DataFrame(data=diccionarios, index=filas, columns=columnas, dtype=tipos)
df3 = pd.DataFrame([{'Nombre':'María', 'Edad':18}, {'Nombre':'Luis', 'Edad':22}, {'Nombre':'Carmen'}])
print(df3, '\n')

# CREACION DE UN DATAFRAME A PARTIR DE UN ARRAY
    # DataFrame(data=array, index=filas, columns=columnas, dtype=tipo)
df4= pd.DataFrame(np.random.randn(4, 3), columns=['a', 'b', 'c'])
print(df4, '\n')

# CREACION DE UN DATAFRAME A PARTIR DE UN FICHERO CSV o EXCEL
    # read_csv(fichero.csv, sep=separador, header=n, index_col=m, na_values=no-validos, decimal=separador-decimal)
    # read_excel(fichero.xlsx, sheet_name=hoja, header=n, index_col=m, na_values=no-validos, decimal=separador-decimal)
df5 = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv', sep=';', decimal=',')
print(df5.head(), '\n') # Devuelve las n primeras filas del DataFrame df. [df.tail(n)]

# EXPORTACION DE FICHEROS
    # df.to_csv(fichero.csv, sep=separador, columns=booleano, index=booleano)
    # df.to_excel(fichero.xlsx, sheet_name = hoja, columns=booleano, index=booleano)

# ATRIBUTOS DE UN DATAGRAME
df6 = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesterol.csv')
print(df6.info()) #m Devuelve información (número de filas, número de columnas, índices, tipo de las columnas y memoria usado) sobre el DataFrame df.
print(df6.shape) # Devuelve una tupla con el número de filas y columnas del DataFrame df.
print(df6.size) # Devuelve el número de elementos del DataFrame.
print(df6.columns) # Devuelve una lista con los nombres de las columnas del DataFrame df.
print(df6.index) # Devuelve una lista con los nombres de las filas del DataFrame df.
print(df6.dtypes)
print(df6.tail(), '\n') # Devuelve las n últimas filas del DataFrame df. [df.tail(n)]

print(df6.rename(columns={'nombre':'nombre y apellido'}, index={0:1000, 1:1001, 2:1002}).head(3), '\n')

# df.reindex(index=filas, columns=columnas, fill_value=relleno)
print(df6.reindex(index=[4,3,1], columns=['nombre','tensión','colesterol']).tail(3), '\n')

# ACCESO MEDIANTE POSICIONES
print(df6.iloc[3, 4]) # df.iloc[i, j] : Devuelve el elemento que se encuentra en la fila i y la columna j del DataFrame df. Pueden indicarse secuencias de índices para obtener partes del DataFrame.
print(df6.iloc[3], '\n') # df.iloc[i] : Devuelve una serie con los elementos de la fila i del DataFrame df.

# ACCESO MEDIANTE NOMBRES
print(df6.loc[2, 'colesterol']) # df.loc[fila, columna] : Devuelve el elemento que se encuentra en la fila con nombre fila y la columna de con nombre columna del DataFrame df.
print(df6.loc[:3, ('colesterol','peso')]) # df.loc[filas, columnas] : Devuelve un DataFrame con los elemento que se encuentra en las filas con los nombres de la lista filas y las columnas con los nombres de la lista columnas del DataFrame df.
print(df6['colesterol']) # df[columna] : Devuelve una serie con los elementos de la columna de nombre columna del DataFrame df.

# AÑADIR COLUMNAS A UN DATAFRAME
df6['diabetes'] = pd.Series([False, False, True, False, True])
print(df6.head(5), '\n')# d[nombre] = lista: Añade al DataFrame df una nueva columna con el nombre nombre y los valores de la lista lista. La lista debe tener el mismo tamaño que el número de filas de df.
# d[nombre] = serie: Añade al DataFrame df una nueva columna con el nombre nombre y los valores de la serie serie. Si el tamaño de la serie es menor que el número de filas de df se rellena con valores NaN mientras que si es mayor se recorta.

# OPERACIONES SOBRE COLUMNAS
print(df6['altura']*100, '\n')

# APLICAR FUNCIONES A COLUMNAS
print(df6['altura'].apply(log), '\n')

print(df6.describe(), '\n') # Todas las funciones...  .count() ; .max() ; .min() ; etc

# ELIMINAR COLUMNAS DE UN DATAFRAME
edad = df.pop('edad')# df.pop(nombre) : Elimina la columna con nombre nombre del DataFrame df y la devuelve como una serie.
print(edad, '\n')

# ELIMINAR FILAS DE UN DATAFRAME
print(df6.drop([1, 3]).head(), '\n') # df.drop(filas) : Devuelve el DataFrame que resulta de eliminar las filas con los nombres indicados en la lista filas del DataFrame df.

# AÑADIR UNA FILA A UN DATAFRAME
# df.append(serie, ignore_index=True) : Devuelve el DataFrame que resulta de añadir una fila al DataFrame df con los valores de la serie serie. 
# Los nombres del índice de la serie deben corresponderse con los nombres de las columnas de df. 
# Si no se pasa el parámetro ignore_index entonces debe pasarse el parámetro name a la serie, donde su argumento será el nombre de la nueva fila.
df = df6.append(pd.Series(['Carlos Rivas', 28, 'H', 89.0, 1.78, 245.0], index=['nombre','edad','sexo','peso','altura','colesterol']), ignore_index=True)
print(df.tail(3), '\n')

# FILTRADO DE FILAS DE UN DATAFRAME
print(df6[(df6['sexo']=='H') & (df6['colesterol'] > 260)], '\n') # df[condicion]

# COLUMNA A DATETIME
df7 = pd.DataFrame({'Name': ['María', 'Carlos', 'Carmen'], 'Nacimiento':['05-03-2000', '20-05-2001', '10-12-1999']})
print(pd.to_datetime(df7.Nacimiento, format = '%d-%m-%Y'), '\n')

# ORDENAR UN DATAFRAME
# df.sort_values(columna, ascending=booleano) : Devuelve el DataFrame que resulta de ordenar las filas del DataFrame df según los valores del la columna con nombre columna. 
#                                           Si argumento del parámetro ascending es True el orden es creciente y si es False decreciente.
# df.sort_index(ascending=booleano) : Devuelve el DataFrame que resulta de ordenar las filas del DataFrame df según los nombres de las filas. 
#                                   Si el argumento del parámetro ascending es True el orden es creciente y si es False decreciente.
print(df6.sort_values('colesterol').head(), '\n')

# ELIMINAR LAS FILAS QUE CONTENGAN DATOS NaN o NULL
# df.dropna(subset=columnas) : Devuelve el DataFrame que resulta de eliminar las filas que 
# contienen algún dato desconocido o nulo en las columnas de la lista columna del DataFrame df. 
# Si no se pasa un argumento al parámetro subset se aplica a todas las columnas del DataFrame.
print(df6.dropna(), '\n')

# DIVIDIR UN DATAFRAME EN GRUPOS
# df.groupby(columnas).groups : Devuelve un diccionario con cuyas claves son las tuplas que resultan de todas las combinaciones
# de los valores de las columnas con nombres en la lista columnas, y valores las listas de los nombres de las filas que contienen
# esos valores en las correspondientes columnas del DataFrame df.
print(df6.groupby('sexo').groups, '\n')

# df.groupby(columnas).get_group(valores) : Devuelve un DataFrame con las filas del DataFrame df que cumplen que las columnas
# de la lista columnas presentan los valores de la tupla valores. La lista columnas y la tupla valores deben tener el mismo tamaño.
print(df6.groupby('sexo').get_group('H').head(2), '\n')

# APLICAR UNA FUNCION DE AGREGACION A GRUPOS
# df.groupby(columnas).agg(funciones) : Devuelve un DataFrame con el resultado de aplicar las funciones de agregación de la lista funciones
# a cada uno de los DataFrames que resultan de dividir el DataFrame según las columnas de la lista columnas.
# np.min : Devuelve el mínimo de una lista de valores.
# np.max : Devuelve el máximo de una lista de valores.
# np.count_nonzero : Devuelve el número de valores no nulos de una lista de valores.
# np.sum : Devuelve la suma de una lista de valores.
# np.mean : Devuelve la media de una lista de valores.
# np.std : Devuelve la desviación típica de una lista de valores.
print(df6.groupby('sexo').agg(np.mean), '\n')


# CONVERTIR UN DATAFRAME A FORMATO LARGO
# df.melt(id_vars=id-columnas, value_vars=columnas, var_name=nombre-columnas, var_value=nombre-valores) : Devuelve el DataFrame que resulta
# de convertir el DataFrame df de formato ancho a formato largo. Todas las columnas de lista columnas se reestructuran en dos nuevas columnas
# con nombres nombre-columnas y nombre-valores que contienen los nombres de las columnas originales y sus valores, respectivamente.
# Las columnas en la lista id-columnas se mantienen sin reestructurar. Si no se pasa la lista columnas entonces se reestructuran todas las columnas
# excepto las columnas de la lista id-columnas.
datos = {'nombre':['María', 'Luis', 'Carmen'],'edad':[18, 22, 20],'Matemáticas':[8.5, 7, 3.5],'Economía':[8, 6.5, 5],'Programación':[6.5, 4, 9]}
df8 = pd.DataFrame(datos)
x = df8.melt(id_vars=['nombre', 'edad'], var_name='asignatura', value_name='nota')
print(x, '\n')

#df.pivot(index=filas, columns=columna, values=valores) : Devuelve el DataFrame que resulta de convertir el DataFrame df de formato largo a formato ancho.
# Se crean tantas columnas nuevas como valores distintos haya en la columna columna. Los nombres de estas nuevas columnas son los valores de la columna
# mientras que sus valores se toman de la columna valores. Los nombres del índice del nuevo DataFrame se toman de los valores de la columna filas.
print(x.pivot(index='nombre', columns='asignatura', values='nota'), '\n')

