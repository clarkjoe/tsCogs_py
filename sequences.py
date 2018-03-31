import numpy as npy

# Find longest sequence of zeros
def findSignedSequence(array, sign):
    poten_max = real_max = 0

    if sign in set(npy.sign(array)):
        for number in npy.sign(array):
            if number == sign:
                poten_max += 1
            else:
                if poten_max > real_max:
                    real_max = poten_max
                poten_max = 0
    else:
        return 0
    return real_max

# Find ladder sequences
def findLadderSequence(array, seq):
    max_Inc_Seq = max_Dec_Seq= max_Inc_Pos_Seq = max_Dec_Pos_Seq = max_Inc_Neg_Seq = max_Dec_Neg_Seq = 0
    poten_Max_Inc_Seq = poten_Max_Dec_Seq = poten_Max_Inc_Pos_Seq = poten_Max_Dec_Pos_Seq = poten_Max_Inc_Neg_Seq = poten_Max_Dec_Neg_Seq = 0
