from scapy.all import *

# Fill in the MAC address for ARP request
mac_addr = ""

# Fill in the IP address of the machine
ip_addr = ""

# Are we sending at L2 or L3? (bool)
# Explain why!
layer_two = 

# The following line creates an Ethernet frame (Layer 1)
# An ARP message operates on top of an Layer 1 frame.
arp_frame = Ether(dst=mac_addr) / ARP(op=1, pdst=ip_addr)

# Send the frame and wait for answers
if layer_two:
	resp, unans = srp(arp_frame)
else:
	resp, unans = sr(arp_frame)

for s, r in resp:
    print(r[Ether].src)
