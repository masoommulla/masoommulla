import re

# Fix lanyard-green.svg
with open('lanyard-green.svg', 'r', encoding='utf-8') as f:
    lanyard = f.read()

lanyard = lanyard.replace('L226 236 L194 236', 'L226 248 L194 248')
lanyard = lanyard.replace('y2="234"', 'y2="246"')
lanyard = lanyard.replace('<rect x="188" y="232"', '<rect x="188" y="244"')
lanyard = lanyard.replace('<rect x="199" y="238"', '<rect x="199" y="250"')
lanyard = lanyard.replace('<circle cx="210" cy="272"', '<circle cx="210" cy="284"')

with open('lanyard-green.svg', 'w', encoding='utf-8') as f:
    f.write(lanyard)

# Fix banner-green.svg and banner-green-light.svg
for filename in ['banner-green.svg', 'banner-green-light.svg']:
    with open(filename, 'r', encoding='utf-8') as f:
        banner = f.read()
    
    # The quote box: <rect x="48" y="262" width="380" height="72" rx="8" fill="#021406" stroke="#166534" stroke-width="1"
    banner = banner.replace('stroke="#166534" stroke-width="1"', 'stroke="#10b981" stroke-width="2" filter="url(#glow)"')
    # The snippet box: <rect x="552" y="40" width="286" height="212" rx="12" fill="#021406" fill-opacity=".94" stroke="#166534"
    # Wait, earlier I replaced #3b2a5c with #166534, but maybe it wasn't exact. Let's just use regex to add the glow.
    banner = re.sub(r'(<rect x="552" y="40" width="286" height="212" rx="12" fill="[^"]+" fill-opacity="[^"]+" stroke="[^"]+")', r'\1 filter="url(#glow)" stroke-width="2"', banner)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(banner)

# Fix README.md indentation and add green glow table styles
readme = """<div align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="banner-green.svg?v=11">
        <source media="(prefers-color-scheme: light)" srcset="banner-green-light.svg?v=11">
        <img alt="Animated GitHub Banner" src="banner-green.svg?v=11">
    </picture>
</div>

<br/>

<div align="center">
<table border="0" style="border: none;">
<tr style="border: none;">
<td width="35%" align="center" style="border: none; background: transparent;">
<img src="lanyard-green.svg?v=11" alt="Swinging Lanyard" width="300">
</td>
<td width="65%" valign="top" style="border: none; background: transparent;">
<br/>
<h3>👨‍💻 About Me</h3>
<p>I am an aspiring web developer and UI/UX designer from Gokak, Karnataka. Currently in my pre-final year of B.E. in Computer Science with a deep passion for modern web development. I love exploring the development ecosystem by building projects through "vibe coding" and continuously experimenting with new tools.</p>
<br/>
<h3>🎓 Education</h3>
<table width="100%" border="1" bordercolor="#4ade80" style="border: 2px solid #4ade80; box-shadow: 0 0 15px #4ade80; border-radius: 8px;">
<tr>
<th>Degree</th>
<th>Institution</th>
<th>Year</th>
</tr>
<tr>
<td>B.E. Computer Science</td>
<td>KLECET Chikodi</td>
<td>2023 - 2027</td>
</tr>
<tr>
<td>Pre-University (PUC)</td>
<td>KLE Society C.S. Angadi College</td>
<td>2020 - 2022</td>
</tr>
<tr>
<td>SSLC</td>
<td>Volart Academy High School</td>
<td>2019 - 2020</td>
</tr>
</table>
</td>
</tr>
</table>
</div>
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("Done")
