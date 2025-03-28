package main

import (
   "math"
)

func isPrime(number int) bool { 
   if number <= 1 { return false }

   upperBound := math.Sqrt(float64(number))

   for i := 2; i < int(upperBound); i++ {
      if number % i == 0 { return false }
   }
   return true
}

func main() {
   const upperBound int = 9000000
   for i := 1; i <= upperBound; i++ { isPrime(i) }
}
