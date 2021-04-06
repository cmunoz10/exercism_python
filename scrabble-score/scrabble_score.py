def score(palabra):
    mayus_palabra=palabra.upper()
    puntajeA=mayus_palabra.count("A")*1
    puntajeB=mayus_palabra.count("B")*3
    puntajeC=mayus_palabra.count("C")*3
    puntajeD=mayus_palabra.count("D")*2
    puntajeE=mayus_palabra.count("E")*1
    puntajeF=mayus_palabra.count("F")*4
    puntajeG=mayus_palabra.count("G")*2
    puntajeH=mayus_palabra.count("H")*4
    puntajeI=mayus_palabra.count("I")*1
    puntajeJ=mayus_palabra.count("J")*8
    puntajeK=mayus_palabra.count("K")*5
    puntajeL=mayus_palabra.count("L")*1
    puntajeM=mayus_palabra.count("M")*3
    puntajeN=mayus_palabra.count("N")*1
    puntajeO=mayus_palabra.count("O")*1
    puntajeP=mayus_palabra.count("P")*3
    puntajeQ=mayus_palabra.count("Q")*10
    puntajeR=mayus_palabra.count("R")*1
    puntajeS=mayus_palabra.count("S")*1
    puntajeT=mayus_palabra.count("T")*1
    puntajeU=mayus_palabra.count("U")*1
    puntajeV=mayus_palabra.count("V")*4
    puntajeW=mayus_palabra.count("W")*4
    puntajeX=mayus_palabra.count("X")*8
    puntajeY=mayus_palabra.count("Y")*4
    puntajeZ=mayus_palabra.count("Z")*10
    puntajeTotal=puntajeW+puntajeA+puntajeB+puntajeC+puntajeD+puntajeE+puntajeF+puntajeG+puntajeH+puntajeI+puntajeJ+puntajeK+puntajeL+puntajeM+puntajeN+puntajeO+puntajeP+puntajeQ+puntajeR+puntajeS+puntajeT+puntajeU+puntajeV+puntajeX+puntajeY+puntajeZ
    
    return puntajeTotal
  
