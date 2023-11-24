import socket

import psutil

def get_local_ip():
    try:
        # Create a socket object and connect to an external server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to Google's public DNS server
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error:
        return None

# Example usage
local_ip_address = get_local_ip()

if local_ip_address:
    print(f"Local IP address: {local_ip_address}")
else:
    print("Unable to retrieve local IP address.")


def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout to limit the connection attempt duration

    try:
        sock.connect((host, port))
        print(f"Port {port} is open on {host}")
    except socket.error:
        print(f"Port {port} is closed on {host}")
    finally:
        sock.close()

# Example usage
host = "155.158.58.91"  # Replace with the IP address or hostname of the target machine

ports_to_check = [3074, 4000, 6112, 6113, 6114, 6115, 6116, 6117, 6118, 6119, 20500, 20510, 27014, 27015, 27016, 27017, 27018, 27019, 27020, 27021, 27022, 27023, 27024, 27025, 27026, 27027, 27028, 27029, 27030, 27031, 27036, 28960]

for port in ports_to_check:
    check_port(host, port)




def get_process_using_port(port):
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            return psutil.Process(conn.pid)
    return None

# Example usage
port_to_check = 3074  # Replace with the port you want to check

process_using_port = get_process_using_port(port_to_check)

if process_using_port:
    print(f"Process using port {port_to_check}: {process_using_port.name()}")
else:
    print(f"No process found using port {port_to_check}")
