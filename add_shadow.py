import re

gradient_def = """<radialGradient id="floorShadow" cx="50%" cy="50%" r="50%">
  <stop offset="0%" stop-color="#000000" stop-opacity="0.9"/>
  <stop offset="60%" stop-color="#000000" stop-opacity="0.4"/>
  <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
</radialGradient>
"""

shadow_ellipse = '<ellipse cx="1001" cy="670" rx="240" ry="22" fill="url(#floorShadow)"/>\n'

for filename in ['banner-green.svg', 'banner-green-light.svg']:
    with open(filename, 'r', encoding='utf-8') as f:
        svg = f.read()

    # Add radial gradient to defs
    if '<defs>' in svg:
        svg = svg.replace('<defs>', '<defs>\n' + gradient_def)

    # 1. Stop floating animation (remove class="fl")
    # We find `<g class="fl">` right before `<g clip-path="url(#girlReveal)">`
    svg = svg.replace('<g class="fl">\n<g clip-path="url(#girlReveal)">', '<g>\n<g clip-path="url(#girlReveal)">')
    # If the file uses \r\n instead:
    svg = svg.replace('<g class="fl">\r\n<g clip-path="url(#girlReveal)">', '<g>\r\n<g clip-path="url(#girlReveal)">')
    
    # Just in case it's on the same line or differently formatted:
    svg = re.sub(r'<g class="fl">\s*<g clip-path="url\(#girlReveal\)">', '<g>\n<g clip-path="url(#girlReveal)">', svg)

    # 2. Add realistic floor shadow behind the avatar
    # The avatar section starts with <circle cx="1000" cy="440" ... girlGlow ...>
    # We can place the ellipse right after that circle so it's behind the avatar.
    target_circle = '<circle cx="1000" cy="440" r="270" fill="url(#girlGlow)"><animate attributeName="r" values="270;292;270" dur="5s" repeatCount="indefinite"/></circle>'
    if target_circle in svg:
        svg = svg.replace(target_circle, target_circle + '\n' + shadow_ellipse)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)

# Also bump the ?v=6 to ?v=7 in README.md to ensure it loads
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
readme = re.sub(r'v=\d+', 'v=7', readme)
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("Done")
