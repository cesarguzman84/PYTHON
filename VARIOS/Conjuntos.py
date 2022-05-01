#Conjuntos (no admiten colecciones o listas dentro de ellos, no puede tener valores duplicados)

conjunto = set() #set es solo cuando se va a crear un conjunto vacio

conjunto = {1,2,3, "Hola", 4.56}

conjunto.add(5)

print(conjunto)

conjunto.discard("Hola")

print(conjunto)

a={1,2,3}
b={3,4,5}

c= a | b

print(c)

