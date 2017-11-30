from scapy.all import * #arping, rdpcap
##from IPScanner import IPScanner
from random import randint
from IPScanner import IPScanner
"""
11/29/17
Authors: Ethan Hendrix, Hitarth Patel

The Remap class will be a remapper to provide the PacketGenerator with local IP addresses
that it can send packets to. The IP addresses will be chosen at random from a list of IPs
that is a class attribute for Remap. These IP addresses will then be used by the PacketGenerator
to substitute in as a destination.
"""
class Remap:

    def __init__(self, source_ip, available_hosts):
        self.source_ip = source_ip

        self.available_hosts = available_hosts


    def remap(self, pkt):
        try:
            i = randint(1,255) % len(self.available_hosts)
            rand_host = self.available_hosts[i]
            pkt[IP].src = self.source_ip
            pkt[IP].dst = rand_host
            return pkt
        except ZeroDivisionError:
            print("Divided by zero")

    def get_available_hosts(self):
        return self.available_hosts

    def main():
        """
        from Remap import Remap
        source_ip = '192.168.1.111'
        net_addr = "192.168.1.0"
        print("Testing the Remap function, source ip is ",source_ip)
        remapper = Remap(source_ip, net_addr)
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
        """
        from Remap import Remap
        from IPScanner import IPScanner
        print("Testing Remap\n")
        source_ip = "192.168.1.111"
        net_addr = "192.168.1.0"
        remapper = Remap(source_ip,net_addr)
        print(remapper.get_available_hosts())
        pkt = rdpcap("testFiles/test00.pcapng")[1]
        remapper.remap(pkt)


    if __name__ == "__main__":
        main()
