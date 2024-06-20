from scapy.all import sniff
from scapy.all import Raw
import sys

def packet_handler(packet):
    try:
        if Raw in packet:
            payload = packet[Raw].load
            print(f"Packet captured: {payload}")

            with open(output_file, "ab") as f:
                f.write(payload)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <interface> <port> <output_file>")
        sys.exit(1)

    interface = sys.argv[1]
    port = sys.argv[2]
    output_file = sys.argv[3]

    filter_exp = f"tcp port {port}"

    print(f"Starting sniffing on interface {interface} for port {port}")

    sniff(iface=interface, filter=filter_exp, prn=packet_handler)
