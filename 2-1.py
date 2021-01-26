from mcpi.minecraft import Minecraft
MC=Minecraft.create()

X,Y,Z=MC.player.getTilePos()
MC.setBlock(X,Y,Z+1,7)
MC.setBlock(X,Y,Z-1,7)
MC.setBlock(X-1,Y,Z,7)
MC.setBlock(X+1,Y,Z,7)
MC.setBlock(X+1,Y,Z+1,7)
MC.setBlock(X-1,Y,Z+1,7)
MC.setBlock(X-1,Y,Z-1,7)
MC.setBlock(X+1,Y,Z-1,7)