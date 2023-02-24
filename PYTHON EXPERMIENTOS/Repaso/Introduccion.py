#Tipos de datos

Lista = [1, 'A', "Hola", [4,3], False]
Tipla = (1, 'A', "Hola", [4,3], False)
Diccionario = {"1":1, "2":2, "3":3}

#Clase de un dato type()
print(type(Lista), '\n')

# Cadena vacía
''
# Cadena con un espacio en blanco
' '
# Cambio de línea
'\n'
# Tabulador
'\t'
    
c = [4,5,6,7,8,9]
print("len ->", len(c))
print("min ->", min(c))
print("max ->", max(c), '\n')

d = "valorant es una verga"
print("upper ->", d.upper())
print("lower ->", d.lower())
print("title ->", d.title())
print("split ->", d.split(), '\n')

e = int('2')
print(e)
e = float('5.23')
print(e)
e = str(532)
print(e)
e = bool('')
print(e, '\n')

# Input de datos
# x = input("hola decime: ")
# print(x)

edad = 14
if edad <= 18 : 
    print('Menor')
elif edad > 65:
    print('Jubilado')
else:
    print('Activo')

num = 0
while num != 0:
    num = int(input('Introduce un número: '))
    
palabra = 'ASD'
for letra in palabra:
    print(letra)

# range(fin) : Genera una secuencia de números enteros desde 0 hasta fin-1.
# range(inicio, fin, salto) : Genera una secuencia de números enteros desde inicio hasta fin-1 con un incremento de salto.
for i in range(1, 10, 2):
    print(i, end = ", ")

print('\n')

# LISTAS 
a = list("Valorant")
print(a, '\n')

# l.index(dato) : Devuelve la posición que ocupa en la lista l el primer elemento con valor dato.
# l.count(dato) : Devuelve el número de veces que el valor dato está contenido en la lista l.
# all(l) : Devuelve True si todos los elementos de la lista l son True y False en caso contrario.
# any(l) : Devuelve True si algún elemento de la lista l es True y False en caso contrario.
b = [4,5,6,6,7,8,9,6]
print(b.index(8))
print(b.count(6))
print(all(b))
print(any(b), '\n')

# l1 + l2 : Crea una nueva lista concatenan los elementos de la listas l1 y l2.
# l.append(dato) : Añade dato al final de la lista l.
# l.extend(sequencia) : Añade los datos de sequencia al final de la lista l.
# l.insert(índice, dato) : Inserta dato en la posición índice de la lista l y desplaza los elementos una posición a partir de la posición índice.
# l.remove(dato) : Elimina el primer elemento con valor dato en la lista l y desplaza los que están por detrás de él una posición hacia delante.
# l.pop([índice]) : Devuelve el dato en la posición índice y lo elimina de la lista l, desplazando los elementos por detrás de él una posición hacia delante.
# l.sort() : Ordena los elementos de la lista l de acuerdo al orden predefinido, siempre que los elementos sean comparables.
# l.reverse() : invierte el orden de los elementos de la lista l.


# DICCIONARIOS
ejemplo = {'ID': 1, 'Nombre': "Roberto", 'Edad': 55, 'Mail': "roberto@outlook.com"}
ejemplo['Mail']
print(ejemplo.get(0, 'Nombre'))
print(ejemplo.keys())
print(ejemplo.values())
print(ejemplo.items())

# d[clave] = valor : Añade al diccionario d el par formado por la clave clave y el valor valor.
# d.update(d2). Añade los pares del diccionario d2 al diccionario d.
# d.pop(clave, alternativo) : Devuelve del valor asociado a la clave clave del diccionario d y lo elimina del diccionario. Si la clave no está devuelve el valor alternativo.
# d.popitem() : Devuelve la tupla formada por la clave y el valor del último par añadido al diccionario d y lo elimina del diccionario.
# del d[clave] : Elimina del diccionario d el par con la clave clave.
# d.clear() : Elimina todos los pares del diccionario d de manera que se queda vacío.

ejemplo1 = {}
ejemplo2 = {}
ejemplo1 = ejemplo # Copia por referencia
ejemplo2 = list(ejemplo) # Copia por valor
print(ejemplo1)
print(ejemplo2, "\n")

f = open('fichero.txt', 'w')
f.write("Valorant es una pija!")
f = open('fichero.txt')
print(f.read())
f.close()

import os
f = 'fichero.txt'
if os.path.isfile(f):
    os.rename(f, 'saludo.txt') # renombrado
    print("Archivo renombrado")
else:
    print('¡El fichero', f, 'no existe!')

f = 'saludo.txt'
if os.path.isfile(f):
    os.remove(f) # borrado
    print("Archivo borrado")
else:
    print('¡El fichero', f, 'no existe!')
    
# os.listdir(ruta) : Devuelve una lista con los ficheros y directiorios contenidos en la ruta ruta.
# os.mkdir(ruta) : Crea un nuevo directorio en la ruta ruta.
# os.chdir(ruta) : Cambia el directorio actual al indicado por la ruta ruta.
# os.getcwd() : Devuelve una cadena con la ruta del directorio actual.
# os.rmdir(ruta) : Borra el directorio de la ruta ruta, siempre y cuando esté vacío.

# LEER UN FICHERO DE INTERNET
# Para leer un fichero de internet hay que utilizar la función urlopen del módulo urllib.request.
# urlopen(url) : Abre el fichero con la url especificada y devuelve un objeto del tipo fichero al que se puede acceder
#               con los métodos de lectura de ficheros anteriores.

from urllib import request
f = request.urlopen('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md')
datos = f.read()
print(datos.decode('utf-8'))

# TIPOS DE EXCEPCIONES
# TypeError : Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.
# ZeroDivisionError : Ocurre cuando se itenta dividir por cero.
# OverflowError : Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
# IndexError : Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
# KeyError : Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
# FileNotFoundError : Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
# ImportError : Ocurre cuando falla la importación de un módulo.

def division(a,b) :
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Es imposible dividir por 0")
    else:
        print(resultado)
division(5, 2)

#CLASES
# Los métodos de una clase son las funciones que definen el comportamiento de los objetos de esa clase.
# Se definen como las funciones con la palabra reservada def. La única diferencia es que su primer parámetro es especial y se denomina self. 
# Este parámetro hace siempre referencia al objeto desde donde se llama el método, de manera que para acceder a los atributos o métodos de una clase
# en su propia definición se puede utilizar la sintaxis

class Saludo:
    mensaje = "\nBienvenido "            # Definición de un atributo
    def saludar(self, nombre):         # Definición de un método   
        print(self.mensaje + nombre)
        return

s = Saludo()
s.saludar('Jhon')


class Tarjeta :
    def __init__(self, numero, cantidad = 0):
        self.numero = numero
        self.saldo = cantidad
        return
        
    def __str__(self) : # es el toString() de java
        return 'Tarjeta número {} con saldo {:.2f} $'.format(self.numero, self.saldo)
t = Tarjeta('00523412354', 2650)
print(t)

#HERENCIA
class Tarjeta_descuento(Tarjeta):
    def __init__(self, id, descuento, cantidad = 0):
        self.id = id
        self.descuento = descuento
        self.saldo = cantidad
        return
    def mostrar_descuento(self):   # Método exclusivo de la clase Tarjeta_descuento
        print('Descuento de', self.descuento, '% en los pagos.')
        return
t = Tarjeta_descuento('00523412354', 5, 2650)
t.mostrar_descuento