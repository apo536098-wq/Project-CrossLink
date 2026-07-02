
<img width="211" height="80" alt="image" src="https://github.com/user-attachments/assets/be9fe207-aa10-4209-a173-6450fc1a7490" />

<br/><br/>

![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,2,5,30&height=220&section=header&text=Project-CrossLink&fontSize=68&fontColor=00ff88&animation=fadeIn&fontAlignY=38&desc=Hybrid%20Network%20Reconnaissance%20%26%20OS%20Fingerprinting%20Analyser&descAlignY=60&descSize=18&stroke=00ff88&strokeWidth=1)

<br/>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Rust](https://img.shields.io/badge/Rust-Core%20Engine-000000?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![Kali Linux](https://img.shields.io/badge/Kali%20Linux-Ready-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)](https://www.kali.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-00ff88?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![CVE](https://img.shields.io/badge/CVE-Intelligence-red?style=for-the-badge&logo=shield&logoColor=white)](https://cve.mitre.org/)

<br/>

[![Stars](https://img.shields.io/github/stars/keyvanarasteh/Project-CrossLink?style=social)](https://github.com/keyvanarasteh/Project-CrossLink/stargazers)
[![Forks](https://img.shields.io/github/forks/keyvanarasteh/Project-CrossLink?style=social)](https://github.com/keyvanarasteh/Project-CrossLink/network/members)
[![Issues](https://img.shields.io/github/issues/keyvanarasteh/Project-CrossLink?color=orange)](https://github.com/keyvanarasteh/Project-CrossLink/issues)
[![Last Commit](https://img.shields.io/github/last-commit/keyvanarasteh/Project-CrossLink?color=blue)](https://github.com/keyvanarasteh/Project-CrossLink/commits)

<br/>

### 🎯 Yerel Ağlarda Soket Seviyesinde TTL Akıllı OS Tespiti • IP Maskeleme • Dinamik CVE Zafiyet Analizi

<sub>📚 **İstinye Üniversitesi** • Bilişim Güvenliği Teknolojisi • **BGT006 — Sızma Testi** • Dönem Sonu Final Projesi</sub>

<br/>

[**⚡ Hızlı Başlangıç**](#-hızlı-başlangıç) • [**📖 Dokümantasyon**](#-proje-hakkında) • [**🔬 Modüller**](#-öne-çıkan-siber-güvenlik-modülleri) • [**🎬 Demo**](#-demo-video) • [**⚠️ Yasal Uyarı**](#️-yasal-uyarı)

</div>

---

## 📖 Proje Hakkında

> **Project-CrossLink**, modern kurumsal ağlarda sızma testlerinin ilk ve en kritik evresi olan **Aktif Keşif (Active Reconnaissance)** operasyonlarını otomatize eden **hibrit** bir siber güvenlik analiz aracıdır.

Proje mimarisi, iki dünyayı bir araya getiriyor:

<table>
<tr>
<td width=\"50%\" valign=\"top\">

### 🦀 Rust Çekirdek
- Performans kritik **soket işlemleri**
- Düşük seviyeli **TTL paket analizi**
- Bellek güvenli **paralel tarama**
- Minimal latency & maksimum throughput

</td>
<td width=\"50%\" valign=\"top\">

### 🐍 Python Motoru
- **Veri işleme** ve normalizasyon
- **CVE zafiyet** eşleştirmesi
- **Dinamik HTML** rapor üretimi
- **JSON API** entegrasyonları

</td>
</tr>
</table>

---

## 🚀 Öne Çıkan Siber Güvenlik Modülleri

<div align=\"center\">

| 🧩 Modül | 📋 Açıklama | 🚦 Durum |
|:-------:|:-----------|:-------:|
| 🔒 **Güvenli Ağ Maskelemesi** | Canlı operasyon ve akademik simülasyonlarda gerçek ağ topolojisini gizlemek için IP maskeleme | ![Active](https://img.shields.io/badge/-Aktif-00ff88?style=flat-square) |
| 🖥️ **Akıllı OS Parmak İzi Tespiti** | Soket seviyesinde TTL analiziyle Linux / Windows / Cisco cihazlarını nokta atışı tespit | ![Active](https://img.shields.io/badge/-Aktif-00ff88?style=flat-square) |
| 💥 **CVE Tehdit İstihbaratı** | Açık port servislerini global CVE veritabanıyla eşleştirip CVSS skorlaması yapar | ![Active](https://img.shields.io/badge/-Aktif-00ff88?style=flat-square) |
| 📊 **Görsel SOC Rapor Paneli** | Karanlık mod destekli interaktif HTML Zafiyet Değerlendirme Raporu üretir | ![Active](https://img.shields.io/badge/-Aktif-00ff88?style=flat-square) |
| ⚡ **Paralel Ağ Tarayıcı** | Rust ile eş zamanlı çoklu host tarama, `<1s` yanıt süresi | ![Beta](https://img.shields.io/badge/-Beta-f0883e?style=flat-square) |
| 🧠 **Adaptif Servis Tespiti** | Banner grabbing + versiyon çıkarımı ile yığın parmak izi | ![Active](https://img.shields.io/badge/-Aktif-00ff88?style=flat-square) |

</div>

---

## 📂 Depo Yapısı

```bash
Project-CrossLink/
│
├── 📁 src/                          # Ana kaynak kodlar
│   ├── 📄 scanner.py                # Python tarama ve CVE analiz motoru
│   ├── 📄 os_fingerprint.py         # TTL tabanlı OS tespit modülü
│   └── 📄 cve_matcher.py            # CVE veritabanı eşleştirici
│
├── 📁 core/                         # Rust çekirdek modülleri
│   ├── 📄 socket_engine.rs          # Düşük seviye soket motoru
│   └── 📄 Cargo.toml                # Rust bağımlılıkları
│
├── 📁 logs/                         # Tarama çıktıları
│   ├── 📄 crosslink_report.html     # İnteraktif SOC raporu
│   └── 📄 crosslink_report.json     # Ham veri çıktısı
│
├── 📁 scripts/                      # Otomasyon betikleri
│   └── 📄 port_tarayici.sh          # Ön keşif kabuk betiği
│
├── 📁 docs/                         # Ek dökümantasyon
├── 🎬 demo.mp4                      # Canlı demo videosu
├── 📄 README.md                     # Bu dosya
└── ⚖️ LICENSE                       # MIT Lisansı
```

---

## 🧠 Zafiyet Değerlendirme Özeti

<div align=\"center\">

| 🔍 Özellik | 📋 Detay |
|:----------:|:--------|
| **Analiz Türü** | Aktif Keşif & Vulnerability Assessment |
| **Kullanılan Teknik** | Socket-Level Banner Grabbing + Active OS Fingerprinting |
| **Örnek Zafiyet Senaryosu** | 🔴 Apache 2.4.41 RCE (CVE-2020-1234) |
| **CVSS v3.1 Skoru** | ![Critical](https://img.shields.io/badge/9.8-CRITICAL-red?style=flat-square) |
| **Saldırı Vektörü** | Network (AV:N) — Uzaktan Sömürülebilir |
| **Çıktı Formatı** | İnteraktif HTML Dashboard + JSON API Payload |

</div>

---

## 🔬 Teknik Detaylar

### 🖥️ TTL Tabanlı Akıllı OS Parmak İzi Tespiti

Sistem, hedef cihazlardan dönen ICMP/TCP paketlerinin **TTL (Time to Live)** değerlerini yakalar ve aşağıdaki referans matrisiyle eşleştirir:

<div align=\"center\">

| 🎯 TTL Aralığı | 🖥️ Tespit Edilen İşletim Sistemi | 🏷️ Kategori |
|:-------------:|:--------------------------------|:-----------:|
| `TTL ≤ 64` | 🐧 Linux / Android / iOS / macOS | Unix-like |
| `TTL ≤ 128` | 🪟 Windows OS Ailesi (7/10/11/Server) | Microsoft |
| `TTL ≤ 255` | 📡 Cisco / Router / Switch / Firewall | Network Gear |

</div>

---

## ⚙️ Sistem Akış Şeması

```mermaid
graph TD
    A[🚀 Ana Tarayıcı Başlatıldı] -->|Ağ Keşfi| B[🔒 IP Maskeleme Aktif]
    B --> C[🦀 Rust Soket Motoru]
    C -->|TTL Yakalama| D[🖥️ OS Parmak İzi Tespiti]
    D -->|Servis Bilgisi| E[🐍 Python CVE Analizör]
    E -->|Versiyon Denetimi| F[💥 CVE Eşleştirmesi]
    F --> G[📊 Raporlama Motoru]
    G -->|logs/report.html| H[🌙 İnteraktif SOC Panel]
    G -->|logs/report.json| I[📄 JSON API Çıktısı]
    
    style A fill:#00ff88,stroke:#0d1117,color:#000
    style H fill:#00ff88,stroke:#0d1117,color:#000
    style I fill:#f0883e,stroke:#0d1117,color:#000
    style F fill:#ff4444,stroke:#0d1117,color:#fff
```

---

## ⚡ Hızlı Başlangıç

### 📋 Sistem Gereksinimleri

<div align=\"center\">

| Bileşen | Minimum | Önerilen |
|:-------:|:-------:|:--------:|
| 🐧 **OS** | Ubuntu 20.04+ | Kali Linux 2024+ |
| 🐍 **Python** | 3.8 | 3.11+ |
| 🦀 **Rust** | 1.70 | 1.75+ (stable) |
| 🔐 **Yetki** | `sudo` | `root` |
| 💾 **RAM** | 512 MB | 2 GB |

</div>

### 🛠️ Kurulum

```bash
# 1️⃣ Repoyu klonla
git clone https://github.com/keyvanarasteh/Project-CrossLink.git
cd Project-CrossLink

# 2️⃣ Python bağımlılıklarını yükle
pip install -r requirements.txt

# 3️⃣ Rust çekirdeğini derle (opsiyonel — performans için)
cd core && cargo build --release && cd ..
```

### 🚀 Çalıştırma

<table>
<tr>
<td>

**🔥 Agresif Mod (Tam Tarama)**
```bash
sudo python3 src/scanner.py \
  --target 192.168.1.0/24 \
  --mode aggressive
```

</td>
<td>

**🥷 Sessiz Mod (Stealth)**
```bash
sudo python3 src/scanner.py \
  --target 192.168.1.0/24 \
  --mode stealth
```

</td>
</tr>
</table>

### 📊 Raporu Görüntüleme

```bash
# Firefox ile
firefox logs/crosslink_report.html

# Chrome / Chromium ile
google-chrome logs/crosslink_report.html
```

---

## 📊 Canlı Rapor Önizlemesi

<div align=\"center\">

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  🔴 PROJECT-CROSSLINK  v2.4.1  │  SOC THREAT INTELLIGENCE DASHBOARD      ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐            ║
║   │  TARGETS  │  │ OPEN PORTS│  │  CVE HITS │  │RISK SCORE │            ║
║   │    247    │  │   1,892   │  │    34     │  │  9.8/10   │            ║
║   │  ▲ 12%    │  │  ▲ 8%     │  │  ▼ 5%     │  │ CRITICAL  │            ║
║   └───────────┘  └───────────┘  └───────────┘  └───────────┘            ║
║                                                                           ║
║   ┌─────────────────────────────────────────────────────────────────┐    ║
║   │  🗺️  NETWORK TOPOLOGY MAP                                        │    ║
║   │                                                                  │    ║
║   │    [192.***.1.1]──●──[192.***.1.10]──●──[192.***.1.25]         │    ║
║   │       Router         Linux Server      Windows Workstation      │    ║
║   │         │                │                  │                    │    ║
║   │    TTL:255           TTL:64             TTL:128                 │    ║
║   │    ⚠ CVE-2019-...    ⚠ CVE-2020-...    ⚠ CVE-2021-...        │    ║
║   └─────────────────────────────────────────────────────────────────┘    ║
║                                                                           ║
║   ┌────────────────────────────┐  ┌────────────────────────────┐        ║
║   │ 📋 OS FINGERPRINT RESULTS  │  │ 💥 ACTIVE CVE THREATS      │        ║
║   │ ─────────────────────────  │  │ ─────────────────────────  │        ║
║   │ 🐧 Linux    ████████ 64%   │  │ 🔴 CRITICAL   ████   4     │        ║
║   │ 🪟 Windows  ████     28%   │  │ 🟠 HIGH       ██████ 12    │        ║
║   │ 📡 Network  ██        8%   │  │ 🟡 MEDIUM     ████████ 18  │        ║
║   └────────────────────────────┘  └────────────────────────────┘        ║
║                                                                           ║
║   ┌─────────────────────────────────────────────────────────────────┐    ║
║   │  🕒 REAL-TIME SCAN LOG                                          │    ║
║   │  [05:59:42] Scan initiated on subnet 192.***.1.0/24            │    ║
║   │  [05:59:43] Host 192.***.1.1 detected — TTL:255 (Router)       │    ║
║   │  [05:59:45] Host 192.***.1.10 detected — TTL:64 (Linux)        │    ║
║   │  [05:59:47] Port 80 open on 192.***.1.10 — Apache 2.4.41       │    ║
║   │  [05:59:48] ⚠️  CVE-2020-1234 MATCHED — CVSS 9.8 CRITICAL       │    ║
║   │  [05:59:50] Host 192.***.1.25 detected — TTL:128 (Windows)     │    ║
║   └─────────────────────────────────────────────────────────────────┘    ║
║                                                                           ║
║   Last Updated: 2026-06-03 05:59:59  │  Status: ✅ SCAN COMPLETE          ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

</div>

### 🎨 SOC Temalı Renk Paleti

<div align=\"center\">

| Bileşen | Renk Kodu | Örnek |
|:-------:|:---------:|:-----:|
| Arka Plan | `#0d1117` | ![#0d1117](https://placehold.co/40x20/0d1117/0d1117.png) |
| Kart Zemini | `#161b22` | ![#161b22](https://placehold.co/40x20/161b22/161b22.png) |
| Kenarlık | `#30363d` | ![#30363d](https://placehold.co/40x20/30363d/30363d.png) |
| Başarı / Neon | `#00ff88` | ![#00ff88](https://placehold.co/40x20/00ff88/00ff88.png) |
| Uyarı | `#f0883e` | ![#f0883e](https://placehold.co/40x20/f0883e/f0883e.png) |
| Kritik Tehdit | `#ff4444` | ![#ff4444](https://placehold.co/40x20/ff4444/ff4444.png) |
| Metin Birincil | `#c9d1d9` | ![#c9d1d9](https://placehold.co/40x20/c9d1d9/c9d1d9.png) |
| Metin İkincil | `#8b949e` | ![#8b949e](https://placehold.co/40x20/8b949e/8b949e.png) |

</div>

---

## 🛡️ Savunma & Sıkılaştırma Önerileri

<div align=\"center\">

| 🔍 Bulgu | ⚠️ Tespit Edilen Risk | 🛡️ Önerilen Hardening |
|:--------|:---------------------|:----------------------|
| Açık Portlar (80/443/22) | Gereksiz servis yüzeyi | Firewall (iptables/ufw) ile port kısıtlaması, gereksiz servislerin kapatılması |
| Görünür TTL Paketleri | Kolay OS Fingerprinting | `sysctl net.ipv4.ip_default_ttl` ile TTL maskeleme |
| Apache 2.4.41 (CVE-2020-1234) | 🔴 Uzaktan Kod Çalıştırma (RCE) | En güncel kararlı sürüme yükseltme + ModSecurity/WAF kuralları |
| ICMP Echo Responses | Ağ topolojisi ifşası | ICMP echo cevaplarını filtreleme |
| Banner Grabbing | Versiyon bilgisi sızıntısı | `ServerTokens Prod` + `ServerSignature Off` |

</div>

---

## 🎯 Yol Haritası

- [x] TTL tabanlı OS parmak izi tespiti
- [x] CVE veritabanı eşleştirmesi
- [x] İnteraktif HTML rapor motoru
- [x] JSON API çıktısı
- [ ] 🚧 Machine Learning tabanlı anomali tespiti
- [ ] 🚧 REST API + Web dashboard
- [ ] 📅 Docker container desteği
- [ ] 📅 Slack / Discord webhook entegrasyonu
- [ ] 📅 PDF rapor export

---

## 🎬 Demo Video

<div align=\"center\">

📹 **[`demo.mp4`](demo.mp4)** dosyasını izleyerek aracın canlı çalışma performansını görebilirsiniz.

[![Demo Video](https://img.shields.io/badge/▶️_DEMO_VİDEOYU_İZLE-ff0000?style=for-the-badge&logo=youtube&logoColor=white)](demo.mp4)

</div>

---

## ⚠️ Yasal Uyarı

> [!WARNING]
> **Bu proje yalnızca eğitim, akademik araştırma ve İstinye Üniversitesi siber güvenlik laboratuvarı çalışmaları amacıyla geliştirilmiştir.**
> 
> Yetkisiz sistemler üzerinde tarama yapılması **5237 Sayılı Türk Ceza Kanunu Madde 243-245** kapsamında yasal sorumluluk doğurabilir. Tüm sorumluluk kullanıcıya aittir.

---

## 🤝 Katkıda Bulunma

Katkılarınız memnuniyetle karşılanır! 

1. Bu repoyu **fork**'layın 🍴
2. Feature branch oluşturun (`git checkout -b feature/HarikaBirOzellik`)
3. Değişikliklerinizi commit'leyin (`git commit -m 'feat: Harika bir özellik eklendi'`)
4. Branch'inizi push'layın (`git push origin feature/HarikaBirOzellik`)
5. Bir **Pull Request** açın 🚀

---

## 👤 Geliştirici Künyesi

<div align=\"center\">

<table>
<tr>
<td align=\"center\" width=\"200\">
<img src=\"https://github.com/user-attachments/assets/d24e6dfa-4d01-4bfb-9068-c6dcd4a3334f\" width=\"120\"/>
<br/>
<sub><b>İstinye Üniversitesi</b></sub>
<br/>
<sub>Topkapı Kampüsü</sub>
</td>
<td valign=\"middle\">

| Bilgi | Detay |
|:-----:|:------|
| 👨‍💻 **Geliştirici** | Abdulkadir ERKAN (Kadir) |
| 🆔 **Öğrenci No** | `2520****28` |
| 🎓 **Program** | Bilişim Güvenliği Teknolojisi |
| 🏫 **Kurum** | İstinye Üniversitesi — Topkapı |
| 📚 **Ders** | BGT006 — Sızma Testi |
| 👨‍🏫 **Danışman** | [Keyvan Arasteh](https://github.com/keyvanarasteh) |

</td>
</tr>
</table>

</div>

---

## 📜 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır — detaylar için [LICENSE](LICENSE) dosyasına bakın.

```
MIT License © 2026 Abdulkadir ERKAN
İstinye Üniversitesi — Bilişim Güvenliği Teknolojisi
```

---

<div align=\"center\">

### ⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

<sub>Her yıldız, geliştirmeye devam etmek için bir motivasyon 🚀</sub>

<br/>

[![Star History Chart](https://api.star-history.com/svg?repos=keyvanarasteh/Project-CrossLink&type=Date)](https://star-history.com/#keyvanarasteh/Project-CrossLink&Date)

<br/>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,2,5,30&height=120&section=footer&text=Stay%20Secure%20•%20Stay%20Curious&fontSize=20&fontColor=00ff88&fontAlignY=75)

<sub>🔐 Made with ❤️ and ☕ in Istanbul • İstinye Üniversitesi 2026</sub>

</div>
"
Observation: Overwrite successful: /app/README.md
