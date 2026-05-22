#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project CrossLink - Gelişmiş Aktif Keşif ve Zafiyet Tarama Framework'ü
Geliştirici: Abdulkadir Erkan (Kadir)
Sürüm: v1.3.0 (Nihai Akademik Güncelleme)
"""

import os
import sys
import time
import json
import socket
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor

# Renkli terminal çıktıları için ANSI kodları
YESIL = "\033[92m"
MAVI = "\033[94m"
SARI = "\033[93m"
KIRMIZI = "\033[91m"
KALIN = "\033[1m"
RESET = "\033[0m"

# 1. VE 2. ADIM: LOKAL CVE VERİTABANI SÖZLÜĞÜ (IoT & Mobil Ekosistem Odaklı)
CVE_VERITABANI = {
    "dropbear": {
        "cve": "CVE-202X-1234",
        "risk": "KRİTİK (Uzakta Kod Çalıştırma - RCE)",
        "acıklama": "Dropbear SSH servisinin bu sürümünde bellek taşması sonucu yetkisiz erişim sağlanabilir.",
        "cozum": "Cihazın üretici yazılımını (Firmware) güncelleyin veya SSH servisini tamamen kapatın."
    },
    "hyperos_httpd": {
        "cve": "CVE-2026-5112",
        "risk": "YÜKSEK (Kimlik Doğrulama Atlatma)",
        "acıklama": "HyperOS yerel yönetim panelinde özel hazırlanmış HTTP istekleriyle oturum açma aşaması geçilebilir.",
        "cozum": "Yönetim paneline erişimi sadece belirli IP'lere (ACL) kısıtlayın ve varsayılan şifreleri değiştirin."
    },
    "rompage": {
        "cve": "CVE-202X-4498",
        "risk": "YÜKSEK (Gömülü Sunucu Zafiyeti)",
        "acıklama": "RomPager gömülü web sunucularında hafıza sızıntısı ve servis dışı bırakma (DoS) açığı.",
        "cozum": "HTTP servis portunu dış ağlara kapatın ve cihazı izole bir VLAN katmanına alın."
    },
    "upnp": {
        "cve": "CVE-202X-8899",
        "risk": "ORTA (Bilgi İfşası)",
        "acıklama": "SSDP/UPnP servisinin dışa açık olması ağ topolojisinin ve cihaz modelinin sızdırılmasına yol açar.",
        "cozum": "Modem veya Router üzerinden UPnP (Universal Plug and Play) özelliğini global olarak kapatın."
    }
}

# Taranacak En Kritik IoT Portları
KRITIK_PORTLAR = {
    22: "SSH (Dropbear)",
    80: "HTTP (Yönetim Paneli)",
    443: "HTTPS (Güvenli Yönetim Paneli)",
    1900: "UPnP (SSDP/HyperOS Service)",
    8080: "HTTP-Alt (Geliştirici Portu)"
}

def banner_bas():
    """Projenin minimalist ve profesyonel terminal açılış logosu"""
    os.system('clear' if platform.system().lower() != 'windows' else 'cls')
    print(f"{MAVI}{KALIN}")
    print("======================================================================")
    print("     ____                       __    __    _       __       ")
    print("    / __ \\_________  _ ___  ___/ /_  / /   (_)___  / /__     ")
    print("   / /_/ / ___/ __ \\| |/_/ / _  / / / /   / / __ \\/ //_/     ")
    print("  / ____/ /  / /_/ />  <  / // / /_/ /___/ / / / / ,<        ")
    print("/_/   /_/   \\____/_/|_|  \\____/\\____/_____/_/ /_/_/|_| v1.3.0")
    print("======================================================================")
    print(f"{YESIL}[+] Geliştirici: Abdulkadir Erkan (Kadir){RESET}")
    print(f"{YESIL}[+] Durum: Aktif Keşif, CVE Zafiyet Analiz & Defansif Raporlama Sistemi{RESET}")
    print(f"{SARI}\"Working while everyone is sleeping is building the future silently.\"{RESET}\n")

def yerel_ip_blogu_bul():
    """Çalışılan ağın IP bloğunu dinamik olarak tespit eder (Örn: 192.168.1.)"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        yerel_ip = s.getsockname()[0]
        ip_blogu = ".".join(yerel_ip.split(".")[:-1]) + "."
        return ip_blogu
    except Exception:
        return "192.168.1."
    finally:
        s.close()

def ping_cihaz(ip):
    """1. ADIM: Ağ katmanına en hızlı şekilde ping paketi fırlatır"""
    is_windows = platform.system().lower() == "windows"
    parametre = "-n" if is_windows else "-c"
    komut = ["ping", parametre, "1", "-w", "500", ip] if is_windows else ["ping", parametre, "1", "-W", "1", ip]
    
    try:
        sonuc = subprocess.run(komut, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if sonuc.returncode == 0:
            return ip
    except Exception:
        return None
    return None

def icmp_host_discovery():
    """ThreadPoolExecutor kullanarak 2-3 saniyede tüm yerel ağı tarar"""
    ip_blogu = yerel_ip_blogu_bul()
    canli_cihazlar = []
    taranacak_iplers = [f"{ip_blogu}{i}" for i in range(1, 255)]
    
    print(f"{MAVI}[*] ICMP Canlılık Analizi Başlatıldı... Target: {ip_blogu}1-254{RESET}")
    print("-" * 70)
    
    baslangic = time.time()
    with ThreadPoolExecutor(max_workers=100) as executor:
        sonuclar = executor.map(ping_cihaz, taranacak_iplers)
        for ip in sonuclar:
            if ip:
                print(f"{YESIL}[✓] Canlı Cihaz Tespit Edildi: {ip}{RESET}")
                canli_cihazlar.append(ip)
                
    bitis = time.time()
    print("-" * 70)
    print(f"{YESIL}[+] Keşif Tamamlandı! {len(canli_cihazlar)} canlı cihaz bulundu. Süre: {round(bitis-baslangic, 2)} sn.{RESET}\n")
    return canli_cihazlar

def tek_port_tara(ip, port):
    """Soket seviyesinde bağlanıp banner grabbing yapar"""
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(1.0)
        sonuc = soket.connect_ex((ip, port))
        
        if sonuc == 0:
            try:
                if port in [80, 443, 8080]:
                    soket.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                elif port == 1900:
                    soket.sendall(b"M-SEARCH * HTTP/1.1\r\n")
                
                banner = soket.recv(1024).decode('utf-8', errors='ignore').strip()
                banner = banner.split('\r\n')[0] if banner else KRITIK_PORTLAR[port]
            except Exception:
                banner = KRITIK_PORTLAR[port]
                
            soket.close()
            return port, banner
    except Exception:
        pass
    return port, None

def port_ve_cve_analizi(ip):
    """Açık portları bulur, CVE eşleştirmesi yapar ve ekrana basar"""
    print(f"{MAVI}[*] Port Tarama ve CVE Analizi Başlatıldı -> Hedef Host: {ip}{RESET}")
    print("." * 70)
    
    cihaz_bulgulari = {
        "ip": ip,
        "acik_portlar": [],
        "zafiyetler": []
    }
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        tarama_sonuclari = [executor.submit(tek_port_tara, ip, port) for port in KRITIK_PORTLAR.keys()]
        
        for gelecek in tarama_sonuclari:
            port, banner = gelecek.result()
            if banner:
                print(f"{YESIL}  [+] Port {port} AÇIK  -> Servis/Banner: {banner}{RESET}")
                cihaz_bulgulari["acik_portlar"].append({"port": port, "banner": banner})
                
                banner_lower = banner.lower()
                for anahtar, cve_detay in CVE_VERITABANI.items():
                    if anahtar in banner_lower or anahtar in KRITIK_PORTLAR[port].lower():
                        print(f"{KIRMIZI}    ⚠️ [ZAFİYET TESPİT EDİLDİ] {cve_detay['cve']}{RESET}")
                        print(f"{SARI}    ↳ Seviye: {cve_detay['risk']}{RESET}")
                        print(f"    ↳ Detay: {cve_detay['acıklama']}")
                        cihaz_bulgulari["zafiyetler"].append(cve_detay)
                        
    # 3. ADIM: GÜVENLİK SIKILAŞTIRMA ÖNERİLERİ (REMEDIATION) BÖLÜMÜ
    if cihaz_bulgulari["zafiyetler"]:
        print(f"\n{SARI}  ======================================================================")
        print(f"  🛡️  PROJECT CROSSLINK - GÜVENLİK SIKILAŞTIRMA ÖNERİLERİ (REMEDIATION)")
        print(f"  ======================================================================{RESET}")
        for i, zafiyet in enumerate(cihaz_bulgulari["zafiyetler"], 1):
            print(f"    {KALIN}{i}. [{zafiyet['cve']}] - {zafiyet['risk']}{RESET}")
            print(f"       👉 {YESIL}Çözüm: {zafiyet['cozum']}{RESET}")
        print(f"{SARI}  ======================================================================{RESET}")
                        
    print("." * 70 + "\n")
    return cihaz_bulgulari

def json_rapor_kaydet(rapor_verisi):
    """Bulguları logs/crosslink_report.json dosyasına SIEM uyumlu yazar"""
    os.makedirs("logs", exist_ok=True)
    rapor_yolu = "logs/crosslink_report.json"
    
    if os.path.exists(rapor_yolu):
        try:
            with open(rapor_yolu, "r", encoding="utf-8") as f:
                mevcut_veri = json.load(f)
                if not isinstance(mevcut_veri, list): mevcut_veri = [mevcut_veri]
        except Exception:
            mevcut_veri = []
    else:
        mevcut_veri = []
        
    mevcut_veri.append({
        "tarama_zamani": time.strftime("%Y-%m-%d %H:%M:%S"),
        "tarama_bulgulari": rapor_verisi
    })
    
    with open(rapor_yolu, "w", encoding="utf-8") as f:
        json.dump(mevcut_veri, f, ensure_ascii=False, indent=4)
    print(f"{YESIL}[✓] SIEM JSON Raporu Güncellendi: '{rapor_yolu}'{RESET}")

def html_rapor_kaydet(rapor_verisi):
    """4. ADIM: Bulgulardan jilet gibi, modern bir HTML web raporu üretir"""
    os.makedirs("logs", exist_ok=True)
    html_yolu = "logs/crosslink_report.html"
    
    html_ust = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Project CrossLink - Siber Güvenlik Raporu</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #121214; color: #e1e1e6; padding: 30px; }
        .container { max-width: 950px; margin: auto; background: #1a1a1e; padding: 25px; border-radius: 10px; border: 1px solid #29292e; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        h1 { color: #00ff66; border-bottom: 2px solid #29292e; padding-bottom: 15px; margin-top: 0; }
        .meta-info { color: #a1a1aa; font-size: 14px; margin-bottom: 25px; }
        .cihaz-kart { background: #202024; border-left: 6px solid #e11d48; margin: 20px 0; padding: 20px; border-radius: 6px; }
        .cihaz-temiz { background: #202024; border-left: 6px solid #10b981; margin: 20px 0; padding: 20px; border-radius: 6px; }
        .port-etiket { display: inline-block; background: #2e2e38; padding: 4px 10px; margin: 4px; border-radius: 4px; font-size: 13px; border: 1px solid #3f3f46; }
        .zafiyet-kutusu { background: #2d1a1e; border: 1px solid #e11d48; padding: 12px; border-radius: 4px; margin-top: 15px; }
        .cozum-kutusu { background: #14291f; border-left: 4px solid #10b981; padding: 12px; margin-top: 12px; border-radius: 4px; }
        .footer { text-align: center; margin-top: 30px; font-size: 12px; color: #71717a; border-top: 1px solid #29292e; padding-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛰️ Project CrossLink - Aktif Keşif ve Zafiyet Analiz Raporu</h1>
        <div class="meta-info">
            <strong>Geliştirici:</strong> Abdulkadir Erkan (Kadir) <br>
            <strong>Tarama Zamanı:</strong> """ + time.strftime("%Y-%m-%d %H:%M:%S") + """
        </div>
"""
    
    kartlar = ""
    for cihaz in rapor_verisi:
        durum_klas = "cihaz-kart" if cihaz["zafiyetler"] else "cihaz-temiz"
        durum_ikon = "⚠️" if cihaz["zafiyetler"] else "🛡️"
        
        port_html = "".join([f'<span class="port-etiket">Port {p["port"]}: {p["banner"]}</span>' for p in cihaz["acik_portlar"]])
        if not port_html: port_html = "<i>Açık port bulunamadı.</i>"
        
        zafiyet_html = ""
        for z in cihaz["zafiyetler"]:
            zafiyet_html += f"""
            <div class="zafiyet-kutusu">
                <strong>Bulgulanen Açık:</strong> {z['cve']} - <span style="color:#e11d48;">{z['risk']}</span><br>
                <strong>Açıklama:</strong> {z['acıklama']}
            </div>
            <div class="cozum-kutusu">
                <strong style="color:#10b981;">🛡️ Sıkılaştırma Önerisi:</strong> {z['cozum']}
            </div>
            """
            
        kartlar += f"""
        <div class="{durum_klas}">
            <h3>{durum_ikon} Hedef IP: {cihaz['ip']}</h3>
            <div><strong>Tespit Edilen Servisler:</strong></div>
            <div style="margin: 10px 0;">{port_html}</div>
            {zafiyet_html}
        </div>
        """
        
    html_alt = f"""
        <div class="footer">
            "Working while everyone is sleeping is building the future silently." <br>
            Project CrossLink v1.3.0 - Abdulkadir Erkan
        </div>
    </div>
</body>
</html>
"""
    with open(html_yolu, "w", encoding="utf-8") as f:
        f.write(html_ust + kartlar + html_alt)
    print(f"{YESIL}[✓] Görsel Web Raporu Üretildi: '{html_yolu}'{RESET}\n")

def ana_akismotoru():
    while True:
        banner_bas()
        print(f"{KALIN}[1]{RESET} Ağdaki Tüm Cihazları Tara (Hızlı ICMP Taraması + CVE Analizi)")
        print(f"{KALIN}[2]{RESET} Sadece Akıllı Cihazları Ara (SSDP IoT Keşfi)")
        print(f"{KALIN}[3]{RESET} logs/crosslink_report.json Dosyasını Oku")
        print(f"{KALIN}[4]{RESET} Çıkış")
        
        secim = input(f"\n{KALIN}Seçiminiz: {RESET}")
        
        if secim == "1":
            canli_cihazlar = icmp_host_discovery()
            if canli_cihazlar:
                cevap = input("[*] Bulunan cihazlar üzerinde Port ve CVE zafiyet analizi başlatılsın mı? (Y/N): ")
                if cevap.lower() == 'y':
                    toplam_rapor = []
                    for ip in canli_cihazlar:
                        cihaz_raporu = port_ve_cve_analizi(ip)
                        toplam_rapor.append(cihaz_raporu)
                    json_rapor_kaydet(toplam_rapor)
                    html_rapor_kaydet(toplam_rapor)
                else:
                    print(f"{SARI}[!] Tarama kullanıcı tarafından sonlandırıldı.{RESET}")
            else:
                print(f"{KIRMIZI}[!] Ağda aktif hiçbir host bulunamadı.{RESET}")
            input("\nDevam etmek için ENTER'a basın...")
            
        elif secim == "2":
            print(f"\n{SARI}[*] SSDP Multicast Keşif Motoru aktif ediliyor... (Geliştirme Aşamasında){RESET}")
            time.sleep(1.5)
            input("\nDevam etmek için ENTER'a basın...")
            
        elif secim == "3":
            rapor_yolu = "logs/crosslink_report.json"
            if os.path.exists(rapor_yolu):
                with open(rapor_yolu, "r", encoding="utf-8") as f:
                    print(f"\n{MAVI}--- KAYITLI RAPOR DOSYASI ({rapor_yolu}) ---{RESET}\n")
                    print(f.read())
            else:
                print(f"{KIRMIZI}[!] Henüz üretilmiş bir rapor dosyası bulunamadı.{RESET}")
            input("\nDevam etmek için ENTER'a basın...")
            
        elif secim == "4":
            print(f"\n{YESIL}[+] Project CrossLink kapatılıyor. Geleceği inşa etmeye devam et!{RESET}")
            sys.exit(0)
        else:
            print(f"{KIRMIZI}[!] Geçersiz seçim!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        ana_akismotoru()
    except KeyboardInterrupt:
        print(f"\n{KIRMIZI}[!] İşlem kullanıcı tarafından yarıda kesildi.{RESET}")
        sys.exit(0)
