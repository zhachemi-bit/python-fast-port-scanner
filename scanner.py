import socket as s
import concurrent.futures

def PortScanner(port ,target):
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target,port))
    if result == 0:
        print(f"the port{port} is open")
    sock.close()

target = input("enter the ip address that you want to scan")
port = int(input("how many port you want to scan"))

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:

    for n in range(1, port+1):
        executor.submit(PortScanner,n ,target, )
print("\nscan finished")


