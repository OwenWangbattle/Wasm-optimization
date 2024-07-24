#include <stdint.h>
#include <stdio.h>
int32_t arr[9];
int32_t *p = &arr[4];
int32_t foo () {
int32_t c = 110;
int32_t *d = &arr[4];
*p = c; //arr[4] = 110
*d ^= 123; //arr[4] = 21
return *d;
}
int main () {
int e = foo();
printf("%d\n", arr[4]+e);
return 0;
}