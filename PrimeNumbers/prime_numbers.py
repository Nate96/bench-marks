import time
import os
import math
from datetime import datetime


def test_python():
    # 1000000000
    UPPER_BOUND = 100000

    start_time = time.time()
    res = []

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

    return res, round(end_time - start_time, 2)


if __name__ == "__main__":
    MAX_lOOPS = 5

    python_time = 0
    python_res = []

    print("Test Time Stamp", datetime.now())
    for _i in range(MAX_lOOPS):
        python_time += test_python()[1]

    print("Python:", round(python_time/MAX_lOOPS, 2))
