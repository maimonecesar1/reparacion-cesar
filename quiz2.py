a = int(input('ingrese la cantidad de poblacion a : '))
b = int(input('ingrese la cantidad de poblacion b: '))
tiempo = int(input('ingrese el tiempo: '))
if a<=0  :
    print("debe ingresar un numero mayor de o en las poblaciones")
    a = int(input('ingrese la cantidad de poblacion a : '))
if b<=0 :
    print("debe ingresar un numero mayor de o en las poblaciones")
    b = int(input('ingrese la cantidad de poblacion b: '))

if tiempo < 0 :
    print("debe ingresar un numero de tiempo mayor a 0 ")
    tiempo = int(input('ingrese el tiempo: '))

def bacterias(a, b, tiempo):
    contador_minutos = 0
    while(contador_minutos <= tiempo):
        if contador_minutos != 0:
            b = b*2
            if contador_minutos%2 == 0 and contador_minutos != 0:
                a = a*2

                if a <= b/3:
                    b = b - (a*3)
                                                 
                elif a > b/3 and a <= b/2:
                    b = b - (a*2)
                    
                elif a > b/2:
                    b = b - (a)
                    
            if contador_minutos%10 == 0:
                a = a - (a/2)

        print(f'a:{a}, b:{b} tiempo: {contador_minutos}')
        if a <= 0 or b <= 0:
            print(f'una de las poblaciones de bacterias se a extinto en el minuto: {contador_minutos}')
            break
        contador_minutos = contador_minutos + 1
    print(f'el numero final de la poblacion a es : {a}')
    print(f'el numero final de la poblacion b es : {b}')
    





bacterias(a,b,tiempo)

