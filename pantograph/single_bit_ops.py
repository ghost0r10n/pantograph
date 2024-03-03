def pn(bit1):
    return 1 if bit1==0 else 0

def pand_1(bit1, bit2):
    return 1 if bit1==1 and bit2==1 else 0

def pnand_1(bit1, bit2):
    return pn(pand_1(bit1,bit2))

def pxor_1(bit1, bit2):
    return por_1(pand_1(bit1, pn(bit2)), pand_1(pn(bit1),bit2))
    
def por_1(bit1, bit2):
    return pn(pand_1(pn(bit1),pn(bit2)))

def pha_1(bit1, bit2):
    sum = pxor_1(bit1, bit2)
    carry = pand_1(bit1, bit2)
    return sum, carry

def phs_1(bit1, bit2):
    sub = pxor_1(bit1, bit2)
    borrow = pand_1(pn(bit1), bit2)
    return sub, borrow 

def pfa_1(bit1, bit2, carry_in):
    s_b1b2, c_b1b2= pha_1(bit1, bit2)
    sum,carry_tmp= pha_1(s_b1b2, carry_in)
    carry= por_1(carry_tmp, c_b1b2)
    return sum, carry 

def pfs_1(bit1, bit2, borrow_in):
    s_b1b2, b_b1b2= phs_1(bit1, bit2)
    sub,borrow_tmp= phs_1(s_b1b2, borrow_in)
    borrow= por_1(borrow_tmp, b_b1b2)
    return sub,borrow 


