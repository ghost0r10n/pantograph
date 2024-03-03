import unittest
from pantograph.single_bit_ops import *

class TestLogicFunctions(unittest.TestCase):

    def test_pn(self):
        self.assertEqual(pn(0), 1)
        self.assertEqual(pn(1), 0)

    def test_pand_1(self):
        self.assertEqual(pand_1(0, 0), 0)
        self.assertEqual(pand_1(0, 1), 0)
        self.assertEqual(pand_1(1, 0), 0)
        self.assertEqual(pand_1(1, 1), 1)

    def test_pnand_1(self):
        self.assertEqual(pnand_1(0, 0), 1)
        self.assertEqual(pnand_1(0, 1), 1)
        self.assertEqual(pnand_1(1, 0), 1)
        self.assertEqual(pnand_1(1, 1), 0)

    def test_pxor_1(self):
        self.assertEqual(pxor_1(0, 0), 0)
        self.assertEqual(pxor_1(0, 1), 1)
        self.assertEqual(pxor_1(1, 0), 1)
        self.assertEqual(pxor_1(1, 1), 0)

    def test_por_1(self):
        self.assertEqual(por_1(0, 0), 0)
        self.assertEqual(por_1(0, 1), 1)
        self.assertEqual(por_1(1, 0), 1)
        self.assertEqual(por_1(1, 1), 1)

    def test_pha_1(self):
        self.assertEqual(pha_1(0, 0), (0, 0))
        self.assertEqual(pha_1(0, 1), (1, 0))
        self.assertEqual(pha_1(1, 0), (1, 0))
        self.assertEqual(pha_1(1, 1), (0, 1))

    def test_phs_1(self):
        self.assertEqual(phs_1(0, 0), (0, 0))
        self.assertEqual(phs_1(0, 1), (1, 1))
        self.assertEqual(phs_1(1, 0), (1, 0))
        self.assertEqual(phs_1(1, 1), (0, 0))

    def test_pfa_1(self):
        self.assertEqual(pfa_1(0, 0, 0), (0, 0))
        self.assertEqual(pfa_1(0, 0, 1), (1, 0))
        self.assertEqual(pfa_1(0, 1, 0), (1, 0))
        self.assertEqual(pfa_1(1, 0, 0), (1, 0))
        self.assertEqual(pfa_1(1, 1, 0), (0, 1))
        self.assertEqual(pfa_1(1, 1, 1), (1, 1))

    def test_pfs_1(self):
        self.assertEqual(pfs_1(0, 0, 0), (0, 0))
        self.assertEqual(pfs_1(0, 0, 1), (1, 1))
        self.assertEqual(pfs_1(0, 1, 0), (1, 1))
        self.assertEqual(pfs_1(0, 1, 1), (0, 1))
        self.assertEqual(pfs_1(1, 0, 0), (1, 0))
        self.assertEqual(pfs_1(1, 1, 0), (0, 0))
        self.assertEqual(pfs_1(1, 1, 1), (1, 1))

if __name__ == '__main__':
    unittest.main()
