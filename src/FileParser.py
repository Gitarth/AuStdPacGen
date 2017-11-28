from scapy.all import *
import sys

class FileParser:
    """
    def hasNext(): #method to determine if the parser has reached the end of the file or not
        return self.index != self.fileLen #determine if it is the end of the file

    NOT SURE IF WE'LL NEED THIS, BECAUSE WE CAN JUST PARSE LINE BY LINE


    def parseLine(self): #return one line of the file
        line = data[self.index].split(",") ##assume that it's CSV for now, split into an array
        self.index += 1 #increment the index so the hasNext() function can successfully test
        return line #return the line as an array

    NOT SURE WE'LL NEED THIS EITHER

    """

    def __init__(self, fileSrc): #FileParser will have to be initialized with String fileSrc which will be the path to the pcap file. We'll have to change this from path/to/file format to path.to.file format for Python
        self.fileSrc = fileSrc ## An array of file sources that we get from parsing arguments
        self.pktDataList = [] # A list of data from the pcap files we read, we can parse through these later to send packets using them.



    def __str__(self): #toString() method for the parser just to show the fileSrc as String path
        return self.fileSrc # just a simple str method to print the file source

    def parseFile(self):
        ### self.pktDataList = rdpcap(self.fileSrc)

        try:
            self.pktDataList = rdpcap(self.fileSrc) ## just going to read the pcap and append that data to our list if it's valid

        except FileNotFoundError: # catch the error if the file is invalid
            print("Invalid File Name or Path - Please Check")

    def getPktData(self):
        return self.pktDataList # get method for run.py to use to pass to PacketGenerator

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
