import time
import os
from datetime import datetime


def test_python():
    BILLION = 1000000000
    count = 0

    start_time = time.time()
    while count < BILLION:
        count = count + 1
    end_time = time.time()

    return round(end_time - start_time, 2)


def test_c():
    os.system("gcc billion.c -o billion")
    start_time = time.time()
    os.system("./billion")
    end_time = time.time()

    return round(end_time - start_time, 2)


def test_go():
    start_time = time.time()
    os.system("go run billion.go")
    end_time = time.time()

    return round(end_time - start_time, 2)


def test_csharp():
    # os.system("dotnet build")

    start_time = time.time()
    os.system("./bin/Debug/net8.0/bench-marks")
    end_time = time.time()

    return round(end_time - start_time, 2)


if __name__ == "__main__":
    python_time = 0
    c_time = 0
    go_time = 0
    csharp_time = 0
    LOOPS = 5

    print("Test Time Stamp", datetime.now())
    for _ in range(LOOPS):
        python_time += test_python()
        c_time += test_c()
        go_time += test_go()
        csharp_time += test_csharp()

    print(f"All Results is an average of {LOOPS} loops")
    print("python:", round(python_time/LOOPS, 2))
    print("C:     ", round(c_time/LOOPS, 2))
    print("Go:    ", round(go_time/LOOPS, 2))
    print("CSharp:", round(csharp_time/LOOPS, 2))
