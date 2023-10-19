// generates random numbers to run matrix operations; times runs of 1000

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "linear_algebra.h"

int main(int argc, char *argv[])
{
    printf("Timing 100 trials of 100,000 matrix multiplications\n");
    printf("Matrix size: 5x5; times are summed and averaged\n");

    // testing linear algebra function:
    printf("Testing linear algebra function with identity times [[1, 2], [3, 4]]:\n");
    double *f = (double *)malloc(4 * sizeof(double));
    double *g = (double *)malloc(4 * sizeof(double));
    double *h = (double *)malloc(4 * sizeof(double));

    // assign identity
    f[0] = 1;
    f[1] = 0;
    f[2] = 0;
    f[3] = 1;

    // assign matrix g
    for (int i = 1; i < 5; i++)
    {
        g[i-1] = i;
    }

    printf("Matrix h:\n");
    mult(2, 2, 2, f, g, h);
    for (int i = 0; i < 4; i++)
    {
        printf("%lf\n", h[i]);
    }

    clock_t start, end;
    double time;

    // input matrix params
    int n = 5; // 5 x 5
    double *a = (double *)malloc(n * n * sizeof(double));
    double *b = (double *)malloc(n * n * sizeof(double));
    double *result = (double *)malloc(n * n * sizeof(double));

    // array of data
    double *data = (double *)malloc(100 * sizeof(double));

    // 100 trials
    for (int i = 0; i < 100; i++)
    {
        // generate random matrices
        for (int j = 0; j < n * n; j++)
        {
            a[j] = (double)(rand() % 10); // num will be between 0 and 9
            b[j] = (double)(rand() % 10); // casted to double
        }

        // do 100,000 runs of mult
        start = clock();

        for (int k = 0; k < 100000; k++)
        {
            mult(n, n, n, a, b, result);
        }

        end = clock();
        data[i] = ((double)(end - start)) / CLOCKS_PER_SEC;
    }

    // return average and sum of time values
    double sum = 0;
    for (int i = 0; i < 100; i++)
    {
        sum += data[i];
    }
    printf("Average time: %f\n", sum / 100);
    printf("Total Time: %f\n", sum);

    // print array of data
    printf("Data: \n");

    for (int i = 0; i < 100; i++)
    {
        printf("%lf\n", data[i]);
    }

    return 0;
}