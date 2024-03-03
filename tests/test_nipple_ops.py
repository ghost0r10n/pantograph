import unittest
import numpy as np
from pantograph.nipple_ops import *
from pantograph.utils.nipple_utils import get_empty_nipple 

class TestSingleBitOps(unittest.TestCase):

    def setUp(self):
        self.nipple1 = np.array([0]*25, dtype=np.int8)
        self.nipple2 = np.array([1]*25, dtype=np.int8)
        self.selector = np.array([1]*25, dtype=np.int8)

    def test_pn_25(self):
        output_nipple = pn_25(self.nipple1)
        self.assertTrue(np.all(output_nipple == 1))
        output_nipple = pn_25(self.nipple2)
        self.assertTrue(np.all(output_nipple == 0))

    def test_pand_25(self):
        output_nipple = pand_25(self.nipple1, self.nipple2)
        self.assertTrue(np.all(output_nipple == 0))
        output_nipple = pand_25(self.nipple1, self.selector)
        self.assertTrue(np.all(output_nipple == self.nipple1))

    def test_pnand_25(self):
        output_nipple = pnand_25(self.nipple1, self.nipple2)
        self.assertTrue(np.all(output_nipple == 1))
        output_nipple = pnand_25(self.nipple1, self.selector)
        self.assertTrue(np.all(output_nipple == pn_25(self.nipple1)))

    def test_por_25(self):
        output_nipple = por_25(self.nipple1, self.nipple2)
        self.assertTrue(np.all(output_nipple == 1))
        output_nipple = por_25(self.nipple1, self.selector)
        self.assertTrue(np.all(output_nipple == self.selector))

    def test_pxor_25(self):
        output_nipple = pxor_25(self.nipple1, self.nipple2)
        self.assertTrue(np.all(output_nipple == 1))

    def test_pfa_25(self):
        output_nipple = pfa_25(self.nipple1, self.nipple2)
        self.assertTrue(np.all(output_nipple == 1))
        output_nipple = pfa_25(self.nipple1, self.selector)
        self.assertTrue(np.all(output_nipple == self.selector))

    def test_pfs_25(self):
        output_nipple = pfs_25(self.nipple2, self.nipple1)
        self.assertTrue(np.all(output_nipple == 1))

if __name__ == '__main__':
    unittest.main()

