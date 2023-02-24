import numpy as np

a = np.array([1,2,3])
print(a, '\n')

b = np.array([[5,6,7], [8,9,10]])
print(b, '\n')

print(np.empty(2), '\n') # np.empty(dimensiones) : Crea y devuelve una referencia a un array vacío con las dimensiones especificadas en la tupla dimensiones.
print(np.zeros(2), '\n') # np.zeros(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos ceros.
print(np.ones(3), '\n') # np.ones(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos unos.
print(np.full(3, 4), '\n') # np.full(dimensiones, valor) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos valor.
print(np.identity(2), '\n') # np.identity(n) : Crea y devuelve una referencia a la matriz identidad de dimensión n.
print(np.arange(1, 10, 4), '\n') # np.arange(inicio, fin, salto) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia desde inicio hasta fin tomando valores cada salto.
print(np.linspace(0, 10, 5), '\n') # np.linspace(inicio, fin, n) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia de n valores equidistantes desde inicio hasta fin.
print(np.random.random(3), '\n') # np.random.random(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son aleatorios.

print(b.ndim) # a.ndi : Devuelve el número de dimensiones del array a.
print(b.shape) # a.shape : Devuelve una tupla con las dimensiones del array a.
print(b.size) # a.size : Devuelve el número de elementos del array a.
print(b.dtype, '\n') # a.dtype: Devuelve el tipo de datos de los elementos del array a.

print(b[1, 0], '\n') # Acceso al elemento de la fila 1 columna 0
print(b[(b % 2 == 0)], '\n') # a[condicion] : Devuelve una lista con los elementos del array a que cumplen la condicion.

c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[1, 1, 1], [2, 2, 2]])
print(c + d, '\n')
print(c / d, '\n')
print(c ** 2, '\n')

e = np.array([[1, 2, 3], [4, 5, 6]])
f = np.array([[1, 1], [2, 2], [3, 3]])
print(e.dot(f), '\n') # Devuelve el array resultado del producto matricial de los arrays a y b siempre y cuando sus dimensiones sean compatibles.
print(e.T) # Devuelve el array resultado de trasponer el array a.

