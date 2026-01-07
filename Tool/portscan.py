import socket
import termcolor

def scan(target, ports):
	print('\n' + ' Starting scan for  ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port opened" + str(port))
		sock.close()
	except:
		pass

targets = input("[*] Enter target to scan(split them by ,): ") 
ports = int(input("[*] Enter how many ports you want to scan: "))
if ',' in targets:
	print("[*] Scanning multiple targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)

