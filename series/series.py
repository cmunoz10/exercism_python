def slices(series, tamaño):
    
    if len(series) < tamaño:
        raise ValueError("el tamaño es mayor que la serie")

    if tamaño < 1:
        raise ValueError("el tamaño debe ser mayor de 1 ")

    return [series[i:i+tamaño] for i, _ in enumerate(series[:len(series) - tamaño +1]) ]