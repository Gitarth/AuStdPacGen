#! /bin/python3

import os
import subprocess

def convert_pcap_to_json(file):
    tshark_call = ["tshark", "-r", "-T", "json"]
    tshark_in = open(file, "rb")
    tshark_out = open(file+".json", "w")

    tshark = run(tshark_call, stdin=tshark_in, stdout = tshark_out)


def main():
    directory = os.fsencode("/AuStdTrRe/austre_logs")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".pcapng") or filename.endswith(".pcap"):
            json_file = convert_pcap_to_json(file)
            write(json_file)
            continue
        else:
            continue
