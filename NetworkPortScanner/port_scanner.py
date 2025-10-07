# port_scanner.py
import socket
import sys

def scan_port(ip, port):
    """
    Scans a single port on the given IP.
    """
    try:
        # Buat socket baru
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout agar tidak menunggu terlalu lama
        socket.setdefaulttimeout(1)
        
        # Coba koneksi
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: \t [Terbuka]")
        sock.close()

    except socket.error:
        print("Tidak bisa terhubung ke server.")
        sys.exit()

# --- Main Program ---
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Penggunaan: python3 port_scanner.py <target_ip>")
        sys.exit(1)
        
    target_ip = sys.argv[1]
    
    print("-" * 50)
    print(f"Memindai target: {target_ip}")
    print("-" * 50)
    
    try:
        # Pindai 100 port pertama
        for port in range(1, 101):
            scan_port(target_ip, port)
            
    except KeyboardInterrupt:
        print("\nKeluar dari program.")
        sys.exit()
