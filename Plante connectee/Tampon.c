#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

void Blabla (int size);
void Print(int t[]);

int main (int octet[])
{
    printf("%i", 1==1);

    return 0;
}

void Blabla (int size)
{
    printf("size: %i", size);
}

void Print(int *t)
{
    int s = sizeof(t)/sizeof(int);
    printf("size: %i", s);
}
