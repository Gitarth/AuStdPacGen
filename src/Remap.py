from scapy.all import arping

class Remap:

    __init__(self,IP_array):
        self.IP_array = IP_array
        self.available_hosts = []

    def getCurrentNetwork(self):
            return "192.168.0.*"
    def findHosts(self):
        return self.available_hosts = arping(getCurrentNetwork())
    
    def main():
        print("Testing the Remapping function")
