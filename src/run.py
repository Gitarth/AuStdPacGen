from FileParser import FileParser
from scapy.all import rdpcap
from PacketGenerator import PacketGenerator
from Remap import Remap
##import Remap

def main():
    logFileLocation = "~/AuStdPacGen/logs"
    fileSrc = "testFiles/test00.pcapng"
    fp = FileParser(fileSrc)
    pg = PacketGenerator(Remap())
    fp.parseFile()
    data = fp.getPktData()
    for pkt in data:
        pg.generate(pkt)
    print("\nYour packets have finished being generated and sent - please check the log file")
    print("Log file(s) located: ",logFileLocation)
if __name__ == "__main__":
    print("Welcome to the Gold Standard Packet Generator!")
    print("Please enter your command in the form generate -f filename1 filename2 filenameX\n")

    main()
