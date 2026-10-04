import socket
import concurrent.futures

# za mu iya amfani da  127.0.01 ko scanme.nmap.org
TARGET = "127.0.0.1"
PORTS = [22, 80, 135, 139, 445]

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3.0)

        result = s.connect_ex((TARGET, port))

        if result == 0:
            try:
               service_name = socket.getservbyport(port)
            except Exception:
               service_name = "Unknown service"

            print(f"[+] port {port:>5} is OPEN --> service: {service_name}")
        else:
            print(f"[-] port {port:<5} is closed")

        s.close()
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")

def main():
    print(f"[*] starting advanced scan on {TARGET}...")
    print(f"[*] Checking ports 1 to 100 with service Detection...\n")

    # Rage max_workers zuwa 5 don gujewa toshewa gada firewall
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(scan_port, PORTS)

    print("\n[*] scan completed successfully!")

    if __name__ == "__main__":
        main()