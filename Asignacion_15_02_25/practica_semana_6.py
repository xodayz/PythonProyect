# Dayhan Garcia dg19-1913

#Ejercicio 1: Multiplicar todos los elementos por 3
#Dada una lista de números, multiplica todos los elementos por 3.
numbers = [1,2,3,4,5]
print(f"Ejercicio 3: {list(map(lambda n: n * 3, numbers))}")

#Ejercicio 2: Filtrar números mayores a 10
#Dada una lista de números, filtra los números que son mayores a 10.
numbers02 = [5, 10, 15, 20, 25]
print(f"Ejercicio 2: {list(filter(lambda x: x > 10, numbers02))}")

#Ejercicio 3: Convertir una lista de palabras a mayúsculas
#Dada una lista de palabras, conviértelas todas a mayúsculas.
words03 = ["hola", "mundo", "python"]
print(f"Ejercicio 3: {list(map(lambda word: word.upper(), words03))}")

#Ejercicio 4: Filtrar palabras que empiezan con 'p'
#Dada una lista de palabras, filtra aquellas que comienzan con la letra 'p'.
words04 = ["hola", "mundo", "python", "programacion"]
print(f"Ejercicio 4: {list(filter(lambda word: word.startswith("p") , words04))}")

#Ejercicio 5: Calcular la longitud de cada palabra
#Dada una lista de palabras, calcula la longitud de cada una.
words05 = ["hola", "mundo", "python"]
words_n_letters = {word05: len(words05) for word05 in words05}
print(f"Ejercicio 5: {words_n_letters}")

#Ejercicio 6: Filtrar palabras con longitud mayor a 4
#Dada una lista de palabras, filtra aquellas que tienen una longitud mayor a 4.
words06 = ["hola", "mundo", "python", "hi"]
print(f"Ejercicio 6: {list(filter(lambda word: len(word) > 4, words06))}")

#Ejercicio 7: Convertir una lista de temperaturas de Celsius a Fahrenheit
#Dada una lista de temperaturas en Celsius, conviértelas a Fahrenheit.
celsius = [0, 20, 37, 100]
print(f"Ejercicio 7: {list(map(lambda celsius: (celsius * 1.8) + 32, celsius))}")

#Ejercicio 8: Filtrar temperaturas mayores a 50 grados Fahrenheit
#Dada una lista de temperaturas en Fahrenheit, filtra aquellas que son mayores a 50 grados.
fahrenheit = [32.0, 68.0, 98.6, 212.0]
print(f"Ejercicio 8: {list(filter(lambda grade: grade > 50, fahrenheit))}")

#Ejercicio 9: Sumar 5 a todos los elementos de una lista
#Dada una lista de números, suma 5 a cada uno de ellos.
numbers09 = [1, 2, 3, 4, 5]
print(f"Ejercicio 9: {list(map(lambda n: n+5, numbers09))}")

#Ejercicio 10: Filtrar palabras que contienen la letra 'a'
#Dada una lista de palabras, filtra aquellas que contienen la letra 'a'.
words10 = ["hola", "mundo", "python", "vida"]
print(f"Ejercicio 10: {list(filter(lambda word: "d" in word, words10))}")