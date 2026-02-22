#Autor: Juan Antonio Gómez Martín
import pytest, pandas as pd
from librerias import pedido as ped

def test_iva():
    iva = ped.calcular_iva(20)
    assert iva == 2

def test_pedido_vacio():
    pedido = pd.DataFrame()
    subtotal = ped.calcular_subtotal(pedido)
    iva = ped.calcular_iva(subtotal)
    total = ped.calcular_total_final(subtotal, iva)
    assert total == 0
