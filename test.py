import sequences
import nest_generic
<<<<<<< HEAD
from dplython import diamonds
=======
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()
>>>>>>> 4c02b191edc65fce9d9f468f50d42de5376f4ae5

readRDS = robjects.r['readRDS']
df = readRDS('rawData.rds')
df = pandas2ri.ri2py(df)

print("This is the end")

# var = sequences.findLadderSequence(vec, "IP")

<<<<<<< HEAD
var = nest_generic.nest_core(diamonds, 'string')
print (var)
=======
# nest_generic.nest_core(1, 'string')
# print (var)
>>>>>>> 4c02b191edc65fce9d9f468f50d42de5376f4ae5
