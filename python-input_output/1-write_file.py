#!/usr/bin/python3
"""Writes text to a UTF-8 encoded file."""


def write_file(filename="", text=""):
    """
    Writes text to a UTF-8 encoded file and returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
