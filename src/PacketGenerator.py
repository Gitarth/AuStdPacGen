from Remap import Remap
from scapy.all import send,rdpcap, wrpcap
"""
11/28/17
Authors: Ethan Hendrix, Hitarth Patel

PacketGenerator.py to create packets after receiving an array of packets from the file FileParser
This will call Remap to remap all necessary information before the packets are sent
"""
class PacketGenerator:

    def __init__(self):
        self.remapper = Remap() # I was thinking we could just take a fileParser as an init paramter this way we would already have it
        self.logPkts = []

    def generate(self, arrData):
        """
        Generate packet functiont that will
        """
        for pkt in arrData:

            # newPkt = self.remapper.remap(pkt)
            # send(newPkt)
            send(pkt) # will be phased out after the remapping is done
            # self.logPkts.append(newPkt)

        wrpcap("logs/temp.pcap", arrData) # will change to logPkts after the remapping
    def getRemapper(self):
        return self.remapper # simple get method to return file parser for simplicity's sake when implementing our driver

    def __str__():
        print("PacketGenerator") # str function to prove there's a packet generator

    def main():
        from PacketGenerator import PacketGenerator
        from Remap import Remap
        from FileParser import FileParser

        """
        TODO:

        test function for our PacketGenerator
        arrData = [ source, destination, source_port, destination_port, protocol ]
        """
        pg = PacketGenerator(Remap())
        fp = FileParser("testFiles/test00.pcapng")
        fp.parseFile()
        pkts = fp.getPktData()
        pg.generate(pkts)



    if __name__ == "__main__":
        print("Testing the Packet Generator")
        main()
