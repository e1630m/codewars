#include <stdio.h>
#include <math.h>

int last_digit(const unsigned long int *arr, size_t arr_size) {
    long int base, exp, ldigit = 1;
    for (int i = (int) arr_size - 1; i >= 0; i--)
    {
        exp = ldigit < 4 ? ldigit : ldigit % 4 + 4;
        base = !i ? arr[i] % 10 : arr[i] < 4 ? arr[i] : arr[i] % 4 + 4;
        ldigit = pow(base, exp);
    }
    return ldigit % 10;
}
