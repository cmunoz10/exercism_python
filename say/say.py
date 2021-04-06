numeros = {0: "zero",1: "one",2: "two",3: "three",4: "four",5: "five",6: "six",7: "seven",8: "eight",9: "nine",10: "ten",11: "eleven",12: "twelve",13: "thirteen",14: "fourteen",15: "fifthteen",16: "sixteen",17: "seventeen",18: "eighteen",19: "nineteen",20: "twenty",30: "thirty",40: "forty",50: "fifty",60: "sixty",70: "seventy",80: "eighty",90: "ninety",100: "hundred",1000: "thousand",1000000: "million",1000000000: "billion"}
def say(numero):
    residuo = 0
    guion = " "
    if numero < 0:
        raise ValueError("numero no debe ser negativo")
    elif numero < 21:
        resultado = numeros[numero]
    elif numero < 100:
        resultado = numeros[int(numero/10)*10]
        residuo = numero % 10
        guion = "-"
    elif numero < 1000:
        resultado = numeros[int(numero/100)] + guion + numeros[100]
        residuo = numero % 100
    elif numero < 1000000:
        resultado = say(int(numero/1000)) + guion + numeros[1000]

        residuo = numero % 1000
    elif numero < 1000000000:
        resultado = say(int(numero/1000000)) + guion + numeros[1000000]

        residuo = numero % 1000000
    elif numero < 1000000000000:
        resultado = say(int(numero/1000000000)) + guion + numeros[1000000000]
        residuo = numero % 1000000000
    else:
        raise ValueError("valor fuera de rango")

    if residuo > 0:
        resultado += guion + say(residuo)
    return resultado