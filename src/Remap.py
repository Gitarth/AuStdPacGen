from scapy.all import arping, rdpcap
from ipaddress import IPv4Network

class Remap:

    def __init__(self):
        self.available_hosts = []
        self.lanIP = ""
        self.network = "127.0.0.1"

    def findNetwork(self):
        self.network = "192.168.0.1"

    def getNetwork(self):
        return self.network

    def findHosts(self):
        net = IPv4Network(self.network)
        self.available_hosts = list(net.hosts())

    def getHosts(self):
        return self.available_hosts

    def findLanIP(self):
         "192.168.0.1"

    def getLanIP(self):
        return self.lanIP

    def remap(self, pkt):
        findHosts()
        findLanIp()
        pkt[IP].src = self.LanIP

    def main():
        print("Testing the Remapping function")
        fileSrc = "testFiles/test00.pcapng"
        pkts = rdpcap(fileSrc)
