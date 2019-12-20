#!/usr/bin/python3
def best_score(a_dictionary):
    d = a_dictionary
    if d:
        max_score = max(d, key=lambda k: d[k])
        return max_score
    return None
