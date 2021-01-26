from mcpi.minecraft import Minecraft
MC=Minecraft.create()

import random
while True:
    X,Y,Z=MC.player.getTilePos()
    color=random.randrange(0,9)
    MC.setBlock(X,Y,Z-1,38,color)
    