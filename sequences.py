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

    for index, number in enumerate(array):
        if index < len(array) - 1:
            # Increasing
            if number < array[index + 1]:
                poten_Max_Dec_Seq = poten_Max_Dec_Pos_Seq = poten_Max_Dec_Neg_Seq = 0
                poten_Max_Inc_Seq += 1

                # Increasing
                if poten_Max_Inc_Seq > max_Inc_Seq:
                    max_Inc_Seq = poten_Max_Inc_Seq

                # Increasing Negative
                if array[index + 1] < 1:
                    poten_Max_Inc_Neg_Seq += 1
                    if poten_Max_Inc_Neg_Seq > max_Inc_Neg_Seq:
                        max_Inc_Neg_Seq = poten_Max_Inc_Neg_Seq
                
                # Increasing Positive
                if array[index + 1] > 0:
                    poten_Max_Inc_Pos_Seq += 1
                    if poten_Max_Inc_Pos_Seq > max_Inc_Pos_Seq:
                        max_Inc_Pos_Seq = poten_Max_Inc_Pos_Seq
            
            # Decreasing
            #else:
            if number > array[index + 1]:

                poten_Max_Inc_Seq = poten_Max_Inc_Pos_Seq = poten_Max_Inc_Neg_Seq = 0
                poten_Max_Dec_Seq += 1

                # Decreasing
                if poten_Max_Dec_Seq > max_Dec_Seq:
                    max_Dec_Seq = poten_Max_Dec_Seq
                
                # Decreasing Negative
                if array[index + 1] < 0:
                    poten_Max_Dec_Neg_Seq += 1
                    if poten_Max_Dec_Neg_Seq > max_Dec_Neg_Seq:
                        max_Dec_Neg_Seq = poten_Max_Dec_Neg_Seq
                
                # Decreasing Positive
                if array[index + 1] > -1:
                    poten_Max_Dec_Pos_Seq += 1
                    if poten_Max_Dec_Pos_Seq > max_Dec_Pos_Seq:
                        max_Dec_Pos_Seq = poten_Max_Dec_Pos_Seq
        
    # Make sequence selection
    if seq == "I":
        return max_Inc_Seq
    elif seq == "IP":
        return max_Inc_Pos_Seq
    elif seq == "IN":
        return max_Inc_Neg_Seq
    elif seq == "D":
        return max_Dec_Seq
    elif seq == "DP":
        return max_Dec_Pos_Seq
    elif seq == "DN":
        return max_Dec_Neg_Seq