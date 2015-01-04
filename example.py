#!/usr/bin/python


from ecc_cycl import EccCycl


gears = EccCycl()

gears.setRnN(60, 20)
gears.eccentricity = 0.5
gears.dt = 0.1
gears.smallGearAxisRadius = 1
gears.bigGearAxisRadius = 1
gears.smallGearFn = 200
gears.slices = 20
gears.bigGearConvexity = 1000
gears.cycleHeight = 20

res = gears.bigGear(20)
res += (gears.smallGear(20) / [0, 0, 180]) << [63, 0,0]
res.save('result.scad')


