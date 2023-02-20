import scapy.all as scapy
"""from scapy.layers import http



def sniff(interface):
    scapy.sniff(iface= interface, store = False, prn= sniff_packets)


def sniff_packets(packets):
    if packets.haslayer(http.HTTPRequest):

        print(packets.show())
sniff("wlan0")"""


file = open( "/home/xen/PycharmProjects/pythonProject/SCAPY/test.py", "rb")
data = file.read  # file object
print(type (data))
print(data)
print("\n\nfile has been sended\n\n")