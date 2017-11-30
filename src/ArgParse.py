import argparse

#%% Create parser
def create_parser():
    parser = argparse.ArgumentParser( description = "Gold Standard Traffic Replayer")
    parser.add_argument('-f', '--pcapfile', help="Enter pcap traffic file to replay")
    parser.add_argument('-ip', '--hostip', help="Enter your host ip")
    parser.add_argument('-s', '--subnetmask', help="Enter your subnet mask")
    args = parser.parse_args()
    return args

#%% Main
def main():
    args = create_parser()
