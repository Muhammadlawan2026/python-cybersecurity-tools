import socket
import concurrent.futures

# target da kofofi (ports) da  muke so mu duba
TARGET = "scanme.nmap.org"
PORTS = range(1, 101) # za mu duba daga port 1 zuwa 100


def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)

        # kokarin hadawa da port din
        result = s.connect_ex((TARGET, port))

        if result == 0:
            print(f"[+] port {port} is OPEN!")
            s.close()
    except Exception:
        pass

def main():
    print(f"[*] starting fast Multi-Threded scan on {TARGET}...")
    print(f"[*] scanning ports 1 to 100...\n")

    # Amfani da ThreadpoolExecutor don saurin scan (threads 20 a lokaci guda)
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(scan_port, PORTS)

    print("\n[*] scan completed successfully!")

if __name__ =="__main__":
    main()