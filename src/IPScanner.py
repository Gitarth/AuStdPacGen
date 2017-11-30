import subprocess
import ipaddress
from subprocess import Popen, PIPE

"""
Python file to find online hosts
"""

class IPScanner:
    def __init__(self):
        self.available_hosts = []

    def find_online_hosts(self):
        network = ipaddress.ip_network("10.0.0.0/24")

        available_hosts = []
        ###count = 0

        for i in network.hosts():

            i = str(i)
            toping = Popen(['ping','-c','3', '-W', '200', i], stdout = PIPE)
            output = toping.communicate()[0]
            hostalive = toping.returncode
            if hostalive == 0:
                ##print (i, "is appended to the list.")
                available_hosts.append(i)
            ##count += 1
            ###print("So far " + str(count) + " ips scanned.")

        self.available_hosts = available_hosts
    def get_available_hosts(self):
        return self.available_hosts

    def main():
        from IPScanner import IPScanner
        net_addr = "192.168.1.0/24"
        print("The network address ", net_addr)
        network = ipaddress.ip_network(net_addr)
        ip_scanner = IPScanner()
        ip_scanner.find_online_hosts()
        available_hosts = ip_scanner.get_available_hosts()
        print("The available hosts are: \n", available_hosts)

    if __name__ == "__main__":
        main()
