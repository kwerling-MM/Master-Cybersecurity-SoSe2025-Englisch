import socket

def tcp_ping_scan(network_prefix, start_ip, end_ip, port=80):
    print(f"Scanning network {network_prefix}.0 on port {port}...")
    active_hosts = []
    for host in range(start_ip, end_ip + 1):
        ip = f"{network_prefix}.{host}"
        print(f"Connecting to {ip}:{port}...", end="")
        try:
            sock = socket.create_connection((ip, port), timeout=1)
            print("Active")
            active_hosts.append(ip)
            sock.close()
        except (socket.timeout, socket.error):
            print("Inactive")
    return active_hosts

if __name__ == "__main__":
    # Netzwerk und IP-Bereich angeben
    network_prefix = "192.168.100"  # Beispielnetzwerk
    active = tcp_ping_scan(network_prefix, 5, 15, port=80)  # Scan von .5 bis .15 auf Port 80
    print("\nActive hosts:")
    print("\n".join(active))