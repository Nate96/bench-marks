import time
import os
import math
from datetime import datetime

UPPER_BOUND = 9000000


def test_python():
    start_time = time.time()

    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    for number in range(2, int(UPPER_BOUND + 1)):
        is_prime(number)
#        if is_prime(number):
#            res.append(number)
    end_time = time.time()

    return round(end_time - start_time, 2)


def test_c():
    # os.system("gcc c-prime-numbers.c -o c-prime-numbers -lm")

    start_time = time.time()
    os.system("./c-prime-numbers")
    end_time = time.time()

    return round(end_time - start_time, 2)


def test_go():
    start_time = time.time()
    os.system("go run primeNumbers.go")
    end_time = time.time()

    return round(end_time - start_time, 2)


def test_csharp():
    # os.system("dotnet build")

    start_time = time.time()
    os.system("./bin/Debug/net8.0/PrimeNumbers")
    end_time = time.time()

    return round(end_time - start_time, 2)


def test_rust():
    # os.system("rustc billion-rust.rs")

    start_time = time.time()
    os.system("./rust-prime-numbers")
    end_time = time.time()

    return round(end_time - start_time, 2)


def test_java():
    # os.system("javac BillionJava.java")

    start_time = time.time()
    os.system("java PrimeNumbers")
    end_time = time.time()

    return round(end_time - start_time, 2)


if __name__ == "__main__":
    python_time = 0
    c_time = 0
    go_time = 0
    csharp_time = 0
    rust_time = 0
    java_time = 0

    LOOPS = 5

    print(" ")
    print("Test Time Stamp", datetime.now())
    for _ in range(LOOPS):
        python_time += test_python()
        c_time += test_c()
        go_time += test_go()
        csharp_time += test_csharp()
        rust_time += test_rust()
        java_time += test_java()

    print("Finding all numbers between 0 and ", UPPER_BOUND)
    print(f"All Results is an average of {LOOPS} loops")
    print("python:", round(python_time/LOOPS, 2))
    print("Rust:  ", round(rust_time/LOOPS, 2))
    print("C:     ", round(c_time/LOOPS, 2))
    print("Go:    ", round(go_time/LOOPS, 2))
    print("Java:  ", round(java_time/LOOPS, 2))
    print("CSharp:", round(csharp_time/LOOPS, 2))
