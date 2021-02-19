#This module stores the functions for unit conversion.
#Functions are named after the following pattern:
#   <target unit>f<source unit>

# convert from mm to m
def mfmm(mm):
    return mm/1000.0
# convert from mm^2 to m^2
def m2fmm2(mm2):
    return mm2/10**6
# convert from m^3/h to m^3/s
def m3_sfm3_h(m3_h):
    return m3_h/3600.0
