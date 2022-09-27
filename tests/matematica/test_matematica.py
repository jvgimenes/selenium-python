from unittest import result
from src.matematica import somar, numero_par

def test_somar():
    result = somar(1, 2)
    assert result == 3

def test_numero_par():
    result = numero_par(10)
    assert result == True

def test_somar_pares():
    first_number = 2
    sec_number = 4
    result = numero_par(first_number)
    assert result == True
    result = numero_par(sec_number)
    assert result == True
    result = somar(first_number, sec_number)
    assert result == 6