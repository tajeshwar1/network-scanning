import subprocess
import platform
import re

def get_arp_table():
    system = platform.system().lower()

    try:
        if system == "windows":
            command = ["arp", "-a"]
        else:
            command = ["arp", "-n"]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print("[ERROR] Unable to retrieve ARP table")
            return

        parse_arp_output(result.stdout)

    except Exception as e:
        print(f"[ERROR] {e}")


def parse_arp_output(output):
    print("\nIP Address\t\tMAC Address")
    print("-" * 40)

    pattern = r"(\d+\.\d+\.\d+\.\d+)[^\n]*?(([a-fA-F0-9]{2}[:-]){5}[a-fA-F0-9]{2})"

    matches = re.findall(pattern, output)

    for match in matches:
        ip = match[0]
        mac = match[1]
        print(f"{ip}\t\t{mac}")


if __name__ == "__main__":
    get_arp_table()