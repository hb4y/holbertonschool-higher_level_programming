#!/usr/bin/python3
"""
text_indentation - print when find . ? :
text: string
Return: void
"""


def text_indentation(text):
    """
    text indentation
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    aux = 0
    line = ""
    length = len(text)
    for letter in text:
        if ("." is letter) or (":" is letter) or ("?" is letter):
            line = line + letter
            aux = aux + 1
            print(line.strip(), end="\n\n")
            line = ""
        else:
            line = line + letter
            aux = aux + 1
            if aux >= length:
                print(line.strip(), end="")
