import socket
import struct
import time
import json
import os
from datetime import datetime

CRITICAL_PORTS = {
    22: "SSH (Güvenli Erişim)",
    80: "HTTP (Web Arayüzü)",
    443: "HTTPS (Güvenli Web)",
    1900: "UPnP (Cihaz Keşif Servisi)",
    5000: "UPnP/SSDP (Alternatif)",
    8080: "HTTP-Proxy / Yönetim Paneli",
    8443: "HTTPS-Alt / Yönetim Paneli"
}

def save_report_to_json(scan_data):
    """Tarama sonuçlarını logs/crosslink_report.json dosyasına profesyonelce kaydeder."""
    log_dir = "logs"
    log_file = os.path.join(log_dir, "crosslink_report.json")
    
    # logs klasörü yoksa otomatik oluştur
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    reports = []
    
    # Eğer önceden kalma bir rapor dosyası varsa eski verileri oku
    if os.path.exists(log_file):
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                reports = json.load(f)
        except:
            reports = []
            
    # Yeni tarama verisini listeye ekle
    reports.append(scan_data)
    
    # Dosyaya düzenli bir şekilde yaz (indent=4 formatı temiz gösterir)
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(reports, f, ensure_ascii=False, indent=4)
    print(f"[+] ANALİZ RAPORU GÜNCELLENDİ: {log_file}")

def port_scanner(target_ip):
    """Bulunan hedef cihazın açık portlarını tarar ve listeler."""
    print(f"\n[!] {target_ip} İÇİN DETAYLI PORT VE SERVİS ANALİZİ BAŞLADI...")
    print(f"{'.' * 50}")
    
    open_ports = []
    
    for port, service_name in CRITICAL_PORTS.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.8)
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"  [+] Port {port:4} : AÇIK  --> {service_name}")
                banner_info = "Bilinmiyor"
                
                try:
                    sock.sendall(b"\r\n")
                    banner = sock.recv(512).decode('utf-8', errors='ignore').strip()
                    if banner:
                        banner_info = banner.splitlines()[0]
                        print(f"      [v] Servis Detayı: {banner_info}")
                except:
                    pass
                    
                open_ports.append({
                    "port": port,
                    "service": service_name,
                    "banner": banner_info
                })
            sock.close()
        except:
            pass

    if not open_ports:
        print("  [-] Kritik portlarda açık servis bulunamadı.")
    print(f"{'.' * 50}\n")
    return open_ports

def hyper_scanner():
    print(f"\n{'-'*50}")
    print(f"  PROJECT CROSS-LINK: AKTİF KEŞİF VE OTOMATİK RAPORLAMA")
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

    print("[*] Cihaz yanıtları bekleniyor...\n")

    discovered_ips = set()
    scan_start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        while True:
            data, addr = sock.recvfrom(2048)
            msg = data.decode('utf-8', errors='ignore')
            ip_address = addr[0]
            
            if ip_address not in discovered_ips:
                if any(key in msg for key in ["Xiaomi", "HyperConnect", "Vela", "Mi-interconnect", "Linux", "UPnP"]):
                    print(f"[+] HEDEF YAKALANDI: {ip_address}")
                    discovered_ips.add(ip_address)
                    
                    # Port taramayı başlat ve sonuçları al
                    detected_ports = port_scanner(ip_address)
                    
                    # Rapor verisini hazırla
                    scan_data = {
                        "scan_time": scan_start_time,
                        "target_ip": ip_address,
                        "raw_response_sample": msg[:200].replace("\r\n", " "), # Örnek veri
                        "open_ports": detected_ports
                    }
                    
                    # JSON dosyasına kaydet
                    save_report_to_json(scan_data)
                    
    except socket.timeout:
        if not discovered_ips:
            print("\n[!] Süre doldu. Aktif sorguya yanıt veren uyumlu bir cihaz olmadı.")
            # Boş tarama raporunu da loglayalım (Sistemin kararlı çalıştığının kanıtı)
            save_report_to_json({
                "scan_time": scan_start_time,
                "status": "No devices discovered on this segment"
            })
        else:
            print("\n[*] Tarama tamamlandı. Tüm raporlar başarıyla JSON formatında loglandı.")
    except KeyboardInterrupt:
        print("\n[!] Tarama kullanıcı tarafından durduruldu.")

if __name__ == "__main__":
    hyper_scanner()
