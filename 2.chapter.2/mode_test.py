import Pmf
import mode
import unittest

class TestMode(unittest.TestCase):
    def test_mono(self):
        hist = Pmf.MakeHistFromList([1, 1, 1, 2, 3, 4])
        result = mode.Mode(hist)
        self.assertEqual([1], result)

    def test_multi(self):
        hist = Pmf.MakeHistFromList([1, 1, 2, 2, 3, 4])
        result = mode.Mode(hist)
        self.assertEqual([1, 2], result)

if __name__ == '__main__':
    unittest.main()
