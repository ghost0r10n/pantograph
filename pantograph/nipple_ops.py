from pantograph.single_bit_ops import * 

def pand_25(nipple1, nipple2):
    nipple3 = ["0"] * 25
    for i in range(25):
        nipple3[i] = pand_1(nipple1[i],nipple2[i])
    return nipple3

def pnand_25(nipple1, nipple2):
    nipple3 = ["0"] * 25
    for i in range(25):
        nipple3[i] = pnand_1(nipple1[i],nipple2[i])
    return nipple3

def por_25(nipple1, nipple2):
    nipple3 = ["0"] * 25
    for i in range(25):
        nipple3[i] = por_1(nipple1[i],nipple2[i])
    return nipple3

def pxor_25(nipple1, nipple2):
    nipple3 = ["0"] * 25
    for i in range(25):
        nipple3[i] = pxor_1(nipple1[i],nipple2[i])
    return nipple3

def pfa_25(nipple1, nipple2):
    nipple3 = ["0"] * 25
    carry_tmp = "0"
    for i in range(25):
        nipple3[i], carry_tmp = pfa_1(nipple1[i],nipple2[i],carry_tmp)
    return nipple3

def pfs_25(nipple1, nipple2):
    nipple3 = ["0"] * 25
    borrow_tmp = "0"
    for i in range(25):
        nipple3[i], borrow_tmp = pfs_1(nipple1[i],nipple2[i],borrow_tmp)
    return nipple3


