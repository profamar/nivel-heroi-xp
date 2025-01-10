import unittest
from main import classificar_nivel_heroi  # Certifique-se de que a função está importada corretamente

class TestClassificadorHeroi(unittest.TestCase):

    def test_ferro(self):
        self.assertEqual(classificar_nivel_heroi(999), "Ferro")

    def test_bronze(self):
        self.assertEqual(classificar_nivel_heroi(1500), "Bronze")

if __name__ == '__main__':
    unittest.main()
