import socket as s
import concurrent.futures
import argparse
import ipaddress

def PortScanner(port, target):
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        try:

            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            
            if banner:
                print(f"[+] the port {port} is open --> {banner}")
            else:
                print(f"[+] the port {port} is open --> (no banner sent)")
        except:
            print(f"[+] Port {port} is OPEN  -->  (Timeout/No banner)")

    sock.close()
parser = argparse.ArgumentParser(description="Fast Python Port Scanner")
parser.add_argument("-t","--target", required=True, help="Target IP address")
parser.add_argument("-p","--ports", type=int , default=65535, help="number of ports to scan")
parser.add_argument("-w","--worker",default=100,type=int,help="number of threads")
args = parser.parse_args()

target = args.target
port = args.ports
worker = args.worker
net = ipaddress.ip_network(target,strict=False)
targets =list(net.hosts()) if net.num_addresses > 1 else [target]



with concurrent.futures.ThreadPoolExecutor(max_workers=worker) as executor:
    for single_ip in targets:
        for n in range(1, port+1):
            executor.submit(PortScanner, n, str(single_ip))

print("\nscan is done!")
