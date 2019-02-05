#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "DecimalToBinaire.h"

/*THIS CODE WAS MADE BY THOMAS GIOVANNONI*/

int* DecimalToBinaire(int decimal){
    int lenght = 0;
    int* binaryValue = calloc(8, sizeof(int));

    while (decimal != 0)
    {
        *(binaryValue+lenght) = decimal%2;
        decimal = decimal / 2;
        lenght++;
    }

    return binaryValue;
}
