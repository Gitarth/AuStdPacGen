"""
Python file to find online hosts
"""
def IPScanner():
    import subprocess
    import ipaddress
    from subprocess import Popen, PIPE

    network = ipaddress.ip_network("10.0.0.0/24")

    available_hosts = []
    count = 0

    for i in network.hosts():

        i = str(i)
        toping = Popen(['ping','-c','3', '-W', '200', i], stdout = PIPE)
        output = toping.communicate()[0]
        hostalive = toping.returncode
        if hostalive == 0:
            print (i, "is appended to the list.")
            available_hosts.append(i)
        #else:

        #     print(i, "is unreachable")
        count += 1
        print("So far " + str(count) + " ips scanned.")

    return available_hosts

if __name__ == "__main__":
    IPScanner()
