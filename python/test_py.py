import time
import random

from linear_algebra import mult


def main():
    print("Timing 100 trials of 100,000 matrix multiplications")
    print("Matrix size: 5x5; times are summed and averaged")

    data = []

    n = 5

    result = [0] * (n * n)

    for _ in range(100):
        # Generate random matrices, ensures only ints but stored as float
        a = [float(random.randint(0, 9)) for _ in range(n * n)]
        b = [float(random.randint(0, 9)) for _ in range(n * n)]

        start = time.time()
        for _ in range(100000):
            mult(n, n, n, a, b, result)
        end = time.time()

        data.append(end - start)

    # Calculate the average and total time
    total_time = sum(data)
    average_time = total_time / 100

    print(f"Average time: {average_time:.6f}")
    print(f"Total Time: {total_time:.6f}")

    # Print the array of data
    print("Data:")
    for d in data:
        print(f"{d:.6f}")


if __name__ == "__main__":
    main()
