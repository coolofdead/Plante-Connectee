#include <stdio.h>
#include <stdlib.h>
#include "time.h"
#include "BinaireToDecimal.h"
#include "DecimalToBinaire.h"
#include "FileManaging.h"

/*THIS CODE WAS MADE BY THOMAS GIOVANNONI*/

void ChangeFrame (int *frame)
{
    scanf("%i", frame);
}

int main()
{
    int frameCounter = 0;
    int writeFrame = 0;
    int readFrame = 0;

    int choice = -1;

    while (choice != 0 && choice != 1)
    {
        printf("Enter 0 to ONLY read & print the contents of the txt\n");
        printf("Enter 1 to ONLY write random values over time in the txt\n");
        scanf("%i", &choice);
    }

    printf("%s", choice == 0 ? "How many seconds between each read ?\n" : "How many seconds between each write ?\n");
    ChangeFrame(choice == 0 ? &readFrame : &writeFrame);

    while(1)
    {
        frameCounter++;

        if(frameCounter == (choice == 0 ? readFrame : writeFrame))
        {
            frameCounter = 0;
            if(choice == 0)
            {
                //READ
                int *octet = ReadNextOctet();
                printf("%s", octet != NULL ? "Next octet is " : "There is nothing in the txt error ");
                printf("%i\n",  octet != NULL ? BinaireToDecimal(octet) : 404);
            }
            else
            {
                //WRITE
                int newDecimal = rand()%256;
                WriteOctet(DecimalToBinaire(newDecimal));
                printf("%i a ete ecrit dans le tampon\n", newDecimal);
            }
        }
        clock_t startTime = clock();
        while(clock() < startTime + (choice == 0 ? readFrame*1000 : writeFrame*1000));
    }

    return 0;
}
