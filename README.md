# Project CrossLink 🛰️

Project CrossLink, yerel ağ (LAN) üzerindeki **Xiaomi, Vela ve HyperOS** tabanlı akıllı cihazları ve IoT sistemlerini otomatik olarak tespit etmek, bu cihazların üzerinde çalışan kritik servisleri analiz etmek ve bulguları siber güvenlik standartlarında raporlamak için geliştirilmiş bağımsız bir **Aktif Keşif ve Zafiyet Tarama (Reconnaissance) Framework**'üdür.

## 🚀 Özellikler
* **Aktif SSDP Keşfi:** Ağ katmanına çoklu gönderim (Multicast - 239.255.255.250:1900) sorguları fırlatarak akıllı cihazları milisaniyeler içinde tespit eder.
* **Akıllı Cihaz Analizi:** Gelen ham paket verilerinden imza analizi (Fingerprinting) yaparak hedef cihazın işletim sistemini doğrular.
* **Otomatik Port & Servis Taraması:** Keşfedilen cihazlara yönelik en kritik IoT portlarını (SSH, HTTP, HTTPS, UPnP, Yönetim Panelleri) soket seviyesinde tarar.
* **Banner Grabbing:** Açık portlardaki servislerin sürüm ve başlık bilgilerini yakalar.
* **SIEM Uyumlu Raporlama:** Tüm tarama süreçlerini ve bulguları `logs/crosslink_report.json` dosyasına merkezi log yönetim sistemlerinin okuyabileceği formatta kaydeder.
* **İnteraktif CLI Arayüzü:** Kullanıcı dostu terminal menüsü ve grafiksel rapor okuyucusu içerir.

## 🛠️ Kurulum ve Çalıştırma
Proje hiçbir harici kütüphaneye (Nmap vb.) ihtiyaç duymadan, tamamen Python'ın yerel soket ve ağ kütüphaneleriyle çalışır.

```bash
# Proje klasörüne gidin
cd ~/Desktop/Project-CrossLink

# Aracı çalıştırın
python3 src/scanner.py

📂 Proje Yapısı
src/scanner.py - Ana tarayıcı mimarisi, soket motoru ve CLI menüsü.

logs/crosslink_report.json - Otomatik üretilen tarama ve keşif raporları.

logs/nmap_report.txt - Manuel doğrulama ve analiz raporu.

Geliştirici: Abdulkadir Erkan (Kadir)

Sürüm: v1.2.0 (Nihai)

"Working while everyone is sleeping is building the future silently."


---

### 3. ADIM: GitHub'a Son Fırlatış 🚀
Şimdi bu dosyayı da güvenli SSH hattımız üzerinden GitHub'a gönderip projeye son noktayı koyalım:

```bash
git add README.md
git commit -m "Docs: Added professional README documentation"
git push
