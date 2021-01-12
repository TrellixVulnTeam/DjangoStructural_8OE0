# =========================================================================
# R.C Wall calculation functions in accordance with AS3600:2018, Section 11
# 11/07/2020 - David Hill
# =========================================================================

import math
from userinputs import UserInputs
import wallCalcs


# In-plane Shear Capacity classes
class InPlaneShearCapacity:

    @staticmethod
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

    @staticmethod
    def Vuc_lowerbound():
        Vuc_lb = 0.17 * math.sqrt(UserInputs.fc) * 0.8 * UserInputs.Lw * UserInputs.tw
        return Vuc_lb / 1000

    def Vuc_design(self):
        Vuc_des = max(Vuc_lowerbound(self), Vuc(self))  # REVIEW CODE!!!
        phi_Vuc_des = sc_phi * Vuc_des                  # REVIEW CODE!!!
        return Vuc_des, phi_Vuc_des                     # REVIEW CODE!!!

    # Proportion of wall reinforcement
    Pw = 0.0025

    # (kN) Contribution shear strength from wall reinforcement
    def Vus(self):
        Vus_shear = (self.Pw * UserInputs.fy * 0.8 * UserInputs.Lw * UserInputs.tw) / 1000
        phi_Vus = UserInputs.sc_phi * Vus_shear
        return Vus_shear, phi_Vus

    # (kN) Maximum design shear strength
    @staticmethod
    def Vu_max():
        Vu_m = 0.2 * UserInputs.fc * (0.8 * UserInputs.Lw * UserInputs.tw)
        phi_Vu_m = wallCalcs.sc_phi * Vu_m
        return Vu_m, phi_Vu_m

    # (kN) Maximum design shear strength with reduction factor applied
    phiVu = min(Vu_max(), (Vus() + Vuc_design()))  # REVIEW CODE!!!
