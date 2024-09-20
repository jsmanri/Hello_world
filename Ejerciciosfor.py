import time
def ejercicio1 ():
    palabra= str(input("Por favor ingresar palabra: "))
    cantidad= int(input("Ingrese la cantidad de veces: "))
    for i in range(cantidad):
        print("Valor de la variable i: ", i+1)
        time.sleep(2)
        print(palabra)
    return
#ejercicio1()

def edad ():
    edad= int(input("Ingrese su edad: "))
    for i in range (edad):
        print(i+1)
        time.sleep(1)
    return
#edad()

def Edad_actual():  
    actual = 2024
    Año_nac= int(input("Ingrese su año de nacimiento: "))
    for i in range (actual- Año_nac):
        print(i+1)
        time.sleep(1)
    return

#Edad_actual()
    
def numeros_impares():
    numero=int(input("Ingrese el  numero: "))
    for i in range (1,numero+1,2):
        time.sleep(1)
        print(i, end=", \n")
        if i==15:
            break;
        
#numeros_impares()        
        

def reloj_60():
    Detener=int(input("Ingrese cunado detener: "))
    for i in range(60,1,-1):
        time.sleep(1)
        print(i)
        if i==Detener:
            print("\33[103m"+"Tiempo acabado"+"\33[om")
            break;
        
        
#reloj_60()

def Ganacias_ia():
    Cantidad_invertida=float(input("Ingrese la cantidad que va invertir: "))
    Interes_inversion=float(input("Ingrese el interes anual: "))
    Años_inversion=int(input("Ingrese años a invertir: "))
    dinero_ganado = Cantidad_invertida
    for i in range(1,Años_inversion+1):
        Inversion= dinero_ganado * (Interes_inversion / 100)
        time.sleep(1)
        Inversion_año=dinero_ganado+Inversion
        dinero_ganado=Inversion_año
        print(Inversion)
        print(Inversion_año)
        print("Dinero ganado al año es: ", dinero_ganado)
        
#Ganacias_ia()
    
def Triangulo_astericos():
    altura=int(input("Ingrese la altura deseada: "))
    for i in range(1,altura+1):
        print(" "*(altura-i), end="")
        print("*"*(2*i-1))
        
#Triangulo_astericos()
    
    
    
    
    
    
    
    
def Triangulo_aste():
    altura=int(input("Ingrese la altura del triangulo: "))
    for i in range(1,altura+1):
        print(" "*(altura-i), end="")
        print("*"*i)
        
            

#Triangulo_aste()


def descubrir_contraseña ():
    contraseña = "12345678"
    contraseña_ingresada = ""
    intento_ingresado = int(input("Por favor ingrese un numero de intentos: "))
    intento = 1
    while contraseña_ingresada != contraseña:
        contraseña_ingresada = str(input("Ingrese la contraseña: "))
        if contraseña_ingresada != contraseña: 
            print("La contraseña no coincide")
        elif contraseña_ingresada == contraseña:
            print("Contraseña correcta")
            break
        if intento == intento_ingresado:
            print("Se llego al limite de intentos")
            break
        intento = intento + 1
#descubrir_contraseña()

def Caracteres_palabra():
    frase=str(input("Ingrese la frase: "))
    letra=str(input("Ingrese la letra a buscar: "))
    contador=0
    for i in frase:

        if i == letra:
            contador=contador+1
    print("La letra ",letra," se repite",contador,"veces")
    
            
            
Caracteres_palabra()
    
    
    
    
