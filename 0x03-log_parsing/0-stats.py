#!/usr/bin/python3
"""
This script reads input from stdin line by line,
computes metrics on HTTP status codes and file sizes,
and prints a summary of these metrics every 10 lines
and at the end of input.
"""
import sys

# Initialize counters for total file size and number of lines processed
counters = {"size": 0, "lines": 1}

# Dictionary to store counts of different HTTP status codes
cntCode = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def printCodes():
    """
    Print the current total file size and counts of each HTTP status code.
    Only status codes with non-zero counts are printed.
    """
    print("File size: {}".format(counters["size"]))
    for key in sorted(cntCode.keys()):
        if cntCode[key] != 0:
            print("{}: {}".format(key, cntCode[key]))


def countCodeSize(listData):
    """
    Update the total file size and increment the count
    for the encountered HTTP status code.

    params
    :listData: A list containing the split elements of an input line,
                where the last element is the file size and
                the second-to-last is the status code.
    """
    # Update total file size
    counters["size"] += int(listData[-1])

    # Increment count for the status code if it's one we're tracking
    if listData[-2] in cntCode:
        cntCode[listData[-2]] += 1


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                # Process each line of input
                countCodeSize(line.split(" "))
            except:
                # Silently ignore any lines that cause errors when processing
                pass

            # Print metrics every 10 lines
            if counters["lines"] % 10 == 0:
                printCodes()
            counters["lines"] += 1
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        # by printing current metrics before exiting
        printCodes()
        raise

    # Print final metrics after processing all input
    printCodes()
