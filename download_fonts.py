import urllib.request
import base64
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120'}

def get_font_b64(family):
    """Download font from Google Fonts and return base64 woff2 + font-face CSS"""
    css_url = f'https://fonts.googleapis.com/css2?family={family}&display=swap'
    req = urllib.request.Request(css_url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        css = r.read().decode('utf-8')
    # Extract the woff2 URL
    match = re.search(r'url\((https://fonts\.gstatic\.com/[^\)]+\.woff2)\)', css)
    if not match:
        print(f'WARNING: no woff2 found for {family}')
        return None, None
    woff2_url = match.group(1)
    req2 = urllib.request.Request(woff2_url, headers=HEADERS)
    with urllib.request.urlopen(req2) as r2:
        font_data = r2.read()
    b64 = base64.b64encode(font_data).decode('utf-8')
    face_name = family.replace('+', ' ')
    face_css = f"@font-face{{font-family:'{face_name}';src:url('data:font/woff2;base64,{b64}') format('woff2');}}"
    print(f'Downloaded {face_name}: {len(b64)//1024}KB')
    return face_name, face_css

# Download the three fonts
black_ops_name, black_ops_css  = get_font_b64('Black+Ops+One')
audiowide_name, audiowide_css  = get_font_b64('Audiowide')
righteous_name, righteous_css  = get_font_b64('Righteous')

all_fonts_css = (black_ops_css or '') + (audiowide_css or '') + (righteous_css or '')

# Save to file for reuse
with open('fonts_embedded.txt', 'w', encoding='utf-8') as f:
    f.write(all_fonts_css)

print("All fonts saved to fonts_embedded.txt")
