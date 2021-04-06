def is_isogram(string):
    #convertir todo a mayusculas para casos mixtos 
    mayus_string = string.upper()

    for test in mayus_string:
        
        espacios= " "
        guiones = "-"
        # contar el numero de repeticiones 
        if mayus_string.count(test) > 1 :
            return False

        elif string.count(espacios) > 1 or string.count(guiones) > 1:
            return True 
        else:
            pass
    return True