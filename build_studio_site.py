import json
import os

languages = {
    "en": {
        "title": "AE Interactive | Crafting Premium Digital Experiences",
        "nav_apps": "Apps",
        "nav_philosophy": "Philosophy",
        "nav_contact": "Contact",
        "hero_headline": "Crafting Premium<br>Digital Experiences",
        "hero_sub": "An independent studio dedicated to native iOS performance, uncompromising privacy, and zero distractions.",
        "apps_title": "Our Apps",
        "app1_tag": "FLAGSHIP",
        "app1_title": "Workout Timer",
        "app1_subtitle": "Voice Coach",
        "app1_desc": "The ultimate high-intensity interval timer featuring real studio voice coaches, Apple Watch sync, and 100% offline privacy.",
        "btn_appstore": "Learn More",
        "phil_title": "Our Philosophy",
        "phil_1_title": "100% Privacy",
        "phil_1_desc": "No accounts. No ads. No trackers. Your data stays on your device.",
        "phil_2_title": "Native Performance",
        "phil_2_desc": "Built purely with Swift for maximum hardware efficiency and seamless OS integration like Dynamic Island.",
        "phil_3_title": "Global First",
        "phil_3_desc": "We build for the world. Multilingual support and localized experiences from day one.",
        "phil_4_title": "Zero Distractions",
        "phil_4_desc": "We respect your focus. Clean interfaces designed solely to solve your problems.",
        "footer_rights": "© 2026 AE Interactive. All rights reserved."
    },
    "zh-Hant": {
        "title": "AE Interactive | 打造極致數位互動體驗",
        "nav_apps": "產品",
        "nav_philosophy": "理念",
        "nav_contact": "聯絡我們",
        "hero_headline": "打造極致的<br>數位互動體驗",
        "hero_sub": "專注於 iOS 原生效能、絕對隱私與零干擾設計的獨立開發團隊。",
        "apps_title": "旗下產品",
        "app1_tag": "主打產品",
        "app1_title": "Workout Timer",
        "app1_subtitle": "真人語音健身計時",
        "app1_desc": "次世代高強度間歇計時器，搭載多國語言錄音室真人教練、Apple Watch 同步與 100% 離線隱私。",
        "btn_appstore": "了解更多",
        "phil_title": "核心理念",
        "phil_1_title": "100% 絕對隱私",
        "phil_1_desc": "免註冊、無廣告、無追蹤器。您的健康數據絕對保密，僅存於設備本機。",
        "phil_2_title": "原生流暢效能",
        "phil_2_desc": "純 Swift 原生打造，完美整合動態島與 iOS 最新硬體加速技術。",
        "phil_3_title": "生而全球化",
        "phil_3_desc": "從第一天起就支援多國語系，為全球使用者打造深度的在地化體驗。",
        "phil_4_title": "零干擾設計",
        "phil_4_desc": "我們尊重您的專注力。拒絕彈窗疲勞，專注於解決痛點的純淨介面。",
        "footer_rights": "© 2026 AE Interactive. 保留所有權利。"
    },
    "zh-Hans": {
        "title": "AE Interactive | 打造极致数字互动体验",
        "nav_apps": "产品",
        "nav_philosophy": "理念",
        "nav_contact": "联系我们",
        "hero_headline": "打造极致的<br>数字互动体验",
        "hero_sub": "专注于 iOS 原生性能、绝对隐私与零干扰设计的独立开发团队。",
        "apps_title": "旗下产品",
        "app1_tag": "主打产品",
        "app1_title": "Workout Timer",
        "app1_subtitle": "真人语音健身计时",
        "app1_desc": "次世代高强度间歇计时器，搭载多国语言录音室真人教练、Apple Watch 同步与 100% 离线隐私。",
        "btn_appstore": "了解更多",
        "phil_title": "核心理念",
        "phil_1_title": "100% 绝对隐私",
        "phil_1_desc": "免注册、无广告、无追踪器。您的健康数据绝对保密，仅存于设备本机。",
        "phil_2_title": "原生流畅性能",
        "phil_2_desc": "纯 Swift 原生打造，完美整合灵动岛与 iOS 最新硬件加速技术。",
        "phil_3_title": "生而全球化",
        "phil_3_desc": "从第一天起就支持多国语系，为全球使用者打造深度的本地化体验。",
        "phil_4_title": "零干扰设计",
        "phil_4_desc": "我们尊重您的注意力。拒绝弹窗疲劳，专注于解决痛点的纯净界面。",
        "footer_rights": "© 2026 AE Interactive. 保留所有权利。"
    },
    "es": {
        "title": "AE Interactive | Creando Experiencias Digitales Premium",
        "nav_apps": "Apps",
        "nav_philosophy": "Filosofía",
        "nav_contact": "Contacto",
        "hero_headline": "Creando Experiencias<br>Digitales Premium",
        "hero_sub": "Un estudio independiente dedicado al rendimiento nativo de iOS, la privacidad sin compromisos y cero distracciones.",
        "apps_title": "Nuestras Apps",
        "app1_tag": "DESTACADO",
        "app1_title": "Workout Timer",
        "app1_subtitle": "Voice Coach",
        "app1_desc": "El temporizador de intervalos definitivo con entrenadores de voz reales, sincronización con Apple Watch y privacidad 100% offline.",
        "btn_appstore": "Saber Más",
        "phil_title": "Nuestra Filosofía",
        "phil_1_title": "100% Privacidad",
        "phil_1_desc": "Sin cuentas. Sin anuncios. Sin rastreadores. Tus datos se quedan en tu dispositivo.",
        "phil_2_title": "Rendimiento Nativo",
        "phil_2_desc": "Desarrollado puramente con Swift para la máxima eficiencia de hardware y Dynamic Island.",
        "phil_3_title": "Global desde el inicio",
        "phil_3_desc": "Construimos para el mundo. Soporte multilingüe y experiencias localizadas.",
        "phil_4_title": "Cero Distracciones",
        "phil_4_desc": "Respetamos tu concentración. Interfaces limpias diseñadas solo para resolver tus problemas.",
        "footer_rights": "© 2026 AE Interactive. Todos los derechos reservados."
    }
}

html_template = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{t[title]}</title>
  <meta name="description" content="{t[hero_sub]}">
  
  <!-- Canonical & Multilingual SEO -->
  <link rel="canonical" href="https://appengine.fun/?lang={lang_code}">
  <link rel="alternate" hreflang="en" href="https://appengine.fun/?lang=en">
  <link rel="alternate" hreflang="zh-Hant" href="https://appengine.fun/?lang=zh-Hant">
  <link rel="alternate" hreflang="zh-Hans" href="https://appengine.fun/?lang=zh-Hans">
  <link rel="alternate" hreflang="es" href="https://appengine.fun/?lang=es">
  <link rel="alternate" hreflang="x-default" href="https://appengine.fun/">

  <!-- Open Graph / Social Media Sharing -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="AE Interactive">
  <meta property="og:url" content="https://appengine.fun/?lang={lang_code}">
  <meta property="og:title" content="{t[title]}">
  <meta property="og:description" content="{t[hero_sub]}">
  <meta property="og:image" content="https://appengine.fun/images/brand_logo_v2.png">
  <meta property="og:image:width" content="707">
  <meta property="og:image:height" content="592">
  <meta property="og:image:alt" content="AE Interactive Logo">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{t[title]}">
  <meta name="twitter:description" content="{t[hero_sub]}">
  <meta name="twitter:image" content="https://appengine.fun/images/brand_logo_v2.png">
  
  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "AE Interactive",
    "url": "https://appengine.fun/?lang={lang_code}",
    "logo": "https://appengine.fun/images/brand_logo_v2.png",
    "description": "{t[hero_sub]}",
    "owns": [
      {{
        "@type": "SoftwareApplication",
        "name": "Workout Timer",
        "url": "https://workout.appengine.fun/?lang={lang_code}",
        "applicationCategory": "HealthAndFitnessApplication",
        "operatingSystem": "iOS, watchOS",
        "offers": {{
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "USD"
        }}
      }}
    ]
  }}
  </script>
  <meta name="description" content="{t[hero_sub]}">
  <style>
    :root {{
      --bg-color: #000000;
      --card-bg: #1c1c1e;
      --text-main: #f5f5f7;
      --text-muted: #86868b;
      --primary-green: #30d158;
      --accent-blue: #0a84ff;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-main);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}
    a {{ text-decoration: none; color: inherit; }}
    
    /* Navbar */
    nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 40px;
      position: fixed;
      top: 0; width: 100%;
      background: rgba(0,0,0,0.8);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      z-index: 100;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }}
    .logo {{
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.5px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .nav-links {{ display: flex; gap: 30px; }}
    .nav-links a {{ font-size: 14px; font-weight: 500; color: var(--text-muted); transition: color 0.3s; }}
    .nav-links a:hover {{ color: var(--text-main); }}

    /* Hero */
    .hero {{
      padding: 180px 24px 100px;
      text-align: center;
      max-width: 900px;
      margin: 0 auto;
    }}
    .hero h1 {{
      font-size: clamp(48px, 8vw, 80px);
      font-weight: 800;
      line-height: 1.05;
      letter-spacing: -2px;
      margin-bottom: 24px;
      background: linear-gradient(135deg, #fff 0%, #a1a1a6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero p {{
      font-size: 21px;
      color: var(--text-muted);
      max-width: 600px;
      margin: 0 auto;
    }}

    /* Container */
    .container {{
      max-width: 1000px;
      margin: 0 auto;
      padding: 0 24px 120px;
    }}
    .section-title {{
      font-size: 32px;
      font-weight: 700;
      margin-bottom: 40px;
      text-align: center;
    }}

    /* Apps Showcase */
    .app-card {{
      background: var(--card-bg);
      border-radius: 32px;
      padding: 60px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      border: 1px solid rgba(255,255,255,0.05);
      position: relative;
      overflow: hidden;
      margin-bottom: 80px;
    }}
    .app-card::before {{
      content: '';
      position: absolute;
      top: -50%; left: -50%;
      width: 200%; height: 200%;
      background: radial-gradient(circle at top, rgba(48,209,88,0.1) 0%, transparent 50%);
      pointer-events: none;
    }}
    .tag {{
      background: rgba(48,209,88,0.2);
      color: var(--primary-green);
      font-size: 12px;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: 20px;
      margin-bottom: 20px;
      letter-spacing: 1px;
    }}
    .app-title {{ font-size: 40px; font-weight: 800; margin-bottom: 8px; }}
    .app-subtitle {{ font-size: 24px; font-weight: 600; color: var(--text-muted); margin-bottom: 24px; }}
    .app-desc {{ font-size: 18px; color: var(--text-muted); max-width: 580px; margin: 0 auto 40px auto; text-align: left; line-height: 1.6; }}
    .btn {{
      background: var(--text-main);
      color: var(--bg-color);
      padding: 16px 32px;
      border-radius: 30px;
      font-weight: 600;
      font-size: 16px;
      transition: transform 0.2s, opacity 0.2s;
      display: inline-block;
    }}
    .btn:hover {{ transform: scale(1.02); opacity: 0.9; }}

    /* Bento Grid (Philosophy) */
    .bento-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
    }}
    .bento-card {{
      background: var(--card-bg);
      border-radius: 24px;
      padding: 40px;
      border: 1px solid rgba(255,255,255,0.05);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      min-height: 250px;
    }}
    .bento-card h3 {{ font-size: 24px; font-weight: 700; margin-bottom: 12px; }}
    .bento-card p {{ color: var(--text-muted); font-size: 16px; }}
    .bento-icon {{ font-size: 40px; margin-bottom: auto; }}

    /* Footer */
    footer {{
      border-top: 1px solid rgba(255,255,255,0.1);
      padding: 60px 40px;
      text-align: center;
      color: var(--text-muted);
      font-size: 14px;
    }}

    @media (max-width: 768px) {{
      nav {{ padding: 16px 24px; }}
      .nav-links {{ display: none; }}
      .bento-grid {{ grid-template-columns: 1fr; }}
      .app-card {{ padding: 40px 24px; }}
    }}
  </style>
</head>
<body>
  <nav>
    <a href="/" class="logo" style="display: flex; align-items: center; gap: 12px; text-decoration: none;">
      <img src="/images/brand_icon_v2.png" alt="AE Interactive" style="height: 36px; width: auto; object-fit: contain;">
      <span style="font-size: 19px; font-weight: 800; letter-spacing: -0.4px; color: #ffffff;">AE Interactive</span>
    </a>
    <div class="nav-right" style="display: flex; align-items: center; gap: 30px;">
      <div class="nav-links">
        <a href="#apps">{t[nav_apps]}</a>
        <a href="#philosophy">{t[nav_philosophy]}</a>
        <a href="mailto:support@appengine.fun">{t[nav_contact]}</a>
      </div>
      <div class="lang-picker" style="display: flex; gap: 12px; font-size: 13px; font-weight: 600;">
        <a href="/?lang=en" style="color: {c_en}; text-decoration: none;">EN</a>
        <a href="/?lang=zh-Hant" style="color: {c_zh_hant}; text-decoration: none;">繁中</a>
        <a href="/?lang=zh-Hans" style="color: {c_zh_hans}; text-decoration: none;">简中</a>
        <a href="/?lang=es" style="color: {c_es}; text-decoration: none;">ES</a>
      </div>
    </div>
  </nav>

  <section class="hero">
    <div style="display: flex; justify-content: center; margin-bottom: 32px;">
        <img src="/images/brand_logo_v2.png" alt="AE Interactive Logo" style="height: 140px; width: auto; filter: drop-shadow(0 0 35px rgba(48,209,88,0.45));">
    </div>
    <h1>{t[hero_headline]}</h1>
    <p>{t[hero_sub]}</p>
  </section>

  <div class="container" id="apps">
    <div class="section-title">{t[apps_title]}</div>
    
    <a href="https://workout.appengine.fun/?lang={lang_code}" class="app-card" style="text-decoration: none; display: block; color: inherit; cursor: pointer; transition: transform 0.2s ease;">
      <div class="tag">{t[app1_tag]}</div>
      <div class="app-title">{t[app1_title]}</div>
      <div class="app-subtitle">{t[app1_subtitle]}</div>
      <p class="app-desc">{t[app1_desc]}</p>
      <div class="btn">{t[btn_appstore]}</div>
    </a>
  </div>

  <div class="container" id="philosophy">
    <div class="section-title">{t[phil_title]}</div>
    <div class="bento-grid">
      <div class="bento-card">
        <div class="bento-icon">🔒</div>
        <h3>{t[phil_1_title]}</h3>
        <p>{t[phil_1_desc]}</p>
      </div>
      <div class="bento-card">
        <div class="bento-icon">⚡️</div>
        <h3>{t[phil_2_title]}</h3>
        <p>{t[phil_2_desc]}</p>
      </div>
      <div class="bento-card">
        <div class="bento-icon">🌍</div>
        <h3>{t[phil_3_title]}</h3>
        <p>{t[phil_3_desc]}</p>
      </div>
      <div class="bento-card">
        <div class="bento-icon">💎</div>
        <h3>{t[phil_4_title]}</h3>
        <p>{t[phil_4_desc]}</p>
      </div>
    </div>
  </div>

  <footer>
    {t[footer_rights]}
  </footer>
</body>
</html>"""

os.makedirs("public", exist_ok=True)


gtm_head = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-W7N52ZML');</script>
<!-- End Google Tag Manager -->"""

gtm_body = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W7N52ZML"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

def gen_html(lang):
    c_en = 'var(--text-main)' if lang == 'en' else 'var(--text-muted)'
    c_zh_hant = 'var(--text-main)' if lang == 'zh-Hant' else 'var(--text-muted)'
    c_zh_hans = 'var(--text-main)' if lang == 'zh-Hans' else 'var(--text-muted)'
    c_es = 'var(--text-main)' if lang == 'es' else 'var(--text-muted)'
    rendered = html_template.format(lang_code=lang, t=languages[lang], c_en=c_en, c_zh_hant=c_zh_hant, c_zh_hans=c_zh_hans, c_es=c_es)
    rendered = rendered.replace("<head>", f"<head>\n  {gtm_head}", 1)
    rendered = rendered.replace("<body>", f"<body>\n  {gtm_body}", 1)
    return rendered

with open("public/index.html", "w", encoding="utf-8") as f: f.write(gen_html("en"))
with open("public/index_zh-Hant.html", "w", encoding="utf-8") as f: f.write(gen_html("zh-Hant"))
with open("public/index_zh-Hans.html", "w", encoding="utf-8") as f: f.write(gen_html("zh-Hans"))
with open("public/index_es.html", "w", encoding="utf-8") as f: f.write(gen_html("es"))

print("Generated studio website templates with GTM-W7N52ZML.")

