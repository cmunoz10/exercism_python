from collections import Counter
import re
def count_words(frase):
    cantidad = Counter()
    palabras = re.findall("([A-Za-z]+'[A-Za-z]+|[0-9]+|[A-Za-z]+)",frase.lower())
    for palabra in palabras:
        cantidad[palabra] += 1
    return cantidad