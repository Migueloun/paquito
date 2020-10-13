#include <stdio.h>
#include <inttypes.h>

int main() {
  
  float num[2];
  float resultado = 0.0;
  uint8_t i = 0;
  char operador = 0;
  
  for(i=0; i<2; i++) {
    printf("Introduce un numero: ");
    scanf("%f", &num[i]);
    printf("%f\n", num[i]);
  }

  printf("Introduce operacion: ");
  scanf("%s", &operador);

  switch(operador) {
    case '+': resultado = num[0] + num[1]; break;
    case '-': resultado = num[0] - num[1]; break;
    case '*': resultado = num[0] * num[1]; break;
    case '/': resultado = num[0] / num[1]; break;
    default: return -1;
  }

  printf("Resultado: %f\n", resultado);

  
  return 0;
}
