import socket

def grab_banner(ip_address, port):
    try:

        s = socket.socket()
        s.settimeout(3) # tsayawa na sakanni 3 kacal
        s.connect((ip_address, port))

        # idan port 80 (HTTP) ce muna bukatar aike mata da bukata kafin ta ba mu banner
        if port == 80:
            s.send(b'GET / HTTP/1.1\r\nHost: ' + ip_address.encode() + b'\r\n\r\n')

        banner = s.recv(1024)
        return banner.decode().strip()
    except Exception as e:
        return f"Ba a samu banner ba: {e}"

if __name__ == "__main__":
    target_host = input("shiga da IP ko gidan yanar gizo (misali: scanme.nmap.org):")
    target_port = int(input("shigar da port din da kake so ka duba(misali:  80, 21, 22):"))

    print(f"\n[*] muna kokarin ciro banner daga {target_host}:{target_port}...\n")
    result = grab_banner(target_host, target_port)
    print("=== BANNER DA AKA SAMU ===")
    print(result)
