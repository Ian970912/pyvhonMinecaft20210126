from mcpi.minecraft import Minecraft
MC=Minecraft.create()

Name=input("請輸入姓名:")
GG=input("請輸入發言:")
MC.postToChat("<"+Name+">"+GG)