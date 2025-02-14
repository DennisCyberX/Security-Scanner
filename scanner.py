```python
import os
import hashlib
import socket

def scan_file(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    print(f"File: {file_path} | Hash: {file_hash}")

def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            scan_file(os.path.join(root, file))

def scan_ports(host, start_port, end_port):
    print(f"Scanning ports {start_port}-{end_port} on {host}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    print("1. Scan Directory")
    print("2. Scan Ports")
    choice = input("Choose an option: ")

    if choice == "1":
        directory = input("Enter directory to scan: ")
        scan_directory(directory)
    elif choice == "2":
        host = input("Enter host to scan: ")
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        scan_ports(host, start_port, end_port)
    else:
        print("Invalid choice")
