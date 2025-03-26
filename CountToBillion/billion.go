package main

import "fmt"

func main() {
   count := 0

    for i := 1; i <= 1000000000; i++ {
       count++
    }
    fmt.Println("Counting to a billion completed!")
}
