#This module stores the functions for unit conversion.
#Functions are named after the following pattern:
#   <target unit>f<source unit>

# convert from mm2 to m2
def m2fmm2(mm2):
    return mm2/10**6
