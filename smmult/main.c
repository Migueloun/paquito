#include <stdio.h>
#include <inttypes.h>

#include "myLibrary.h"

uint32_t suma_uno(uint32_t num)
{
    return num+1;
}

int main( int argc, char * argv [] )
{
    uint32_t num = 5;
    
    num = suma_uno(num);
    printf("Resultado: %d\n", num);

    return 0;
}
