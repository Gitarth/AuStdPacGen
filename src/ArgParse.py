import argparse

#%% Create parser
class ArgParse:
    def __init__(self):
        
    def create_parser():
        parser.add_argument('-f', '--pcapfiles', nargs="+", help="Enter pcap traffic file to replay")
        parser = argparse.ArgumentParser( description = "Gold Standard Traffic Replayer")
        parser.add_argument('-ip', '--hostip', help="Enter your host ip")
        parser.add_argument('-na','--netaddr', help="Enter network address with netmask")
        args = parser.parse_args()
        return args

    #%% Gets pcapfiles array's legth
    def getListSize():
        size = len(args.pcapfiles)
        #print(size)
        return size

    #%% Main
    def main():
        args = create_parser()
