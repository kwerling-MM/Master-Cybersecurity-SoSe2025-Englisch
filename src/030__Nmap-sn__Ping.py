import nmap

def nmap_sn_scan(network_range):
    # Nmap-Scanner initialisieren
    nm = nmap.PortScanner()
    
    print(f"Scanning network range: {network_range}")
    
    # Ping-Scan (-sn) ausführen
    nm.scan(hosts=network_range, arguments='-sn')
    
    # Ergebnisse auswerten
    active_hosts = []
    for host in nm.all_hosts():
        if nm[host].state() == 'up':  # Prüfen, ob der Host aktiv ist
            active_hosts.append(host)
            print(f"Host {host} is active.")
    
    return active_hosts

if __name__ == "__main__":
    # Beispiel: Scan für ein Subnetz
    network_range = "192.168.100.0/28"
    active = nmap_sn_scan(network_range)
    
    print("\nActive hosts found:")
    print("\n".join(active))