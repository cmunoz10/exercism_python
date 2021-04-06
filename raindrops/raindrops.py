def convert(numero):
    output = ""
    
    #divisible entre 3 
    if numero % 3 == 0:
        output = "Pling"
    
    #divisible entre 5     
    if numero % 5 == 0:
        output = "Plang"
    
    #divisible entre 7    
    if numero % 7 == 0:
        output = "Plong"
    
    #divisible entre 3 y 5 
    if numero % 3== 0 and numero % 5==0:
        output = "PlingPlang"
    
    #divisible entre 3 y 7
    if numero % 3== 0 and numero % 7==0:
        output = "PlingPlong"
    
    #divisible entre 5 y 7
    if numero % 5== 0 and numero % 7==0:
        output = "PlangPlong"
    
    #divisible entre todos 
    if numero % 5== 0 and numero % 7==0 and numero % 3== 0:
        output = "PlingPlangPlong"
    return output or str(numero)