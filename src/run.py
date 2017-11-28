from FileParser import FileParser
from PacketGenerator import PacketGenerator

##import Remap

def main():
    fileSrcArr = ["testFiles/test00.pcapng","testFiles/test01.pcapng"]
    fp = FileParser(fileSrcArr)
    pg = PacketGenerator(fp)
    fp.parseFile()
    arrData = fp.getPktData()
    pg.generate(arrData)

if __name__ == "__main__":
    print("Welcome to the Gold Standard Packet Generator!")
    print("Please enter your command in the form generate -f filename1 filename2 filenameX")
    args = input("> ")
    main()
