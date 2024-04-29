from dia import Dia
import pytest

def test_instanciar_dia_por_defecto():
    dia = Dia()
    assert dia.anyo == 1970
    assert dia.mes == 1
    assert dia.dia == 1

def test_instanciar_cumple_didier():
    dia = Dia(2024, 11, 28)
    assert dia.anyo == 2024
    assert dia.mes == 11
    assert dia.dia == 28

def test_mes_incorrecto():
    with pytest.raises(ValueError):
        dia = Dia(20224, 13, 1)

def test_dia_entre_1_y_31():
    with pytest.raises(ValueError):
        dia = Dia(2024, 12, 32)

def test_anyo_pisitivo():
    with pytest.raises(ValueError):
        dia = Dia(-2024, 12, 1)

def test_dia_incorrecto():
    with pytest.raises(ValueError):
        dia = Dia (2023, 2, 29)
    with pytest.raises(ValueError):
        dia = Dia (2024, 4, 31)
    with pytest.raises(ValueError):
        dia = Dia (2024, 6, 31)
    with pytest.raises(ValueError):
        dia = Dia (2024, 9, 31)
    with pytest.raises(ValueError):
        dia = Dia (2024, 11, 31)

def test_dis_correcto_29_febrero_en_bisiesto():
    dia = Dia(2024, 2, 29)
    assert dia.dia == 29
    

def test_anyos_bisiestos():
    dia = Dia(2024, 1, 1) #divisible entre 4
    assert dia.es_bisiesto() == True

    dia = Dia(2022, 1, 1) #año que no sea divisible
    assert dia.es_bisiesto() == False

    dia = Dia(2000, 1, 1) #entre 100 y no entre 400
    assert dia.es_bisiesto() == True

    dia = Dia(1900, 1, 1) #divisible entre 100 y 400
    assert dia.es_bisiesto() == False
    
    








