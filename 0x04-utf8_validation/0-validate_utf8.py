#!/usr/bin/python3
"""
This module contains validUTF8 that determines if a given data set
represents a valid UTF-8 encoding function
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding function

    Props:
        data: represented by a list of integers
    """
    num_bytes = 0

    # Masks for extracting bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine how many bytes the character uses
            if (byte & mask1) == 0:
                # 1-byte character
                continue
            elif (byte & (mask1 >> 1)) == 0:
                return False
            elif (byte & (mask1 >> 2)) == 0:
                num_bytes = 1
            elif (byte & (mask1 >> 3)) == 0:
                num_bytes = 2
            elif (byte & (mask1 >> 4)) == 0:
                num_bytes = 3
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
