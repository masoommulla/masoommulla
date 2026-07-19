import re

for filename in ['banner-green.svg', 'banner-green-light.svg']:
    with open(filename, 'r', encoding='utf-8') as f:
        svg = f.read()
    
    # 1. Update terminal background (quote box)
    # The original was fill="#1c1230" stroke="#3b2a5c" but my previous script didn't change them if they were different.
    # Wait, my previous script left them untouched! So they are still #1c1230.
    svg = svg.replace('fill="#1c1230"', 'fill="#021406"')
    svg = svg.replace('stroke="#3b2a5c"', 'stroke="#166534"')
    
    # 2. Update Code snippet window background
    # Was fill="#160f26" and "#211538"
    svg = svg.replace('fill="#160f26"', 'fill="#021406"')
    svg = svg.replace('fill="#211538"', 'fill="#064e3b"')
    
    # 3. Text replacements for the quote
    # In case it's still 'I don't watch anime,' or 'I don't just write code,'
    svg = svg.replace("I don't just write code,", "Building scalable web apps,")
    svg = svg.replace("I don't watch anime,", "Building scalable web apps,")
    
    # Second line of quote
    svg = re.sub(r'I <tspan fill="[^"]+" font-weight="bold">craft</tspan><tspan fill="[^"]+"> experiences\.</tspan>', 'With a <tspan fill="#4ade80" font-weight="bold">passion</tspan><tspan fill="#e6edf3"> for engineering.</tspan>', svg)
    svg = re.sub(r'I <tspan fill="[^"]+" font-weight="bold">code</tspan><tspan fill="[^"]+"> anime\.</tspan>', 'With a <tspan fill="#4ade80" font-weight="bold">passion</tspan><tspan fill="#e6edf3"> for engineering.</tspan>', svg)
    
    # 4. Remove any remaining purple/pink from other elements (like the bit heart)
    svg = svg.replace('#ff7eb6', '#4ade80')
    svg = svg.replace('#c084fc', '#10b981')
    svg = svg.replace('#8b5cf6', '#059669')
    svg = svg.replace('#e879f9', '#22c55e')
    svg = svg.replace('#f9a8d4', '#86efac')
    svg = svg.replace('#a855f7', '#22c55e') # purple bit graphic
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)

print("Done")
