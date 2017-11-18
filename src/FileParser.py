import scapy.all
import sys

def FileParser():

    def __init__(self, fileSrc): #FileParser will have to be initialized with String fileSrc which will be the path to the pcap file. We'll have to change this from path/to/file format to path.to.file format for Python
        self.fileSrc = fileSrc
        self.data = []
        self.fileLen = 0
        self.index = 0

    def __str__(self): #toString() method for the parser just to show the fileSrc as String path
        print(self.fileSrc) # just a simple str method to print the file src 

    def hasNext(): #method to determine if the parser has reached the end of the file or not
        return self.index != self.fileLen #determine if it is the end of the file
    def parseFile(self):
        self.data = self.fileSrc.read().split("'n") #split at new lines, may change based on pcap format
        self.fileLen = len(data) # set the fileLen based on the lenght of the array we've gotten
        
    def parseLine(self): #return one line of the file
        line = data[self.index].split(",") ##assume that it's CSV for now, split into an array
        self.index += 1 #increment the index so the hasNext() function can successfully test
        return line #return the line as an array

    def main(): ## Just a function to test the functionality of the FileParser, I think we can just print the lines here to test if they're actually being read and parsed
        fp = FileParser("test.pcap")
        fp.parseFile()
        while(fp.hasNext()):
            print(fp.parseLine()) # should return as an array of the line separated by the necessary delimeter above 

