import platform
import subprocess
import time
import ipaddress

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(host)]

    try:
        start = time.time()
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=3)
        end = time.time()

        if output.returncode == 0:
            latency = round((end - start) * 1000, 2)
            print(f"[+] {host} is UP ({latency} ms)")
        else:
            print(f"[-] {host} is DOWN")

    except subprocess.TimeoutExpired:
        print(f"[!] {host} request timed out")
    except Exception as e:
        print(f"[ERROR] {host}: {e}")


def scan_range(target):
    try:
        network = ipaddress.ip_network(target, strict=False)
        for ip in network.hosts():
            ping_host(ip)
    except ValueError:
        ping_host(target)


if __name__ == "__main__":
    target = input("Enter IP / Hostname / Network (e.g. 192.168.1.0/24): ")
    scan_range(target)