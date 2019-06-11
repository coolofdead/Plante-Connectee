#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include "BinaireToDecimal.h"

/*THIS CODE WAS MADE BY THOMAS GIOVANNONI*/

int BinaireToDecimal (int octet[]){
    int decimal = 0;

    for(int i=0; i<8; i++)
    {
        decimal += (int)(octet[i] * pow(2, i));
    }

    return decimal;
}
