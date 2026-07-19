import re

for filename in ['banner-green.svg', 'banner-green-light.svg']:
    with open(filename, 'r', encoding='utf-8') as f:
        svg = f.read()

    # Remove the animation from the classes
    svg = re.sub(r'\.fl\{[^\}]+\}', '.fl{}', svg)
    svg = re.sub(r'\.fl2\{[^\}]+\}', '.fl2{}', svg)
    
    # Just in case, let's also remove the class attribute if possible
    svg = svg.replace('<g class="fl">', '<g>')
    svg = svg.replace('<g class="fl2">', '<g>')
    
    # And check the shadow ellipse
    if 'url(#floorShadow)' not in svg:
        print(f"Warning: floor shadow missing in {filename}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)

# Bump version number in README.md to v=12
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
readme = re.sub(r'v=\d+', 'v=12', readme)
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("Animations removed!")
