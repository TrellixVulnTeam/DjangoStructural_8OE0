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


print("Applied Bearing Pressure = " + str(BP_round) + "kPa")

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


def ultBearingStressCheck():
    designBearingRound = round(designBearingStress(), 2)
    ultBearingRound = round(ultimateBearingStress(), 2)

    if ultimateBearingStress() >= designBearingStress():
        return "Design Bearing Stress: " + str(designBearingRound) + "MPa < " "Ultimate Bearing Stress: " \
               + str(ultBearingRound) + "MPa, OK!"
    else:
        return "Design Bearing Stress: " + str(designBearingRound) + "MPa > " "Ultimate Bearing Stress: " \
               + str(ultBearingRound) + "MPa, NOT OK!"


print(ultBearingStressCheck())  # - Move to main.py later on


# --------------------------------Check Footing Minimum Depth ---------------------------------- #

def lsy_cb():
    lsycb = max((0.22*fsy_pad)/(concgrade**0.5), 200, 0.0435*fsy_pad*reinfcol)
    return lsycb


def Dmin():
    d_min = lsy_cb() + Reinf_dir1 + Reinf_dir2 + cover
    return d_min


def footingDepthCheck():
    print("Minimum footing Depth: " + str(Dmin()) + "mm")


footingDepthCheck()


# --------------------------------Punching Shear Check---------------------------------- #

class punchingShearCheck:
    pass
