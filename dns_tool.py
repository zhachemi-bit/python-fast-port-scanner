import socket
import argparse
def forward_dns(domain):
	try :
			ip = socket.gethostbyname(domain)
			print(f"[+] IP for{domain} is {ip}")
	except  socket.gaierror:
		         print(f"[-] could not resolve domain : {domain}")


def reverse_dns(ip):
	try :
			socket.gethostbyaddr(ip)
			host , alias , address = socket.gethostbyaddr(ip)
			print(f"[+] Hostname for {ip} is {host}")
	except  socket.herror:
			print(f"[-] Could not find hostname for {ip}")
parser = argparse.ArgumentParser(description = "DNS and reverse DNS Resolver")
parser.add_argument("-d" , "--domain" , help="ENTER DOMAIN NAME (e.g , google.com)")
parser.add_argument("-i" , "--ip" , help = "ENTER IP address (e.g., 8.8.8.8)")

args = parser.parse_args()

if args.domain:
        forward_dns(args.domain)

if args.ip:
        reverse_dns(args.ip)
