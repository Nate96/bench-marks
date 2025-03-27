using System;

class Program
{
   static bool IsPrime(int number)
   {
      if (number <= 1) { return false; }

      double upperBound = Math.Sqrt((double)number);
      
      for (int i = 2; i <= (int)upperBound; i++)
      {
         if (number % i == 0) { return false; }
      }
      return true;
   }

   static void Main()
   {
      const long UPPER_BOUND = 100000;
      for (int i = 1; i <= UPPER_BOUND; i++)
      {
         IsPrime(i);
      }
   }
}
