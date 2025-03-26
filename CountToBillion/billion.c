#include <stdio.h>

int main() {
   int BILLION = 1000000000;
   int count = 0;

   for (int i = 0; i < BILLION; i++) {
      count++;
   }
   
   printf("Done");
}
