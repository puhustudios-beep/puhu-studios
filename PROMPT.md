Referanslar (incele ve benzerini üret)

Ana sayfa: https://www.dreamgames.com

Games sayfası: https://www.dreamgames.com/games

Not: Tasarım ve düzen “aynı hissiyat + aynı akış” olacak; metinleri ve görselleri 1:1 kopyalama, bana özgün placeholder içerik üret.

Hedef

Dream Games’in (home + games) yapısını ve görsel dilini yakalayan, 2 sayfalı modern bir web sitesi üret:

index.html (Home)

games.html (Games)

Kodlar statik olacak (framework yok). Placeholder görseller free kaynaklardan (ör. Unsplash) gelsin; ben sonra değiştireceğim.

Bilgi Mimarisi / Navigasyon (birebir aynı mantık)

Header’da üst menü şu ana kategorileri içerecek:

ABOUT US → alt linkler: Offices, News

GAMES → alt linkler: Game 1, Game 2 (Dream’de Royal Match / Royal Kingdom)

CAREERS → alt linkler: Life at Dream, Summer Internship, Open Positions

Menü hover ile açılan dropdown gibi çalışsın (mobilde hamburger menü).
Menü linkleri sayfa içi anchor + sayfalar arası link kombinasyonu ile çalışsın.

Home Sayfa (index.html) Yapısı (Dream ana sayfa akışı)

A) Hero (üst açılış alanı)

Büyük başlık + kısa açıklama + bir CTA butonu (ör. “Learn More” benzeri)

Sağda/arkada büyük bir görsel (placeholder)

B) ABOUT US bölümü

Başlık: “ABOUT US”

1–2 paragraf kısa tanıtım (özgün placeholder metin)

“Learn More” link/buton hissi

C) OUR GAMES bölümü

Başlık: “OUR GAMES”

Kısa açıklama + iki oyun ismi/mini kart (Game 1 / Game 2)

“Explore Games” butonu → games.html

D) CAREERS bölümü

Başlık: “CAREERS”

Kısa açıklama + “Explore Careers” CTA hissi

E) Footer
Footer’da şu öğeler olmalı:

İletişim e-postası satırı (Dream’de info@dreamgames.com
)

Copyright satırı (Dream’de “© 2026 Dream Games”)

Linkler: Terms of Service, Privacy Policy, Statements, ayrıca “Cookie Settings” metni

Not: Linkler placeholder olabilir ama isimleri ve yerleşimi aynı mantıkta olsun.

Games Sayfa (games.html) Yapısı (Dream /games akışı)

A) Sayfa Hero

Başlık: “Our Games”

Altında kısa tagline (Dream’de “Royal Universe” anlatımı var; sen özgün placeholder yaz)

B) Oyun Liste Alanı (2 kart)
İki büyük oyun bölümü/kartı:

Kart 1: Game 1

Büyük görsel

Kısa açıklama

“Learn More” butonu (istersen oyun detaya gitsin; şimdilik placeholder)

Kart 2: Game 2

Büyük görsel

Kısa açıklama

“Learn More” butonu

C) Footer
Home ile aynı footer yapısı

Stil / UI (Dream hissiyatı)

Minimal, premium, bol boşluklu (whitespace)

Koyu zemin + yumuşak gradient/glow efektleri (abartmadan)

Büyük başlık tipografisi, temiz sans-serif

Kartlarda hafif border + blur/backdrop hissi (glassmorphism çok hafif)

Hover animasyonları (kart yükselme, link underline vs.)

Scroll reveal gibi basit bir animasyon olabilir (IntersectionObserver)

Teknik Gereksinimler

Dosya yapısı:

index.html

games.html

assets/styles.css

assets/script.js

Sadece vanilla HTML/CSS/JS

Tam responsive (desktop/tablet/mobil)

Erişilebilirlik: doğru heading hiyerarşisi, alt text, aria-label, klavye ile menü erişimi

Placeholder görseller: Unsplash (veya benzeri free)

Kod çıktısını eksiksiz ver: her dosyanın içeriği ayrı başlık altında.

Çıktı Formatı

Aşağıdaki sırayla üret:

index.html (tam kod)

games.html (tam kod)

assets/styles.css (tam kod)

assets/script.js (tam kod)