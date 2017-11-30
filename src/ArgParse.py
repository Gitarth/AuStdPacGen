import argparse

#%% Create parser
def create_parser():
    parser = argparse.ArgumentParser( description = "Gold Standard Traffic Replayer")
    parser.add_argument('-f', '--pcapfile', nargs="+", help="Enter pcap traffic file to replay")
    parser.add_argument('-ip', '--hostip', help="Enter your host ip")
    parser.add_argument('-na','-netaddr', help="Enter network address with netmask")
    args = parser.parse_args()
    return args


#%% Main
def main():
    args = create_parser()
