"""
Python file to find online hosts
"""
def main():
    import subprocess
    import ipaddress
    from subprocess import Popen, PIPE

    network = ipaddress.ip_network()

    for i in network.hosts():
        i = str(i)
        toping = Popen(['ping','-c','3', '-W', '200' i], stdout = PIPE)
        output = toping.communicate()[0]
        hostalive = toping.returncode
        if hostalive == 0:
            print (i, "is reachable")
        else:
            print(i, "is unreachable")




# def scan_and_print_neighbors(net, interface, timeout=1):
#     logger.info("arping %s on %s" % (net, interface))
#     try:
#         ans, unans = scapy.layers.l2.arping(net, iface=interface, timeout=timeout, verbose=True)
#         for s, r in ans.res:
#             line = r.sprintf("%Ether.src%  %ARP.psrc%")
#             try:
#                 hostname = socket.gethostbyaddr(r.psrc)
#                 line += " " + hostname[0]
#             except socket.herror:
#                 # failed to resolve
#                 pass
#             logger.info(line)
#     except socket.error as e:
#         if e.errno == errno.EPERM:     # Operation not permitted
#             logger.error("%s. Did you run as root?", e.strerror)
#         else:
#             raise

if __name__ == "__main__":
    main()
