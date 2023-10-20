# Test all implementations and plot results

import time
import random
import numpy as np
import matplotlib.pyplot as plt

import linear_algebra as pylinalg
import clib_linalg as clinalg


def main():

    n = 7

    print("Timing 1000 trials of 1000 matrix multiplications for each implementation")
    print(f"Matrix size: {n}x{n}; times are summed, averaged, and graphed")

    data_py = []
    data_numpy = []
    data_c = []

    for i in range(1000):
        # Generate random matrices
        a = np.array([float(random.randint(0, 9)) for _ in range(n * n)])
        b = np.array([float(random.randint(0, 9)) for _ in range(n * n)])

        anp = a.reshape(n, n)  # make sure arrays are n x n for numpy
        bnp = b.reshape(n, n)

        # empty result arrays
        npresult = np.zeros((n, n), dtype=float)
        result = [0] * (n * n)

        # raw Python testing
        start = time.time()
        for _ in range(1000):
            pylinalg.mult(n, n, n, a, b, result)
        end = time.time()

        data_py.append(end - start)

        # Numpy testing
        start = time.time()
        for _ in range(1000):
            np.matmul(anp, bnp, out=npresult)
        end = time.time()

        data_numpy.append(end - start)

        # re-empty result array for C testing
        result = np.zeros(n * n, dtype=float)

        # C library testing
        start = time.time()
        for _ in range(1000):
            clinalg.multpy(n, n, n, a, b, result)
        end = time.time()

        data_c.append(end - start)

        if i == 99:
            print("100 trials done")
        elif i == 299:
            print("300 trials done")
        elif i == 699:
            print("700 trials done\n")

    # Calculate the average and total time for each implementation, and plot the results

    total_time = sum(data_py)
    average_time = total_time / 100

    print(f"Results for raw Python:")
    print(f"Average time: {average_time:.6f}")
    print(f"Total Time: {total_time:.6f}\n")
    print("Data:")
    for d in data_py:
        print(f"{d:.6f}")

    total_time = sum(data_numpy)
    average_time = total_time / 100

    print(f"Results for NumPy:")
    print(f"Average time: {average_time:.6f}")
    print(f"Total Time: {total_time:.6f}\n")
    print("Data:")
    for d in data_numpy:
        print(f"{d:.6f}")

    total_time = sum(data_c)
    average_time = total_time / 100

    print(f"Results for C library:")
    print(f"Average time: {average_time:.6f}")
    print(f"Total Time: {total_time:.6f}\n")
    print("Data:")
    for d in data_c:
        print(f"{d:.6f}")

    plt.hist(data_c, bins='auto', alpha=0.5, color='red', label='C library')
    plt.hist(data_numpy, bins='auto', alpha=0.5, color='blue', label='NumPy')
    plt.hist(data_py, bins='auto', alpha=0.5,
             color='green', label='raw Python')

    plt.title(f"1000 {n}x{n} Matrix Multiplications Times")

    plt.xlabel('Time per 1000 operations (s)')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')

    plt.show()


if __name__ == "__main__":
    main()
