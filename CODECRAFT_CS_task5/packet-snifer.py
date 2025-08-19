from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

# Callback function to process each captured packet
def analyze_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ""
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        else:
            protocol = str(ip_layer.proto)

        print(f"[+] Packet Captured:")
        print(f"    Source IP: {ip_layer.src}")
        print(f"    Destination IP: {ip_layer.dst}")
        print(f"    Protocol: {protocol}")
        if hasattr(packet, 'payload'):
            print(f"    Payload: {bytes(packet.payload)[:50]}...")  # first 50 bytes
        print("-" * 50)

# Start sniffing packets (requires root/admin)
print("Starting packet sniffer... Press Ctrl+C to stop.")
sniff(prn=analyze_packet, store=False)
