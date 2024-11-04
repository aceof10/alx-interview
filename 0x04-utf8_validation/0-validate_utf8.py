#!/usr/bin/python3
"""
This module provides a function to validate whether a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes.
    :return: True if data is valid UTF-8, otherwise False.
    """
    num_bytes = 0

    for byte in data:
        # Keep only the last 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count leading 1s to determine byte length
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False  # Invalid if starting with 10xxxxxx
        else:
            # Check if it's a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
