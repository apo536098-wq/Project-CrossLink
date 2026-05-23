# Project CrossLink 🛰️ (v1.3.0 - Akademik Sürüm)

Project CrossLink; yerel ağ (LAN) üzerindeki aktif cihazları otomatik olarak tespit etmek, bu cihazların üzerinde çalışan kritik servisleri soket seviyesinde analiz etmek, bilinen zafiyetlerle (CVE) eşleştirmek ve defansif sıkılaştırma önerileriyle birlikte siber güvenlik standartlarında raporlamak için geliştirilmiş bağımsız bir **Aktif Keşif ve Zafiyet Tarama (Reconnaissance & Vulnerability Assessment) Framework'üdür.**

---

## 📝 1. BÖLÜM: PROJENİN ÖZETİ VE SİBER GÜVENLİK MANTIĞI

Bu proje, bir sızma testinde (Pentest) siber güvenlik uzmanlarının attığı ilk ve en kritik iki adımı (Keşif ve Zafiyet Tarama) harici hiçbir siber güvenlik aracına (Nmap, Masscan vb.) bağımlı olmadan gerçekleştirir. Hocanın istediği gibi çorba bir kod yapısında değil; **bölüm bölüm, kısa parçalara ayrılmış modüler bir mimariye sahiptir:**

1. **Modül - Hızlı Ağ Keşfi (Host Discovery):** Çalıştırıldığı bilgisayarın yerel ağ IP bloğunu otomatik tespit eder ve `ThreadPoolExecutor` (Multi-threading) mimarisi sayesinde 254 farklı IP'ye aynı anda asenkron ping fırlatır. Tüm ağı sadece 3 saniyede haritalandırır.
2. **Modül - Port & Servis Analizi (Banner Grabbing):** Canlı cihazların kritik kapılarını (SSH, HTTP, UPnP) saf Python soketleriyle çalar. TCP el sıkışması kurarak içeride çalışan servisin imza bilgisini (Banner) çeker (Örn: `OpenSSH_10.3p1`).
3. **Modül - Lokal CVE Analiz Motoru:** Çekilen servis sürüm bilgisini kodun içindeki gömülü "Sabıka Kaydı Sözlüğü" ile kıyaslar. Sürüm açığıyla eşleşirse resmi siber güvenlik açığını (**CVE Kodunu**) ve risk seviyesini (Kritik/Yüksek) anında teşhis eder.
4. **Modül - Defansif Çözüm & Raporlama (Remediation):** Açığı bulduktan sonra ağ yöneticisine "Güvenlik Sıkılaştırma Önerisi" sunar. Bulguları SIEM log sistemlerine uygun JSON formatında ve tarayıcıda açılabilen jilet gibi bir HTML raporuna dönüştürür.

---

## 📊 2. BÖLÜM: OPERASYONEL AKIŞ DİYAGRAMI (OPERATIONAL FLOWCHART)

Aşağıdaki şema, framework çalıştırıldığında arka planda dönen siber güvenlik operasyonunun modüler akış mimarisini göstermektedir:

```text
[ Başlangıç: python3 src/scanner.py ]
                  │
                  ▼
┌───────────────────────────────────────────────┐
│       1. MODÜL: HIZLI AĞ KEŞFİ (ICMP)         │
│  - Lokal IP Bloğunu Otomatik Tespit Et        │
│  - ThreadPoolExecutor ile Asenkron Ping At    │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
            [ Canlı Cihazlar Bulundu mu? ]
                  ├──► (Hayır) ──► [ Hata Bas & Menüye Dön ]
                  └──► (Evet)
                        │
                        ▼
┌───────────────────────────────────────────────┐
│     2. MODÜL: SERVİS KAPILARI (PORT SCAN)     │
│  - Kritik IoT Portlarına Soket Seviyesinde Bağlan│
│  - TCP El Sıkışması ile Banner Grabbing Yap    │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│     3. MODÜL: LOKAL CVE ANALİZ MOTORU         │
│  - Çekilen Banner Bilgisini Sözlükle Kıyasla  │
│  - Sürüm Açıklarını (CVE-2026) Teşhis Et       │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│   4. MODÜL: DEFANSİF ÇÖZÜM & RAPORLAMA        │
│  - Hardening (Güvenlik Sıkılaştırma) Önerisi Üret│
│  - logs/crosslink_report.json (SIEM Uyumlu)   │
│  - logs/crosslink_report.html (Görsel Rapor)  │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
[ Bitiş: Raporları Tarayıcıda Aç & GitHub'a Pushla ]

🛠️ 3. BÖLÜM: KURULUM VE ÇALIŞTIRMA
Proje hiçbir harici kütüphaneye veya bağımlılığa ihtiyaç duymadan, tamamen Python'ın yerel soket, alt süreç ve ağ kütüphaneleriyle çalışır.

# Proje klasörüne gidin
cd ~/Desktop/Project-CrossLink

# Aracı çalıştırın
python3 src/scanner.py


📂 4. BÖLÜM: PROJE YAPISI

Project-CrossLink/
│
├── src/
│   └── scanner.py          # Ana tarayıcı mimarisi, soket motoru, CVE sözlüğü ve CLI arayüzü.
│
├── logs/
│   ├── crosslink_report.json  # SIEM uyumlu otomatik üretilen JSON raporları.
│   └── crosslink_report.html  # Tarayıcı üzerinden incelenebilen görsel web raporu.
│
└── README.md               # Proje konusu, operasyonel akış diyagramı ve dokümantasyon.


**Geliştirici:** Abdulkadir Erkan (Kadir)  
**Sürüm:** v1.3.0 (NetForge-RTC Final Projesi Teslimi)  
**Akademik Dönem:** 2025-2026 Bahar Yarıyılı Final Ödevi  


