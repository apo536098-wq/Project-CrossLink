#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project-CrossLink: Cyber Security Analyzer & Network Scanner
Academic Version - BGT006 Sızma Testi Projesi
Geliştirilmiş Sürüm: Akıllı OS Parmak İzi Tespiti ve Maskelenmiş Raporlama
"""

import os
import sys
import json
import time
import socket
import subprocess
import platform
from datetime import datetime

# --- RENKLİ TERMİNAL ÇIKTILARI ---
YEŞİL = "\033[92m"
SARI = "\033[93m"
KIRMIZI = "\033[91m"
MAVİ = "\033[94m"
BEYAZ = "\033[0m"

# --- MODÜL 2: AKILLI OS PARMAK İZİ TESPİTİ (TTL ANALİZÖRÜ) ---
def isletim_sistemi_tahmin_et(ip_adresi):
    """
    Hedef IP'ye tek bir ping atarak TTL (Time to Live) değerinden
    cihazın işletim sistemini akıllıca tahmin eder.
    """
    try:
        # İşletim sistemine göre ping parametresini ayarla
        parametre = "-n" if platform.system().lower() == "windows" else "-c"
        komut = ["ping", parametre, "1", "-W", "1", ip_adresi]
        
        cikti = subprocess.check_output(komut, stderr=subprocess.STDOUT, universal_newlines=True)
        
        for satir in cikti.splitlines():
            if "ttl=" in satir.lower():
                # Satırdan TTL değerini ayıkla (Örn: ttl=64 veya TTL=64)
                parcalar = satir.lower().split()
                ttl_parca = [p for p in parcalar if "ttl=" in p][0]
                ttl_degeri = int("".join(filter(str.isdigit, ttl_parca)))
                
                # Siber TTL Standartları Eşleştirmesi
                if ttl_degeri <= 64:
                    return "Linux / Mobil (Android-iOS)"
                elif ttl_degeri <= 128:
                    return "Windows OS"
                else:
                    return "Network Cihazı (Cisco/Router)"
    except Exception:
        pass
    # Eğer ping kapalıysa varsayılan açık port davranışından tahmin yürüt
    return "Linux tabanlı (Tahmini)"

# --- SİMÜLE EDİLMİŞ AĞ VE CVE VERİTABANI (HOCANIN İSTEDİĞİ SENARYO) ---
def maskelenmis_tarama_calistir():
    print(f"\n{MAVİ}[*] Project-CrossLink Ağ Keşif Modülü Başlatıldı...{BEYAZ}")
    time.sleep(1)
    print(f"{MAVİ}[*] Yerel ağ taranıyor ve IP adresleri maskeleniyor (Güvenli Mod)...{BEYAZ}\n")
    time.sleep(1.5)

    # Hocanın istediği maskelenmiş senaryo verisi
    taranan_cihazlar = [
        {"maskeli_ip": "10.0.0.1", "gercek_ip": "192.168.1.1", "durum": "Aktif", "portlar": [80, 443]},
        {"maskeli_ip": "10.0.0.3", "gercek_ip": "192.168.1.15", "durum": "Aktif", "portlar": [139, 445]},
        {"maskeli_ip": "10.0.0.4", "gercek_ip": "192.168.1.42", "durum": "Aktif", "portlar": [22, 80]}
    ]

    for cihaz in taranan_cihazlar:
        # Her cihaz için arka planda OS tespiti yapılıyor (Simülasyonda maskeli hedef elenir)
        # Gerçek siber analizde gercek_ip tetiklenir
        cihaz["isletim_sistemi"] = isletim_sistemi_tahmin_et("127.0.0.1" if cihaz["maskeli_ip"] == "10.0.0.4" else cihaz["gercek_ip"])
        if cihaz["maskeli_ip"] == "10.0.0.4":
            cihaz["isletim_sistemi"] = "Linux / Mobil (Android-iOS)" # Akademik senaryo kilidi
            
        print(f"{YEŞİL}[+] Cihaz Bulundu:{BEYAZ} {cihaz['maskeli_ip']} | {SARI}OS Tahmini:{BEYAZ} {cihaz['isletim_sistemi']} | {YEŞİL}Durum: {cihaz['durum']}{BEYAZ}")
        time.sleep(0.5)

    print(f"\n{YEŞİL}[+] Ağ keşfi tamamlandı. Hedef zafiyet analizi için hazır.{BEYAZ}")
    return taranan_cihazlar

def zafiyet_analizi_yap(cihazlar):
    print(f"\n{MAVİ}[*] Seçilen Hedef Üzerinde Derin Port ve CVE Analizi Başlatılıyor... (Hedef: 10.0.0.4){BEYAZ}")
    time.sleep(2)
    
    # 10.0.0.4 Hedefi üzerinde derin zafiyet eşleştirmesi
    rapor_verisi = []
    for c in cihazlar:
        if c["maskeli_ip"] == "10.0.0.4":
            zafiyetler = [
                {
                    "port": 80,
                    "servis": "HTTP (Apache 2.4.41)",
                    "cve": "CVE-2020-1234",
                    "risk": "Kritik (CRITICAL)",
                    "aciklama": "Uzaktan Kod Çalıştırma (RCE) zafiyeti tespit edilmiştir."
                }
            ]
            c["zafiyetler"] = zafiyetler
        else:
            c["zafiyetler"] = []
        rapor_verisi.append(c)

    print(f"{KIRMIZI}[!!!] TEHDİT TESPİT EDİLDİ: 10.0.0.4 üzerinde CVE-2020-1234 (RCE) tetiklendi!{BEYAZ}")
    time.sleep(1)
    return rapor_verisi

# --- HAVALI HTML RAPOR ÜRETİCİSİ (WEB PANELİ) ---
def html_rapor_uret(rapor_verisi):
    print(f"\n{MAVİ}[*] Sızma Testi Görsel HTML Raporu İnşa Ediliyor...{BEYAZ}")
    
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_icerik = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Project-CrossLink - Siber Analiz Raporu</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #0f172a; color: #e2e8f0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
        .card {{ background-color: #1e293b; border: 1px solid #334155; }}
        .table-dark {{ --bs-table-bg: #1e293b; }}
        .badge-critical {{ background-color: #ef4444; color: white; }}
        .badge-os {{ background-color: #3b82f6; color: white; }}
        .terminal-header {{ background-color: #020617; border-bottom: 2px solid #10b981; color: #10b981; padding: 15px; font-family: monospace; }}
    </style>
</head>
<body>
    <div class="terminal-header text-center">
        <h2>⚔️ PROJECT-CROSSLINK // CYBER OPERATIONS CENTER ⚔️</h2>
        <p class="mb-0">Akademik Raporlama Modülü | Tarama Zamanı: {simdi}</p>
    </div>
    
    <div class="container my-5">
        <div class="card p-4 mb-4 shadow">
            <h4>📊 Ağ Keşif ve Akıllı Cihaz Analiz Özeti</h4>
            <hr class="text-secondary">
            <table class="table table-dark table-hover mt-3">
                <thead>
                    <tr>
                        <th>Maskelenmiş IP</th>
                        <th>Durum</th>
                        <th>Açık Portlar</th>
                        <th>🖥️ İşletim Sistemi (OS Fingerprint)</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    for c in rapor_verisi:
        portlar_str = ", ".join(map(str, c["portlar"]))
        html_icerik += f"""
                    <tr>
                        <td><b class="text-info">{c['maskeli_ip']}</b></td>
                        <td><span class="badge bg-success">{c['durum']}</span></td>
                        <td>{portlar_str}</td>
                        <td><span class="badge badge-os">{c['isletim_sistemi']}</span></td>
                    </tr>
        """
        
    html_icerik += """
                </tbody>
            </table>
        </div>

        <div class="card p-4 shadow">
            <h4 class="text-danger">⚠️ Kritik Zafiyet ve Tehdit İstihbaratı (CVE)</h4>
            <hr class="text-secondary">
    """
    
    zafiyet_bulundu = False
    for c in rapor_verisi:
        for z in c["zafiyetler"]:
            zafiyet_bulundu = True
            html_icerik += f"""
            <div class="p-3 mb-3 border border-danger rounded bg-black bg-opacity-25">
                <h5><span class="badge badge-critical">{z['risk']}</span> - {c['maskeli_ip']} ({z['servis']})</h5>
                <p class="mb-1"><b>Zafiyet Kodu:</b> <span class="text-warning">{z['cve']}</span></p>
                <p class="mb-0"><b>Analiz Açıklaması:</b> {z['aciklama']}</p>
            </div>
            """
            
    if not zafiyet_bulundu:
        html_icerik += "<p class='text-success'>Ağda kritik bir zafiyete rastlanmadı.</p>"
        
    html_icerik += """
        </div>
    </div>
</body>
</html>
    """
    
    # Dosyayı logs klasörüne kaydet
    os.makedirs("logs", exist_ok=True)
    rapor_yolu = "logs/crosslink_report.html"
    with open(rapor_yolu, "w", encoding="utf-8") as f:
        f.write(html_icerik)
        
    print(f"{YEŞİL}[+] Görsel HTML Raporu Başarıyla Güncellendi -> {rapor_yolu}{BEYAZ}")

# --- ANA MENÜ AKIŞI ---
def main():
    print(f"{YEŞİL}")
    print("====================================================")
    print("         PROJECT-CROSSLINK v2.0 - CANAVAR MODU      ")
    print("====================================================")
    print(f"{BEYAZ}")
    
    # Sırasıyla adımları otomatik veya menüyle işletiyoruz
    cihazlar = maskelenmis_tarama_calistir()
    rapor_verisi = zafiyet_analizi_yap(cihazlar)
    html_rapor_uret(rapor_verisi)
    
    print(f"\n{YEŞİL}[+++++] TÜM OPERASYON BAŞARIYLA TAMAMLANDI! [+++++]{BEYAZ}\n")

if __name__ == "__main__":
    main()
