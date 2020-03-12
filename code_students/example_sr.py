from scapy.all import *

ans, unans = sr(IP(dst="192.168.0.155")/ICMP(), timeout=5)
ans.show()
unans.show()

for s,r in ans:
    # iterate over send and received messages
