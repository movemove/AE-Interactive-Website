import json
import os

languages = {
    "en": {
        "title": "AE Interactive | Crafting Premium Digital Experiences",
        "nav_apps": "Apps",
        "nav_philosophy": "Philosophy",
        "nav_contact": "Contact",
        "hero_headline": "Crafting Premium<br>Digital Experiences",
        "hero_sub": "An independent studio dedicated to native Apple ecosystem performance, uncompromising privacy, and zero distractions.",
        "apps_title": "Our Flagship Ecosystem",
        "app1_tag": "FLAGSHIP • V1.3.1 UNIVERSAL PURCHASE",
        "app1_title": "Workout Timer",
        "app1_subtitle": "Voice Coach & Apple TV 4K Gym Clock",
        "app1_desc": "The ultimate high-intensity interval timer across iPhone, iPad, Apple Watch, and Apple TV 4K. Featuring 5 studio-recorded voice coaches, 7 guided coach video programs with UP NEXT rest previews, AirPods Pro & Apple Watch live heart rate sync, and 100% offline privacy.",
        "btn_website": "Explore Website",
        "btn_appstore": " App Store",
        "btn_video_hannah": "▶ Coach Hannah Promo",
        "btn_video_elena": "▶ Dr. Elena Promo",
        "vid_section_label": "NEW 1080P COACH PROMO SHOWCASE",
        "vid_1_title": "Coach Hannah Lin • 10-Min Core Abs + Box Breathing",
        "vid_2_title": "Dr. Elena Lindqvist, DPT • 12-Min Clinical Core (No Neck Pain)",
        "phil_title": "Our Philosophy",
        "phil_1_title": "100% Privacy",
        "phil_1_desc": "No accounts. No ads. No trackers. Your data stays strictly on your device.",
        "phil_2_title": "Native Performance",
        "phil_2_desc": "Built purely with Swift for maximum hardware efficiency across iOS, watchOS, iPadOS, and tvOS 4K.",
        "phil_3_title": "Global First",
        "phil_3_desc": "We build for the world. Multilingual studio voice coaches and localized experiences from day one.",
        "phil_4_title": "Zero Distractions",
        "phil_4_desc": "We respect your focus. Clean, athletic interfaces designed solely to elevate your performance.",
        "footer_rights": "© 2026 AE Interactive. All rights reserved."
    },
    "zh-Hant": {
        "title": "AE Interactive | 打造極致數位互動體驗",
        "nav_apps": "產品",
        "nav_philosophy": "理念",
        "nav_contact": "聯絡我們",
        "hero_headline": "打造極致的<br>數位互動體驗",
        "hero_sub": "專注於 Apple 全生態系原生效能、絕對隱私與零干擾設計的獨立開發團隊。",
        "apps_title": "主打產品生態系",
        "app1_tag": "主打產品 • V1.3.1 全設備通用購買",
        "app1_title": "Workout Timer",
        "app1_subtitle": "真人語音健身計時 & Apple TV 4K 客廳運動鐘",
        "app1_desc": "橫跨 iPhone、iPad、Apple Watch 與 Apple TV 4K 的次世代高強度間歇計時器。搭載 5 位多國語言錄音室真人教練、7 大精選真人影片課表（含 UP NEXT 休息預習）、AirPods Pro 與 Apple Watch 即時心率串流，以及 100% 離線純淨隱私。",
        "btn_website": "探索官方網站",
        "btn_appstore": " App Store 下載",
        "btn_video_hannah": "▶ Hannah 教練宣傳片",
        "btn_video_elena": "▶ Dr. Elena 教練宣傳片",
        "vid_section_label": "全新 1080P 真人教練課表宣傳片",
        "vid_1_title": "Hannah Lin 教練 • 10 分鐘高密度核心腹肌 ＋ 方盒呼吸恢復",
        "vid_2_title": "Dr. Elena Lindqvist 物理治療博士 • 12 分鐘零頸壓臨床核心雕塑",
        "phil_title": "核心理念",
        "phil_1_title": "100% 絕對隱私",
        "phil_1_desc": "免註冊、無廣告、無追蹤器。您的健康數據絕對保密，僅存於設備本機。",
        "phil_2_title": "原生流暢效能",
        "phil_2_desc": "純 Swift 原生打造，完美整合動態島、Apple TV 4K 與最新硬體加速技術。",
        "phil_3_title": "生而全球化",
        "phil_3_desc": "從第一天起就支援多國語系，為全球使用者打造深度的在地化語音體驗。",
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
        "hero_sub": "专注于 Apple 全生态系原生性能、绝对隐私与零干扰设计的独立开发团队。",
        "apps_title": "主打产品生态系",
        "app1_tag": "主打产品 • V1.3.1 全设备通用购买",
        "app1_title": "Workout Timer",
        "app1_subtitle": "真人语音健身计时 & Apple TV 4K 客厅运动钟",
        "app1_desc": "横跨 iPhone、iPad、Apple Watch 与 Apple TV 4K 的次世代高强度间歇计时器。搭载 5 位多国语言录音室真人教练、7 大精选真人视频课表（含 UP NEXT 休息预习）、AirPods Pro 与 Apple Watch 实时心率同步，以及 100% 离线纯净隐私。",
        "btn_website": "探索官方网站",
        "btn_appstore": " App Store 下载",
        "btn_video_hannah": "▶ Hannah 教练宣传片",
        "btn_video_elena": "▶ Dr. Elena 教练宣传片",
        "vid_section_label": "全新 1080P 真人教练课表宣传片",
        "vid_1_title": "Hannah Lin 教练 • 10 分钟高密度核心腹肌 ＋ 方盒呼吸恢复",
        "vid_2_title": "Dr. Elena Lindqvist 物理治疗博士 • 12 分钟零颈压临床核心雕塑",
        "phil_title": "核心理念",
        "phil_1_title": "100% 绝对隐私",
        "phil_1_desc": "免注册、无广告、无追踪器。您的健康数据绝对保密，仅存于设备本机。",
        "phil_2_title": "原生流畅性能",
        "phil_2_desc": "纯 Swift 原生打造，完美整合灵动岛、Apple TV 4K 与最新硬件加速技术。",
        "phil_3_title": "生而全球化",
        "phil_3_desc": "从第一天起就支持多国语系，为全球使用者打造深度的本地化语音体验。",
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
        "hero_sub": "Un estudio independiente dedicado al rendimiento nativo del ecosistema Apple, privacidad sin compromisos y cero distracciones.",
        "apps_title": "Nuestro Ecosistema Destacado",
        "app1_tag": "DESTACADO • V1.3.1 COMPRA UNIVERSAL",
        "app1_title": "Workout Timer",
        "app1_subtitle": "Entrenador de Voz y Reloj 4K para Apple TV",
        "app1_desc": "El temporizador de intervalos definitivo para iPhone, iPad, Apple Watch y Apple TV 4K. Con 5 entrenadores de voz reales de estudio, 7 programas guiados en video con vista previa UP NEXT, pulso en vivo con AirPods Pro y Apple Watch, y privacidad 100% offline.",
        "btn_website": "Explorar Sitio Web",
        "btn_appstore": " App Store",
        "btn_video_hannah": "▶ Promo Coach Hannah",
        "btn_video_elena": "▶ Promo Dra. Elena",
        "vid_section_label": "NUEVOS VIDEOS PROMOCIONALES 1080P",
        "vid_1_title": "Coach Hannah Lin • Abdomen en 10 Min + Respiración en Caja",
        "vid_2_title": "Dra. Elena Lindqvist, DPT • Core Clínico en 12 Min (Sin Dolor de Cuello)",
        "phil_title": "Nuestra Filosofía",
        "phil_1_title": "100% Privacidad",
        "phil_1_desc": "Sin cuentas. Sin anuncios. Sin rastreadores. Tus datos se quedan en tu dispositivo.",
        "phil_2_title": "Rendimiento Nativo",
        "phil_2_desc": "Desarrollado puramente con Swift para máxima eficiencia en iOS, watchOS, iPadOS y tvOS 4K.",
        "phil_3_title": "Global desde el inicio",
        "phil_3_desc": "Construimos para el mundo. Entrenadores multilingües y experiencias localizadas.",
        "phil_4_title": "Cero Distracciones",
        "phil_4_desc": "Respetamos tu concentración. Interfaces limpias diseñadas solo para potenciar tu entrenamiento.",
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
      --bg-color: #030407;
      --card-bg: linear-gradient(165deg, rgba(24, 27, 36, 0.88) 0%, rgba(11, 13, 19, 0.94) 100%);
      --text-main: #f5f7fa;
      --text-muted: #9498a6;
      --primary-green: #30d158;
      --accent-cyan: #64d2ff;
      --accent-orange: #ff9f0a;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-main);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      background-image:
        radial-gradient(ellipse 80% 45% at 50% -5%, rgba(48, 209, 88, 0.18) 0%, transparent 65%),
        radial-gradient(circle at 85% 20%, rgba(100, 210, 255, 0.12) 0%, transparent 45%),
        linear-gradient(rgba(255, 255, 255, 0.022) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.022) 1px, transparent 1px);
      background-size: 100% 100%, 100% 100%, 56px 56px, 56px 56px;
      background-repeat: no-repeat, no-repeat, repeat, repeat;
    }}
    a {{ text-decoration: none; color: inherit; }}
    
    /* Floating Glass Pill Navbar */
    .nav-wrap {{
      position: fixed;
      top: 16px;
      left: 0;
      width: 100%;
      padding: 0 20px;
      z-index: 100;
    }}
    nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 13px 26px;
      max-width: 1120px;
      margin: 0 auto;
      background: rgba(10, 12, 18, 0.78);
      backdrop-filter: blur(24px) saturate(180%);
      -webkit-backdrop-filter: blur(24px) saturate(180%);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 999px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.12);
    }}
    .logo {{
      font-size: 19px;
      font-weight: 800;
      letter-spacing: -0.5px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .nav-links {{ display: flex; gap: 28px; }}
    .nav-links a {{ font-size: 14px; font-weight: 600; color: var(--text-muted); transition: color 0.25s; }}
    .nav-links a:hover {{ color: var(--primary-green); }}

    /* Hero */
    .hero {{
      padding: 150px 24px 70px;
      text-align: center;
      max-width: 960px;
      margin: 0 auto;
    }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 18px;
      border-radius: 999px;
      background: rgba(48, 209, 88, 0.12);
      border: 1px solid rgba(48, 209, 88, 0.38);
      color: var(--primary-green);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.9px;
      text-transform: uppercase;
      margin-bottom: 24px;
    }}
    .hero h1 {{
      font-size: clamp(44px, 7.2vw, 76px);
      font-weight: 900;
      line-height: 1.05;
      letter-spacing: -2.2px;
      margin-bottom: 22px;
      background: linear-gradient(135deg, #ffffff 0%, #30d158 55%, #64d2ff 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero p {{
      font-size: clamp(17px, 2.2vw, 21px);
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 36px;
    }}
    .studio-stats {{
      display: inline-flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 12px;
    }}
    .stat-pill {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 8px 18px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 700;
      color: #fff;
    }}

    /* Container */
    .container {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 0 24px 100px;
    }}
    .section-title {{
      font-size: clamp(28px, 4vw, 40px);
      font-weight: 900;
      letter-spacing: -1px;
      margin-bottom: 36px;
      text-align: center;
    }}

    /* Apps Showcase */
    .app-card {{
      background: var(--card-bg);
      border-radius: 32px;
      padding: 52px 44px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      border: 1px solid rgba(48, 209, 88, 0.28);
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.12);
      position: relative;
      overflow: hidden;
      margin-bottom: 40px;
    }}
    .app-card::before {{
      content: '';
      position: absolute;
      top: -50%; left: -50%;
      width: 200%; height: 200%;
      background: radial-gradient(circle at top, rgba(48,209,88,0.12) 0%, transparent 50%);
      pointer-events: none;
    }}
    .tag {{
      background: rgba(48,209,88,0.16);
      border: 1px solid rgba(48,209,88,0.4);
      color: var(--primary-green);
      font-size: 12px;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 99px;
      margin-bottom: 18px;
      letter-spacing: 0.8px;
    }}
    .app-title {{ font-size: clamp(32px, 5vw, 48px); font-weight: 900; letter-spacing: -1.2px; margin-bottom: 6px; }}
    .app-subtitle {{ font-size: clamp(18px, 2.5vw, 24px); font-weight: 700; color: var(--accent-cyan); margin-bottom: 20px; }}
    .app-desc {{ font-size: 17px; color: var(--text-muted); max-width: 720px; margin: 0 auto 28px auto; text-align: center; line-height: 1.65; }}
    .btn {{
      background: var(--text-main);
      color: var(--bg-color);
      padding: 15px 28px;
      border-radius: 99px;
      font-weight: 800;
      font-size: 15px;
      transition: transform 0.2s, box-shadow 0.2s, background 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .btn:hover {{ transform: translateY(-2px); }}
    .btn-green {{
      background: linear-gradient(135deg, #30d158 0%, #24b247 100%);
      color: #000;
      box-shadow: 0 10px 32px rgba(48, 209, 88, 0.4);
    }}
    .studio-video-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      width: 100%;
      margin-top: 24px;
      text-align: left;
      align-items: stretch;
    }}
    .studio-video-box {{
      background: rgba(6, 8, 14, 0.72);
      border: 1px solid rgba(48, 209, 88, 0.28);
      border-radius: 22px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
      box-shadow: 0 18px 48px rgba(0, 0, 0, 0.65);
    }}
    .studio-video-box h4 {{
      font-size: 16px;
      font-weight: 800;
      color: #fff;
      margin-bottom: 14px;
      line-height: 1.35;
      min-height: 2.7em;
      display: flex;
      align-items: flex-start;
    }}
    .studio-iframe-wrap {{
      position: relative;
      width: 100%;
      padding-bottom: 56.25%;
      height: 0;
      margin-top: auto;
      flex-shrink: 0;
      border-radius: 14px;
      overflow: hidden;
      background: #000;
      border: 1px solid rgba(255, 255, 255, 0.14);
    }}
    .studio-iframe-wrap iframe {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }}
    @media (max-width: 820px) {{
      .studio-video-grid {{ grid-template-columns: 1fr; }}
    }}

    /* Bento Grid (Philosophy) */
    .bento-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 22px;
    }}
    .bento-card {{
      background: var(--card-bg);
      border-radius: 26px;
      padding: 36px;
      border: 1px solid rgba(255,255,255,0.08);
      box-shadow: 0 18px 45px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.08);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      min-height: 230px;
      transition: transform 0.25s, border-color 0.25s;
    }}
    .bento-card:hover {{
      transform: translateY(-4px);
      border-color: rgba(48, 209, 88, 0.45);
    }}
    .bento-card h3 {{ font-size: 22px; font-weight: 800; margin-bottom: 10px; }}
    .bento-card p {{ color: var(--text-muted); font-size: 15.5px; line-height: 1.55; }}
    .bento-icon {{ font-size: 38px; margin-bottom: auto; }}

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

    /* Video Cinema Modal */
    .video-modal {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 99999;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.25s ease, visibility 0.25s ease;
      padding: 24px;
      box-sizing: border-box;
    }}
    .video-modal.active {{
      opacity: 1;
      visibility: visible;
    }}
    .video-modal-backdrop {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
    }}
    .video-modal-dialog {{
      position: relative;
      width: 100%;
      max-width: 920px;
      z-index: 2;
      transform: scale(0.95);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .video-modal.active .video-modal-dialog {{
      transform: scale(1);
    }}
    .video-modal-close {{
      position: absolute;
      top: -46px;
      right: 0;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #fff;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      font-size: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: background 0.2s, transform 0.2s;
    }}
    .video-modal-close:hover {{
      background: rgba(255, 255, 255, 0.3);
      transform: scale(1.08);
    }}
    .video-modal-player-wrap {{
      position: relative;
      width: 100%;
      padding-bottom: 56.25%;
      height: 0;
      border-radius: 18px;
      overflow: hidden;
      background: #000;
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.15);
    }}
    .video-modal-player-wrap iframe {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }}
  </style>
</head>
<body>
  <div class="nav-wrap">
    <nav>
      <a href="/" class="logo" style="display: flex; align-items: center; gap: 12px; text-decoration: none;">
        <img src="/images/brand_icon_v2.png" alt="AE Interactive" style="height: 36px; width: auto; object-fit: contain;">
        <span style="font-size: 19px; font-weight: 800; letter-spacing: -0.4px; color: #ffffff;">AE Interactive</span>
      </a>
      <div class="nav-right" style="display: flex; align-items: center; gap: 26px;">
        <div class="nav-links">
          <a href="#apps">{t[nav_apps]}</a>
          <a href="#philosophy">{t[nav_philosophy]}</a>
          <a href="mailto:support@appengine.fun">{t[nav_contact]}</a>
        </div>
        <div class="lang-picker" style="display: flex; gap: 10px; font-size: 12.5px; font-weight: 700; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); padding: 5px 14px; border-radius: 999px;">
          <a href="/?lang=en" style="color: {c_en}; text-decoration: none;">EN</a>
          <a href="/?lang=zh-Hant" style="color: {c_zh_hant}; text-decoration: none;">繁中</a>
          <a href="/?lang=zh-Hans" style="color: {c_zh_hans}; text-decoration: none;">简中</a>
          <a href="/?lang=es" style="color: {c_es}; text-decoration: none;">ES</a>
        </div>
      </div>
    </nav>
  </div>

  <section class="hero">
    <div style="display: flex; justify-content: center; margin-bottom: 24px;">
        <img src="/images/brand_logo_v2.png" alt="AE Interactive Logo" style="height: 132px; width: auto; filter: drop-shadow(0 0 38px rgba(48,209,88,0.5));">
    </div>
    <div class="hero-badge">✦ NATIVE APPLE ECOSYSTEM STUDIO</div>
    <h1>{t[hero_headline]}</h1>
    <p>{t[hero_sub]}</p>
    <div class="studio-stats">
      <span class="stat-pill">📺 iOS • iPadOS • watchOS • tvOS 4K</span>
      <span class="stat-pill">🎬 7 Guided 1080p Coach Programs</span>
      <span class="stat-pill">🎙️ 5 Studio Human Voice Coaches</span>
      <span class="stat-pill">🔒 100% Offline Privacy</span>
    </div>
  </section>

  <div class="container" id="apps">
    <div class="section-title">{t[apps_title]}</div>
    
    <div class="app-card" style="display: block; color: inherit;">
      <div class="tag">{t[app1_tag]}</div>
      <div class="app-title">{t[app1_title]}</div>
      <div class="app-subtitle">{t[app1_subtitle]}</div>
      <p class="app-desc" style="max-width: 680px; text-align: center;">{t[app1_desc]}</p>
      <div style="display: flex; gap: 12px; align-items: center; justify-content: center; flex-wrap: wrap; margin-top: 20px;">
        <a href="https://workout.appengine.fun/?lang={lang_code}" class="btn btn-green" style="text-decoration: none;">{t[btn_website]}</a>
        <a href="https://apps.apple.com/app/id6811742209" target="_blank" rel="noopener noreferrer" class="btn" style="text-decoration: none;">{t[btn_appstore]}</a>
        <a href="https://apps.apple.com/redeem?ctx=offercodes&id=6811742209&code=DRELENA" target="_blank" rel="noopener noreferrer" class="btn" style="background: linear-gradient(135deg, rgba(255,159,10,0.22) 0%, rgba(48,209,88,0.18) 100%); color: #ff9f0a; border: 1px solid rgba(255,159,10,0.55); text-decoration: none;">
          🎁 Redeem Code: <span style="font-family: monospace; font-weight: 900; color: #fff; background: rgba(0,0,0,0.5); padding: 2px 8px; border-radius: 6px;">DRELENA</span>
        </a>
        <a href="https://youtu.be/Lr17qfFtyIk" data-video-id="Lr17qfFtyIk" target="_blank" rel="noopener noreferrer" class="btn btn-video-trigger" style="background: rgba(255,255,255,0.08); color: #ffffff; border: 1px solid rgba(255,255,255,0.18); text-decoration: none;">
          <span style="color: #ff0033;">▶</span> {t[btn_video_hannah]}
        </a>
        <a href="https://youtu.be/l3AbmjBSlKc" data-video-id="l3AbmjBSlKc" target="_blank" rel="noopener noreferrer" class="btn btn-video-trigger" style="background: rgba(255,255,255,0.08); color: #ffffff; border: 1px solid rgba(255,255,255,0.18); text-decoration: none;">
          <span style="color: #ff0033;">▶</span> {t[btn_video_elena]}
        </a>
      </div>

      <div style="margin-top: 44px; pt: 20px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 32px;">
        <div style="font-size: 12px; font-weight: 800; letter-spacing: 1px; color: var(--primary-green); margin-bottom: 4px;">{t[vid_section_label]}</div>
        <div class="studio-video-grid">
          <div class="studio-video-box">
            <h4>🔥 {t[vid_1_title]}</h4>
            <div class="studio-iframe-wrap">
              <iframe src="https://www.youtube-nocookie.com/embed/Lr17qfFtyIk?rel=0" title="{t[vid_1_title]}" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
          </div>
          <div class="studio-video-box">
            <h4>🩺 {t[vid_2_title]}</h4>
            <div class="studio-iframe-wrap">
              <iframe src="https://www.youtube-nocookie.com/embed/l3AbmjBSlKc?rel=0" title="{t[vid_2_title]}" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
          </div>
        </div>
      </div>
    </div>
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
    <div style="margin-bottom: 16px; display: flex; justify-content: center; align-items: center; gap: 18px; font-weight: 500; flex-wrap: wrap;">
      <a href="https://www.youtube.com/@appengine-a" target="_blank" rel="noopener noreferrer" style="color: var(--text-muted); text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
        <span style="color: #ff0033;">▶</span> YouTube
      </a>
      <span style="color: rgba(255,255,255,0.2);">•</span>
      <a href="https://workout.appengine.fun" target="_blank" rel="noopener noreferrer" style="color: var(--text-muted); text-decoration: none;">Workout Timer</a>
      <span style="color: rgba(255,255,255,0.2);">•</span>
      <a href="https://reviewcloud.net" target="_blank" rel="noopener noreferrer" style="color: var(--text-muted); text-decoration: none;">ReviewCloud</a>
    </div>
    {t[footer_rights]}
  </footer>

  <!-- Video Cinema Modal -->
  <div id="videoModal" class="video-modal" aria-hidden="true" role="dialog">
    <div class="video-modal-backdrop" id="videoModalBackdrop"></div>
    <div class="video-modal-dialog">
      <button class="video-modal-close" id="videoModalClose" aria-label="Close Video">✕</button>
      <div class="video-modal-player-wrap">
        <iframe id="videoModalIframe" src="" title="Workout Timer App Showcase" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      </div>
    </div>
  </div>

  <script>
    const videoModal = document.getElementById('videoModal');
    const videoModalBackdrop = document.getElementById('videoModalBackdrop');
    const videoModalClose = document.getElementById('videoModalClose');
    const videoModalIframe = document.getElementById('videoModalIframe');

    function openVideoModal(e) {{
      if (e) e.preventDefault();
      const vidId = (this && this.getAttribute && this.getAttribute('data-video-id')) || 'Lr17qfFtyIk';
      if (videoModal && videoModalIframe) {{
        videoModalIframe.src = "https://www.youtube-nocookie.com/embed/" + vidId + "?autoplay=1&rel=0";
        videoModal.classList.add('active');
        videoModal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      }}
    }}

    function closeVideoModal() {{
      if (videoModal && videoModalIframe) {{
        videoModal.classList.remove('active');
        videoModal.setAttribute('aria-hidden', 'true');
        videoModalIframe.src = '';
        document.body.style.overflow = '';
      }}
    }}

    document.querySelectorAll('.btn-video-trigger').forEach(btn => {{
      btn.addEventListener('click', openVideoModal);
    }});

    if (videoModalClose) videoModalClose.addEventListener('click', closeVideoModal);
    if (videoModalBackdrop) videoModalBackdrop.addEventListener('click', closeVideoModal);
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape' && videoModal && videoModal.classList.contains('active')) {{
        closeVideoModal();
      }}
    }});
  </script>
</body>
</html>"""

os.makedirs("public", exist_ok=True)


gtm_head = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-W7N52ZML');</script>
<!-- End Google Tag Manager -->
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-1JL7EP8YTN"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-1JL7EP8YTN');
</script>"""

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

