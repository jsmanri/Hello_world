import random
def Suma_dos_valores(sumando1, sumando2):
    global resultado
    resultado = sumando1 + sumando2
    
    return resultado 

#Suma_dos_valores(4,5)
#print("Primera suma")
#print(resultado)
#Suma_dos_valores(1,2)
#print("Segunda suma")
#print(resultado)

def Calculadora_dos_valores(numero1,numero2,operador):
    global resultado
    if operador ==1:#Si el operador es 1 es suma
        resultado = numero1 + numero2
        return resultado
    elif operador ==2:#Si el operador es 2 es resta
        resultado = numero1 - numero2
        return resultado
    elif operador ==3:#Si el operador es 3 es multiplicacion
        resultado = numero1 * numero2
        return resultado
    elif operador ==4:#Si el operador es 4 es division
        if numero2 == 0:
            print("Error: Division por cero")
            return None
        else:
            resultado = numero1 / numero2
            return resultado
    

#Calculadora_dos_valores(1,8,1)       
#print("Resultado suma",resultado)
#Calculadora_dos_valores(1,8,2)       
#print("Resultado resta",resultado)
#Calculadora_dos_valores(1,8,3)       
#print("Resultado multiplicacion",resultado)
#Calculadora_dos_valores(1,8,4)       
#print("Resultado division",resultado)

def Teorema_pitagoras(numero1,numero2,):
    global resultado
    return (numero1**2 + numero2**2)**0.5

#print("Resultado hipotenusa",Teorema_pitagoras(3,4))

def Despeje_x():
    global x
    b=int(input("Ingrese el valor de B= "))
    c=int(input("Ingrese el valor de C= "))
    x=(c-b)/2
    #print("El valor de X es: ",x)
    return x

#Despeje_x()

def funcion_and_3():
    global resultado
    A=bool(input("Inserte un numero del 1 o 0= "))
    B=bool(input("Inserte un numero del 1 a 0= "))
    A=bool(input("Inserte un numero del 1 a 0= "))
    resultado= A and B and A
    return resultado
    
    
    
#funcion_and_3()
#print("El resultado es: ", resultado)



def Pitagoras_funcion_sumar():
    global resul_pitagoras
    a=int(input("Ingrese el valor de a= "))
    b=int(input("Ingrese el valor de b= "))
    a2= a**2
    b2= b**2
    suma=Suma_dos_valores(a2,b2)
    resul_pitagoras = suma**0.5
    #print("El valor de pitagoras es de= ",resul_pitagoras)
    #return resul_pitagoras

#Pitagoras_funcion_sumar()

def contar_letras():
    global resultado_contador
    palabra=str(input("Ingrese la palabra= "))
    letra=str(input("Ingrese la letra acontar= "))
    resultado_contador = palabra.count(letra)
    #print("La cantidad de letras", letra,"es= ",resultado_contador)
    #print("La cantidad de letras de la palabra es= ",len(palabra))
    #print("Palabra separada por letras= ",list(palabra))
    return resultado_contador


#contar_letras()

def piedra_papel_tijera():
    opciones=["piedra","papel","tijeras"]
    jugador1=random.choice(opciones)
    jugador2=random.choice(opciones)
    if jugador1 == jugador2:
        resultado = "empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 =="papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        resultado = "gana jugador 1"
    else:
        resultado = "gana jugador 2"
    print("el jugador 1:",jugador1)
    print("el jugador 2:",jugador2)
    print("el resultado es:",resultado)
    return resultado

piedra_papel_tijera()



    
    
    

    