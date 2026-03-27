#!/usr/bin/env python3
import sys

def print_header(name):
    length = len(name) + 4
    print("*" * (length + 2))
    print(f"* {name} *")
    print("*" * (length + 2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Header"
    print_header(name)
