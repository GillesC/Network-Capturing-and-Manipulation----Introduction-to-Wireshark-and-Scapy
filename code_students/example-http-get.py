from scapy.all import *

# Build our packet layer by layer
server = 'google.com'

packet = Ether(src='00:00:00:11:11:11')
print(F'Ethernet: {repr(packet)}\n')

ip = packet/IP(dst=server)
print(F'IP: {repr(ip)}\n')

tcp = ip/TCP(dport=80)
print(F'TCP: {repr(tcp)}\n')

http = tcp/"GET /index.html HTTP/1.0\r\n\r\n"
print(F'HTTP-1: {repr(http)}')

# Build the packet in one step
http = Ether()/IP(dst=server)/TCP(dport=80)/"GET /index.html HTTP/1.0\r\n\r\n"
print(F'HTTP-2: {repr(http)}')
