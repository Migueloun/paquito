#include <stdio.h>
#include <inttypes.h>

int main() {
  uint8_t arr1[5] = {1,2,4,8,16};
  uint16_t arr2[5] = {512, 1024, 2048, 4096, 8192};

  uint8_t* ptr1 = NULL;
  uint16_t* ptr2 = NULL;
  
  ptr2 = &arr2[1];

  printf("%d\n", *ptr2);
  return 0;
}
