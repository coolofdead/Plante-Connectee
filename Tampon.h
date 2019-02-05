typedef struct TamponArray TamponArray;
struct TamponArray {
    int *binaryValue;
    TamponArray *next;
};

void AddTampon(int octet[]);
