import ctypes
import numpy as np

# Load the C library (change the library filename as needed)
dll = ctypes.CDLL("..\c\out\linear_algebra.dll")

# Define the function signature
mult = dll.mult
mult.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int,
                 np.ctypeslib.ndpointer(dtype=np.double, flags='C_CONTIGUOUS'),
                 np.ctypeslib.ndpointer(dtype=np.double, flags='C_CONTIGUOUS'),
                 np.ctypeslib.ndpointer(dtype=np.double, flags='C_CONTIGUOUS')]
mult.restype = None


def multpy(m1, n1m2, n2, A, B, Y):
    # Ensure A and B are NumPy arrays and are C-contiguous
    A = np.ascontiguousarray(A, dtype=np.double)
    B = np.ascontiguousarray(B, dtype=np.double)

    # Call the C function
    mult(m1, n1m2, n2, A, B, Y)

    # return Y
