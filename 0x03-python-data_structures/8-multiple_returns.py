#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0] == None:
        return None
    else:
        a = list(sentence)
        return (len(a), a[0])
