import FileParser
from scapy.all import * 

class PacketGenerator:

    def __init__(self, fileParser):
        self.fileParser = fileParser # I was thinking we could just take a fileParser as an init paramter this way we would already have it

    def generate(self, arrData):
        # generate a packet based on the arrData that we will receive from the file parser as an array of the line
        #implementation to come
        return 0 # return 0 for now while we're working on the implementation

    def getParser():
        return self.fileParser # simple get method to return file parser for simplicity's sake when implementing our driver

    def __str__():
        print("PacketGenerator") # str function to prove there's a packet generator

    def main(): # test function for our PacketGenerator
        ## arrData = [ source, destination, source_port, destination_port, protocol ]
        pkts = rdpcap("testFiles/test00.pcapng")
        for pkt in pkts:
            pkt.show()
            send(pkt)
    if __name__ == "__main__":
        print("Testing the Packet Generator")
        main()
