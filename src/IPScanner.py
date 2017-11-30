"""
Python file to find online hosts
"""
def main():
    import ipaddress
    import subprocess
    import logger
    """

    net_addr = "192.168.1.0/24"

    ip_net = ipaddress.ip_network(net_addr)

    all_hosts = list(ip_net.hosts())

    for i in range(len(all_hosts)):
        out = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE).communicate()[0]

        if "Destination host unreachable" in output.decode('utf-8'):
            print(str(all_hosts[i]), "is Offline")
        elif "Request timed out" in output.decode('utf-8'):
            print(str(all_hosts[i]), "is Offline")
        else:
            print(str(all_hosts[i]), "is Online")

    """


def scan_and_print_neighbors(net, interface, timeout=1):
    logger.info("arping %s on %s" % (net, interface))
    try:
        ans, unans = scapy.layers.l2.arping(net, iface=interface, timeout=timeout, verbose=True)
        for s, r in ans.res:
            line = r.sprintf("%Ether.src%  %ARP.psrc%")
            try:
                hostname = socket.gethostbyaddr(r.psrc)
                line += " " + hostname[0]
            except socket.herror:
                # failed to resolve
                pass
            logger.info(line)
    except socket.error as e:
        if e.errno == errno.EPERM:     # Operation not permitted
            logger.error("%s. Did you run as root?", e.strerror)
        else:
            raise

if __name__ == "__main__":
    scan_and_print_neighbors("192.168.1.0\24","enp1s0")
