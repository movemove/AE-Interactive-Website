import os
import base64
import json
import urllib.request

base_dir = os.path.dirname(os.path.abspath(__file__))

# Read all images from public
IMAGES = {}
public_dir = os.path.join(base_dir, "public")
for fname in os.listdir(public_dir):
    if fname.endswith(('.png', '.svg', '.jpg', '.jpeg', '.webp')):
        with open(os.path.join(public_dir, fname), "rb") as f:
            IMAGES[fname] = base64.b64encode(f.read()).decode('utf-8')
print("Bundling images:", list(IMAGES.keys()))

# Read pages
PAGES = {}
with open(os.path.join(base_dir, "public", "index.html"), "r", encoding="utf-8") as f:
    PAGES["en"] = f.read()

with open(os.path.join(base_dir, "public", "index_zh-Hant.html"), "r", encoding="utf-8") as f:
    PAGES["zh-Hant"] = f.read()
with open(os.path.join(base_dir, "public", "index_zh-Hans.html"), "r", encoding="utf-8") as f:
    PAGES["zh-Hans"] = f.read()
with open(os.path.join(base_dir, "public", "index_es.html"), "r", encoding="utf-8") as f:
    PAGES["es"] = f.read()


sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://appengine.fun/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://appengine.fun/?lang=en"/>
    <xhtml:link rel="alternate" hreflang="zh-Hant" href="https://appengine.fun/?lang=zh-Hant"/>
    <xhtml:link rel="alternate" hreflang="zh-Hans" href="https://appengine.fun/?lang=zh-Hans"/>
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
  if (param === "zh" || param === "tw" || param === "hk") return "zh-Hant";
  if (param === "cn") return "zh-Hans";

  const accept = (request.headers.get("accept-language") || "").toLowerCase();
  if (accept.includes("zh-tw") || accept.includes("zh-hk") || accept.includes("zh-hant")) return "zh-Hant";
  if (accept.includes("zh")) return "zh-Hans";
  if (accept.includes("es")) return "es";
  return "en";
}}

export default {{
  async fetch(request, env, ctx) {{
    const url = new URL(request.url);
    const pathname = url.pathname;

    if (pathname === "/sitemap.xml") {{
      return new Response(`{sitemap_xml}`, {{
        headers: {{ "content-type": "application/xml", "cache-control": "public, max-age=86400" }}
      }});
    }}
    
    if (pathname === "/robots.txt") {{
      return new Response(`{robots_txt}`, {{
        headers: {{ "content-type": "text/plain", "cache-control": "public, max-age=86400" }}
      }});
    }}

    if (pathname.startsWith("/images/")) {{
      const filename = pathname.replace("/images/", "");
      if (IMAGES[filename]) {{
        const bytes = base64ToUint8Array(IMAGES[filename]);
        const contentType = filename.endsWith(".svg") ? "image/svg+xml" : "image/png";
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
        "cache-control": "public, max-age=60"
      }}
    }});
  }}
}};
"""

with open("worker.js", "w", encoding="utf-8") as f:
    f.write(worker_js)

import os
token = os.environ.get("CF_API_TOKEN", "")
account_id = "9fb3b494e6d4d659f2cf567efb94fc38"
script_name = "aeinteractive-site"
url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts/{script_name}"

boundary = "----WebKitFormBoundary"
body = []
body.append(f"--{boundary}".encode())
body.append(b'Content-Disposition: form-data; name="metadata"')
body.append(b'Content-Type: application/json')
body.append(b'')
body.append(json.dumps({
    "main_module": "index.js",
    "compatibility_date": "2024-03-03"
}).encode())

body.append(f"--{boundary}".encode())
body.append(b'Content-Disposition: form-data; name="index.js"; filename="index.js"')
body.append(b'Content-Type: application/javascript+module')
body.append(b'')
body.append(worker_js.encode())
body.append(f"--{boundary}--".encode())
body.append(b'')
payload = b"\r\n".join(body)

req = urllib.request.Request(url, data=payload, method="PUT", headers={
    "Authorization": f"Bearer {token}",
    "Content-Type": f"multipart/form-data; boundary={boundary}"
})

try:
    with urllib.request.urlopen(req) as resp:
        print("Worker deployed successfully:", resp.read().decode())
except urllib.error.HTTPError as e:
    print("HTTPError:", e.code, e.read().decode())
