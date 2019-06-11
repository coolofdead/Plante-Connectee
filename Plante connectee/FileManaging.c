#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "FileManaging.h"

/*THIS CODE WAS MADE BY THOMAS GIOVANNONI*/

char filePath[] = "TransferLog.txt";
FILE *file = NULL;

bool IsFileEmpty ()
{
    bool isEmpty = true;

    if(file != NULL)
    {
        rewind(file);
        char c = (char)fgetc(file);
        if(c == '0' || c == '1')
        {
            isEmpty = false;
        }
        rewind(file);
    }
    return isEmpty;
}

void WriteOctet (int octet[])
{
    file = OpenFile("r+");

    if(!IsFileEmpty())
    {
        fseek(file, 0, SEEK_END);
        fputs("\n", file);
    }

    for(int i=0; i<8; i++)
    {
        fputc((char)octet[i]+'0', file);
    }

    CloseFile(file);
}

int* ReadNextOctet ()
{
    file = OpenFile("r");
    int* octet = (file != NULL && !IsFileEmpty()) ? calloc(8, sizeof(int)) : NULL;

    if(octet != NULL)
    {
        for(int i=0; i<8; i++)
        {
            char b = (char)fgetc(file);
            if(b == '0')
            {
                *(octet+i) = 0;
            }
            else if (b == '1')
            {
                *(octet+i) = 1;
            }
        }
        DeleteNextOctet();
    }

    return octet;
}

void DeleteNextOctet ()
{
    rewind(file);

    if(file != NULL)
    {
        FILE* temp = fopen("temp.txt", "w");

        fseek(file, 10, SEEK_SET);
        char c;
        while(c != EOF)
        {
            c = getc(file);
            if(c != EOF)
            {
                fputc(c, temp);
            }
        }

        CloseFile(file);
        CloseFile(temp);
        remove("TransferLog.txt");
        rename("temp.txt", "TransferLog.txt");
    }
    else
    {
        printf("File couldn't be opened\n");
    }
}

FILE* OpenFile (char action[]){
    return fopen(filePath, action);
}

void CloseFile (FILE *file){
    fclose(file);
}
