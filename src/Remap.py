from scapy.all import * #arping, rdpcap
from ipaddress import IPv4Network
##from IPScanner import IPScanner
from random import randint
"""
11/29/17
Authors: Ethan Hendrix, Hitarth Patel

The Remap class will be a remapper to provide the PacketGenerator with local IP addresses
that it can send packets to. The IP addresses will be chosen at random from a list of IPs
that is a class attribute for Remap. These IP addresses will then be used by the PacketGenerator
to substitute in as a destination.
"""
class Remap:

    def __init__(self, source_ip):
        ##self.ip_scanner = IPScanner()
        ##self.online_hosts = self.ip_scanner.find_online_hosts()
        self.online_hosts = ["192.168.1.254"]
        self.number_of_online_hosts = len(self.online_hosts)
        self.source_ip = source_ip

    def remap(self, pkt):
        i = randint(0,255) % len(self.online_hosts)
        rand_host = self.online_hosts[i]
        pkt[IP].src = self.source_ip
        pkt[IP].dst = rand_host
        return pkt


    def main():
        from Remap import Remap
        source_ip = '192.168.1.111'
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



    if __name__ == "__main__":
        main()
