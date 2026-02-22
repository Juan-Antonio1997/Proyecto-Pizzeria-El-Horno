#Autor: Juan Antonio Gómez Martín
import pytest
from librerias import acceso_admin as adm

def test_password():
    passCheck = adm.check_password("password")
    assert passCheck == True