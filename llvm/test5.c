#include <stdio.h>

int globalVar = 5;

void overwriteGlobal()
{
    globalVar = 6;
    globalVar = 10;
}

int main()
{
    printf("Global variable before: %d\n", globalVar);
    overwriteGlobal();
    printf("Global variable after: %d\n", globalVar);
    return 0;
}