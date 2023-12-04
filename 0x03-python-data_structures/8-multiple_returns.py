#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        a = list(sentence)
        return (len(a), a[0])
    else:
        return (0, sentence)
