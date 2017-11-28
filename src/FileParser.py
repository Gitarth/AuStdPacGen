from scapy.all import *
import sys

def FileParser():

    def __init__(self, fileSrc): #FileParser will have to be initialized with String fileSrc which will be the path to the pcap file. We'll have to change this from path/to/file format to path.to.file format for Python
        self.fileSrcArr = fileSrcArr
        self.pktDataList = []


    def __str__(self): #toString() method for the parser just to show the fileSrc as String path
        print(self.fileSrcArr) # just a simple str method to print the file sources
    """
    def hasNext(): #method to determine if the parser has reached the end of the file or not
        return self.index != self.fileLen #determine if it is the end of the file

    NOT SURE IF WE'LL NEED THIS, BECAUSE WE CAN JUST PARSE LINE BY LINE

    """

    def parseFile(self):
        for file in fileSrcArr:
            try:
                self.pktDataList.append(rdpcap(file))
            except FileNotFoundError:
                print("There is an invalid file that you have given")
    def getPktData(self):
        return self.pktDataList

    """
    def parseLine(self): #return one line of the file
        line = data[self.index].split(",") ##assume that it's CSV for now, split into an array
        self.index += 1 #increment the index so the hasNext() function can successfully test
        return line #return the line as an array

    NOT SURE WE'LL NEED THIS EITHER

    """
    def main(): ## Just a function to test the functionality of the FileParser, I think we can just print the lines here to test if they're actually being read and parsed
        fileSrcArr = ["testFiles/test00.pcapng","testFiles/test01.pcapng"]
        print(rdpcap(fileSrcArr[0]))
        print(rdpcap(fileSrcArr[1]))
        fp = FileParser(fileSrcArr)
        fp.parseFile()
        pktsArray = fp.getPktData
        for file in pktsArray:
            for pkt in file:
                pkt.show()

    if __name__ == "__main__":
        print("Testing FileParser.py")
        main()
