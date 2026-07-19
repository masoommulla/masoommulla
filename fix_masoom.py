import re
with open('lanyard-green.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

# Fix duplicate font-family on Masoom line: keep only "Black Ops One", remove old cursive family and italic
svg = re.sub(
    r'<text font-family="Black Ops One" x="96" y="0" font-family="[^"]*" font-style="italic" font-size="45" font-weight="bold" text-anchor="middle">Masoom</text>',
    '<text font-family="Black Ops One" x="96" y="0" font-size="45" font-weight="bold" text-anchor="middle" fill="#4ade80">Masoom</text>',
    svg
)

with open('lanyard-green.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
print("Fixed!")

# Check
with open('lanyard-green.svg', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'Masoom' in l:
        print(f"{i+1}: {l.strip()[:150]}")
