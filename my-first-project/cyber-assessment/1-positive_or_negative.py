#!/usr/bin/env python3
import sys
import random

random.seed()
n = random.randint(-10, 10)
print(f"{n} is ", end="")

if n > 0:
    print("positive")
elif n == 0:
    print("zero")
else:
    print("negative")
