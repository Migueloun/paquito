#include <stdio.h>
#include "myLibrary.h"
#include <stdlib.h>
#include <time.h>

#define N 3

int main( int argc, char * argv [] )
{
    //uint32_t num = 5;
    
    //num = suma_uno(num);
    //printf("Resultado: %d\n", num);
    
    
    float A[N][N] = {};
    uint8_t i=0;
    uint8_t j=0;
        
    srand(time(NULL));
    
    for(i=0; i<N; i++)
    {
        for(j=0; j<N; j++)
        {
            A[i][j] = (float)rand()/(float)(RAND_MAX/10);
            printf("%f\n", A[i][j]);
        }
    }                

    return 0;
}
