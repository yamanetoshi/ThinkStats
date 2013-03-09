import Pmf
import PmfRemainingLifetime
import unittest

class TestPmfRemainingLifetime(unittest.TestCase):
    def test_PmfRemainingLifetime(self):
        pmf = Pmf.MakePmfFromDict({0: 0.2, 1: 0.2, 2: 0.2, 3: 0.2, 4: 0.2})
        newPmf = PmfRemainingLifetime.PmfRemainingLifetime(2, pmf)
        self.assertEqual([(1, 0.5), (2, 0.5)], newPmf.Items())

if __name__ == '__main__':
    unittest.main()
