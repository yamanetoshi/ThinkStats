import Pmf
import PmfMean
import unittest

class TestPmfMean(unittest.TestCase):
    def test_PmfMean(self):
        p = Pmf.MakePmfFromDict({1: 0.2, 2: 0.2, 3: 0.2, 4: 0.2, 5: 0.2})
        self.assertEqual(p.Mean(), PmfMean.PmfMean(p))

if __name__ == '__main__':
    unittest.main()
