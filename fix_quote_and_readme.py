import re

# ── 1. Fix the quote in banner SVGs ──────────────────────────────────────────
old_line1 = '<text clip-path="url(#q1)" x="76" y="292" font-size="15" fill="#e6edf3">Building scalable web apps,</text>'
new_line1 = '<text clip-path="url(#q1)" x="76" y="292" font-size="15" fill="#e6edf3">Crafting sleek frontends,</text>'

old_line2 = '<text clip-path="url(#q2)" x="76" y="318" font-size="15"><tspan fill="#e6edf3">I </tspan><tspan fill="#4ade80" font-weight="bold">code</tspan><tspan fill="#e6edf3"> anime.</tspan></text>'
new_line2 = '<text clip-path="url(#q2)" x="76" y="318" font-size="15"><tspan fill="#e6edf3">one </tspan><tspan fill="#4ade80" font-weight="bold">pixel</tspan><tspan fill="#e6edf3"> at a time.</tspan></text>'

for filename in ['banner-hacker.svg', 'banner-hacker-light.svg']:
    with open(filename, 'r', encoding='utf-8') as f:
        svg = f.read()
    
    svg = svg.replace(old_line1, new_line1)
    svg = svg.replace(old_line2, new_line2)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f'Quote fixed in {filename}')


# ── 2. Fix README: use SVG icons + green glow table ──────────────────────────
readme = """<div align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="banner-hacker.svg?v=14">
        <source media="(prefers-color-scheme: light)" srcset="banner-hacker-light.svg?v=14">
        <img alt="Animated GitHub Banner" src="banner-hacker.svg?v=14">
    </picture>
</div>

<br/>

<div align="center">
<table border="0" cellspacing="0" cellpadding="0" style="border: none; background: transparent;">
<tr>
<td width="35%" align="center" valign="top" style="border: none; background: transparent; padding: 16px;">
<img src="lanyard-green.svg?v=11" alt="Developer ID Card" width="300">
</td>
<td width="65%" valign="top" style="border: none; background: transparent; padding: 16px;">

<h3>
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Technologist.png" width="28" align="absmiddle" alt="dev"/>
&nbsp; About Me
</h3>

<p>
I am an aspiring web developer and UI/UX designer from Gokak, Karnataka.
Currently in my pre-final year of B.E. in Computer Science with a deep passion for
modern web development. I love exploring the development ecosystem by building
projects through "vibe coding" and continuously experimenting with new tools.
</p>

<br/>

<h3>
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Graduation%20Cap.png" width="28" align="absmiddle" alt="edu"/>
&nbsp; Education
</h3>

<table width="100%" style="border-collapse: separate; border-spacing: 0; border: 2px solid #4ade80; border-radius: 8px; overflow: hidden; box-shadow: 0 0 16px #22c55e;">
<thead>
<tr style="background-color: #052e16;">
<th align="center" style="padding: 8px 12px; border: 1px solid #4ade80; color: #4ade80;">Degree</th>
<th align="center" style="padding: 8px 12px; border: 1px solid #4ade80; color: #4ade80;">Institution</th>
<th align="center" style="padding: 8px 12px; border: 1px solid #4ade80; color: #4ade80;">Year</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center" style="padding: 8px 12px; border: 1px solid #4ade80;">B.E. Computer Science</td>
<td align="center" style="padding: 8px 12px; border: 1px solid #4ade80;">KLECET Chikodi</td>
<td align="center" style="padding: 8px 12px; border: 1px solid #4ade80;">2023 - 2027</td>
</tr>
<tr>
<td align="center" style="padding: 8px 12px; border: 1px solid #4ade80;">Pre-University (PUC)</td>
<td align="center" style="padding: 8px 12px; border: 1px solid #4ade80;">KLE Society C.S. Angadi College</td>
<td align="center" style="padding: 8px 12px; border: 1px solid #4ade80;">2020 - 2022</td>
</tr>
<tr>
<td align="center" style="padding: 8px 12px; border: 1px solid #4ade80;">SSLC</td>
<td align="center" style="padding: 8px 12px; border: 1px solid #4ade80;">Volart Academy High School</td>
<td align="center" style="padding: 8px 12px; border: 1px solid #4ade80;">2019 - 2020</td>
</tr>
</tbody>
</table>

</td>
</tr>
</table>
</div>
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
print("README updated!")
