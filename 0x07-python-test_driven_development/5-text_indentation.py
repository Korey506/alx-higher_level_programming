#!/usr/bin/python3
"""Module containing text_indentation method."""


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' chars.

    Args:
        text: The str text.

    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

   c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
