#!/usr/bin/env python

"""
Script to make a DNS Request in order to resolve a domain-name to an IP address

Requirements:
    - Python3 (we recommend installing Anaconda)
    - npcap (https://nmap.org/npcap/)
    - Scapy (https://scapy.net/)
"""

__author__  =   "Gilles Callebaut"
__email__   =   "gilles.callebaut@kuleuven.be"


from scapy.all import * 

# FILL IN THE FOLLOWING VARIABLES
dst_ip_address = 		# Use IP address of Google Public DNS or local DNS
sends_over_udp =  		# False or True?
dest_port =  			# Port DNS listens to
src_port = 				# Port where the query was sent from (make random allowed port)
site_name =  			# name of website
layer_two = 			# True of False? L2 or L3?
dns_transaction_id = 	# generate random  16-bit transaction id
dns_qtype = 			# DNS query type


# DO NOT TOUCH THIS CODE, but feel free to check out the code :)
network_layer = IP(dst=dst_ip_address)
transport_layer = UDP() if sends_over_udp else TCP()
transport_layer.dport = dest_port
transport_layer.sport = src_port
app_layer = DNS(id=dns_transaction_id, rd=1,qd=DNSQR(qname=site_name,qtype= dns_qtype))

dns_query = network_layer/transport_layer/app_layer
print(dns_query.summary())

#send query and wait for 1 response
if layer_two:
	response = srp1(dns_query)
else:
	response = sr1(dns_query)
print(response.summary())
