import unittest

from app import somar


class TestSomar(unittest.TestCase):
    def test_somar_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_somar_zero(self):
        self.assertEqual(somar(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
