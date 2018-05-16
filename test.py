import sequences
import nest_generic
from dplython import diamonds

vec = [-1,0,1]

# var = sequences.findLadderSequence(vec, "IP")

var = nest_generic.nest_core(diamonds, 'string')
print (var)
