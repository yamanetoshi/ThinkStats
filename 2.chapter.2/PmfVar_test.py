import Pmf
import PmfVar
import unittest

class TestPmfVar(unittest.TestCase):
    def test_PmfVar(self):
        p = Pmf.MakePmfFromDict({1: 0.2, 2: 0.2, 3: 0.2, 4: 0.2, 5: 0.2})
        self.assertEqual(p.Var(), PmfVar.PmfVar(p))

if __name__ == '__main__':
    unittest.main()
