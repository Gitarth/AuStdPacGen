#! /bin/python3

import os
import subprocess

def convert_pcap_to_json(file):
    tshark_in = file
    tshark_out = open(file.split('.')[0]+".json", "w")
    tshark_call = ["tshark", "-r",tshark_in, "-T", "json"]

    tshark = run(tshark_call, stdout = tshark_out)


def main():
    directory = os.fsencode("/AuStdTrRe/austre_logs")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".pcapng") or filename.endswith(".pcap"):
            json_file = convert_pcap_to_json(file)
            ##write(json_file)
            continue
        else:
            continue
