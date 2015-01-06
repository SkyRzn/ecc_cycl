#!/usr/bin/python


from ecc_cycl import EccCycl


gears = EccCycl()

h = 14

gears.setRnN(30, 6)
gears.eccentricity = 0.3
gears.dt = 0.1
gears.smallGearAxisRadius = 1
gears.smallGearFn = 100
gears.slices = 28
gears.cycleHeight = 12

big = gears.bigGear(h, shell=0.01)

small = (gears.smallGear(h) / [0, 0, 180]) << [35, 0, 0]

res =  big + small

res.save('result.scad')

