import json
import os

LANG_ORDER = ("en", "zh-Hant", "zh-Hans", "ja", "ko", "es")

LANG_APPS = [
    {
        "slug": "nihongo",
        "name": "NihonGo",
        "accent": "#818CF8",
        "flag": "🇯🇵",
        "version": "1.2.0",
        "website": "https://nihongo.appengine.fun",
        "appstore": "https://apps.apple.com/app/id6836279889",
        "sub": {
            "en": "Japanese · 104 Kana & 100 Videos",
            "zh-Hant": "旅遊日語 · 104 五十音與 100 影片",
            "zh-Hans": "旅游日语 · 104 五十音与 100 视频",
            "ja": "旅行日本語 · 104かな＆100動画",
            "ko": "여행 일본어 · 104 가나 & 100 영상",
            "es": "Japonés · 104 Kana y 100 Vídeos",
        },
    },
    {
        "slug": "englishgo",
        "name": "EnglishGo",
        "accent": "#38BDF8",
        "flag": "🇺🇸",
        "version": "1.0.0",
        "website": "https://englishgo.appengine.fun",
        "appstore": "https://apps.apple.com/app/id6837609680",
        "sub": {
            "en": "English · 44 US/UK IPA & 100 Videos",
            "zh-Hant": "旅遊英語 · 44 美英音標與 100 影片",
            "zh-Hans": "旅游英语 · 44 美语音标与 100 视频",
            "ja": "旅行英語 · 米英44 IPA＆100動画",
            "ko": "여행 영어 · 44 US/UK IPA & 100 영상",
            "es": "Inglés · 44 IPA US/UK y 100 Vídeos",
        },
    },
    {
        "slug": "espanolgo",
        "name": "EspanolGo",
        "accent": "#FB7185",
        "flag": "🇪🇸",
        "version": "1.0.0",
        "website": "https://espanolgo.appengine.fun",
        "appstore": "https://apps.apple.com/app/id6837611917",
        "sub": {
            "en": "Spanish · 32 Sounds & 100 Videos",
            "zh-Hant": "旅遊西語 · 32 發音規則與 100 影片",
            "zh-Hans": "旅游西语 · 32 发音规则与 100 视频",
            "ja": "旅行スペイン語 · 32音声＆100動画",
            "ko": "여행 스페인어 · 32 발음 & 100 영상",
            "es": "Español · 32 Sonidos y 100 Vídeos",
        },
    },
    {
        "slug": "koreango",
        "name": "KoreanGo",
        "accent": "#2DD4BF",
        "flag": "🇰🇷",
        "version": "1.0.0",
        "website": "https://koreango.appengine.fun",
        "appstore": "https://apps.apple.com/app/id6838241626",
        "sub": {
            "en": "Korean · 40 Hangul & 100 Seoul Videos",
            "zh-Hant": "旅遊韓語 · 40 字母手寫與 100 首爾片",
            "zh-Hans": "旅游韩语 · 40 字母手写与 100 首尔片",
            "ja": "旅行韓国語 · 40ハングル＆100動画",
            "ko": "여행 한국어 · 한글 40자 & 100 영상",
            "es": "Coreano · 40 Hangul y 100 Vídeos",
        },
    },
    {
        "slug": "mandaringo",
        "name": "MandarinGo",
        "accent": "#F59E0B",
        "flag": "🇹🇼",
        "version": "1.0.0",
        "website": "https://mandaringo.appengine.fun",
        "appstore": "https://apps.apple.com/app/id6838245896",
        "sub": {
            "en": "Mandarin · Zhuyin/Pinyin & 100 Videos",
            "zh-Hant": "華語雙軌 · 注音／拼音與 100 影片",
            "zh-Hans": "汉语双轨 · 注音／拼音与 100 视频",
            "ja": "中国語 · 注音/ピンイン＆100動画",
            "ko": "대만·중국어 · 주음/병음 & 100 영상",
            "es": "Mandarín · Zhuyin/Pinyin y 100 Vídeos",
        },
    },
]

languages = {
    "en": {
        "title": "AE Interactive | Native Apple Fitness & Travel Language Apps",
        "nav_apps": "Apps",
        "nav_languages": "AE Languages",
        "nav_philosophy": "Philosophy",
        "nav_contact": "Contact",
        "hero_badge": "✦ NATIVE APPLE ECOSYSTEM STUDIO",
        "hero_headline": "Crafting Premium<br>Digital Experiences",
        "hero_sub": "An independent studio building 6 native Apple apps across fitness and travel languages—engineered purely in Swift with uncompromising privacy and zero distractions.",
        "stat_1": "📱 6 Live Apple Apps",
        "stat_2": "🌍 5 Travel Languages + Fitness",
        "stat_3": "🎬 500+ Video Dialogues & Coach Workouts",
        "stat_4": "🔒 100% Offline Privacy",
        "apps_title": "Our Flagship Ecosystem",
        "lang_tag": "NEW SERIES • 5 LIVE APPS • IPHONE, IPAD & IPHONE DUO",
        "lang_title": "Travel Language Go Series",
        "lang_subtitle": "Japanese · English · Spanish · Korean · Mandarin",
        "lang_desc": "Five dedicated native apps built for real travel confidence—each pairing 15 guided lessons, interactive script & sound labs, 100 real-world travel video dialogues, 12-scene Guided Voice Practice, and live 2-way voice translation. Free forever to start, or $3.99 one-time Lifetime Pro.",
        "btn_lang_portal": "Explore AE Languages Portal →",
        "btn_site_short": "Site",
        "btn_store_short": "App Store",
        "app1_tag": "FLAGSHIP FITNESS • V1.3.1 UNIVERSAL PURCHASE",
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
        "phil_1_desc": "No accounts. No ads. No trackers inside our apps. Your progress and health data stay strictly on your device.",
        "phil_2_title": "Native Performance",
        "phil_2_desc": "Built purely with Swift for maximum hardware efficiency across iOS, iPadOS, watchOS, and tvOS 4K.",
        "phil_3_title": "Global First",
        "phil_3_desc": "We build for the world—spanning 6 interface languages, studio native recordings, and real-world travel localization.",
        "phil_4_title": "Zero Distractions",
        "phil_4_desc": "No subscription traps or pop-up fatigue. Clean, purposeful interfaces designed to help you act immediately.",
        "footer_rights": "© 2026 AE Interactive. All rights reserved.",
    },
    "zh-Hant": {
        "title": "AE Interactive | 原生 Apple 健身與五大旅遊語言 App 工作室",
        "nav_apps": "產品",
        "nav_languages": "語言總站",
        "nav_philosophy": "理念",
        "nav_contact": "聯絡我們",
        "hero_badge": "✦ 專注 APPLE 生態系的獨立工作室",
        "hero_headline": "打造極致的<br>數位互動體驗",
        "hero_sub": "專注於 Apple 全生態系原生效能、絕對隱私與零干擾設計的獨立開發團隊——旗下 6 款 App 橫跨健身訓練與五大旅遊語言學習。",
        "stat_1": "📱 6 款 App Store 正式上架",
        "stat_2": "🌍 五大旅遊語言 ＋ 健身計時",
        "stat_3": "🎬 500+ 實境對話與教練課表影片",
        "stat_4": "🔒 100% 離線本機隱私",
        "apps_title": "主打產品生態系",
        "lang_tag": "全新系列 • 5 款上架 • IPHONE / IPAD / IPHONE DUO",
        "lang_title": "Travel Language Go 語言系列",
        "lang_subtitle": "日語 · 英語 · 西語 · 韓語 · 華語雙軌",
        "lang_desc": "五款純 Swift 原生打造的獨立旅遊語言 App：每款收錄 15 堂系統課、音標與手寫筆順畫板、100 部當地實境對話短片、12 情境語音口說練習，以及現場雙向即時語音口譯。基礎永久免費，可選 $3.99 單次永久買斷。",
        "btn_lang_portal": "前往 AE Languages 語言總站 →",
        "btn_site_short": "官網",
        "btn_store_short": "App Store",
        "app1_tag": "旗艦健身 • V1.3.1 全設備通用購買",
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
        "phil_1_desc": "免註冊、無廣告、App 內無追蹤器。您的運動紀錄與學習進度皆僅存於設備本機。",
        "phil_2_title": "原生流暢效能",
        "phil_2_desc": "純 Swift 原生打造，完美整合動態島、iPhone Duo、Apple TV 4K 與最新硬體加速技術。",
        "phil_3_title": "生而全球化",
        "phil_3_desc": "橫跨 6 種介面語言、數千支原生錄音室語音與深度在地化情境內容。",
        "phil_4_title": "零干擾設計",
        "phil_4_desc": "拒絕訂閱陷阱與彈窗疲勞，專注打造打開就能立刻上手的純淨工具。",
        "footer_rights": "© 2026 AE Interactive. 保留所有權利。",
    },
    "zh-Hans": {
        "title": "AE Interactive | 原生 Apple 健身与五大旅游语言 App 工作室",
        "nav_apps": "产品",
        "nav_languages": "语言总站",
        "nav_philosophy": "理念",
        "nav_contact": "联系我们",
        "hero_badge": "✦ 专注 APPLE 生态系的独立工作室",
        "hero_headline": "打造极致的<br>数字互动体验",
        "hero_sub": "专注于 Apple 全生态系原生性能、绝对隐私与零干扰设计的独立开发团队——旗下 6 款 App 覆盖健身训练与五大旅游语言学习。",
        "stat_1": "📱 6 款 App Store 正式上线",
        "stat_2": "🌍 五大旅游语言 ＋ 健身计时",
        "stat_3": "🎬 500+ 实景对话与教练视频",
        "stat_4": "🔒 100% 离线本地隐私",
        "apps_title": "主打产品生态系",
        "lang_tag": "全新系列 • 5 款上线 • IPHONE / IPAD / IPHONE DUO",
        "lang_title": "Travel Language Go 语言系列",
        "lang_subtitle": "日语 · 英语 · 西语 · 韩语 · 汉语双轨",
        "lang_desc": "五款纯 Swift 原生打造的独立旅游语言 App：每款内置 15 节系统课、音标与手写描红画板、100 部当地实景对话视频、12 情景语音口语模拟及现场双向实时翻译。基础永久免费，可选 $3.99 一次永久买断。",
        "btn_lang_portal": "前往 AE Languages 语言总站 →",
        "btn_site_short": "官网",
        "btn_store_short": "App Store",
        "app1_tag": "旗舰健身 • V1.3.1 全设备通用购买",
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
        "phil_1_desc": "免注册、无广告、App 内零追踪器。您的健康数据与学习记录仅保存于设备本地。",
        "phil_2_title": "原生流畅性能",
        "phil_2_desc": "纯 Swift 原生打造，完美整合灵动岛、iPhone Duo、Apple TV 4K 与硬件加速。",
        "phil_3_title": "生而全球化",
        "phil_3_desc": "覆盖 6 种界面语言、数千句录音室真人语音与地道出行本地化体验。",
        "phil_4_title": "零干扰设计",
        "phil_4_desc": "拒绝订阅套路与弹窗疲劳，专注解决真实痛点的纯净工具体验。",
        "footer_rights": "© 2026 AE Interactive. 保留所有权利。",
    },
    "ja": {
        "title": "AE Interactive | Apple ネイティブ・フィットネス＆5言語学習アプリスタジオ",
        "nav_apps": "アプリ",
        "nav_languages": "語学ポータル",
        "nav_philosophy": "哲学",
        "nav_contact": "お問い合わせ",
        "hero_badge": "✦ NATIVE APPLE ECOSYSTEM STUDIO",
        "hero_headline": "プレミアムなデジタル体験を、<br>Apple ネイティブで",
        "hero_sub": "フィットネスとトラベル語学の計6アプリをすべて純 Swift で開発する独立系スタジオ。徹底したオフライン・プライバシーと心地よい操作性を追求しています。",
        "stat_1": "📱 App Store 配信中 6アプリ",
        "stat_2": "🌍 5言語トラベル ＋ フィットネス",
        "stat_3": "🎬 500本以上の実境＆コーチ動画",
        "stat_4": "🔒 100% オフライン設計",
        "apps_title": "フラッグシップ・エコシステム",
        "lang_tag": "新シリーズ • 全5アプリ配信中 • IPHONE / IPAD / IPHONE DUO",
        "lang_title": "Travel Language Go シリーズ",
        "lang_subtitle": "日本語 · 英語 · スペイン語 · 韓国語 · 中国語",
        "lang_desc": "旅行先ですぐ話せる5つのネイティブ語学アプリ。各アプリに15課カリキュラム、文字＆発音ラボ、現地会話動画100本、12場面ロールプレイ、双方向リアルタイム音声通訳を統合。基本無料・一度きり $3.99 Pro。",
        "btn_lang_portal": "AE Languages ポータルを見る →",
        "btn_site_short": "公式サイト",
        "btn_store_short": "App Store",
        "app1_tag": "フラッグシップ運動 • V1.3.1 ユニバーサル購入",
        "app1_title": "Workout Timer",
        "app1_subtitle": "音声コーチ＆Apple TV 4K ジムクロック",
        "app1_desc": "iPhone・iPad・Apple Watch・Apple TV 4K 対応の次世代 HIIT タイマー。5名のスタジオ収録音声コーチ、UP NEXT プレビュー付き7種類のガイド動画、AirPods Pro / Watch 心拍連携を完全オフラインで。",
        "btn_website": "公式サイトを見る",
        "btn_appstore": " App Store",
        "btn_video_hannah": "▶ Hannah コーチ動画",
        "btn_video_elena": "▶ Dr. Elena 動画",
        "vid_section_label": "1080P コーチ・プロモ動画ショーケース",
        "vid_1_title": "Coach Hannah Lin • 10分コア腹筋＋ボックス呼吸",
        "vid_2_title": "Dr. Elena Lindqvist, DPT • 首に負担をかけない12分体幹プログラム",
        "phil_title": "スタジオの哲学",
        "phil_1_title": "100% プライバシー重視",
        "phil_1_desc": "アカウント登録不要・広告なし・アプリ内トラッキングゼロ。学習・健康データは端末内にのみ保存。",
        "phil_2_title": "純ネイティブ性能",
        "phil_2_desc": "iOS・iPadOS・watchOS・tvOS 4K に最適化された純 Swift 設計で軽快に動作。",
        "phil_3_title": "グローバル設計",
        "phil_3_desc": "6言語UIと数千本のネイティブ音声で、世界中のユーザーに自然な体験を届けます。",
        "phil_4_title": "集中を妨げない UI",
        "phil_4_desc": "サブスクの押し売りや不要なポップアップを排除し、開いた瞬間から使える明快さを追求。",
        "footer_rights": "© 2026 AE Interactive. All rights reserved.",
    },
    "ko": {
        "title": "AE Interactive | 네이티브 Apple 피트니스 및 5개 언어 앱 스튜디오",
        "nav_apps": "앱",
        "nav_languages": "언어 포털",
        "nav_philosophy": "철학",
        "nav_contact": "문의",
        "hero_badge": "✦ NATIVE APPLE ECOSYSTEM STUDIO",
        "hero_headline": "프리미엄 디지털 경험을<br>Apple 네이티브로",
        "hero_sub": "피트니스와 5개 여행 외국어 앱을 100% 순수 Swift로 제작하는 독립 스튜디오입니다. 타협 없는 오프라인 개인정보 보호와 방해 없는 몰입을 추구합니다.",
        "stat_1": "📱 App Store 출시 앱 6종",
        "stat_2": "🌍 5개국어 여행 ＋ 피트니스",
        "stat_3": "🎬 500편+ 실전 회화·코치 영상",
        "stat_4": "🔒 100% 오프라인 프라이버시",
        "apps_title": "대표 앱 생태계",
        "lang_tag": "신규 시리즈 • 5개 앱 정식 출시 • IPHONE / IPAD / IPHONE DUO",
        "lang_title": "Travel Language Go 시리즈",
        "lang_subtitle": "일본어 · 영어 · 스페인어 · 한국어 · 중국어",
        "lang_desc": "현지에서 바로 통하는 5개의 네이티브 외국어 앱. 각 앱마다 15개 핵심 유닛, 발음·필순 연구실, 실전 여행 회화 영상 100편, 12장면 음성 롤플레이, 양방향 실시간 통역을 무료 기본 제공(1회 평생 $3.99 Pro)합니다.",
        "btn_lang_portal": "AE Languages 포털 열기 →",
        "btn_site_short": "웹사이트",
        "btn_store_short": "App Store",
        "app1_tag": "대표 피트니스 • V1.3.1 유니버설 구매",
        "app1_title": "Workout Timer",
        "app1_subtitle": "보이스 코치 & Apple TV 4K 홈짐 타이머",
        "app1_desc": "iPhone, iPad, Apple Watch, Apple TV 4K를 아우르는 차세대 HIIT 인터벌 타이머. 5명의 스튜디오 음성 코치, UP NEXT 미리보기가 포함된 7개 코치 영상 프로그램, 실시간 심박수 연동 및 100% 오프라인 보호.",
        "btn_website": "공식 사이트 열기",
        "btn_appstore": " App Store",
        "btn_video_hannah": "▶ Hannah 코치 영상",
        "btn_video_elena": "▶ Dr. Elena 영상",
        "vid_section_label": "1080P 코치 프로모 쇼케이스",
        "vid_1_title": "Coach Hannah Lin • 10분 코어 복근 + 박스 호흡",
        "vid_2_title": "Dr. Elena Lindqvist, DPT • 목 부담 없는 12분 임상 코어",
        "phil_title": "스튜디오 철학",
        "phil_1_title": "100% 프라이버시",
        "phil_1_desc": "계정 가입 없음, 광고 없음, 앱 내 추적기 없음. 모든 운동 및 학습 기록은 기기 내부에만 저장됩니다.",
        "phil_2_title": "네이티브 퍼포먼스",
        "phil_2_desc": "iOS, iPadOS, watchOS, tvOS 4K 하드웨어에 최적화된 순수 Swift 아키텍처로 구현합니다.",
        "phil_3_title": "글로벌 퍼스트",
        "phil_3_desc": "6개 인터페이스 언어와 수천 개의 스튜디오 원어민 녹음으로 전 세계 사용자를 지원합니다.",
        "phil_4_title": "방해 없는 집중",
        "phil_4_desc": "구독 유도나 팝업 피로 없이 앱을 열자마자 바로 연습하고 운동할 수 있는 명쾌한 인터페이스.",
        "footer_rights": "© 2026 AE Interactive. All rights reserved.",
    },
    "es": {
        "title": "AE Interactive | Apps Nativas Apple de Fitness y 5 Idiomas de Viaje",
        "nav_apps": "Apps",
        "nav_languages": "Idiomas",
        "nav_philosophy": "Filosofía",
        "nav_contact": "Contacto",
        "hero_badge": "✦ ESTUDIO NATIVO DEL ECOSISTEMA APPLE",
        "hero_headline": "Creando Experiencias<br>Digitales Premium",
        "hero_sub": "Un estudio independiente con 6 apps nativas para Apple en fitness e idiomas de viaje—programadas en Swift con privacidad total y cero distracciones.",
        "stat_1": "📱 6 Apps Activas en App Store",
        "stat_2": "🌍 5 Idiomas de Viaje + Fitness",
        "stat_3": "🎬 500+ Vídeos de Viaje y Entreno",
        "stat_4": "🔒 Privacidad 100% Offline",
        "apps_title": "Nuestro Ecosistema Destacado",
        "lang_tag": "NUEVA SERIE • 5 APPS ACTIVAS • IPHONE, IPAD E IPHONE DUO",
        "lang_title": "Serie Travel Language Go",
        "lang_subtitle": "Japonés · Inglés · Español · Coreano · Mandarín",
        "lang_desc": "Cinco apps nativas creadas para hablar con soltura al viajar: cada una incluye 15 unidades guiadas, laboratorio de fonética y trazos, 100 vídeos reales de viaje, Práctica Oral en 12 escenas e Intérprete Bidireccional en Vivo. Gratis para siempre o $3.99 pago único Pro.",
        "btn_lang_portal": "Explorar Portal AE Languages →",
        "btn_site_short": "Web",
        "btn_store_short": "App Store",
        "app1_tag": "FITNESS DESTACADO • V1.3.1 COMPRA UNIVERSAL",
        "app1_title": "Workout Timer",
        "app1_subtitle": "Entrenador de Voz y Reloj 4K para Apple TV",
        "app1_desc": "El temporizador de intervalos definitivo para iPhone, iPad, Apple Watch y Apple TV 4K. Con 5 entrenadores de voz reales de estudio, 7 programas guiados en video con vista previa UP NEXT, pulso en vivo con AirPods Pro y Apple Watch, y privacidad 100% offline.",
        "btn_website": "Explorar Sitio Web",
        "btn_appstore": " App Store",
        "btn_video_hannah": "▶ Promo Coach Hannah",
        "btn_video_elena": "▶ Promo Dra. Elena",
        "vid_section_label": "VIDEOS PROMOCIONALES 1080P",
        "vid_1_title": "Coach Hannah Lin • Abdomen en 10 Min + Respiración en Caja",
        "vid_2_title": "Dra. Elena Lindqvist, DPT • Core Clínico en 12 Min (Sin Dolor de Cuello)",
        "phil_title": "Nuestra Filosofía",
        "phil_1_title": "100% Privacidad",
        "phil_1_desc": "Sin cuentas, sin anuncios ni rastreadores en nuestras apps. Tu progreso se queda en tu dispositivo.",
        "phil_2_title": "Rendimiento Nativo",
        "phil_2_desc": "Desarrolladas en Swift puro para máxima fluidez en iOS, iPadOS, watchOS y tvOS 4K.",
        "phil_3_title": "Global desde el inicio",
        "phil_3_desc": "6 idiomas de interfaz, miles de audios de estudio y localización cuidada para viajeros.",
        "phil_4_title": "Cero Distracciones",
        "phil_4_desc": "Sin suscripciones forzadas ni ventanas molestas. Interfaces limpias listas para actuar.",
        "footer_rights": "© 2026 AE Interactive. Todos los derechos reservados.",
    },
}

html_template = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{t[title]}</title>
  <meta name="description" content="{t[hero_sub]}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="author" content="AE Interactive">
  <meta name="theme-color" content="#030407">

  <!-- Canonical & Multilingual SEO -->
  <link rel="canonical" href="{canonical_url}">
  <link rel="alternate" hreflang="en" href="https://appengine.fun/">
  <link rel="alternate" hreflang="zh-Hant" href="https://appengine.fun/?lang=zh-Hant">
  <link rel="alternate" hreflang="zh-Hans" href="https://appengine.fun/?lang=zh-Hans">
  <link rel="alternate" hreflang="ja" href="https://appengine.fun/?lang=ja">
  <link rel="alternate" hreflang="ko" href="https://appengine.fun/?lang=ko">
  <link rel="alternate" hreflang="es" href="https://appengine.fun/?lang=es">
  <link rel="alternate" hreflang="x-default" href="https://appengine.fun/">

  <!-- Open Graph / Social Media Sharing -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="AE Interactive">
  <meta property="og:locale" content="{og_locale}">
{og_locale_alts}  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{t[title]}">
  <meta property="og:description" content="{t[hero_sub]}">
  <meta property="og:image" content="https://appengine.fun/images/brand_logo_v2.png">
  <meta property="og:image:width" content="707">
  <meta property="og:image:height" content="592">
  <meta property="og:image:alt" content="AE Interactive Logo">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t[title]}">
  <meta name="twitter:description" content="{t[hero_sub]}">
  <meta name="twitter:image" content="https://appengine.fun/images/brand_logo_v2.png">
  <meta name="twitter:image:alt" content="AE Interactive Logo">

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">{schema_json}</script>
  <style>
    :root {{
      --bg-color: #030407;
      --card-bg: linear-gradient(165deg, rgba(24, 27, 36, 0.88) 0%, rgba(11, 13, 19, 0.94) 100%);
      --text-main: #f5f7fa;
      --text-muted: #9498a6;
      --primary-green: #30d158;
      --accent-cyan: #64d2ff;
      --accent-teal: #2dd4bf;
      --accent-indigo: #818cf8;
      --accent-orange: #ff9f0a;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Apple SD Gothic Neo", "PingFang TC", "PingFang SC", "Hiragino Sans", "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-main);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      background-image:
        radial-gradient(ellipse 80% 45% at 50% -5%, rgba(48, 209, 88, 0.16) 0%, transparent 65%),
        radial-gradient(circle at 85% 20%, rgba(100, 210, 255, 0.13) 0%, transparent 45%),
        radial-gradient(circle at 12% 38%, rgba(129, 140, 248, 0.12) 0%, transparent 42%),
        linear-gradient(rgba(255, 255, 255, 0.022) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.022) 1px, transparent 1px);
      background-size: 100% 100%, 100% 100%, 100% 100%, 56px 56px, 56px 56px;
      background-repeat: no-repeat, no-repeat, no-repeat, repeat, repeat;
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
      gap: 14px;
      flex-wrap: wrap;
      padding: 12px 24px;
      max-width: 1120px;
      margin: 0 auto;
      background: rgba(10, 12, 18, 0.82);
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
    .nav-links {{ display: flex; gap: 22px; }}
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
      font-size: clamp(42px, 7vw, 74px);
      font-weight: 900;
      line-height: 1.06;
      letter-spacing: -2.2px;
      margin-bottom: 22px;
      background: linear-gradient(135deg, #ffffff 0%, #30d158 52%, #64d2ff 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero p {{
      font-size: clamp(17px, 2.2vw, 20.5px);
      color: var(--text-muted);
      max-width: 700px;
      margin: 0 auto 34px;
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
      padding: 0 24px 88px;
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
      padding: 48px 40px;
      display: block;
      text-align: center;
      border: 1px solid rgba(48, 209, 88, 0.28);
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.12);
      position: relative;
      overflow: hidden;
      margin-bottom: 36px;
    }}
    .app-card::before {{
      content: '';
      position: absolute;
      top: -50%; left: -50%;
      width: 200%; height: 200%;
      background: radial-gradient(circle at top, rgba(48,209,88,0.11) 0%, transparent 50%);
      pointer-events: none;
    }}
    .app-card.lang-card {{
      border-color: rgba(45, 212, 191, 0.36);
    }}
    .app-card.lang-card::before {{
      background: radial-gradient(circle at top, rgba(129,140,248,0.16) 0%, rgba(45,212,191,0.08) 30%, transparent 55%);
    }}
    .tag {{
      display: inline-block;
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
    .lang-card .tag {{
      background: rgba(45,212,191,0.15);
      border-color: rgba(45,212,191,0.45);
      color: var(--accent-teal);
    }}
    .app-title {{ font-size: clamp(30px, 4.8vw, 46px); font-weight: 900; letter-spacing: -1.2px; margin-bottom: 6px; }}
    .app-subtitle {{ font-size: clamp(17px, 2.4vw, 22px); font-weight: 700; color: var(--accent-cyan); margin-bottom: 18px; }}
    .app-desc {{ font-size: 16.5px; color: var(--text-muted); max-width: 740px; margin: 0 auto 26px auto; text-align: center; line-height: 1.65; }}
    .btn {{
      background: var(--text-main);
      color: var(--bg-color);
      padding: 14px 26px;
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
    .btn-lang {{
      background: linear-gradient(135deg, #6366f1 0%, #14b8a6 100%);
      color: #fff;
      box-shadow: 0 10px 32px rgba(99, 102, 241, 0.4);
    }}

    /* 5-App Mini Grid inside Language Showcase */
    .lang-apps-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(185px, 1fr));
      gap: 14px;
      margin-top: 32px;
      text-align: left;
      position: relative;
      z-index: 1;
    }}
    .lang-mini {{
      background: rgba(6, 9, 18, 0.78);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 12px;
      transition: transform 0.2s, border-color 0.2s;
    }}
    .lang-mini:hover {{
      transform: translateY(-3px);
      border-color: var(--mini-accent, rgba(45, 212, 191, 0.5));
    }}
    .lang-mini-head {{ display: flex; align-items: center; gap: 11px; }}
    .lang-mini-head img {{ width: 44px; height: 44px; border-radius: 11px; border: 1px solid rgba(255,255,255,0.16); }}
    .lang-mini-name {{ font-size: 16px; font-weight: 850; color: #fff; line-height: 1.2; }}
    .lang-mini-ver {{ font-size: 11px; font-weight: 750; color: var(--mini-accent, #2dd4bf); }}
    .lang-mini-sub {{ font-size: 12.5px; color: var(--text-muted); line-height: 1.4; }}
    .lang-mini-links {{ display: flex; flex-direction: column; gap: 7px; }}
    .mini-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      white-space: nowrap;
      padding: 8px 12px;
      border-radius: 99px;
      font-size: 12px;
      font-weight: 800;
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.14);
      color: #e2e8f0;
      transition: background 0.2s, color 0.2s;
    }}
    .mini-btn:hover {{ background: rgba(255,255,255,0.16); color: #fff; }}
    .mini-btn.store {{ background: #fff; color: #090d16; border-color: #fff; }}
    .mini-btn.store:hover {{ background: #e2e8f0; color: #090d16; }}

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
      min-height: 220px;
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
      padding: 56px 24px;
      text-align: center;
      color: var(--text-muted);
      font-size: 14px;
    }}
    footer a:hover {{ color: #fff; }}

    @media (max-width: 860px) {{
      nav {{ border-radius: 24px; padding: 14px 18px; }}
      .nav-links {{ display: none; }}
      .bento-grid {{ grid-template-columns: 1fr; }}
      .app-card {{ padding: 36px 22px; }}
    }}

    /* Video Cinema Modal */
    .video-modal {{
      position: fixed;
      top: 0; left: 0;
      width: 100vw; height: 100vh;
      z-index: 99999;
      display: flex; align-items: center; justify-content: center;
      opacity: 0; visibility: hidden;
      transition: opacity 0.25s ease, visibility 0.25s ease;
      padding: 24px; box-sizing: border-box;
    }}
    .video-modal.active {{ opacity: 1; visibility: visible; }}
    .video-modal-backdrop {{
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
    }}
    .video-modal-dialog {{
      position: relative; width: 100%; max-width: 920px; z-index: 2;
      transform: scale(0.95);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .video-modal.active .video-modal-dialog {{ transform: scale(1); }}
    .video-modal-close {{
      position: absolute; top: -46px; right: 0;
      background: rgba(255, 255, 255, 0.15); border: 1px solid rgba(255, 255, 255, 0.25);
      color: #fff; width: 36px; height: 36px; border-radius: 50%; font-size: 18px;
      display: flex; align-items: center; justify-content: center; cursor: pointer;
    }}
    .video-modal-player-wrap {{
      position: relative; width: 100%; padding-bottom: 56.25%; height: 0;
      border-radius: 18px; overflow: hidden; background: #000;
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.15);
    }}
    .video-modal-player-wrap iframe {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0; }}
  </style>
</head>
<body>
  <div class="nav-wrap">
    <nav>
      <a href="/?lang={lang_code}" class="logo" style="display: flex; align-items: center; gap: 12px; text-decoration: none;">
        <img src="/images/brand_icon_v2.png" alt="AE Interactive" style="height: 36px; width: auto; object-fit: contain;">
        <span style="font-size: 19px; font-weight: 800; letter-spacing: -0.4px; color: #ffffff;">AE Interactive</span>
      </a>
      <div class="nav-right" style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap;">
        <div class="nav-links">
          <a href="#apps">{t[nav_apps]}</a>
          <a href="https://languages.appengine.fun/?lang={lang_code}" target="_blank" rel="noopener noreferrer">{t[nav_languages]}</a>
          <a href="#philosophy">{t[nav_philosophy]}</a>
          <a href="mailto:help@appengine.fun">{t[nav_contact]}</a>
        </div>
        <div class="lang-picker" style="display: flex; gap: 8px; font-size: 12px; font-weight: 700; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); padding: 5px 12px; border-radius: 999px;">
          <a href="/?lang=en" style="color: {c_en}; text-decoration: none;">EN</a>
          <a href="/?lang=zh-Hant" style="color: {c_zh_hant}; text-decoration: none;">繁中</a>
          <a href="/?lang=zh-Hans" style="color: {c_zh_hans}; text-decoration: none;">简中</a>
          <a href="/?lang=ja" style="color: {c_ja}; text-decoration: none;">日本語</a>
          <a href="/?lang=ko" style="color: {c_ko}; text-decoration: none;">한국어</a>
          <a href="/?lang=es" style="color: {c_es}; text-decoration: none;">ES</a>
        </div>
      </div>
    </nav>
  </div>

  <section class="hero">
    <div style="display: flex; justify-content: center; margin-bottom: 24px;">
      <img src="/images/brand_logo_v2.png" alt="AE Interactive Logo" style="height: 132px; width: auto; filter: drop-shadow(0 0 38px rgba(48,209,88,0.45));">
    </div>
    <div class="hero-badge">{t[hero_badge]}</div>
    <h1>{t[hero_headline]}</h1>
    <p>{t[hero_sub]}</p>
    <div class="studio-stats">
      <span class="stat-pill">{t[stat_1]}</span>
      <span class="stat-pill">{t[stat_2]}</span>
      <span class="stat-pill">{t[stat_3]}</span>
      <span class="stat-pill">{t[stat_4]}</span>
    </div>
  </section>

  <div class="container" id="apps">
    <div class="section-title">{t[apps_title]}</div>

    <!-- Travel Language Go Series Showcase (5 Live Apps) -->
    <div class="app-card lang-card">
      <div class="tag">{t[lang_tag]}</div>
      <div class="app-title">{t[lang_title]}</div>
      <div class="app-subtitle">{t[lang_subtitle]}</div>
      <p class="app-desc">{t[lang_desc]}</p>
      <div style="display: flex; gap: 12px; align-items: center; justify-content: center; flex-wrap: wrap;">
        <a href="https://languages.appengine.fun/?lang={lang_code}" target="_blank" rel="noopener noreferrer" class="btn btn-lang">{t[btn_lang_portal]}</a>
      </div>
      <div class="lang-apps-grid">
        {lang_cards_html}
      </div>
    </div>

    <!-- Workout Timer Flagship Showcase -->
    <div class="app-card">
      <div class="tag">{t[app1_tag]}</div>
      <div class="app-title">{t[app1_title]}</div>
      <div class="app-subtitle">{t[app1_subtitle]}</div>
      <p class="app-desc">{t[app1_desc]}</p>
      <div style="display: flex; gap: 12px; align-items: center; justify-content: center; flex-wrap: wrap; margin-top: 20px;">
        <a href="https://workout.appengine.fun/?lang={workout_lang}" class="btn btn-green">{t[btn_website]}</a>
        <a href="https://apps.apple.com/app/id6811742209" target="_blank" rel="noopener noreferrer" class="btn">{t[btn_appstore]}</a>
        <a href="https://apps.apple.com/redeem?ctx=offercodes&id=6811742209&code=DRELENA" target="_blank" rel="noopener noreferrer" class="btn" style="background: linear-gradient(135deg, rgba(255,159,10,0.22) 0%, rgba(48,209,88,0.18) 100%); color: #ff9f0a; border: 1px solid rgba(255,159,10,0.55);">
          🎁 Redeem Code: <span style="font-family: monospace; font-weight: 900; color: #fff; background: rgba(0,0,0,0.5); padding: 2px 8px; border-radius: 6px;">DRELENA</span>
        </a>
        <a href="https://youtu.be/Lr17qfFtyIk" data-video-id="Lr17qfFtyIk" target="_blank" rel="noopener noreferrer" class="btn btn-video-trigger" style="background: rgba(255,255,255,0.08); color: #ffffff; border: 1px solid rgba(255,255,255,0.18);">
          <span style="color: #ff0033;">▶</span> {t[btn_video_hannah]}
        </a>
        <a href="https://youtu.be/l3AbmjBSlKc" data-video-id="l3AbmjBSlKc" target="_blank" rel="noopener noreferrer" class="btn btn-video-trigger" style="background: rgba(255,255,255,0.08); color: #ffffff; border: 1px solid rgba(255,255,255,0.18);">
          <span style="color: #ff0033;">▶</span> {t[btn_video_elena]}
        </a>
      </div>

      <div style="margin-top: 44px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 32px;">
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
    <div style="margin-bottom: 16px; display: flex; justify-content: center; align-items: center; gap: 14px; font-weight: 500; flex-wrap: wrap;">
      <a href="https://languages.appengine.fun/?lang={lang_code}" target="_blank" rel="noopener noreferrer">AE Languages</a>
      <span style="color: rgba(255,255,255,0.2);">•</span>
      <a href="https://nihongo.appengine.fun" target="_blank" rel="noopener noreferrer">NihonGo</a>
      <a href="https://englishgo.appengine.fun" target="_blank" rel="noopener noreferrer">EnglishGo</a>
      <a href="https://espanolgo.appengine.fun" target="_blank" rel="noopener noreferrer">EspanolGo</a>
      <a href="https://koreango.appengine.fun" target="_blank" rel="noopener noreferrer">KoreanGo</a>
      <a href="https://mandaringo.appengine.fun" target="_blank" rel="noopener noreferrer">MandarinGo</a>
      <span style="color: rgba(255,255,255,0.2);">•</span>
      <a href="https://workout.appengine.fun" target="_blank" rel="noopener noreferrer">Workout Timer</a>
      <span style="color: rgba(255,255,255,0.2);">•</span>
      <a href="https://www.youtube.com/@appengine-a" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 6px;"><span style="color: #ff0033;">▶</span> YouTube</a>
      <span style="color: rgba(255,255,255,0.2);">•</span>
      <a href="https://reviewcloud.net" target="_blank" rel="noopener noreferrer">ReviewCloud</a>
      <span style="color: rgba(255,255,255,0.2);">•</span>
      <a href="mailto:help@appengine.fun">help@appengine.fun</a>
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


OG_LOCALES = {
    "en": "en_US",
    "zh-Hant": "zh_TW",
    "zh-Hans": "zh_CN",
    "ja": "ja_JP",
    "ko": "ko_KR",
    "es": "es_ES",
}


def build_schema(lang: str) -> str:
    owns = [
        {
            "@type": "SoftwareApplication",
            "name": "Workout Timer",
            "url": f"https://workout.appengine.fun/?lang={lang if lang in ('en','zh-Hant','zh-Hans','es') else 'en'}",
            "downloadUrl": "https://apps.apple.com/app/id6811742209",
            "applicationCategory": "HealthAndFitnessApplication",
            "operatingSystem": "iOS, iPadOS, watchOS, tvOS",
            "isAccessibleForFree": True,
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        }
    ]
    for a in LANG_APPS:
        owns.append({
            "@type": "SoftwareApplication",
            "name": a["name"],
            "url": a["website"],
            "downloadUrl": a["appstore"],
            "applicationCategory": "EducationApplication",
            "operatingSystem": "iOS 17.0+, iPadOS 17.0+",
            "isAccessibleForFree": True,
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        })
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": "https://appengine.fun/#organization",
                "name": "AE Interactive",
                "url": "https://appengine.fun/",
                "logo": "https://appengine.fun/images/brand_logo_v2.png",
                "sameAs": [
                    "https://www.youtube.com/@appengine-a",
                    "https://languages.appengine.fun/",
                ],
                "description": languages[lang]["hero_sub"],
                "owns": owns,
            },
            {
                "@type": "WebSite",
                "@id": "https://appengine.fun/#website",
                "name": "AE Interactive",
                "url": "https://appengine.fun/",
                "inLanguage": list(LANG_ORDER),
                "publisher": {"@id": "https://appengine.fun/#organization"},
            },
        ],
    }, ensure_ascii=False)


def build_lang_cards(lang: str) -> str:
    t = languages[lang]
    cards = []
    for a in LANG_APPS:
        cards.append(f"""
        <div class="lang-mini" style="--mini-accent: {a['accent']};">
          <div>
            <div class="lang-mini-head">
              <img src="/images/icon_{a['slug']}.webp" alt="{a['name']}" width="44" height="44">
              <div>
                <div class="lang-mini-name">{a['name']}</div>
                <div class="lang-mini-ver">{a['flag']} v{a['version']}</div>
              </div>
            </div>
            <div class="lang-mini-sub" style="margin-top: 10px;">{a['sub'][lang]}</div>
          </div>
          <div class="lang-mini-links">
            <a class="mini-btn store" href="{a['appstore']}" target="_blank" rel="noopener noreferrer">{t['btn_store_short']}</a>
            <a class="mini-btn" href="{a['website']}/?lang={lang}" target="_blank" rel="noopener noreferrer">{t['btn_site_short']}</a>
          </div>
        </div>""")
    return "".join(cards)


def gen_html(lang: str) -> str:
    colors = {f"c_{k.lower().replace('-', '_')}": ('var(--text-main)' if lang == k else 'var(--text-muted)') for k in LANG_ORDER}
    workout_lang = lang if lang in ("en", "zh-Hant", "zh-Hans", "es") else "en"
    canonical_url = "https://appengine.fun/" if lang == "en" else f"https://appengine.fun/?lang={lang}"
    og_locale = OG_LOCALES[lang]
    og_locale_alts = "".join(
        f'  <meta property="og:locale:alternate" content="{OG_LOCALES[k]}">\n'
        for k in LANG_ORDER if k != lang
    )
    rendered = html_template.format(
        lang_code=lang,
        canonical_url=canonical_url,
        og_locale=og_locale,
        og_locale_alts=og_locale_alts,
        t=languages[lang],
        workout_lang=workout_lang,
        schema_json=build_schema(lang),
        lang_cards_html=build_lang_cards(lang),
        **colors,
    )
    rendered = rendered.replace("<head>", f"<head>\n  {gtm_head}", 1)
    rendered = rendered.replace("<body>", f"<body>\n  {gtm_body}", 1)
    return rendered


for code in LANG_ORDER:
    out_name = "index.html" if code == "en" else f"index_{code}.html"
    with open(f"public/{out_name}", "w", encoding="utf-8") as f:
        f.write(gen_html(code))

print(f"Generated 6-language AE Interactive studio templates ({', '.join(LANG_ORDER)}) with 6 live apps.")
