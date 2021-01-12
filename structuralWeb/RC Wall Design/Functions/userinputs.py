# =========================================================================
# R.C Wall calculation functions in accordance with AS3600:2018, Section 11
# 11/07/2020 - David Hill
# =========================================================================


# -----------------------------INPUTS--------------------------------------
# User Inputs for wall set-out properties

class UserInputs:

    wallHeight = input("Hw = ")
    Hw = float(wallHeight)

    wallLength = input("Lw = ")
    Lw = float(wallLength)

    wallThickness = input("tw = ")
    tw = float(wallThickness)

    effHeightFactor = input("k = ")
    k = float(effHeightFactor)

    concGrade = input("f'c = ")
    fc = float(concGrade)

    concDensity = input("yc = ")
    yc = float(concDensity)

    sc_phi = 0.70

    # print(Hw)
    # print(Lw)
    # print(tw)
    # print(k)
    # print(yc)

# User Inputs for wall reinforcement properties

    reoYield = input("fy = ")
    fy = float(reoYield)

    concCover = input("c = ")
    c = float(concCover)

    reoLayers = input("No. of Vertical Reinforcement Layers = ")
    reo_Layers = float(reoLayers)

    verticalReo = input("N = ")
    vertical_Reo = float(verticalReo)

    verticalSpacing = input("N = ")
    vertical_Spacing = float(verticalSpacing)

    horizontalSpacing = input("centre-to-centre spacing(mm) = ")
    horizontal_Spacing = float(horizontalSpacing)

    horizontalReo = input("centre-to-centre spacing(mm) = ")
    horizontal_Reo = float(horizontalReo)

    reinforcementType = input("Ductility Class = ")

    crackControl = input("Degree of Crack Control = ")

    exposureClassification = input("Exposure Classification = ")
