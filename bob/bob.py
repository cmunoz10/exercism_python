def response(hey_bob):
  #texto con pregunta/incluye mayusculas 
    if hey_bob.strip().endswith("?"):
        return "Calm down, I know what I'm doing!" if hey_bob.isupper() else "Sure."
    #texto en mayusculas
    elif hey_bob.strip().isupper():
        return "Whoa, chill out!"
    #sin espacios al final
    elif not hey_bob.strip():
        return "Fine. Be that way!"
     
    else:
        return "Whatever."