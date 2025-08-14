# conjuntos en Python.

## Los conjuntos en Python se crean usando {}

lista_frutas = ["pera", "manzana", "naranja", "pera"]

# con set elimino duplicados

lista_frutas2 = set(lista_frutas)

# ahora en conjutnos de numeros

conjunto = {1, 2, 3, 4}

conjunto2 = {3, 4, 5, 6}

# Union de los elementos que estan en a y en B sin repetir

print(conjunto | conjunto2)

print(conjunto.union(conjunto2))

# Interseccion de los conjuntos; los elementos que estan en ambos
print(conjunto & conjunto2)
print(conjunto.intersection(conjunto2))

# Diferencia de los conjuntos; lo que esta en uno que no esta en el otro

print(conjunto - conjunto2)
print(conjunto.difference(conjunto2))

# Diferencia simetrica de los conjuntos; lo que no esta en ninguno de los dos 

print(conjunto ^ conjunto2)
print(conjunto.symmetric_difference(conjunto2))