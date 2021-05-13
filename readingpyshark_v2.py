#!/usr/bin/python3
"""
Open a pcap file.
"""

import pyshark

def main():

    # open the pcap file pythoncapture.pcap
    cap = pyshark.FileCapture("pythoncapture.pcap")
    
    # what protocol should we scan the pcap for?
    #scanfor = input("What protocol should we scan the PCAP for (DNS, ICMP, TCP, etc.)? ")
    scanfor = list(map(str,input("Enter up to three protocols, separated by a space, to scan for in the PCAP (DNS, ICMP, TCP, etc.): ").split()))
    #print(scanfor)

    # loop across the entire capture (packet by packet)
    
    for i in scanfor:
        packetmatch = 0 
        for packet in cap:
            #print each packet
            #print(packet)
           # print the PROTOCOL associated with each packet
            if packet.highest_layer == i.upper():
                print(packet)
                packetmatch += 1 # packet matches on protocol

        if packetmatch > 0:
            print(f"A total of {packetmatch} packets match the {i} protocol")
        else:
            print(f"Sorry, we were not able to find any packets matching the {i} protocol")


if __name__ == "__main__":
    main()        

