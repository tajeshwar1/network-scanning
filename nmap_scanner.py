import subprocess

def run_nmap(target, options):
    command = ["nmap"] + options + [target]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=60)

        if result.returncode == 0:
            print(result.stdout)
        else:
            print("[ERROR] Nmap scan failed")
            print(result.stderr)

    except subprocess.TimeoutExpired:
        print("[!] Scan timed out")
    except FileNotFoundError:
        print("[ERROR] Nmap is not installed or not in PATH")
    except Exception as e:
        print(f"[ERROR] {e}")


def menu():
    print("\n--- Nmap Scanner ---")
    print("1. Host Discovery (Ping Scan)")
    print("2. Port Scan")
    print("3. Custom Port Scan")
    print("4. Service Detection")
    print("5. OS Detection")

    choice = input("Select option: ")
    target = input("Enter target (IP/Hostname): ")

    if choice == "1":
        run_nmap(target, ["-sn"])
    elif choice == "2":
        run_nmap(target, ["-p", "1-1024"])
    elif choice == "3":
        ports = input("Enter ports (e.g. 22,80,443): ")
        run_nmap(target, ["-p", ports])
    elif choice == "4":
        run_nmap(target, ["-sV"])
    elif choice == "5":
        run_nmap(target, ["-O"])
    else:
        print("[ERROR] Invalid choice")


if __name__ == "__main__":
    menu()