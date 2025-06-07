import pytest
from area import calcular_area_triangulo

def test_area_valida():
    assert calcular_area_triangulo(5, 7) == 17.5

def test_base_negativa():
    with pytest.raises(ValueError):
        calcular_area_triangulo(-3, 7)

def test_altura_negativa():
    with pytest.raises(ValueError):
        calcular_area_triangulo(5, -2)

def test_base_y_altura_negativas():
    with pytest.raises(ValueError):
        calcular_area_triangulo(-4, -3)

def test_base_cero():
    with pytest.raises(ValueError):
        calcular_area_triangulo(0, 10)

def test_altura_cero():
    with pytest.raises(ValueError):
        calcular_area_triangulo(5, 0)
