# linear-algebra
Implementations of matrix operations in different languages, to test speed differences and experiment with optimizations

Currently finished C, Python, and NumPy implementations. 
Will compare run times to optimized c and the NumPy linear algebra implementation (partially in Fortran).

Each trial consists of running the given operation 100000 times; the time needed for each trial is recorded in seconds.
The numbers in the table are the averages of 100 trials per operation.

Current results:
|          | Matrix Multiplication (5x5, Rand(0-9)) |
|----------|----------------------------------------|
| C        | 0.041380                               |
| Python   | 1.999712                               |
| NumPy    | 0.160758                               |

Notes:
- The time needed to process the loop is included in all implementations. This disadvantages the Python implementations, as looping in C is much faster, and prevents the results from reflecting only the time differences of the matrix operations.
- The individual times per trial have a much lower resolution in C, because of how the time value is derived from the clock
- The unoptimized C multiplication implementation is 48x faster than the unoptimized python, close to the expected 45x speedup (previously, the speedup was claculated to be 45x, but I was incorrectly generating decimal numbers in the range 0-10 in Python. I also reinitialized the result matrix to 0 for each trial in Python. I am unsure why these changes increased the time).
- When the C code was compiled with the -01 flag, the average time was 0.008020 seconds, which could be due to the compiler optimizing out the entire loop. Interestingly, when compiled with the -03 flag, the time was higher, at 0.010730 seconds.
- The NumPy implementation uses numpy arrays for the inputs and outputs; this is different than the row-major single arrays used for C and raw Python, but is optimal for NumPy.
- The first average of the NumPy data is usually much higher than the rest; I am not sure why, but it could have to do with how the result matrix is initialized


