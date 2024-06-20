from scapy.all import sniff, Raw
from scapy.layers.inet import IP, TCP, UDP
import sys
import logging


def setup_logger(output_file):
    logger = logging.getLogger("PacketSniffer")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(output_file)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def packet_handler(packet, logger):
    try:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            protocol = 'TCP'
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            protocol = 'UDP'
        else:
            src_port = dst_port = None
            protocol = 'OTHER'

        payload = packet[Raw].load if Raw in packet else None

        log_message = f"Protocol: {protocol} | Src IP: {src_ip}:{src_port} | Dst IP: {dst_ip}:{dst_port} | Payload: {payload}"
        print(log_message)

        logger.info(log_message)
    except Exception as e:
        print(f"Error handling packet: {e}")


def main():
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <interface> <port> <output_file> [<host>] [<protocol>]")
        sys.exit(1)

    interface = sys.argv[1]
    port = sys.argv[2]
    output_file = sys.argv[3]
    host = sys.argv[4] if len(sys.argv) > 4 else None
    protocol = sys.argv[5].lower() if len(sys.argv) > 5 else None

    logger = setup_logger(output_file)

    filter_exp = f"port {port}"
    if host:
        filter_exp += f" and host {host}"
    if protocol:
        if protocol in ["tcp", "udp"]:
            filter_exp += f" and {protocol}"
        else:
            print(f"Unsupported protocol: {protocol}")
            sys.exit(1)

    print(f"Starting sniffing on interface {interface} for port {port}")
    if host:
        print(f"Filtering for host {host}")
    if protocol:
        print(f"Filtering for protocol {protocol.upper()}")

    try:
        sniff(iface=interface, filter=filter_exp, prn=lambda x: packet_handler(x, logger))
    except Exception as e:
        print(f"Error starting sniffer: {e}")


if __name__ == "__main__":
    main()
