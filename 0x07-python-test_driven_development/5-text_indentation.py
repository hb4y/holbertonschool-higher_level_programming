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
    n = len(text)
    aux = 0
    for word in text.split():
        aux = aux + (len(word) + 1)
        if ("." in word) or (":" in word) or ("?" in word):
            print(word, end="\n\n")
        else:
            print("{}".format(word), end="")
            if aux < n:
                print(" ", end="")
