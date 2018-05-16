import pandas
from dplython import (DplyFrame, X, diamonds, select, sift, sample_n,
    sample_frac, head, arrange, mutate, group_by, summarize, DelayFunction) 

def nest_core(data, timeType):

    type.capitalize()
    letter = type[:1]

    return data >> \
        select(X.carat, X.cut, X.price) >> \
        head(20) >> \
        group_by(X.carat) >> \
        summarize(Count = X.price.sum()) >> \
        group_by(X.carat) >> \
        summarize(join(timeType + '_Count') = X.Count.mean())