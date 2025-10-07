# packet_sniffer.py
from scapy.all import sniff

def packet_callback(packet):
    """
    Fungsi ini akan dipanggil untuk setiap paket yang ditangkap.
    """
    print(packet.summary())

def main():
    print("Memulai penangkapan paket... Tekan Ctrl+C untuk berhenti.")
    # 'prn' adalah fungsi yang akan dijalankan untuk setiap paket
    # 'count=0' berarti menangkap paket tanpa henti
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    # Perlu dijalankan dengan hak akses root
    print("Pastikan Anda menjalankan skrip ini dengan 'sudo'.")
    main()
