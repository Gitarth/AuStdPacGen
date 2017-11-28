import argparse

#%% Create parser
def create_parser():
    parser = argparse.ArgumentParser( description = "Gold Standard Traffic Replayer")
    parser.add_argument('-f', '--pcapfile', help="Enter pcap traffic file to replay")
    parser.add_argument('-d', '--defaultpcap', help="Default pcap file used to generate traffic")
    args = parser.parse_args()
    return args

#%% Main
def main():
    args = create_parser()
