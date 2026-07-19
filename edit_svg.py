import base64

def get_b64(filepath):
    with open(filepath, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

with open('megha-banner.svg', 'r', encoding='utf-8') as f:
    banner = f.read()

with open('megha-lanyard.svg', 'r', encoding='utf-8') as f:
    lanyard = f.read()

# Replace handles and text in banner
banner = banner.replace('Megha Mittal — Frontend Developer', 'Masoom Mulla — Full Stack Developer')
banner = banner.replace('megha@frontend-developer', 'masoom@developer')
banner = banner.replace('Meghamittal0920', 'masoommulla')
banner = banner.replace('meghamittal563@gmail.com', 'masoommulla14@gmail.com')
banner = banner.replace('meghamittal92000', 'masoommulla')

# Remove stats card
start_stats = '<!-- Stats card -->'
end_stats = '<!-- ================= RIGHT: ILLUSTRATION ================= -->'
idx_s = banner.find(start_stats)
idx_e = banner.find(end_stats)
if idx_s != -1 and idx_e != -1:
    banner = banner[:idx_s] + banner[idx_e:]

# Replace name paths with text
start_name = "<!-- Name: Megha Mittal (Pacifico outlines, per-letter pop, animated gradient) -->"
end_name = '<g class="ltr" style="animation-delay:2.50s"><path transform="translate(315.9,0) scale(0.05200,-0.05200)" d="M455 178Q455 138 436 116Q393 63 342.5 29.0Q292 -5 228 -5Q140 -5 97.5 75.0Q55 155 55 282Q55 404 86.5 560.0Q118 716 179.5 828.0Q241 940 326 940Q374 940 401.5 895.5Q429 851 429 768Q429 649 363.0 492.0Q297 335 184 181Q191 140 207.0 122.5Q223 105 249 105Q290 105 321.0 128.5Q352 152 400 209Q412 223 427 223Q440 223 447.5 211.0Q455 199 455 178ZM177 316Q248 433 290.0 550.5Q332 668 332 765Q332 841 304 841Q281 841 252.0 758.0Q223 675 201.0 552.0Q179 429 177 316Z"/></g>\n</g>'

idx1 = banner.find(start_name)
idx2 = banner.find(end_name) + len(end_name)
if idx1 != -1 and idx2 > idx1:
    masoom_name_svg = '''<!-- Name: Masoom Mulla -->
<g class="ltr" style="animation-delay:1.5s">
  <text x="48" y="165" font-family="'Comic Sans MS', 'Brush Script MT', cursive, sans-serif" font-style="italic" font-size="65" font-weight="bold" fill="url(#nameg)" filter="url(#glow)">Masoom Mulla🤍</text>
  <text x="48" y="165" font-family="'Comic Sans MS', 'Brush Script MT', cursive, sans-serif" font-style="italic" font-size="65" font-weight="bold" fill="url(#nameg)">Masoom Mulla🤍</text>
</g>'''
    banner = banner[:idx1] + masoom_name_svg + banner[idx2:]
else:
    print("Could not find name block in banner!")

# Replace the base64 image in banner
banner_img = get_b64('banner.png')
import re
img_pattern = re.compile(r'<image x="722" y="152" width="558" height="522" href="data:image/[^;]+;base64,[^"]+"')
new_img_tag = f'<image x="722" y="50" width="700" height="700" preserveAspectRatio="xMidYMid slice" href="{banner_img}"'
banner = img_pattern.sub(new_img_tag, banner)

with open('banner.svg', 'w', encoding='utf-8') as f:
    f.write(banner)
with open('banner-light.svg', 'w', encoding='utf-8') as f:
    f.write(banner)

# Now Lanyard
lanyard = lanyard.replace('Megha Mittal — swinging ID badge', 'Masoom Mulla — swinging ID badge')
lanyard = lanyard.replace('MEGHA.DEV ♥ CODE ♥ MEGHA.DEV', 'MASOOMMULLA ♥ CODE ♥ MASOOMMULLA')
lanyard = lanyard.replace('MM-0920', 'MM-14')
lanyard = lanyard.replace('FRONTEND DEVELOPER', 'FULL STACK DEVELOPER')
lanyard = lanyard.replace('@Meghamittal0920', '@masoommulla')

profile_img = get_b64('profile.png')
avatar_pattern = re.compile(r'<image x="154" y="356" width="112" height="112" href="data:image/[^;]+;base64,[^"]+"')
new_avatar_tag = f'<image x="154" y="356" width="112" height="112" preserveAspectRatio="xMidYMid slice" href="{profile_img}"'
lanyard = avatar_pattern.sub(new_avatar_tag, lanyard)

start_name2 = '<g transform="translate(114,516)" fill="url(#nameg2)" filter="url(#glow2)">'
end_name2 = '<path transform="translate(182.2,0) scale(0.03000,-0.03000)" d="M455 178Q455 138 436 116Q393 63 342.5 29.0Q292 -5 228 -5Q140 -5 97.5 75.0Q55 155 55 282Q55 404 86.5 560.0Q118 716 179.5 828.0Q241 940 326 940Q374 940 401.5 895.5Q429 851 429 768Q429 649 363.0 492.0Q297 335 184 181Q191 140 207.0 122.5Q223 105 249 105Q290 105 321.0 128.5Q352 152 400 209Q412 223 427 223Q440 223 447.5 211.0Q455 199 455 178ZM177 316Q248 433 290.0 550.5Q332 668 332 765Q332 841 304 841Q281 841 252.0 758.0Q223 675 201.0 552.0Q179 429 177 316Z"/>\n      </g>'

idx3 = lanyard.find(start_name2)
idx4 = lanyard.find(end_name2) + len(end_name2)
if idx3 != -1 and idx4 > idx3:
    masoom_lanyard_name = '''<g transform="translate(114,516)" fill="url(#nameg2)" filter="url(#glow2)">
<text x="96" y="0" font-family="'Comic Sans MS', 'Brush Script MT', cursive, sans-serif" font-style="italic" font-size="45" font-weight="bold" text-anchor="middle">Masoom</text>
</g>'''
    lanyard = lanyard[:idx3] + masoom_lanyard_name + lanyard[idx4:]
else:
    print("Could not find name block in lanyard!")

with open('lanyard.svg', 'w', encoding='utf-8') as f:
    f.write(lanyard)

print("Done generating SVGs")
