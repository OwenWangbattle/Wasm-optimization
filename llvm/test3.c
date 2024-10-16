#include <stdio.h>

typedef struct
{
    int id;
    char name[20];
} Person;

int main()
{
    Person person1 = {1, "Alice"};
    Person person2;
    person2 = person1;

    printf("Person 2 ID: %d, Name: %s\n", person2.id, person2.name);
    return 0;
}