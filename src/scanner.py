import socket
import struct
import time
from datetime import datetime

# Taranacak en kritik IoT ve Servis portları
CRITICAL_PORTS = {
    22: "SSH (Güvenli Erişim)",
    80: "HTTP (Web Arayüzü)",
    443: "HTTPS (Güvenli Web)",
    1900: "UPnP (Cihaz Keşif Servisi)",
    5000: "UPnP/SSDP (Alternatif)",
    8080: "HTTP-Proxy / Yönetim Paneli",
    8443: "HTTPS-Alt / Yönetim Paneli"
}

def port_scanner(target_ip):
    """Bulunan hedef cihazın açık portlarını ve servislerini analiz eder."""
    print(f"\n[!] {target_ip} İÇİN DETAYLI PORT VE SERVİS ANALİZİ BAŞLADI...")
    print(f"{'.' * 50}")
    
    open_ports_found = False
    
    for port, service_name in CRITICAL_PORTS.items():
        try:
            # Her port için 1 saniyelik zaman aşımı ile TCP bağlantısı deniyoruz
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0)
            
            result = sock.connect_ex((target_ip, port))
            
            # Eğer dönen sonuç 0 ise port AÇIKTIR
            if result == 0:
                print(f"  [+] Port {port:4} : AÇIK  --> {service_name}")
                open_ports_found = True
                
                # Servis banner bilgilerini (sürüm) yakalamaya çalışıyoruz (Banner Grabbing)
                try:
                    if port in [80, 8080]:
                        sock.sendall(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")
                    else:
                        sock.sendall(b"\r\n")
                    banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                    if banner:
                        print(f"      [v] Servis Detayı: {banner.splitlines()[0]}")
                except:
                    pass # Banner alınamazsa sessizce geç
            
            sock.close()
            
        except Exception as e:
            pass

    if not open_ports_found:
        print("  [-] Kritik tarama portlarında açık servis bulunamadı (Cihaz kendini gizliyor olabilir).")
    print(f"{'.' * 50}\n")

def hyper_scanner():
    print(f"\n{'-'*50}")
    print(f"  PROJECT CROSS-LINK: AKTİF KEŞİF VE SERVİS ANALİZİ")
    print(f"  Zaman: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'-'*50}\n")
    
    MCAST_GRP = '239.255.255.250'
    PORT = 1900

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(4) 

    search_msg = (
        "M-SEARCH * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "MAN: \"ssdp:discover\"\r\n"
        "MX: 1\r\n"
        "ST: ssdp:all\r\n"
        "\r\n"
    ).encode('utf-8')

    print("[*] Ağdaki akıllı cihazlara aktif sorgu fırlatılıyor...")
    for _ in range(2):
        sock.sendto(search_msg, (MCAST_GRP, PORT))
        time.sleep(0.1)

    print("[*] Cihaz yanıtları bekleniyor ve analiz ediliyor...\n")

    discovered_ips = set()

    try:
        while True:
            data, addr = sock.recvfrom(2048)
            msg = data.decode('utf-8', errors='ignore')
            ip_address = addr[0]
            
            # Aynı IP'yi üst üste taramamak için kontrol
            if ip_address not in discovered_ips:
                if any(key in msg for key in ["Xiaomi", "HyperConnect", "Vela", "Mi-interconnect", "Linux", "UPnP"]):
                    print(f"[+] HEDEF YAKALANDI: {ip_address}")
                    discovered_ips.add(ip_address)
                    
                    # Cihazı bulduğumuz an otomatik olarak port analiz modülünü tetikliyoruz!
                    port_scanner(ip_address)
                    
    except socket.timeout:
        if not discovered_ips:
            print("\n[!] Süre doldu. Aktif sorguya yanıt veren uyumlu bir cihaz olmadı.")
        else:
            print("\n[*] Tarama tamamlandı. Bulunan tüm cihazlar analiz edildi.")
    except KeyboardInterrupt:
        print("\n[!] Tarama kullanıcı tarafından durduruldu.")

if __name__ == "__main__":
    hyper_scanner()
