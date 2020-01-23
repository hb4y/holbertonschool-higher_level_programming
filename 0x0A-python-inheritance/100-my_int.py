#!/usr/bin/python3
"""
rebel == and !=
"""


class MyInt(int):
    """(eq ==)  (ne !=)"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
