from cffi import FFI
import os
from math import ceil,log2
# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))


ffi = FFI()

# Define the C function signature
ffi.cdef("""
void cmv(int* A, int len, int thresh, double p, double* result);
""")

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the shared library
C = ffi.dlopen(os.path.join(current_dir, "cmvinterface/cmv.so"))



def cmv(A, thresh=None, epsilon=0.99, delta=0.9):
    if thresh is None:
        thresh = int(ceil((12 / (epsilon**2)) * log2((8 / delta))))
    p = 1.0

    A_ffi = ffi.new("int[]", A)
    result_ffi = ffi.new("double*")

    C.cmv(A_ffi, len(A), thresh, p, result_ffi)

    return result_ffi[0]
