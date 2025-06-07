def calcular_area_triangulo(base, altura):
    if base <= 0:
        raise ValueError("La base debe ser mayor que cero.")
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")
    return (base * altura) / 2
