# Cette outils a été fait entièrement pas Shawnn
# Ne pas le modifier
# Ne pas revendre
import requests

print("Made By Shawnn for 0z Tools\n")

while True:
    print("Que veux tu faire ?")
    print("[1] REDIRECTION SOLVER")
    print("[2] Exit")
    choice = input("> ").strip()
    if choice == "2":
        break
    if choice == "1":
        url = input("URLS: ").strip()
        try:
            r = requests.get(url, allow_redirects=True, timeout=10)
            if r.history:
                print(f"\n[+] {url} -> {r.url}")
                for i, h in enumerate(r.history, 1):
                    print(f"    {i}. {h.status_code} -> {h.headers.get('Location','-')}")
            else:
                print(f"\n[=] {url} (no redirect)")
        except Exception as e:
            print(f"[!] {url} -> ERROR: {e}")
        print()
