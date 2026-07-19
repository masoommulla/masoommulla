import re
import xml.etree.ElementTree as ET

for filename in ['banner-green.svg', 'banner-green-light.svg']:
    with open(filename, 'r', encoding='utf-8') as f:
        svg = f.read()

    # Fix duplicate stroke-width
    svg = svg.replace('stroke-width="2" stroke-width="1.2"', 'stroke-width="2"')
    svg = svg.replace('stroke-width="2" filter="url(#glow)" stroke-width="1"', 'stroke-width="2" filter="url(#glow)"')
    # If there are others like stroke="#10b981" stroke-width="2" filter="url(#glow)" stroke-width="1"
    svg = re.sub(r'stroke-width="2"\s+filter="url\(#glow\)"\s+stroke-width="\d+"', 'stroke-width="2" filter="url(#glow)"', svg)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)
    
    # Verify XML
    try:
        ET.parse(filename)
        print(f'{filename} is valid XML now')
    except Exception as e:
        print(f'{filename} ERROR:', e)

# Bump version number in README.md to v=13
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
readme = re.sub(r'v=\d+', 'v=13', readme)
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
