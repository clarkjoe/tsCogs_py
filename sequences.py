import numpy as npy

# Find longest sequence of zeros
def findSignedSequence(vector, sign):
    poten_max = real_max = 0

    if len(vector) > 1:
        for number in npy.sign(vector):
            if number == sign:
                poten_max += 1
            else:
                if poten_max > real_max:
                    real_max = poten_max
                poten_max = 0
    return real_max