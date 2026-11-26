import os
import base64
import json
import urllib.request

base_dir = os.path.dirname(os.path.abspath(__file__))

# Read all images from public
IMAGES = {}
public_dir = os.path.join(base_dir, "public")
for fname in sorted(os.listdir(public_dir)):
    if fname.endswith(('.png', '.svg', '.jpg', '.jpeg', '.webp')):
        with open(os.path.join(public_dir, fname), "rb") as f:
            IMAGES[fname] = base64.b64encode(f.read()).decode('utf-8')
print("Bundling images:", list(IMAGES.keys()))

# Read all 6 language pages
PAGES = {}
for code in ("en", "zh-Hant", "zh-Hans", "ja", "ko", "es"):
    fname = "index.html" if code == "en" else f"index_{code}.html"
    with open(os.path.join(base_dir, "public", fname), "r", encoding="utf-8") as f:
        PAGES[code] = f.read()

sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://appengine.fun/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://appengine.fun/?lang=en"/>
    <xhtml:link rel="alternate" hreflang="zh-Hant" href="https://appengine.fun/?lang=zh-Hant"/>
    <xhtml:link rel="alternate" hreflang="zh-Hans" href="https://appengine.fun/?lang=zh-Hans"/>
    <xhtml:link rel="alternate" hreflang="ja" href="https://appengine.fun/?lang=ja"/>
    <xhtml:link rel="alternate" hreflang="ko" href="https://appengine.fun/?lang=ko"/>
    <xhtml:link rel="alternate" hreflang="es" href="https://appengine.fun/?lang=es"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://appengine.fun/"/>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""

robots_txt = """User-agent: *
Allow: /
Sitemap: https://appengine.fun/sitemap.xml
"""

worker_js = f"""
const IMAGES = {json.dumps(IMAGES)};
const PAGES = {json.dumps(PAGES)};

function base64ToUint8Array(base64) {{
  const binaryString = atob(base64);
  const len = binaryString.length;
  const bytes = new Uint8Array(len);
  for (let i = 0; i < len; i++) {{
    bytes[i] = binaryString.charCodeAt(i);
  }}
  return bytes;
}}

function resolveLang(request) {{
  const url = new URL(request.url);
  const param = url.searchParams.get("lang");
  if (param && PAGES[param]) return param;
  if (param === "zh" || param === "tw" || param === "hk" || param === "zh-TW") return "zh-Hant";
  if (param === "cn" || param === "zh-CN") return "zh-Hans";
  if (param === "jp" || param === "ja-JP") return "ja";
  if (param === "kr" || param === "ko-KR") return "ko";
  if (param === "es-ES" || param === "es-MX") return "es";

  const accept = (request.headers.get("accept-language") || "").toLowerCase();
  if (accept.includes("zh-tw") || accept.includes("zh-hk") || accept.includes("zh-hant")) return "zh-Hant";
  if (accept.includes("zh")) return "zh-Hans";
  if (accept.includes("ja")) return "ja";
  if (accept.includes("ko")) return "ko";
  if (accept.includes("es")) return "es";
  return "en";
}}

export default {{
  async fetch(request, env, ctx) {{
    const url = new URL(request.url);
    const pathname = url.pathname;

    if (pathname === "/sitemap.xml") {{
      return new Response(`{sitemap_xml}`, {{
        headers: {{ "content-type": "application/xml;charset=UTF-8", "cache-control": "public, max-age=86400" }}
      }});
    }}

    if (pathname === "/robots.txt") {{
      return new Response(`{robots_txt}`, {{
        headers: {{ "content-type": "text/plain;charset=UTF-8", "cache-control": "public, max-age=86400" }}
      }});
    }}

    if (pathname.startsWith("/images/")) {{
      const filename = pathname.replace("/images/", "");
      if (IMAGES[filename]) {{
        const bytes = base64ToUint8Array(IMAGES[filename]);
        const contentType = filename.endsWith(".svg")
          ? "image/svg+xml"
          : filename.endsWith(".webp")
          ? "image/webp"
          : filename.endsWith(".jpg") || filename.endsWith(".jpeg")
          ? "image/jpeg"
          : "image/png";
        return new Response(bytes, {{
          headers: {{
            "content-type": contentType,
            "cache-control": "public, max-age=31536000, immutable"
          }}
        }});
      }}
      return new Response("Image Not Found", {{ status: 404 }});
    }}

    const lang = resolveLang(request);
    const html = PAGES[lang] || PAGES["en"];
    return new Response(html, {{
      headers: {{
        "content-type": "text/html;charset=UTF-8",
        "cache-control": "public, max-age=0, must-revalidate",
        "vary": "Accept-Language"
      }}
    }});
  }}
}};
"""

with open("worker.js", "w", encoding="utf-8") as f:
    f.write(worker_js)

print(f"Built worker.js ({len(worker_js) / 1024:.1f} KB)")

token = os.environ.get("CF_API_TOKEN", "")
if not token and os.path.exists(os.path.expanduser("~/.cf_token")):
    with open(os.path.expanduser("~/.cf_token"), "r") as f:
        token = f.read().strip()
account_id = "9fb3b494e6d4d659f2cf567efb94fc38"
script_name = "aeinteractive-site"
url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts/{script_name}"

boundary = "----WebKitFormBoundary"
body = [
    f"--{boundary}".encode(),
    b'Content-Disposition: form-data; name="metadata"',
    b'Content-Type: application/json',
    b'',
    json.dumps({"main_module": "index.js", "compatibility_date": "2024-03-03"}).encode(),
    f"--{boundary}".encode(),
    b'Content-Disposition: form-data; name="index.js"; filename="index.js"',
    b'Content-Type: application/javascript+module',
    b'',
    worker_js.encode(),
    f"--{boundary}--".encode(),
    b'',
]
payload = b"\r\n".join(body)

req = urllib.request.Request(url, data=payload, method="PUT", headers={
    "Authorization": f"Bearer {token}",
    "Content-Type": f"multipart/form-data; boundary={boundary}"
})

with urllib.request.urlopen(req, timeout=45) as resp:
    res = json.loads(resp.read().decode())
    assert res.get("success"), f"Deploy failed: {res}"
    print("WORKER_UPLOADED:", script_name)
