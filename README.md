# Project CrossLink 🛰️ (v1.3.0 - Akademik Sürüm)

Project CrossLink; yerel ağ (LAN) üzerindeki aktif cihazları, Xiaomi, Vela ve HyperOS tabanlı IoT sistemlerini otomatik olarak tespit etmek, bu cihazların üzerinde çalışan kritik servisleri soket seviyesinde analiz etmek, bilinen zafiyetlerle (CVE) eşleştirmek ve defansif sıkılaştırma önerileriyle birlikte siber güvenlik standartlarında raporlamak için geliştirilmiş bağımsız bir **Aktif Keşif ve Zafiyet Tarama (Reconnaissance & Vulnerability Assessment) Framework'üdür.**

---

## 🚀 Öne Çıkan Özellikler

* **Asenkron ICMP Host Discovery (1. ADIM):** `ThreadPoolExecutor` mimarisi sayesinde yerel ağdaki (C-Class/B-Class) 254 farklı IP adresini milisaniyeler (2-3 saniye) içinde tarayarak canlı host haritasını çıkartır.
* **Aktif SSDP/UPnP Keşfi (2. ADIM):** Ağ katmanına çoklu gönderim (Multicast - `239.255.255.250:1900`) sorguları fırlatarak akıllı cihazları ve IoT bileşenlerini ayrıştırır.
* **Gelişmiş Banner Grabbing & Port Tarama:** En kritik IoT portlarını (SSH, HTTP, HTTPS, UPnP) soket seviyesinde tarayarak servis imza (Fingerprinting) analizini gerçekleştirir.
* **Lokal CVE Eşleştirme Motoru:** Yakalanan banner ve servis sürümlerini, framework içinde yer alan gömülü zafiyet sözlüğü ile eşleştirerek potansiyel açıklıkları (`CVE-2026-5112` vb.) ve risk skorlarını (Kritik/Yüksek) belirler.
* **Defansif Sıkılaştırma Önerileri (Remediation):** Tespit edilen zafiyetlere yönelik sistem yöneticileri için anlık "Güvenlik Sıkılaştırma (Hardening)" kılavuzu ve çözüm yolları üretir.
* **Çift Katmanlı Raporlama:** * *Merkezi Loglama:* SIEM (Splunk, ELK) sistemleriyle tam uyumlu `logs/crosslink_report.json` çıktısı.
    * *Yönetici Sunum Raporu:* Tarayıcı üzerinden açılabilen, jilet tasarımlı, modern ve renkli `logs/crosslink_report.html` web raporu.

---

## 🛠️ Kurulum ve Çalıştırma

Proje hiçbir harici kütüphaneye veya bağımlılığa (Nmap, Masscan, Pip paketleri vb.) ihtiyaç duymadan, **tamamen Python'ın yerel soket, alt süreç ve ağ kütüphaneleriyle** çalışır. Cross-Platform desteği sayesinde hem Kali Linux hem de Windows üzerinde sorunsuz koşturulabilir.

```bash
# Proje klasörüne gidin
cd ~/Desktop/Project-CrossLink

# Aracı çalıştırın
python3 src/scanner.py


📂 Proje Yapısı
Project-CrossLink/
│
├── src/
│   └── scanner.py          # Ana tarayıcı mimarisi, soket motoru, CVE sözlüğü ve CLI arayüzü.
│
├── logs/
│   ├── crosslink_report.json  # SIEM uyumlu otomatik üretilen JSON raporları.
│   └── crosslink_report.html  # Tarayıcı üzerinden incelenebilen görsel web raporu.
│
└── README.md               # Proje dokümantasyonu.


📊 Örnek Tarama Çıktısı (CLI)
[*] ICMP Canlılık Analizi Başlatıldı... Target: 10.158.146.1-254
----------------------------------------------------------------------
[✓] Canlı Cihaz Tespit Edildi: 10.158.146.165
----------------------------------------------------------------------
[+] Keşif Tamamlandı! 1 canlı cihaz bulundu. Süre: 3.02 sn.

[+] Port 22 AÇIK  -> Servis/Banner: SSH-2.0-OpenSSH_10.3p1 Debian-1
    ⚠️ [ZAFİYET TESPİT EDİLDİ] CVE-202X-1234
    ↳ Seviye: KRİTİK (Uzakta Kod Çalıştırma - RCE)
    ↳ Detay: Dropbear SSH servisinin bu sürümünde bellek taşması sonucu yetkisiz erişim sağlanabilir.

======================================================================
🛡️  PROJECT CROSSLINK - GÜVENLİK SIKILAŞTIRMA ÖNERİLERİ (REMEDIATION)
======================================================================
1. [CVE-202X-1234] - KRİTİK (Uzakta Kod Çalıştırma - RCE)
   👉 Çözüm: Cihazın üretici yazılımını (Firmware) güncelleyin veya SSH servisini tamamen kapatın.
======================================================================


Geliştirici: Abdulkadir Erkan (Kadir)

Sürüm: v1.3.0 (Nihai Akademik Güncelleme)

"Working while everyone is sleeping is building the future silently."


Dosyayı yapıştırdıktan sonra **`CTRL + O`**, **`ENTER`** ve **`CTRL + X`** ile kaydetip çık.

---

### 2. Adım: GitHub'a Gönder (Son Fırlatış 🚀)

Şimdi lokalde güncellediğimiz bu jilet gibi dokümanı GitHub reposuna pushlayalım:

```bash
git add README.md
git commit -m "Docs: Upgraded README.md to v1.3.0 with CVE, Remediation and HTML report specs"
git push origin main
