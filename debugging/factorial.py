#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive integer.")
        else:
            print(f"The factorial of {n} is {factorial(n)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()


