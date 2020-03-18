import ipaddress
import sys

if len(sys.argv) != 2:
    print('Usage: python3 ', sys.argv[0], ' <ipaddress/prefix>')
    exit()

Address = sys.argv[1]

def Create_segment(cider):
    Segment = ipaddress.IPv4Network(cider, strict=False)
    Hosts = Segment.hosts()
    Mask = Segment.netmask

    if Segment.prefixlen == 32:
        print(Segment.network_address, Mask)
    elif Segment.prefixlen == 31:
        print(Segment.network_address, Mask, 'Network Address')
        print(Segment.broadcast_address, Mask, 'Broadcast Address')
    else:
        print(Segment.network_address, Mask, 'Network Address')
        for IP in Hosts:
            print(IP, Mask, 'Usable host')
        print(Segment.broadcast_address, Mask, 'Broadcast Address')

if __name__ == '__main__':
    Create_segment(Address)

