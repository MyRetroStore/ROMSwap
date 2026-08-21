# ROMSwap

A simple Python utility for swapping the two 16 KB halves of a 32 KB ROM image.

This is useful for MSX cartridge ROM images where the two 16 KB blocks need to be reversed before the ROM can be used.

The utility takes a 32 KB ROM file, swaps the first and second 16 KB blocks, and writes the result to a new ROM file. The original file is never overwritten.

## Requirements

- Python 3
- A ROM image that is exactly 32 KB (32,768 bytes)
- No external Python packages are required

## Usage

Run the script from a terminal:

```bash
python3 swaprom.py input.rom output.rom
```
The first filename is the original ROM image.

The second filename is the new ROM image with the two 16 KB halves swapped.

The script requires exactly two arguments:
```bash
swaprom.py <input.rom> <output.rom>
```

For example:
```bash
python3 swaprom.py game.rom game-swapped.rom
```
## What It Does

The utility swaps the two 16 KB halves of the ROM:

Input ROM:
[ First 16 KB ][ Second 16 KB ]


Becomes:
[ Second 16 KB ][ First 16 KB ]

## ROM Size

The input ROM must be exactly 32 KB (32,768 bytes).

The script will stop with an error if the input file is not exactly 32 KB.

## Making the Script Executable

On Linux, you can make the script executable:

```bash
chmod +x swaprom.py
```

You can then run it directly:
```bash
./swaprom.py game.rom game-swapped.rom
```
