def abbreviate(frase):
   
  mayus_frases = frase.upper()
  palabras =( mayus_frases.replace("-", " ").replace("   ", " ").replace("  ", " ").replace("_", "")).split()
    
  acronimo=""
       
  for palabra in palabras:
      
    acronimo=  acronimo + palabra[0]
    
  return acronimo