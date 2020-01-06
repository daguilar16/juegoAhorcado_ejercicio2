#juego ahorcado .py

import time

nombre = input('ingrese su nombre: ')
print('HOla, ' + nombre, ' es hora de jugar el juego de ahorcado')
print('')
time.sleep(1) # esta instruccion permite que la computadora se detenga por el tiempo entre parentesis (1 segundo)
print('Comienza a adivinar')
time.sleep(0.5)
palabra= input('ingrese la palabra a adivinar: ')
tuPalabra = ''
vidas= 5

while vidas > 0:
    fallas =0
    for i in palabra:
        if i == tuPalabra:
            print(i, end='') 
        else:
            print("*", end="")
            fallas+=1
    
    if fallas ==0:
        print('felicidades, ganaste!')
        break
    
    tuLetra = input('ingrese una letra: ')
    tuPalabra+= tuLetra

    if tuLetra not in palabra:
        vidas -=1
        print('Error')
        print('Tu tienes ', + vidas, " vidas")
    
    if vidas == 0:
        print('perdiste')
    
else:
    print('Gracias por participar')

    

