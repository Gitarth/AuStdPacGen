![Gold Standard Logo](https://github.com/Gitarth/AuStdPacGen/blob/master/austdpacketgen.png)
# AuStdTre
Gold Standard Traffic Replayer For Computer Networks and Operating System

## Introduction
Austre is a multithreaded network traffic replayer. It's sole purpose is to duplicate traffic based on user input pcap files. Users can input multiple pcap files to test the network on. Logging for each file is also included with a JSON format file  for network transfer and inspection. 

## Use
- Make sure you have the latest version of Python installed.
    - ![Python](https://www.python.org/downloads/)
- Make sure that all dependencies are installed before running the tool
    - ![Scapy](https://github.com/secdev/scapy)
- Make sure to include network address **AND** netmask
- To start the program:
    - sudo python3 run.py -f [pcapFile1, pcapFile2, pcapFile3, .... , pcapFileN] -ip Src -na Network Address with Netmask
    - example: ```terminal
                  sudo python3 austre.py -f file1.pcap file2.pcap file3.pcap -ip 10.0.0.20 -na 10.0.0.0/24
               ```
    - __**Keep in mind that the flags are not positional and are required.**__
- Please give the tool a few minutes to scan your whole network. This is based on your network address and netmask.
    - For example: ```
                      Your IP scanner has been created.
                      So far x ips scanned.
                   ```
    - ***Disclaimer: If you plan to have a really large netmask, then please be prepared to do some sidework, because best bet is it'll take a good bit of your time to scan the network.***

- Logs will be stored in ~/austre/logs/ 
    - Will find pcap log files


