# =========================================================================
# R.C Wall calculation functions in accordance with AS3600:2018, Section 11
# 11/07/2020 - David Hill
# =========================================================================

import math
from userinputs import UserInputs

# Phi factors - AS3600:2018 - Table 2.2.2
ac_phi = 0.65  # Axial compression reduction factor
sc_phi = 0.70  # Shear reduction factor


# ------------------------------------AXIAL COMPRESSION CALC PER UNIT LENGTH-------------------------------------------

def axialCapacity():
    effHeight = UserInputs.Hw * UserInputs.k
    ecc = 0.05 * UserInputs.tw  # Wall eccentricity CL:11.5.4
    addEcc = (effHeight ** 2 / (2500 * UserInputs.tw))  # Additional eccentricity CL:11.5.2
    effRatio = effHeight / UserInputs.tw  # Effective wall height/thickness ratio
    # ac_phi.Nu - Design Axial Compression Capacity per unit length
    return ac_phi * (UserInputs.tw - (1.2 * ecc) - (2 * addEcc)) * 0.6 * UserInputs.fc


print(axialCapacity(), "kN/m (per unit length")


# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------DESIGN SHEAR CAPACITY PER UNIT LENGTH--------------------------------------------


def shearCapacity():
    # (kN) Shear strength of wall excluding wall reinforcement CL:11.6.3
    # Define Vuc for if statements (Hw/Lw ratio)
    def Vuc():
        if float(UserInputs.Hw / UserInputs.Lw) <= 1.0:
            Vuc_cnd1 = (((0.66 * math.sqrt(UserInputs.fc)) - (0.21 * (UserInputs.Hw / UserInputs.Lw)
                                                              * math.sqrt(
                        UserInputs.fc))) * 0.8 * UserInputs.Lw * UserInputs.tw)
            return Vuc_cnd1
        else:
            Vuc_cnd2 = ((0.05 * math.sqrt(UserInputs.fc) + ((0.1 * math.sqrt(UserInputs.fc)) /
                                                            ((
                                                                         UserInputs.Hw / UserInputs.Lw) - 1))) * 0.8 *
                                                                         UserInputs.Lw * UserInputs.tw)
            return Vuc_cnd2 / 1000

    def Vuc_lowerbound():
        Vuc_lb = 0.17 * math.sqrt(UserInputs.fc) * 0.8 * UserInputs.Lw * UserInputs.tw
        return Vuc_lb / 1000

    def Vuc_design():
        Vuc_des = max(Vuc_lowerbound(), Vuc())
        phi_Vuc_des = sc_phi * Vuc_des
        return Vuc_des, phi_Vuc_des

    # Proportion of wall reinforcement
    Pw = 0.0025

    # (kN) Contribution shear strength from wall reinforcement
    def Vus():
        Vus_shear = (Pw * UserInputs.fy * 0.8 * UserInputs.Lw * UserInputs.tw) / 1000
        phi_Vus = sc_phi * Vus_shear
        return Vus_shear, phi_Vus

    # (kN) Maximum design shear strength
    def Vu_max():
        Vu_m = 0.2 * UserInputs.fc * (0.8 * UserInputs.Lw * UserInputs.tw)
        phi_Vu_m = sc_phi * Vu_m
        return Vu_m, phi_Vu_m

    # (kN) Maximum design shear strength with reduction factor applied
    phiVu = min(Vu_max(), (Vus() + Vuc_design()))
    return phiVu


print(shearCapacity(), "kN/m (per unit length")

# ---------------------------------------------------------------------------------------------------------------------
# ------------------------------------MINIMUM REINFORCEMENT REQUIREMENTS-----------------------------------------------
