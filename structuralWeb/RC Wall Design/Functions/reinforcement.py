# =========================================================================
# R.C Wall calculation functions in accordance with AS3600:2018, Section 11
# 11/07/2020 - David Hill
# =========================================================================

from userinputs import UserInputs


class Reinforcement:

    # Minimum horizontal reinforcement requirements for Crack Control
    def __init__(self):
        self.Pdesign = 0.025
        self.Pmax = 0.04
        self.P = 0.002
        self.p_hori_strong = 0.06
        self.p_hori_moderate = 0.0035
        self.p_hori_minor = 0.0025

    def hori_ReoControl(self):
        if UserInputs.crackControl == "Minor":
            return self.p_hori_strong

        elif UserInputs.crackControl == "Moderate":
            return self.p_hori_moderate

        else:
            return self.p_hori_minor

    # Minimum horizontal reinforcement requirements for Crack Control
    def vert_ReoControl(self):
        return self.Pdesign, self.Pmax, self.P
