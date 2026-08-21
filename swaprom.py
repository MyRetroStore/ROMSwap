#!/usr/bin/env python3

import sys
import os

VERSION = "1.0"
AUTHOR = "MyRetroStore"
WEBSITE = "https://myretrostore.co.uk"
GITHUB = "https://github.com/MyRetroStore/ROMSwap"

ROM_SIZE = 32768
HALF_SIZE = 16384
SEPARATOR = "-" * 40


def print_info():
    print(SEPARATOR)
    print("       ROM 32K Half Swap Utility")
    print(SEPARATOR)
    print(f"Version {VERSION}")
    print(f"Created by {AUTHOR}")
    print(f"Website: {WEBSITE}")
    print(f"Source:  {GITHUB}")
    print(SEPARATOR)
    print()


def main():
    print_info()

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.rom> <output.rom>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print(f"Input ROM : {input_file}")
    print(f"Output ROM: {output_file}")
    print()

    print("Checking input file...", end=" ")

    if not os.path.isfile(input_file):
        print("FAILED")
        print(f"Error: input file does not exist: {input_file}")
        sys.exit(1)

    print("OK")

    try:
        if os.path.samefile(input_file, output_file):
            print("Error: input and output files must be different.")
            print("The original ROM will not be overwritten.")
            sys.exit(1)
    except FileNotFoundError:
        pass

    print("Checking ROM size...", end=" ")

    file_size = os.path.getsize(input_file)

    if file_size != ROM_SIZE:
        print("FAILED")
        print(
            f"Error: ROM must be exactly {ROM_SIZE} bytes "
            f"(32 KiB), but is {file_size} bytes"
        )
        sys.exit(1)

    print(f"OK ({file_size} bytes)")

    print("Reading ROM...", end=" ")

    try:
        with open(input_file, "rb") as f:
            data = f.read()
    except OSError as e:
        print("FAILED")
        print(f"Error reading input file: {e}")
        sys.exit(1)

    print("OK")

    print("Swapping 16 KiB halves...", end=" ")

    swapped = data[HALF_SIZE:] + data[:HALF_SIZE]

    print("OK")

    print("Writing output ROM...", end=" ")

    try:
        with open(output_file, "wb") as f:
            f.write(swapped)
    except OSError as e:
        print("FAILED")
        print(f"Error writing output file: {e}")
        sys.exit(1)

    print("OK")
    print()

    print(SEPARATOR)
    print("             ROM SWAP COMPLETE")
    print(SEPARATOR)
    print(f"Output: {output_file}")
    print("The two 16 KiB halves have been swapped.")
    print(SEPARATOR)


if __name__ == "__main__":
    main()
