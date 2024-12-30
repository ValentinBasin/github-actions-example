import unittest
from src.app import add


class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(2, 1), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)


if __name__ == "__main__":
    unittest.main()
