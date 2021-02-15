# ======================================================================================== #
# User Inputs
# ======================================================================================== #

# ======================================================================================== #
# ============================= Pad Footing Calculator Inputs ============================ #
# ----------------------------------Column Properties------------------------------------- #

Wcol = float(input("Width of Column (mm), Wc = "))
Bcol = float(input("Breadth of Column (mm), Bc = "))
reinfcol = float(input("Nominal Bar Diameter of Column (mm) = "))
fsy_col = float(input("Steel Reinforcement Yield Strength for Column (MPa), fsy = "))

# --------------------------------Pad Footing Properties---------------------------------- #
ln = float(input("Pad Footing Length (mm), Lf = "))
wd = float(input("Pad Footing Width (mm), Wf = "))
df = float(input("Pad Footing Depth (mm), Df = "))

# Concrete Properties of Pad Footing
cover = float(input("Concrete Cover (mm), C = "))
concgrade = float(input("Concrete Grade (MPa) = "))

# Reinforcement Properties of Pad Footing
Reinf_dir1 = float(input("Reinforcement in Direction 1 (mm), R1 = "))
Reinf_dir1_spacing = float(input("Reinforcement in Direction 1 spacing (mm), R1-@ = "))
Reinf_dir2 = float(input("Reinforcement in Direction 2 (mm), R2 = "))
Reinf_dir2_spacing = float(input("Reinforcement in Direction 2 spacing (mm), R2-@ = "))
fsy_pad = float(input("Steel Reinforcement Yield Strength for Pad Footing (MPa) fsy = "))

# ---------------------------------- Design Loads --------------------------------------- #
deadload = float(input("Dead Load (Working Load, kN), DL = "))
liveload = float(input("Live Load (Working Load, kN), LL = "))
ultload = float(input("Ultimate Design Load (kN), N' = "))
wload = deadload + liveload


# ---------------------------------- Geotechnical Properties --------------------------------------- #
allowableBP = float(input("Allowable Bearing Capacity, Ab = "))
ultBP = float(input("Ultimate Bearing Capacity, Ab.ult = "))