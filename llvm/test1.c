#include <stdio.h>

int main() {
    int n = 5;
    int factorial = 1;
    int i = 1;

    while (i <= n) {
        factorial *= i;
        i++;
    }

    printf("Factorial of %d is %d\n", n, factorial);
    
    return 0;
}