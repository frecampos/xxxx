from django.test import TestCase
import unittest
from .models import MisionyVision

# Create your tests here.
class TestUno(unittest.TestCase):

    def test_igualdad_cadenas(self):
        self.assertEqual('iii','iii')

    def test_texto_mayuscula(self):
        self.assertEqual('ii'.upper(),'II')

    def test_no_esta_el_contenido(self):
        self.assertFalse('hola' in 'es un Coca Cola')

    def grabar_mision_y_vision(self):
        m = MisionyVision(
            mision="nuestra mision...",vision="nuestra vision es"
        )
        valor=0
        try:
            m.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

    def listar_mision(self):
        lm= MisionyVision.objects.all()
        self.assertIsInstance(lm,MisionyVision)
        
if __name__ == "__main__":
    unittest.main()