from Remap import Remap
from scapy.all import send,rdpcap

class PacketGenerator:

    def __init__(self, remapper):
        self.remapper = remapper # I was thinking we could just take a fileParser as an init paramter this way we would already have it

    def generate(self, arrData):
        """
        TODO: Remap the IPs

        generate a packet based on the arrData that we will receive from the file parser as an array of the line
        arrData should be an array of arrys that we receive from reading the pcap files

        for data in arrData: # get the first array of packets
            for pkt in data: # now get the individual packet
                send(pkt) # send that packet
        """
        for pkt in arrData:
            
            # newPkt = self.remapper.remap(pkt)
            # send(newPkt)
            send(pkt)

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
