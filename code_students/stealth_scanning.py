import socket  # to convert port number to protcol/service name

import numpy as np
from scapy.all import *

SYNACK = 'SA'


ip_range = # add list of IP addresses
port_range = # add list of port ranges


def scan_port(target, port):
    synack_pkt = sr1(IP(dst=target)/TCP(sport=RandShort(),
                                        dport=port, flags="S"), timeout=1, verbose=False)
    if(synack_pkt):
        flag = synack_pkt['TCP'].flags
        if flag == SYNACK:
            return True
    return False
    # sending a RST packet (to halt the handshake) is not needed because the OS will do this for us,
    # because it has no knowledge of sensing a SYN packet to that server
    # TODO check in wireshark if this is the case


def is_alive(target):
    # TODO use ARP to see if the host is alive

for target in ip_range:
    if is_alive(target):
        print("{} is alive".format(target))
        for port in port_range:
            if(scan_port(target, port)):
                print("\t {} {}".format(
                    target, socket.getservbyport(port, 'tcp')))