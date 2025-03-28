#include <math.h>

int is_prime(int number) {
   if (number <= 1) { return 0; }

   double max_loops = sqrt((double)number);

   for (int i = 2; i < (int)max_loops; i++) {
      if (number % i == 0) { return 0; }
   }
   return 1;
}


int main() { 
   const int MAX = 9000000;

   for (int i = 0; i < MAX; i++) {
      is_prime(i);
   }
      

}
