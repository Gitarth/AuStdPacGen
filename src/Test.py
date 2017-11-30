from IPScanner import IPScanner
from Remap import Remap
from PacketGenerator import PacketGenerator
from ArgParse import create_parser
from FileParser import FileParser
from scapy.all import *

class Test:

    def __init__(self,fileSrc,source_ip):
        self.scanner = IPScanner()
        self.parser = FileParser(fileSrc)
        self.remapper = Remap(source_ip)
        self.generator = PacketGenerator(source_ip)

    def testAll(self):
        print("Testing all of the methods\n")

        source_ip = '192.168.1.111'
        fileSrc = "testFiles/test00.pcapng"

        print("Testing the Remap function, source ip is ",source_ip)
        remapper = Remap(source_ip)
        pkts = rdpcap("testFiles/test00.pcapng")
        pkt = remapper.remap(pkts[1])
        dst_oracle = "192.168.1.254"
        src_oracle = "192.168.1.111"

        if(pkt[IP].src == source_ip):
            print("\nThe source oracle is ",src_oracle)
            print("Test Passed!")
        else:
            print("The source oracle is ", src_oracle)
            print("Test Failed!")
        if(pkt[IP].dst == dst_oracle):
            print("the destination oracle is ",dst_oracle)
            print("Test Passed!")
        else:
            print("The destination oracle is ", dst_oracle)
            print("Test failed!")


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

        from IPScanner import IPScanner
        net_addr = "192.168.1.0/24"
        print("The network address ", net_addr)
        network = ipaddress.ip_network(net_addr)
        ip_scanner = IPScanner()
        ip_scanner.find_online_hosts(net_addr)
        available_hosts = ip_scanner.get_available_hosts()
        print("The available hosts are: \n", available_hosts)

    if __name__ == "__main__":
        from Test import Test
        source_ip = '192.168.1.111'
        fileSrc = "testFiles/test00.pcapng"
        tester = Test(fileSrc , source_ip )
        tester.testAll()
