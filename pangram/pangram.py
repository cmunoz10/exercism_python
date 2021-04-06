def is_pangram(palabra):
    mayus_palabra=palabra.upper()
    puntajeA=mayus_palabra.count("A")
    if puntajeA > 0 :
    	puntajeA=1
    puntajeB=mayus_palabra.count("B")
    if puntajeB > 0 :
    	puntajeB=1
    puntajeC=mayus_palabra.count("C")
    if puntajeC > 0 :
    	puntajeC=1
    puntajeD=mayus_palabra.count("D")
    if puntajeD > 0 :
    	puntajeD=1
    puntajeE=mayus_palabra.count("E")
    if puntajeE > 0 :
    	puntajeE=1
    puntajeF=mayus_palabra.count("F")
    if puntajeF > 0 :
    	puntajeF=1
    puntajeG=mayus_palabra.count("G")
    if puntajeG > 0 :
    	puntajeG=1
    puntajeH=mayus_palabra.count("H")
    if puntajeH > 0 :
    	puntajeH=1
    puntajeI=mayus_palabra.count("I")
    if puntajeI > 0 :
    	puntajeI=1
    puntajeJ=mayus_palabra.count("J")
    if puntajeJ > 0 :
    	puntajeJ=1
    puntajeK=mayus_palabra.count("K")
    if puntajeK > 0 :
    	puntajeK=1
    puntajeL=mayus_palabra.count("L")
    if puntajeL > 0 :
    	puntajeL=1
    puntajeM=mayus_palabra.count("M")
    if puntajeM > 0 :
    	puntajeM=1
    puntajeN=mayus_palabra.count("N")
    if puntajeN > 0 :
    	puntajeN=1
    puntajeO=mayus_palabra.count("O")
    if puntajeO > 0 :
    	puntajeO=1
    puntajeP=mayus_palabra.count("P")
    if puntajeP > 0 :
    	puntajeP=1
    puntajeQ=mayus_palabra.count("Q")
    if puntajeQ > 0 :
    	puntajeQ=1
    puntajeR=mayus_palabra.count("R")
    if puntajeR > 0 :
    	puntajeR=1
    puntajeS=mayus_palabra.count("S")
    if puntajeS > 0 :
    	puntajeS=1
    puntajeT=mayus_palabra.count("T")
    if puntajeT > 0 :
    	puntajeT=1
    puntajeU=mayus_palabra.count("U")
    if puntajeU > 0 :
    	puntajeU=1
    puntajeV=mayus_palabra.count("V")
    if puntajeV > 0 :
    	puntajeV=1
    puntajeW=mayus_palabra.count("W")
    if puntajeW > 0 :
    	puntajeW=1
    puntajeX=mayus_palabra.count("X")
    if puntajeX > 0 :
    	puntajeX=1
    puntajeY=mayus_palabra.count("Y")
    if puntajeY > 0 :
    	puntajeY=1
    puntajeZ=mayus_palabra.count("Z")
    if puntajeZ > 0 :
    	puntajeZ=1
    puntaje_=mayus_palabra.count("_")
    if puntaje_ > 0 :
    	puntaje_=1
    							  
    
    puntajeTotal=puntajeW+puntajeA+puntajeB+puntajeC+puntajeD+puntajeE+puntajeF+puntajeG+puntajeH+puntajeI+puntajeJ+puntajeK+puntajeL+puntajeM+puntajeN+puntajeO+puntajeP+puntajeQ+puntajeR+puntajeS+puntajeT+puntajeU+puntajeV+puntajeX+puntajeY+puntajeZ
    
    if puntajeTotal==26:
        return True
    else: 
        return False
        
 