
# =============================================================
# Stress function library for various cross sections
# 11/07/2020 - David Hill
# =============================================================

# Create classes for cross sections

# ||RECTANGULAR CROSS SECTION

class RectangleStress:
    def __init__(self, width, depth, bendingMoment, shearStress):      # Initialise with constructor init
        self.width = width
        self.depth = depth
        self.bendingMoment = bendingMoment
        self.shearStress = shearStress

    # Calculate maximum stresses & section properties
    def area(self):
        return self.width * self.depth

    def momentOfInertia(self):
        return (1/12)*(self.width*self.depth**3)

    def maxShearStress(self):
        return (3/2)*(self.shearStress/self.area())

    def maxBendingStress(self):
        return (self.bendingMoment*(self.depth/2))/self.momentOfInertia()

