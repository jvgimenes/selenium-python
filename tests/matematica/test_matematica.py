from unittest import result
from src.matematica import somar, numero_par

def test_somar():
    result = somar(1, 2)
    assert result == 3

def numero_par():
    result = numero_par(2)
    assert result == True