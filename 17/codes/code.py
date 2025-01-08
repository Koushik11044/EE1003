import ctypes
lib = ctypes.CDLL('./code.so')
lib.Area.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
lib.Area.restype = ctypes.c_double

a = -1.0 # Lower limit
b = 1.0 # Upper limit
n = 1000 # Number of subintervals

print("Area bounded is: ",lib.Area(a, b, n))
