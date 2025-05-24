import socket
from collections import Counter
from colorama import init, Fore, Style

init(autoreset=True)

# Lista över portar och tjänster
PORT_SERVICES = {
    20: "FTP (Data)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    137: "NetBIOS Name",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
   5009: "Local Admin (AirPort)",
    548: "AFP",
    3306: "MySQL",
    3389: "RDP",
}

SERVICE_CATEGORIES = {
    "FTP (Data)": "Fildelning",
    "FTP (Control)": "Fildelning",
    "SSH": "Fjärrstyrning",
    "Telnet": "Fjärrstyrning",
    "SMTP": "E-post",
    "DNS": "Namnuppslagning",
    "DHCP (Server)": "Nätverkstjänst",
    "DHCP (Client)": "Nätverkstjänst",
    "TFTP": "Fildelning",
    "HTTP": "Webb",
    "POP3": "E-post",
    "NTP": "Tidsynkronisering",
    "NetBIOS Name": "Fildelning",
    "NetBIOS Datagram": "Fildelning",
    "NetBIOS Session": "Fildelning",
    "IMAP": "E-post",
    "SNMP": "Nätverksövervakning",
    "SNMP Trap": "Nätverksövervakning",
    "LDAP": "Katalogtjänst",
    "HTTPS": "Webb",
    "SMB": "Fildelning",
    "IMAPS": "E-post",
    "POP3S": "E-post",
    "Local Admin": "Lokal routeradministration (AirPort)",

    "MySQL": "Databastjänst",
    "RDP": "Fjärrstyrning",
    "AFP": "Fildelning",
    "Okänd tjänst": "Övrigt"
}

open_ports = []
closed_ports = []

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            service = PORT_SERVICES.get(port, "Okänd tjänst")
            category = SERVICE_CATEGORIES.get(service, "Övrigt")
            print(Fore.GREEN + f"[+] Port {port} är ÖPPEN - {service}")
            open_ports.append((port, service, category))
        else:
            print(Fore.RED + f"[-] Port {port} är stängd")
            closed_ports.append(port)
    except Exception as e:
        print(Fore.YELLOW + f"[!] Fel vid port {port}: {e}")
        
def main():
    target = input("Ange IP-adress att scanna: ")
    start_port = int(input("Startport: "))
    end_port = int(input("Slutport: "))
    
    print(Style.BRIGHT + f"\nScannar {target} från port {start_port} till {end_port}...\n")

    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    # Sammanfattning
    print(Style.BRIGHT + "\n--- Sammanfattning ---")
    print(Fore.GREEN + f"Öppna portar ({len(open_ports)}):")
    for port, service, _ in open_ports:
        print(Fore.GREEN + f"  - Port {port} ({service})")

    print(Fore.RED + f"Stängda portar: {len(closed_ports)}")

    # Kategorisammanställning
    categories = [cat for _, _, cat in open_ports]
    counted = Counter(categories)
    most_common = counted.most_common(1)[0] if counted else ("Inget hittat", 0)

    print(Style.BRIGHT + "\n--- Tjänstekategorier ---")
    for cat, count in counted.items():
        print(f"{cat}: {count} port(ar)")

    print(Fore.CYAN + f"\nVanligaste kategorin: {most_common[0]} ({most_common[1]} port(ar))")

if __name__ == "__main__":
    main()