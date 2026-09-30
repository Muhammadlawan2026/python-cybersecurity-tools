



import socket

target = "scanme.nmap.org"

def scan_port(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)

    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"port{port}: OPEN")

        s.close()

        for port in range(1, 101):
            scan_port(port)

            print("scanning ya kammala!")



