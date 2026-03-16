import socket

sniffer = socket.socket(
    socket.AF_PACKET,
    socket.SOCK_RAW,
    socket.ntohs(3)
)

print("Sniffing packets...")

while True:
    raw_data, addr = sniffer.recvfrom(65536)

    dest_mac = raw_data[0:6]
    src_mac = raw_data[6:12]
    proto = raw_data[12:14]

    print("Packet:")
    print("Source:", src_mac.hex(":"))
    print("Destination:", dest_mac.hex(":"))
    print("Protocol:", proto.hex())
    print()
