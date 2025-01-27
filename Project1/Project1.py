#Punto 1 | El IMC
def imc (altura:float, peso:int)-> float: 
    IMC = round (peso / (altura ** 2),2)
    return IMC

altura = float(input("¿Cual es tu altura? : "))    
while altura < 1:
    print ("Ingresa un valor valido")
    altura = float(input("¿Cual es tu altura? : "))

peso = int ( input("¿Cual es tu peso? : "))
while peso < 1:
    print ("Ingresa un peso valido")
    peso = int ( input("¿Cual es tu peso? : "))

IMC_check = imc (altura, peso)

if (IMC_check > 18.5 and IMC_check < 25):
    print (f"Tu IMC es de {IMC_check}, tu peso es saludable")
else:
    print (f"Tu IMC es de {IMC_check}, es mejor ir al medico")



#Punto 2 | Años Bisiestos
def bisiesto(year:int)->bool:
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 !=0):
        print ("No es bisiesto")
        return (False)
    else:
        print ("Es bisiesto")
        return (True)

year = int (input("Ingresa el año que quieres verificar: "))
bisiesto(year)


#Punto 3 | ¿Usted me divide?
def divisibles(num1:int, num2:int)->list:
    div = []
    for number in range (1, 101):
        numero1 = int (num1)
        numero2 = int (num2)
        if number % numero1 == 0 and number % numero2 == 0:
            div.append (number)        
    
    return(div)

numero1 = int (input("Indica el primer numero "))
numero2 = int (input("Indica el segundo numero "))

divisibles_val = divisibles(numero1, numero2)
print (divisibles_val)


#Punto 4 | Clasificando Palabras
def clasificacion(word_list:list)->dict:
    dictionary = {}

    for word in word_list:
        dictionary[word] = len (word)
    print (dictionary)

clasificacion(word_list = ["Muchos", "años", "después", "frente", "al"])

