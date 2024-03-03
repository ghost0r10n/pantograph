from pantograph.single_bit_ops import * 
from pantograph.utils.nipple_utils import get_empty_nipple 

def pn_25(nipple):
	output_nipple = get_empty_nipple()
	for i in range(25):
		output_nipple[i] = pn(nipple[i])
	return output_nipple

def pand_25(nipple1, nipple2):
    nipple3 = get_empty_nipple()
    for i in range(25):
        nipple3[i] = pand_1(nipple1[i],nipple2[i])
    return nipple3

def pnand_25(nipple1, nipple2):
    nipple3 = get_empty_nipple()
    for i in range(25):
        nipple3[i] = pnand_1(nipple1[i],nipple2[i])
    return nipple3

def por_25(nipple1, nipple2):
    nipple3 = get_empty_nipple() 
    for i in range(25):
        nipple3[i] = por_1(nipple1[i],nipple2[i])
    return nipple3

def pnor_25(nipple1, nipple2):
    nipple3 = get_empty_nipple() 
    for i in range(25):
        nipple3[i] = pnor_1(nipple1[i],nipple2[i])
    return nipple3


def pxor_25(nipple1, nipple2):
    nipple3 = get_empty_nipple() 
    for i in range(25):
        nipple3[i] = pxor_1(nipple1[i],nipple2[i])
    return nipple3

def pfa_25(nipple1, nipple2):
    nipple3 = get_empty_nipple()
    carry_tmp = 0
    for i in range(25):
        nipple3[i], carry_tmp = pfa_1(nipple1[i],nipple2[i],carry_tmp)
    return nipple3

def pfs_25(nipple1, nipple2):
    nipple3 = get_empty_nipple()
    borrow_tmp = 0
    for i in range(25):
        nipple3[i], borrow_tmp = pfs_1(nipple1[i],nipple2[i],borrow_tmp)
    return nipple3

def pmux_2(nipple1, nipple2, selector):
	selector_a = pand_25(nipple1, selector)
	selector_b = pand_25(nipple2, pn_25(selector))
	return por_25(selector_a, selector_b)
