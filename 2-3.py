from mcpi.minecraft import Minecraft
MC=Minecraft.create()

import random,time
while True:
    X,Y,Z=MC.player.getTilePos()
    
    color=random.randrange(0,16)
    MC.setBlocks(X+10,Y-1,Z+10,X-10,Y-1,Z-10,95,color)
    time.sleep(0.1)