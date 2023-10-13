#include "linear_algebra.h"
// matrices stored in row-major order

void add(int m, int n, double *A, double *B, double *Y)
{
    int i;
    for (i = 0; i < m * n; i++)
    {
        Y[i] = A[i] + B[i];
    }
} // Y = A + B

void linearcomb(int m, int n, double sa, double sb, double *A, double *B, double *Y)
{
    int i;
    for (i = 0; i < m * n; i++)
    {
        Y[i] = sa * A[i] + sb * B[i];
    }
} // 𝑌 = 𝑠𝑎 × 𝐴 + 𝑠𝑏 × 𝐵

void transpose(int m, int n, double *A, double *A_t)
{
    int i;
    int j;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            A_t[j * m + i] = A[j + i * n];
        }
    }
} // A_t = transpose(A)

int equal(int m, int n, double *A, double *B)
{
    int i;
    for (i = 0; i < m * n; i++)
    {
        if (A[i] != B[i])
        {
            return 0;
        }
    }

    return 1;
} // returns 1 if equal, 0 if not

void mult(int m1, int n1m2, int n2, double *A, double *B, double *Y)
{
    int i;
    int j;
    int k;
    double sum;

    for (i = 0; i < m1; i++)
    {
        for (j = 0; j < n2; j++)
        {
            sum = 0;

            for (k = 0; k < n1m2; k++)
            {
                sum += A[i * n1m2 + k] * B[j + k * n2];
            }

            Y[j + i * n2] = sum;
        }
    }

} // 𝑌 = 𝐴 × B

