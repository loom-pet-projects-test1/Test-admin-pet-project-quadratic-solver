import unittest

from main import main


class MainTest(unittest.TestCase):
    def test_main_returns_zero(self):
        self.assertEqual(main(), 0)


if __name__ == "__main__":
    unittest.main()
