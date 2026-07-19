import re

# Load font CSS
with open('fonts_embedded.txt', 'r', encoding='utf-8') as f:
    fonts_css = f.read()

# ── Banner SVG (banner-hacker.svg + banner-hacker-light.svg) ─────────────────
for fname in ['banner-hacker.svg', 'banner-hacker-light.svg']:
    with open(fname, 'r', encoding='utf-8') as f:
        svg = f.read()

    # 1. Inject fonts into existing <style> block
    svg = svg.replace('<style>', '<style>\n' + fonts_css + '\n')

    # --- Apply Audiowide to section headings (Tech I Know, About Me) ---
    # Heading texts use fill="#10b981" or fill="#4ade80" with font-weight="bold"
    # They look like: font-size="15" fill="#10b981" font-weight="bold"
    # Replace font on those specific heading text elements
    svg = re.sub(
        r'(font-size="15" fill="#10b981" font-weight="bold")',
        r'\1 font-family="Audiowide"',
        svg
    )
    svg = re.sub(
        r'(font-size="15" fill="#4ade80" font-weight="bold")',
        r'\1 font-family="Audiowide"',
        svg
    )

    # --- Apply Righteous to body/paragraph text ---
    # Body text typically has fill="#e6edf3" or fill="#cdd3dd" or fill="#86efac"
    # These are used in tech pill labels, about me lines etc.
    svg = re.sub(
        r'(font-size="13\.5")',
        r'\1 font-family="Righteous"',
        svg
    )
    svg = re.sub(
        r'(font-size="12")',
        r'\1 font-family="Righteous"',
        svg
    )

    # --- Also apply Audiowide to quote text (the featured quote box) ---
    svg = re.sub(
        r'(clip-path="url\(#q[12]\)" x="76"[^>]*font-size="15")',
        r'\1 font-family="Righteous"',
        svg
    )

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f'Fonts applied to {fname}')


# ── Lanyard SVG (lanyard-green.svg) ──────────────────────────────────────────
with open('lanyard-green.svg', 'r', encoding='utf-8') as f:
    lan = f.read()

# 1. Inject fonts
lan = lan.replace('<style>', '<style>\n' + fonts_css + '\n')

# 2. Apply Black Ops One to "Masoom" name text
# The name "Masoom" is usually a large bold green text on the card
lan = re.sub(
    r'(<text[^>]*>Masoom</text>)',
    lambda m: m.group(0).replace('<text', '<text font-family="Black Ops One"'),
    lan
)
# Also search by fill color of the name — it's typically #4ade80 large font
lan = re.sub(
    r'(font-size="32"[^>]*fill="#4ade80")',
    r'\1 font-family="Black Ops One"',
    lan
)
lan = re.sub(
    r'(fill="#4ade80"[^>]*font-size="32")',
    r'\1 font-family="Black Ops One"',
    lan
)
# Try a broader match on the big name text
lan = re.sub(
    r'(<text[^>]*font-size="3[0-9]"[^>]*>)(Masoom)',
    r'<text font-family="Black Ops One"\2',
    lan
)

# 3. Apply Audiowide to card headings (DEVELOPER ID, MM-14 etc.)
lan = re.sub(
    r'(font-size="8")',
    r'\1 font-family="Audiowide"',
    lan
)
lan = re.sub(
    r'(font-size="9")',
    r'\1 font-family="Audiowide"',
    lan
)
lan = re.sub(
    r'(font-size="10")',
    r'\1 font-family="Audiowide"',
    lan
)

# 4. Apply Righteous to smaller label texts
lan = re.sub(
    r'(font-size="10\.5")',
    r'\1 font-family="Righteous"',
    lan
)

with open('lanyard-green.svg', 'w', encoding='utf-8') as f:
    f.write(lan)
print('Fonts applied to lanyard-green.svg')

# Bump README version
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
readme = re.sub(r'v=\d+', 'v=15', readme)
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
print('README version bumped')
