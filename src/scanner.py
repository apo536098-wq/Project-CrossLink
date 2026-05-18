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

LOG_FILE = "logs/crosslink_report.json"

def print_banner():
    """Aracın profesyonel siber güvenlik logosunu basar."""
    print("\033[92m" + "="*60)
    print("""
  _____            _           _      _____                      _     _       _    
 |  __ \          (_)         | |    / ____|                    | |   (_)     | |   
 | |__) | __ ___   _  ___  ___| |_  | |     _ __ ___  ___ ___   | |    _ _ __ | | __
 |  ___/ '__/ _ \ | |/ _ \/ __| __| | |    | '__/ _ \/ __/ __|  | |   | | '_ \| |/ /
 | |   | | | (_) || |  __/ (__| |_  | |____| | | (_) \__ \__ \  | |___| | | | |   < 
 |_|   |_|  \___/ | |\___|\___|\__|  \_____|_|  \___/|___/___/  |______|_|_| |_|_|\_\\
                 _/ |                                                               
                |__/                                                                
    """)
    print("  [+] Geliştirici: Kadir (Abdulkadir Erkan)")
    print("  [+] Sürüm: v1.2.0 (Nihai Sürüm)")
    print("="*60 + "\033[0m")

def read_past_reports():
    """Oluşturulan JSON raporlarını terminalde düzgünce listeler."""
    print(f"\n\033[94m[*] GEÇMİŞ TARAMA RAPORLARI OKUNUYOR...\033[0m")
    if not os.path.exists(LOG_FILE):
        print("[-] Henüz kaydedilmiş bir tarama raporu bulunamadı.")
        return

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            reports = json.load(f)
        
        print(f"{'-'*60}")
        for i, r in enumerate(reports, 1):
            print(f"Rapor #{i} | Zaman: {r.get('scan_time')}")
            if "target_ip" in r:
                print(f"  --> Hedef IP: {r['target_ip']}")
                print(f"  --> Açık Port Sayısı: {len(r['open_ports'])}")
                for p in r['open_ports']:
                    print(f"      [+] Port {p['port']}: {p['service']} ({p['banner']})")
            else:
                print(f"  --> Durum: {r.get('status', 'Veri yok')}")
            print(f"{'-'*60}")
    except Exception as e:
        print(f"[-] Rapor okunurken hata oluştu: {e}")

def save_report_to_json(scan_data):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    reports = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                reports = json.load(f)
        except:
            reports = []
            
    reports.append(scan_data)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(reports, f, ensure_ascii=False, indent=4)
    print(f"\033[93m[+] Analiz raporu JSON dosyasına kilitlendi.\033[0m")

def port_scanner(target_ip):
    print(f"\n[!] {target_ip} İçin Port ve Servis Analizi Başladı...")
    open_ports = []
    
    for port, service_name in CRITICAL_PORTS.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.7)
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"  \033[92m[+] Port {port:4} : AÇIK  --> {service_name}\033[0m")
                banner_info = "Bilinmiyor"
                try:
                    sock.sendall(b"\r\n")
                    banner = sock.recv(512).decode('utf-8', errors='ignore').strip()
                    if banner:
                        banner_info = banner.splitlines()[0]
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
    return open_ports

def hyper_scanner():
    print(f"\n\033[95m[*] Ağdaki Akıllı Cihazlara Aktif SSDP Sorgusu Fırlatılıyor...\033[0m")
    MCAST_GRP = '239.255.255.250'
    PORT = 1900

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(4) 

    search_msg = (
        "M-SEARCH * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "MAN: \"ssdp:discover\"\r\n"
        "MX: 1\033[0m\r\n"
        "ST: ssdp:all\r\n"
        "\r\n"
    ).encode('utf-8')

    for _ in range(2):
        sock.sendto(search_msg, (MCAST_GRP, PORT))
        time.sleep(0.1)

    discovered_ips = set()
    scan_start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        while True:
            data, addr = sock.recvfrom(2048)
            msg = data.decode('utf-8', errors='ignore')
            ip_address = addr[0]
            
            if ip_address not in discovered_ips:
                if any(key in msg for key in ["Xiaomi", "HyperConnect", "Vela", "Mi-interconnect", "Linux", "UPnP"]):
                    print(f"\n\033[92m[+] HEDEF YAKALANDI: {ip_address}\033[0m")
                    discovered_ips.add(ip_address)
                    
                    detected_ports = port_scanner(ip_address)
                    
                    scan_data = {
                        "scan_time": scan_start_time,
                        "target_ip": ip_address,
                        "open_ports": detected_ports
                    }
                    save_report_to_json(scan_data)
                    
    except socket.timeout:
        if not discovered_ips:
            print("\n[!] Süre doldu. Aktif sorguya yanıt veren uyumlu bir cihaz olmadı.")
            save_report_to_json({
                "scan_time": scan_start_time,
                "status": "No devices discovered"
            })
        else:
            print("\n[*] Tarama tamamlandı. Tüm bulgular loglandı.")

def main_menu():
    while True:
        print_banner()
        print("  [1] Aktif Ağ Taramasını Başlat (Keşif + Port Scan)")
        print("  [2] Geçmiş Tarama Raporlarını İncele (JSON Okuyucu)")
        print("  [3] Programdan Çık")
        print("="*60)
        
        secim = input("  Seçiminiz (1/2/3): ").strip()
        
        if secim == "1":
            hyper_scanner()
        elif secim == "2":
            read_past_reports()
        elif secim == "3":
            print("\n[!] Project CrossLink kapatılıyor. Güvenli günler dileriz, başkan!\n")
            break
        else:
            print("\n[-] Geçersiz seçim! Lütfen 1, 2 veya 3 yazın.")
        
        input("\nDevam etmek için ENTER'a basın...")
        os.system('clear')

if __name__ == "__main__":
    main_menu()
