from django.test import TestCase
import unittest
#from .models import MisionyVision,Insumos

# Create your tests here.
class TestUno(unittest.TestCase):

    def grabar_mision_y_vision(self):
        self.assertEqual('i','i')

class TestInsumo(unittest.TestCase):

    def grabar_insumo(self):
        valor = 0
        try:
            insum = Insumos(
                nombre="mm", precio=199, descripcion="kjahsdk",stock=98
            )
            insum.save()
            valor =1
        except:
            valor =0
        self.assertIn(valor,1)
      

if __name__ == "__main__":
    unittest.main()