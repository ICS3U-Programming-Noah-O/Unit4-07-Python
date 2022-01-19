#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 15, 2022
# This program prints out all of the numbers
# from 1000 to 2000 with 5 numbers on each line

def main():

    # Loop that prints and counts from 1000 to 2000
    for counter in range(1000, 2001):

        # If the counter minus 1 is divisible by 5 then start new line
        if (counter + 1) % 5 != 0:
            print(counter, end=" ")
        else:
            print(counter)


if __name__ == "__main__":
    main()
