from mcpi.minecraft import Minecraft
MC=Minecraft.create()

X,Y,Z=MC.player.getTilePos()
MC.setSign(X,Y,Z+1,63,0,"我愛Minecraft","也愛python")

