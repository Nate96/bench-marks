import java.lang.Math;

public class PrimeNumbers {
   private static boolean isPrime(int number) {
      if (number <= 1) { return false; }

      int upperBound = (int)Math.sqrt(number);

      for (int i = 2; i < (int)upperBound; i++) {
         if (number % i == 0) { return false; }
      }
      return true;
   }

   public static void main(String[] args) {
      final int upperBound = 9000000;

      for (int i = 1; i <= upperBound; i++) {
         isPrime(i);
      }
   }

}
