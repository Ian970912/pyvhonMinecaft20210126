from mcpi.minecraft import Minecraft
MC=Minecraft.create()
X,Y,Z=MC.player.getTilePos()

long=10
big=8
high=7

block=7
air=0


MC.setBlocks(X,Y,Z,X+long,Y+high,Z+big,block)
MC.setBlocks(X+1,Y+1,Z+1,X+long-1,Y+high-1,Z+big-1,air)