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
# global variable pcapLog
pcapLog = []

def create_parser():
    parser = argparse.ArgumentParser( description = "Gold Standard Traffic Replayer")
    parser.add_argument('-f', '--pcapfiles', nargs="+", help="Enter pcap traffic file to replay")
    parser.add_argument('-ip', '--hostip', help="Enter your host ip")
    parser.add_argument('-na','--netaddr', help="Enter network address with netmask")
    args = parser.parse_args()
    return args

#%% Gets pcapfiles array's legth
def getListSize(args):
    size = len(args.pcapfiles)
    #print(size)
    return size

#%% Create thread task
def thread_task(fileSrc,source_ip,available_hosts):
    """
    Task for thread
    Create a FileParser with a fileSrc
    Create a Packet generator
    Parse the file - return an array of packets
    packet generator generates packets from that array
    """
    ## Make fileparser and PacketGenerator
    fp = FileParser(fileSrc)
    pg = PacketGenerator(source_ip,available_hosts,fileSrc)
    fp.parseFile()
    pkts = fp.getPktData()
    count = 0
    for pkt in pkts:
        count += 1
        pg.generate(pkt)
    print("\t\t Sent ", count," packets.")


def main():
    """
    The Log File Location will never change
    """

    args = create_parser()

    logFileLocation = "~/AuStdPacGen/logs"

    fileSrcArr = args.pcapfiles
    source_ip = args.hostip
    net_addr = args.netaddr
    try:
        scanner = IPScanner()
        print(scanner)
        available_hosts = scanner.find_online_hosts(net_addr)
        ###available_hosts = ["10.10.1.1","10.10.1.2","10.10.1.3"]
        print("====================================================")
        print("\nAvailable Hosts = ", available_hosts,"\n")
        print("====================================================")

        """
        thread:
        FileParser
        PacketGenerator

        pg = PacketGenerator(source_ip,available_hosts)
        """
        threads = []
        ## creating threads
        print("====================================================")
        print("\nCreating your threads now")
        thread_count = 1
        for i in range(getListSize(args)):
            print("\t Thread " + str(thread_count) + " created.")
            print("\t\t This file was " + fileSrcArr[i] + " used.")
            thread_count += 1
            t = threading.Thread(target=thread_task(fileSrcArr[i],source_ip,available_hosts))
            t.start()
            threads.append(t)
        print("\n===================================================")

        ##print(threads)
        """
        for file_path in args.pcapfiles:
            q.put(file_path)

        # wait for threads to be finished
        q.join()

        # to stop thread_task
        for i in range(getListSize):
            q.put(None)
        # to join threads after completion
        """
        for t in threads:
            t.join()

        print("====================================================")
        print("\nYour packets have finished being generated and sent - please check the log file")
        print("Log file(s) located: ",logFileLocation)
        print("====================================================")
    except AttributeError:
        print("\nYou forgor your netmask - please enter in format -na X.X.X.X/xx")

if __name__ == "__main__":
    print("===================================================")
    print("Welcome to the Gold Standard Traffic Replayer!")
    print("===================================================")
    ## print("Please enter your command in the form generate -f filename1 filename2 filenameX\n")

    main()
