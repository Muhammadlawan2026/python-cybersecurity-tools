import socket
import concurrent.futures

TARGET = "scanme.nmap.org"
PORTS = range(1, 101)

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)

        result = s.connect_ex((TARGET, port))
        if result == 0:
            print(f"[+] port {port:<5} is OPEN")
            s.close()
    except Exception:
        pass

def main():
    print(f"[*] starting fast port scan on {TARGET}...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(scan_port, PORTS)

    print("\n[*] scan completed successfully!")

    if __name__ == "__main__":
        main()