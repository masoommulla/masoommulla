with open('lanyard-green.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

# Fix avatar clipping issue
circle_tag = '<circle cx="210" cy="412" r="59" fill="none" stroke="url(#cardborder)" stroke-width="2.5"/>'
new_circle_tag = '<clipPath id="avatarClip"><circle cx="210" cy="412" r="57.5"/></clipPath>\n      <circle cx="210" cy="412" r="59" fill="none" stroke="url(#cardborder)" stroke-width="2.5"/>'
svg = svg.replace(circle_tag, new_circle_tag)

image_tag = '<image x="154" y="356"'
new_image_tag = '<image clip-path="url(#avatarClip)" x="154" y="356"'
svg = svg.replace(image_tag, new_image_tag)

with open('lanyard-green.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

# Update README.md
readme = """<div align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="banner-green.svg?v=6">
        <source media="(prefers-color-scheme: light)" srcset="banner-green-light.svg?v=6">
        <img alt="Animated GitHub Banner" src="banner-green.svg?v=6">
    </picture>
</div>

<br/>

<div align="center">
  <table border="0" style="border: none;">
    <tr style="border: none;">
      <td width="35%" align="center" style="border: none; background: transparent;">
        <img src="lanyard-green.svg?v=6" alt="Swinging Lanyard" width="300">
      </td>
      <td width="65%" valign="top" style="border: none; background: transparent;">
        <br/>
        <h3>👨‍💻 About Me</h3>
        <p>I am an aspiring web developer and UI/UX designer from Gokak, Karnataka. Currently in my pre-final year of B.E. in Computer Science with a deep passion for modern web development. I love exploring the development ecosystem by building projects through "vibe coding" and continuously experimenting with new tools.</p>
        
        <br/>
        <h3>🎓 Education</h3>
        <table width="100%">
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
