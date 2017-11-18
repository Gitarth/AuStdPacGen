import FileParser
import scapy.all

class PacketGenerator:
    
    def __init__(self, fileParser):
        self.fileParser = fileParser

    def generate(self, arrData):

    
    def getParser():
        return self.fileParser

    def __str__():
        print("PacketGenerator")

    def main():
        pg = PacketGenerator(FileParser("test.pcap"))
        parser = pg.getParser()
        while(parser.hasNext()):
            arrData = parser.parseLine()
            pg.generate(arrData)
