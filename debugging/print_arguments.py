#!/usr/bin/python3
import sys

def main():
    # Check if there are any command-line arguments besides the script name
    if len(sys.argv) <= 1:
        print("No command-line arguments provided.")
    else:
        # Iterate over the command-line arguments, skipping the first one (script name)
        for i in range(1, len(sys.argv)):
            print(sys.argv[i])

if __name__ == "__main__":
    main()
