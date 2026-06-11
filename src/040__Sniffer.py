from scapy.all import sniff

def packet_callback(packet):
    # Initialisieren der Variablen
    ip_src = ip_dst = protocol = payload_size = "N/A"

    # Prüfen, ob das Paket einen IP-Layer enthält
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src  # Sender-IP
        ip_dst = packet['IP'].dst  # Empfänger-IP
        protocol = packet['IP'].proto  # Protokollnummer auf IP-Ebene

    # Prüfen auf zusätzliche Protokoll-Schichten (TCP, UDP)
    if packet.haslayer('TCP'):
        protocol = 'TCP'
        payload_size = len(packet['TCP'].payload)
    elif packet.haslayer('UDP'):
        protocol = 'UDP'
        payload_size = len(packet['UDP'].payload)
    elif packet.haslayer('ICMP'):
        protocol = 'ICMP'
        payload_size = len(packet['ICMP'].payload)

    # Ausgeben der gesammelten Informationen
    print(f"Sender: {ip_src}, Receiver: {ip_dst}, Protocol: {protocol}, Payload Size: {payload_size} bytes")

# Netzwerkverkehr belauschen
if __name__ == "__main__":
    print("Sniffing network traffic... Press Ctrl+C to stop.")
    # Mit sniff() den Verkehr erfassen und die Callback-Funktion aufrufen
    sniff(iface="eth0", prn=packet_callback, filter="ip", store=0)  # "ip" filtert nur IP-Pakete