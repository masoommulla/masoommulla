import base64
import os

def get_base64_image(filepath):
    try:
        with open(filepath, "rb") as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded}"
    except Exception as e:
        print(f"Error reading image: {e}")
        return ""

b64_image = get_base64_image("Transperant.png")

banner_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="740">
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#ff0080;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#7928ca;stop-opacity:1" />
        </linearGradient>
        <clipPath id="rounded">
            <rect width="1280" height="740" rx="20" ry="20"/>
        </clipPath>
        <style>
            @keyframes typing {{
                from {{ width: 0 }}
                to {{ width: 100% }}
            }}
            @keyframes blink {{
                50% {{ border-color: transparent }}
            }}
            @keyframes scanline {{
                0% {{ transform: translateY(-100%); }}
                100% {{ transform: translateY(1000%); }}
            }}
            .terminal {{
                font-family: monospace;
                font-size: 24px;
                fill: #fff;
            }}
            .name {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 80px;
                font-weight: bold;
                fill: url(#grad);
            }}
            .typewriter {{
                overflow: hidden;
                white-space: nowrap;
                border-right: .15em solid #ff0080;
                animation: typing 3.5s steps(40, end), blink .75s step-end infinite;
            }}
            .scanner {{
                width: 100%;
                height: 10px;
                background: rgba(255, 0, 128, 0.5);
                box-shadow: 0 0 10px #ff0080;
                animation: scanline 3.5s linear infinite;
            }}
        </style>
    </defs>
    
    <rect width="1280" height="740" rx="20" ry="20" fill="#0f0c29" />
    
    <!-- Terminal window -->
    <rect x="40" y="40" width="1200" height="660" rx="10" ry="10" fill="#13131a" stroke="#2d2d3d" stroke-width="2"/>
    <circle cx="70" cy="70" r="8" fill="#ff5f56"/>
    <circle cx="100" cy="70" r="8" fill="#ffbd2e"/>
    <circle cx="130" cy="70" r="8" fill="#27c93f"/>
    
    <text x="60" y="140" class="terminal" fill="#27c93f">user@dev:~$ <tspan fill="#fff">cat README.md</tspan></text>
    
    <text x="60" y="240" class="name">Hi, I'm Masoom Mulla</text>
    <text x="60" y="300" class="terminal" fill="#8892b0">Full Stack Developer | Designer | Innovator</text>
    
    <g transform="translate(60, 360)">
        <rect width="400" height="200" rx="10" fill="#1e1e2f" stroke="#3e3e5e" stroke-width="1"/>
        <text x="20" y="40" class="terminal" fill="#ff0080" font-size="18">function <tspan fill="#50fa7b">buildDreams</tspan>() {{</text>
        <text x="40" y="80" class="terminal" fill="#f1fa8c" font-size="18">  while(alive) {{</text>
        <text x="60" y="120" class="terminal" fill="#8be9fd" font-size="18">    code();</text>
        <text x="60" y="160" class="terminal" fill="#8be9fd" font-size="18">    grow();</text>
        <text x="40" y="200" class="terminal" fill="#f1fa8c" font-size="18">  }}</text>
        <text x="20" y="240" class="terminal" fill="#ff0080" font-size="18">}}</text>
    </g>
    
    <!-- Avatar with hologram effect -->
    <g transform="translate(700, 100)" clip-path="url(#rounded)">
        <image href="{b64_image}" width="500" height="500" />
        <rect width="500" height="10" fill="rgba(255, 0, 128, 0.7)" style="animation: scanline 3.5s linear infinite" />
    </g>
</svg>
"""

banner_light_svg = banner_svg.replace('fill="#0f0c29"', 'fill="#f0f0f0"').replace('fill="#13131a"', 'fill="#ffffff"').replace('fill="#fff"', 'fill="#333"')

lanyard_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="400" height="600">
    <defs>
        <style>
            @keyframes swing {{
                0% {{ transform: rotate(5deg); }}
                50% {{ transform: rotate(-5deg); }}
                100% {{ transform: rotate(5deg); }}
            }}
            .card {{
                transform-origin: top center;
                animation: swing 3s ease-in-out infinite;
            }}
        </style>
    </defs>
    <g class="card">
        <!-- Strap -->
        <path d="M150,-100 Q200,0 200,50 Q200,0 250,-100" fill="none" stroke="#ff0080" stroke-width="15"/>
        <circle cx="200" cy="50" r="15" fill="#silver"/>
        <!-- Card -->
        <rect x="50" y="70" width="300" height="450" rx="15" fill="#1a1a2e" stroke="#ff0080" stroke-width="3"/>
        <text x="200" y="120" font-family="sans-serif" font-size="24" fill="#fff" text-anchor="middle" font-weight="bold">GITHUB DEVELOPER</text>
        
        <!-- Avatar inside card -->
        <image href="{b64_image}" x="100" y="150" width="200" height="200" clip-path="circle(100px at 200px 250px)"/>
        <circle cx="200" cy="250" r="100" fill="none" stroke="#ff0080" stroke-width="4"/>
        
        <text x="200" y="400" font-family="monospace" font-size="28" fill="#fff" text-anchor="middle">@masoommulla</text>
        <rect x="100" y="450" width="200" height="30" fill="#fff"/>
        <!-- Fake barcode -->
        <path d="M110,450 v30 M115,450 v30 M120,450 v30 M125,450 v30 M135,450 v30 M140,450 v30 M150,450 v30 M160,450 v30 M165,450 v30 M170,450 v30 M180,450 v30 M190,450 v30 M195,450 v30 M200,450 v30 M210,450 v30 M220,450 v30 M230,450 v30 M235,450 v30 M245,450 v30 M250,450 v30 M260,450 v30 M270,450 v30 M275,450 v30 M280,450 v30 M290,450 v30" stroke="#000" stroke-width="2"/>
    </g>
</svg>
"""

stats_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="400" height="200">
    <rect width="400" height="200" rx="10" fill="#13131a" stroke="#2d2d3d" stroke-width="2"/>
    <text x="20" y="40" font-family="sans-serif" font-size="20" fill="#ff0080" font-weight="bold">GitHub Stats</text>
    <circle cx="80" cy="110" r="50" fill="none" stroke="#3e3e5e" stroke-width="10"/>
    <circle cx="80" cy="110" r="50" fill="none" stroke="#27c93f" stroke-width="10" stroke-dasharray="250" stroke-dashoffset="50" transform="rotate(-90 80 110)"/>
    <text x="80" y="115" font-family="sans-serif" font-size="24" fill="#fff" text-anchor="middle" font-weight="bold">S</text>
    
    <text x="160" y="90" font-family="sans-serif" font-size="16" fill="#8892b0">Total Stars: <tspan fill="#fff" font-weight="bold">1.2k</tspan></text>
    <text x="160" y="120" font-family="sans-serif" font-size="16" fill="#8892b0">Total Commits: <tspan fill="#fff" font-weight="bold">3.4k</tspan></text>
    <text x="160" y="150" font-family="sans-serif" font-size="16" fill="#8892b0">Total PRs: <tspan fill="#fff" font-weight="bold">420</tspan></text>
</svg>
"""

langs_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200">
    <rect width="300" height="200" rx="10" fill="#13131a" stroke="#2d2d3d" stroke-width="2"/>
    <text x="20" y="40" font-family="sans-serif" font-size="20" fill="#ff0080" font-weight="bold">Top Languages</text>
    
    <text x="20" y="80" font-family="sans-serif" font-size="14" fill="#fff">JavaScript</text>
    <rect x="100" y="70" width="150" height="10" rx="5" fill="#f1fa8c"/>
    
    <text x="20" y="110" font-family="sans-serif" font-size="14" fill="#fff">Python</text>
    <rect x="100" y="100" width="120" height="10" rx="5" fill="#8be9fd"/>
    
    <text x="20" y="140" font-family="sans-serif" font-size="14" fill="#fff">HTML/CSS</text>
    <rect x="100" y="130" width="90" height="10" rx="5" fill="#ff5555"/>
    
    <text x="20" y="170" font-family="sans-serif" font-size="14" fill="#fff">TypeScript</text>
    <rect x="100" y="160" width="60" height="10" rx="5" fill="#50fa7b"/>
</svg>
"""

trophies_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="400" height="200">
    <rect width="400" height="200" rx="10" fill="#13131a" stroke="#2d2d3d" stroke-width="2"/>
    <text x="20" y="40" font-family="sans-serif" font-size="20" fill="#ff0080" font-weight="bold">Trophies</text>
    
    <g transform="translate(30, 70)">
        <rect width="80" height="80" rx="10" fill="#1e1e2f" stroke="#ffbd2e" stroke-width="2"/>
        <text x="40" y="40" font-family="sans-serif" font-size="30" fill="#ffbd2e" text-anchor="middle">🏆</text>
        <text x="40" y="70" font-family="sans-serif" font-size="12" fill="#fff" text-anchor="middle">Creator</text>
    </g>
    
    <g transform="translate(130, 70)">
        <rect width="80" height="80" rx="10" fill="#1e1e2f" stroke="#27c93f" stroke-width="2"/>
        <text x="40" y="40" font-family="sans-serif" font-size="30" fill="#27c93f" text-anchor="middle">⭐</text>
        <text x="40" y="70" font-family="sans-serif" font-size="12" fill="#fff" text-anchor="middle">Star</text>
    </g>
    
    <g transform="translate(230, 70)">
        <rect width="80" height="80" rx="10" fill="#1e1e2f" stroke="#ff0080" stroke-width="2"/>
        <text x="40" y="40" font-family="sans-serif" font-size="30" fill="#ff0080" text-anchor="middle">🔥</text>
        <text x="40" y="70" font-family="sans-serif" font-size="12" fill="#fff" text-anchor="middle">Streak</text>
    </g>
</svg>
"""

with open("banner.svg", "w", encoding="utf-8") as f:
    f.write(banner_svg)
with open("banner-light.svg", "w", encoding="utf-8") as f:
    f.write(banner_light_svg)
with open("lanyard.svg", "w", encoding="utf-8") as f:
    f.write(lanyard_svg)
with open("stats.svg", "w", encoding="utf-8") as f:
    f.write(stats_svg)
with open("langs.svg", "w", encoding="utf-8") as f:
    f.write(langs_svg)
with open("trophies.svg", "w", encoding="utf-8") as f:
    f.write(trophies_svg)

readme_md = """
<div align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="banner.svg?v=1">
        <source media="(prefers-color-scheme: light)" srcset="banner-light.svg?v=1">
        <img alt="Animated GitHub Banner" src="banner.svg?v=1">
    </picture>
</div>

<br/>

<div align="center">
    <img src="lanyard.svg?v=1" alt="Swinging Lanyard" height="300" align="left">
    
    <div>
        <img src="stats.svg?v=1" alt="GitHub Stats">
        <img src="langs.svg?v=1" alt="Top Languages">
        <br/>
        <img src="trophies.svg?v=1" alt="Trophies">
    </div>
</div>

<br clear="both"/>
<br/>

<div align="center">
    <h2>Contribution Snake</h2>
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/masoommulla/masoommulla/output/github-contribution-grid-snake-dark.svg">
        <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/masoommulla/masoommulla/output/github-contribution-grid-snake.svg">
        <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/masoommulla/masoommulla/output/github-contribution-grid-snake.svg">
    </picture>
</div>
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_md)

os.makedirs(".github/workflows", exist_ok=True)
github_snake_yml = '''name: generate animation

on:
  # run automatically every 24 hours
  schedule:
    - cron: "0 */24 * * *" 
  
  # allows to manually run the job at any time
  workflow_dispatch:
  
  # run on every push on the master branch
  push:
    branches:
    - master
    - main
    
jobs:
  generate:
    permissions: 
      contents: write
    runs-on: ubuntu-latest
    timeout-minutes: 5
    
    steps:
      - name: generate github-contribution-grid-snake.svg
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          
      - name: push github-contribution-grid-snake.svg to the output branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
'''

with open(".github/workflows/github-snake.yml", "w", encoding="utf-8") as f:
    f.write(github_snake_yml)

print("Generated all files successfully.")
