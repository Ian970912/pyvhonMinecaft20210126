from mcpi.minecraft import Minecraft
MC=Minecraft.create()

X,Y,Z=MC.player.getTilePos()

answer=int(input('請問你右邊要放甚麼方塊:'))
MC.setBlocks(X+1,Y,Z,answer)
