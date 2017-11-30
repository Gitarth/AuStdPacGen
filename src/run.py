from FileParser import FileParser
from scapy.all import rdpcap
from PacketGenerator import PacketGenerator
from Remap import Remap
from IPScanner import IPScanner
import threading
import argparse
"""
11/28/17
Authors: Ethan Hendrix, Hitarth Patel

run.py is the super-driver for the entire program, and it is the main program with which the user will interact
run.py will instantiate a FileParser
run.py will get the file names from the user then pass them to the FileParser
after getting the array of data from the FileParser, it will instantiate a PacketGenerator
then it will pass the array of data into its generate function
once the generator is finished sending all of the packets, it will inform the user where the logs can be found
"""

def create_parser():
    parser = argparse.ArgumentParser( description = "Gold Standard Traffic Replayer")
    parser.add_argument('-f', '--pcapfiles', nargs="+", help="Enter pcap traffic file to replay")
    parser.add_argument('-ip', '--hostip', help="Enter your host ip")
    parser.add_argument('-na','--netaddr', help="Enter network address with netmask")
    args = parser.parse_args()
    return args

#%% Gets pcapfiles array's legth
def getListSize():
    size = len(args.pcapfiles)
    #print(size)
    return size

def main():
    """
    The Log File Location will never change
    """

    args = create_parser()

    logFileLocation = "~/AuStdPacGen/logs"

    fileSrcArr = args.pcapfiles
    source_ip = args.hostip
    net_addr = args.netaddr

    scanner = IPScanner()
    print(scanner)
    available_hosts = scanner.find_online_hosts(net_addr)
    ##available_hosts = scanner.get_available_hosts()
    print("Available Hosts = ", available_hosts)
    """
    thread:
    FileParser
    PacketGenerator

    pg = PacketGenerator(source_ip,available_hosts)
    """




    print("\nYour packets have finished being generated and sent - please check the log file")
    print("Log file(s) located: ",logFileLocation)

if __name__ == "__main__":
    print("Welcome to the Gold Standard Traffic Replayer!")
    print("Please enter your command in the form generate -f filename1 filename2 filenameX\n")

    main()
