#include <math.h>
#include <stdlib.h>

void cmv(int* A, int len, int thresh, double p, double* result) {
    int X[len];
    int X_size = 0;

    for (int i = 0; i < len; i++) {
        int a = A[i];

        // Remove previous elements
        for (int j = 0; j < X_size; j++) {
            if (X[j] == a) {
                for (int k = j; k < X_size - 1; k++) {
                    X[k] = X[k + 1];
                }
                X_size--;
                break;
            }
        }

        // Add element with probability p
        if ((double)rand() / RAND_MAX < p && X_size < thresh) {
            X[X_size++] = a;
        }

        // Remove elements with probability 1/2
        if (X_size >= thresh) {
            int new_size = 0;
            for (int j = 0; j < X_size; j++) {
                if ((double)rand() / RAND_MAX < 0.5) {
                    X[new_size++] = X[j];
                }
            }
            X_size = new_size;
            p /= 2.0;
        }
    }

    *result = (double)X_size / p;
}
