
import unittest
from juego import Ahorcado

 
class TestCuboid(unittest.TestCase):
    '''
        Test comprueba si e   l resultado es el esperado 
    '''
    
    def setUp(self):
        self.ahorcado = Ahorcado()

    def test_value(self):
        self.assertNotEqual(self.ahorcado.elijeLetra('x'), True)

    

if __name__ == "__main__":
    unittest.main()