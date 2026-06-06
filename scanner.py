#!/usr/bin/env python3
import socket
import sys

target = "127.0.0.1"

print("-" * 50)
print(f"Scanning Target: {target}")
print("-" * 50)

ports = [21, 22, 80, 443]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN!")
    else:
        print(f"[-] Port {port} is closed.")
    s.close()
