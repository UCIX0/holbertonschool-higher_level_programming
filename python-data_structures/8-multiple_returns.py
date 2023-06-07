#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if (lent == 0):
        tuple2 = (lent, None)
    else:
        tuple2 = (lent, sentence[0])
    return (tuple2)
