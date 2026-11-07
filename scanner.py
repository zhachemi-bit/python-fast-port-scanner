import socket as s
import concurrent.futures

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

target = input("please enter the IP address that you want to scan: ")
port = int(input("please enter the number of ports that you want to scan: "))

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for n in range(1, port+1):
        executor.submit(PortScanner, n, target)

print("\nscan is done!")
