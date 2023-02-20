import scapy.all as scapy
import re
#this is ARP REQUEST

def arp_request(ip):
    arp_req= scapy.ARP(pdst=ip)     #arp_request is object
    print(arp_req.summary())        # this is to tell what this packet is saying
    scapy.ls(scapy.ARP())           # this is to list the attributes of the ARP class
    arp_req.show()                  # this show the packet info what values set there                            #data is send by mac address in network not by ipaddress
    eth=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    eth.show()

                                                  #for combining the layer 3  and layer 2 to form frame use
    arp_request_broadcast = eth/arp_req
    arp_request_broadcast.show()
    ans=scapy.srp(arp_request_broadcast, timeout=1)[0]#this will return only ans #add time out in para
    print(ans.summary())
                                                # this ans-list has a list of element 2nd element is the answer 1st is query
    clien = []
    for i in ans:
        client_dis= {"ip": i[1].psrc, "mac":i[1].hwsrc }
        clien.append(client_dis)                #MAKING  a list of dictionary
                                                    #print(i[1].hwsrc + "---MAC---")    #this return packets access it attributes
                                                #print(i[1].psrc  + "-----IP-----")    #first use show() to see the values inside it




    mac= clien[0]["mac"]
    return mac



