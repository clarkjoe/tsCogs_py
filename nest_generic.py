import pandas
from dplython import (diamonds, X, select, head)
import dplython

def nest_core(data, type):

    type.capitalize()
    letter = type[:1]

    print (1 + \
        1)

    diamonds >> \
     select(X.carat, X.cut, X.price) >>\
     head(5)