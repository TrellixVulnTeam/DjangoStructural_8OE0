from Functions.stressFunctions import RectangleStress

rectStress = RectangleStress(2, 4, 25, 80)

print(rectStress.area())

print(rectStress.maxBendingStress())

print(rectStress.maxShearStress())

print(rectStress.momentOfInertia())


