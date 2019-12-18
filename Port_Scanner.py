import nmap

ns = nmap.PortScanner()


def nmap():
    victim_ip: str = input("IP adress:")
    port_range = input("Port range:")
    print("Please wait...")
    ns.scan(victim_ip, port_range, "-v")
    print(ns.scaninfo())
    print(ns.csv())
