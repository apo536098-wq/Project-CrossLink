import socket
import struct
import time
from datetime import datetime

def hyper_scanner():
    print(f"\n{'-'*40}")
    print(f" PROJECT CROSS-LINK: AKTİF HYPEROS SORGUSU")
    print(f" Zaman: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'-'*40}\n")
    
    MCAST_GRP = '239.255.255.250'
    PORT = 1900

    # UDP Soketi oluştur
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(3) # Cevap gelmezse 3 saniye sonra durdur

    # Ağı dürtmek için SSDP M-SEARCH paketi hazırlıyoruz
    # Bu paket ağdaki tüm akıllı cihazları ayağa kaldırır
    search_msg = (
        "M-SEARCH * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "MAN: \"ssdp:discover\"\r\n"
        "MX: 1\r\n"
        "ST: ssdp:all\r\n"
        "\r\n"
    ).encode('utf-8')

    print("[*] Ağdaki cihazlara aktif sorgu gönderiliyor...")
    # Paketi ağa fırlatıyoruz (3 kere üst üste gönderelim ki garanti olsun)
    for _ in range(3):
        sock.sendto(search_msg, (MCAST_GRP, PORT))
        time.sleep(0.2)

    print("[*] Cevaplar bekleniyor (3 saniye)... \n")

    try:
        while True:
            data, addr = sock.recvfrom(2048)
            msg = data.decode('utf-8', errors='ignore')
            
            # Gelen cevapları filtrele
            if any(key in msg for key in ["Xiaomi", "HyperConnect", "Vela", "Mi-interconnect"]):
                print(f"[+] ŞAKALANDI! HEDEF BULUNDU: {addr[0]}")
                print(f"Cihaz Detayı:\n{msg}")
                print("-" * 40)
            elif "UPnP" in msg or "Asus" in msg or "Philips" in msg:
                # Ağda başka cihazlar varsa sadece IP'sini yazalım ki çalıştığını anlayalım
                print(f"[*] Başka bir cihaz yanıt verdi: {addr[0]}")
                
    except socket.timeout:
        print("\n[!] Süre doldu. Aktif sorguya yanıt veren Xiaomi cihazı olmadı.")
    except KeyboardInterrupt:
        print("\n[!] Tarama durduruldu.")

if __name__ == "__main__":
    hyper_scanner()
