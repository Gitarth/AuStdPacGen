import subprocess
import ipaddress
from subprocess import Popen, PIPE
from multiprocessing import Pool

"""
11/29/17
Authors: Hitarth Patel, Ethan Hendrix

Python file to find online hosts. This
will scan all of the IPs on a given network
and return the ones that are online. These IPs
will be returned to the Remap class, so it
can properly remap IP addresses
"""
class IPScanner:

    def __init__(self):
        self.available_hosts = []


    def __str__(self):
        return "Your IP Scanner Has Been Created and is now scanning for IPs..."

    def find_online_hosts(self,net_addr):
        network = ipaddress.ip_network(net_addr)

        available_hosts = []
        count = 0

        # for i in network.hosts():
        #
        #     i = str(i)
        #     toping = Popen(['ping','-c','2', '-W', '1', i], stdout = PIPE)
        #     output = toping.communicate()[0]
        #     hostalive = toping.returncode
        #     if hostalive == 0:
        #         print (i, "is appended to the list.")
        #         available_hosts.append(i)
        #     count += 1
        #     print('\r'+ "So far " + str(count) + " ips scanned.", end='')
    @staticmethod
    def check_host(i):
        i = str(i)
        toping = Popen(['ping','-c','2', '-W', '1', i], stdout = PIPE)
        output = toping.communicate()[0]
        hostalive = toping.returncode
        if hostalive == 0:
            print(i, "is appended to the list.")
            return i
        return None
        #print('\r'+ "So far" + i + " ips scanned.", end=" ")

    def find_online_hosts(self,net_addr):
        network = ipaddress.ip_network(net_addr)

        with Pool(10) as p:
            available_hosts = p.map(self.check_host, network.hosts())

            available_hosts = [ i for i in available_hosts if i is not None]

            p.close()
            p.join()

            output_file = open("logs/available_hosts.txt","w")
            output_string = ""
            for host in available_hosts:
                output_string += host + "\n"
                output_file.write(output_string)
                output_file.close()

                return available_hosts

        # output_file = open("logs/available_hosts.txt","w")
        # output_string = ""
        # for host in available_hosts:
        #     output_string += host + "\n"
        # output_file.write(output_string)
        # output_file.close()
        #
        # return available_hosts

    """
    def get_available_hosts(self):
        return self.available_hosts
    """

    def main():
        from IPScanner import IPScanner
        net_addr = "192.168.1.0/24"
        print("The network address ", net_addr)
        ### network = ipaddress.ip_network(net_addr)
        ip_scanner = IPScanner()
        ip_scanner.find_online_hosts(net_addr)
        available_hosts = ip_scanner.get_available_hosts()
        print("The available hosts are: \n", available_hosts)

    if __name__ == "__main__":
        main()
