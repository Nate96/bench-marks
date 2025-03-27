package main

import (
   "fmt"
   "math"
)


func isPrime(number int) bool { 
   if number <= 1 { return false }

   upperBound := math.Sqrt(float64(number))

   for i := 2; i < int(upperBound); i++ {
      if number % i == 0 { 
         return false
      }
   }
   return true
}

func main() {
   const upperBound int = 100000 
   var primes []int

    for i := 1; i <= upperBound; i++ { 
       if isPrime(i) {
          primes = append(primes, i)
       }
    }
    println(primes)
}
