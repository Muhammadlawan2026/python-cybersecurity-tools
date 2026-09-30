import requests

target_url = input("saka url: ")
wordlist = ["admin", "login", "images", "robots.txt"]

if not target_url.endswith("/"):
    target_url += "/"
print("An fara bincike...")
print("\n" + "-" * 50)
print(f"[+] an fara bincikin sunaye a: {target_url}")
print("-" * 50)

for path in wordlist:
    url = target_url + path
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[+]  AN GANO (200 OK)")
        elif response.status_code == 403:
            print(f"[*]  AN HANA SHIGA (403 forbidden): {url}")
    except Exception as e:
        print(f"[!] Errors a {url}: {e}")

print("-" * 50)
print("[!] Bincike ya kammala!")