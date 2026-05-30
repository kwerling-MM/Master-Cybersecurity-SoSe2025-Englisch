from scapy.all import sr1, IP, ICMP

def icmp_ping_scan(network_prefix, start_ip, end_ip):
    print(f"Scanning network {network_prefix}.0...")
    active_hosts = []
    for host in range(start_ip, end_ip + 1):
        ip = f"{network_prefix}.{host}"
        print(f"Pinging {ip}...", end="")
        pkt = IP(dst=ip)/ICMP()
        response = sr1(pkt, timeout=1, verbose=0)
        if response:
            print("Active")
            active_hosts.append(ip)
        else:
            print("Inactive")
    return active_hosts

if __name__ == "__main__":
    # Netzwerk und IP-Bereich angeben
    network_prefix = "192.168.100"  # Beispielnetzwerk
    active = icmp_ping_scan(network_prefix, 5, 15)  # Scan von .5 bis .15
    print("\nActive hosts:")
    print("\n".join(active))