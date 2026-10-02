import socket


def grab_banner(target_host, target_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # mun kara timeout din zuwa dakika 10
        s.settimeout(10)
        s.connect((target_host, target_port))

        if target_port == 80 or target_port == 8080:
            s.send(b"HEAD / HTTP/1.1\r\nhost: " +target_host.encode() + b"\r\n\r\n")

            banner = s.recv(1204)
            print(f"[+] success! Banner received from {target_host}:{target_port}:\n")
            print(banner.decode('utf-8', errors='ignore').strip())
            s.close()

    except Exception as e:
        print(f"[-] could not grab banner from {target_host}:{target_port}")
        print(f"  reason: {e}")

if __name__ == "__main__":
    # an gyara nmao -> nmap
    target = "scanme.nmap.org"
    port = 80
    print(f"[*] starting banner Grabbing on {target}:{port}...\n")
    grab_banner(target, port)
