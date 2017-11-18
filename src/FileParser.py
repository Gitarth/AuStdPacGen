import scapy.all
import sys

def FileParser():

    def __init__(self, fileSrc): #FileParser will have to be initialized with String fileSrc which will be the path to the pcap file. We'll have to change this from path/to/file format to path.to.file format for Python
        self.fileSrc = fileSrc
        self.data = []
        self.fileLen = 0
        self.index = 0

    def __str__(self): #toString() method for the parser just to show the fileSrc as String path
        print(self.fileSrc)

    def hasNext(): #method to determine if the parser has reached the end of the file or not
        return self.index != self.fileLen #determine if it is the end of the file
    def parseFile(self):
        self.data = self.fileSrc.read().split("'n")
        self.fileLen = len(data)
        
    def parseLine(self):
        line = data[self.index].split(",") ##assume that it's CSV for now
        self.index += 1
        return line

    def main():
        fp = FileParser("test.pcap")
        fp.parseFile()
        while(fp.hasNext()):
            print(fp.parseLine())

