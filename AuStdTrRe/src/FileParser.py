from scapy.all import rdpcap
import sys
"""
11/28/17
Authors: Ethan Hendrix, Hitarth Patel

FileParser will receive a file source from run.py
It will read the PCAP file and return an array of packets for the Packet Generator to use
"""
class FileParser:

    def __init__(self, fileSrc): #FileParser will have to be initialized with String fileSrc which will be the path to the pcap file. We'll have to change this from path/to/file format to path.to.file format for Python
        self.fileSrc = fileSrc ## An array of file sources that we get from parsing arguments
        self.pktData = [] # A list of data from the pcap files we read, we can parse through these later to send packets using them.



    def __str__(self): #toString() method for the parser just to show the fileSrc as String path
        return self.fileSrc # just a simple str method to print the file source

    def parseFile(self):
        ### self.pktDataList = rdpcap(self.fileSrc)

        try:
            self.pktData = rdpcap(self.fileSrc) ## just going to read the pcap and append that data to our list if it's valid

        except FileNotFoundError: # catch the error if the file is invalid
            print("Invalid File Name or Path - Please Check")

    def getPktData(self):
        return self.pktData # get method for run.py to use to pass to PacketGenerator

    def main(): ## Just a function to test the functionality of the FileParser, I think we can just print the lines here to test if they're actually being read and parsed
        from FileParser import FileParser
        fileSrc = "testFiles/test00.pcapng"
        print("File source: " , fileSrc)
        fp = FileParser(fileSrc)
        print( "FileParser's file source: " , fp)
        fp.parseFile()
        pktsArray = fp.getPktData()
        for pkt in pktsArray:
            pkt.show()

        invalidFileSrc = "invalid.pcapng"
        invalidFp = FileParser(invalidFileSrc)
        print("")
        invalidFp.parseFile()

    if __name__ == '__main__':
        print("Testing FileParser")
        main()
