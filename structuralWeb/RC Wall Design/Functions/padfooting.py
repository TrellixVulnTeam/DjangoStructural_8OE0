# Inputs
import math
from padfUserInputs import *


# --------------------------------Check Bearing Pressure---------------------------------- #

class bearingPressure:
    def __init__(self, length, width, workingload):
        self.length = length
        self.width = width
        self.workingload = workingload

    def bearingArea(self):
        return self.width/1000 * self.length/1000

    def appliedBP(self):
        return self.workingload / bearingPressure.bearingArea(self)


BP = bearingPressure(ln, wd, wload).appliedBP()  # - Move to main.py later on
BP_round = (round(BP, 2))                        # - Move to main.py later on


def checkBP():
    if allowableBP >= BP:
        return "Applied Bearing Pressure = " + str(BP_round) + " < " + "Allowable Bearing Pressure = " \
               + str(allowableBP) + "kPa, OK!"
    else:
        return "Applied Bearing Pressure = " + str(BP_round) + " > " + "Allowable Bearing Pressure = " \
               + str(allowableBP) + "kPa, NOT OK!"


print(str(BP_round) + "kPa")

print(checkBP())


# --------------------------------Concrete Bearing/Crushing---------------------------------- #

def designBearingStress():
    return (ultload*1000) / (Wcol * Bcol)


def concGradeBearing():
    return concgrade


def stressAreaA1():
    return Wcol * Bcol


def stressAreaA2():
    area1 = min(wd, Bcol + 2*df)
    area2 = min(ln, Wcol + 2*df)
    return area1 * area2


def phiFactorBearing():
    return 0.6


def ultimateBearingStress():
    return min(phiFactorBearing()*0.9*concGradeBearing()*math.sqrt((stressAreaA2()/stressAreaA1())),
               phiFactorBearing()*1.8*concGradeBearing())


print("Design Bearing Stress: " + str(designBearingStress()) + "MPa")
print("Ultimate Bearing Stress: " + str(ultimateBearingStress()) + "MPa")