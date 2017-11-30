from Remap import Remap
from scapy.all import * #send,rdpcap, wrpcap
import subprocess
import json

"""
11/28/17
Authors: Ethan Hendrix, Hitarth Patel

PacketGenerator.py to create packets after receiving an array of packets from the file FileParser
This will call Remap to remap all necessary information before the packets are sent

TODO:
"""
class PacketGenerator:

    def __init__(self,source_ip,available_hosts,fileSrc):
        self.remapper = Remap(source_ip,available_hosts) # I was thinking we could just take a fileParser as an init paramter this way we would already have it
        ## self.local_ips = ["10.0.0.0","172.16.0.0","192.168.0.0"]
        self.logPkts = []
        self.source_ip = source_ip
        self.logDst = "logs/" + fileSrc.split("/")[-1].split(".")[0] +"_log.pcapng"
        self.fileSrc = fileSrc


    def is_local(self, pkt):
        """
        TODO: write a method to determine if the packet is local or not

        method to see if the packet is a local packet
        if it is a local packet we will remap it

        This method will take a packet, split the destination into an array then check to see if they match a local IP pattern
        """
        try:
            dst = pkt[IP].dst.split(".")

            if(dst[0] == "10"):
                return True
            elif(dst[0] == "172" and dst[1] == "16"):
                return True
            elif(dst[0] == "192" and dst[1] == "168"):
                return True
            else:
                return False
        except:
                return False

    def pcap_to_json(self):
        source = self.logDst
        destination = "json>"+source.split(".")[0]+".json"
        execute_arr = ['tshark','-r',source,'-T',destination]
        subprocess.run(execute_arr)

        """
        with open('wrjson.json', 'w') as f:
            json.dump(data, f, sort_keys=True, indent=4)
        """



    def generate(self, arrData):
        """
        Generate packet function that will
        """
        for pkt in arrData:
            if self.is_local(pkt):
                newPkt = self.remapper.remap(pkt)
                self.logPkts.append(newPkt)
                send(newPkt)
            else:
                pkt[IP].src = self.source_ip
                send(pkt)
                self.logPkts.append(pkt)

        wrpcap(self.logDst, self.logPkts) # will change to logPkts after the remapping
        ###self.pcap_to_json()

    def getRemapper(self):
        return self.remapper # simple get method to return file parser for simplicity's sake when implementing our driver

    def __str__():
        print("PacketGenerator") # str function to prove there's a packet generator

    def main():
        from PacketGenerator import PacketGenerator
        from Remap import Remap
        from FileParser import FileParser
        from scapy.all import rdpcap

        """
        TODO:

        test function for our PacketGenerator
        arrData = [ source, destination, source_port, destination_port, protocol ]
        """
        available_hosts = ["192.168.1.111","192.168.1.254"]
        source_ip = "192.168.1.111"
        pg = PacketGenerator(source_ip, available_hosts)
        fp = FileParser("testFiles/test00.pcapng")
        fp.parseFile()
        pkts = fp.getPktData()
        print('Testing is_local\n')
        nonlocal_pkt = pkts[0]
        local_pkt = pkts[1]
        print("Testing non-local packet - Expecting boolean result to be False")
        oracle = False
        result = pg.is_local(nonlocal_pkt)
        if(result == oracle):
            print("Result = %s - Test Passed!\n",result)
        else:
            print("Result = %s - Test Failed!\n",result)
        print("Testing local packet - Expecting boolean result to be True")
        oracle = True
        result = pg.is_local(local_pkt)
        if(result == oracle):
            print("Result = %s - Test Passed!\n")
        else:
            print("Result = %s - Test Failed!\n")

        arrData = rdpcap("testFiles/test00.pcapng")
        pg.generate(arrData)

        ##print("Testing ability to generate packets")
        ##pg.generate(pkts)



    if __name__ == "__main__":
        print("Testing the Packet Generator")
        main()
