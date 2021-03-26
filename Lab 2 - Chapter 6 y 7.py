#num = int(input("Ingrese un numero: "))
#if num < 0:
#    print(num, "Es negativo")
#num = int(input("Enter another number: "))
#if num > 0:
#    print(num, "Es positivo")
#    print(num, "El cuadrado es", num * num)
#    print("Adios")

#num = int(input("Ingrese otro numero: "))
#if num < 0:
#    print("Es Negativo")
#else:
#    print("No es Negativo")

#savings = float(input("Ingrese sus ahorros: "))
#if savings == 0:
#    print("Lo siento no tiene Ahorros")
#elif savings < 500:
#    print("Bien hecho")
#elif savings < 1000:
#    print("Es buen ahorro")
#elif savings < 10000:
#    print("Bienvenido señor!")
#else:
#    print("Gracias")

#snowing = True
#temp = -1
#if temp < 0:
#    print("Esta Helado")
#if snowing:
#    print("Ponte botas")
#print("Tiempo de Chocolate Caliente")
#print('Bye')

#age = 21
#status = None
#if (age > 12) and age < 20:
#    status = "Adolescente"
#else:
#    status = "No es Adolescente"
#print(status)

#age = 25
#status = None
#status = ("Adolescente" if age > 12 and age < 20 else "No Adolescente")
#print(status)

#count = 0
#print("Comienzo")
#while count < 10:
#    print(count,'', end = '') 
#    count += 1 
#print()
#print("Listo!")

#print('Imprimir valores del Rango')
#for i in range(0, 10):
#    print(i, ' ', end='')
#print()
#print('Listo')

#print('Imprimir valores con rango de 2 en 2')
#for i in range(0, 10, 2):
#    print(i, ' ', end='')
#print()
#print('Listo')

#print('Solo Imprimera si se cumplen las Iteraciones')
#num = int(input('Numero a Verificar: '))
#for i in range(0, 6):
#    if i == num:
#       break
#    print(i, ' ', end='')
#print('Listo')

#for i in range(0, 10):
#    print(i, ' ', end='')
#    if i % 2 == 1:
#        continue
#    print('Numero Par')
#    print('Amamos los Numeros Pares')
#print('Listo')

#print('Solo Imprimira si se cumplen las Iteraciones')
#num = int(input('Numero a Verificar: '))
#for i in range(0, 6):
#    if i == num:
#        break
#    print(i, ' ', end='')
#else:
#    print()
#    print('Iteraciones Completas')

import random

MIN = 1
MAX = 6

roll_again = 'y'

while roll_again == 'y':
    print('Tirando Dados...')
    print('Los Valores Son...')
    dice1 = random.randint(MIN, MAX)
    print(dice1)
    dice2 = random.randint(MIN, MAX)
    print(dice2)
    roll_again = input('Quiere tirar los Dados de nuevo? (y / n): ')