# linear-algebra
Implementations of matrix operations in different languages, to test speed differences and experiment with optimizations

Currently finished c and python implementations. 
Will compare run times to optimized c and the NumPy linear algebra implementation (partially in Fortran).

Each trial consists of running the given operation 100000 times; the time needed for each trial is recorded in seconds.
The numbers in the table are the averages of 100 trials per operation.

Current results:
| Header 1 | Matrix Multiplication (5x5, Rand(0-9)) |
|----------|----------------------------------------|
| C        | 0.041380                               |
| Python   | 1.864539                               |

Notes:
- The individual times per trial have a much lower resolution in C, because of how the time value is derived from the clock
- The unoptimized C multiplication implementation is almost exactly 45x faster than the unoptimized python, as expected

