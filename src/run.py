from FileParser import FileParser
from scapy.all import rdpcap
from PacketGenerator import PacketGenerator
from Remap import Remap
##import Remap

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

def main():
    logFileLocation = "~/AuStdPacGen/logs"
    fileSrc = "testFiles/test00.pcapng"
    fp = FileParser(fileSrc)
    pg = PacketGenerator()
    fp.parseFile()
    data = fp.getPktData()
    for pkt in data:
        pg.generate(pkt)
    print("\nYour packets have finished being generated and sent - please check the log file")
    print("Log file(s) located: ",logFileLocation)
if __name__ == "__main__":
    print("Welcome to the Gold Standard Packet Generator!")
    print("Please enter your command in the form generate -f filename1 filename2 filenameX\n")

    main()
