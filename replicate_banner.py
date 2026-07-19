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

# Use Transperant.png as the main avatar
b64_image = get_base64_image("Transperant.png")

banner_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="740" viewBox="0 0 1280 740">
    <defs>
        <!-- Glow filters -->
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="6" result="blur" />
            <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
        <filter id="glow-light" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3" result="blur" />
            <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
        
        <!-- Gradients -->
        <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#ff71ce" />
            <stop offset="100%" stop-color="#b967ff" />
        </linearGradient>
        <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0a0310" />
            <stop offset="100%" stop-color="#19092b" />
        </linearGradient>
        
        <style>
            .title {{ font-family: 'Segoe UI', sans-serif; font-size: 32px; fill: #ffffff; font-weight: 700; }}
            .name {{ font-family: 'Brush Script MT', 'Comic Sans MS', cursive; font-size: 85px; fill: url(#name-grad); font-weight: bold; filter: url(#glow-light); }}
            .terminal {{ font-family: 'Fira Code', 'Consolas', monospace; font-size: 16px; }}
            .terminal-top {{ font-family: 'Fira Code', 'Consolas', monospace; font-size: 18px; }}
            .text-sm {{ font-family: 'Segoe UI', sans-serif; font-size: 16px; fill: #a596bb; }}
            .text-md {{ font-family: 'Segoe UI', sans-serif; font-size: 20px; fill: #d1c5e5; font-weight: 600; }}
            
            @keyframes scanline {{
                0% {{ transform: translateY(-20px); }}
                100% {{ transform: translateY(760px); }}
            }}
            .scan {{
                width: 1280px;
                height: 6px;
                background: linear-gradient(to right, transparent, #ff71ce, transparent);
                opacity: 0.8;
                animation: scanline 4s linear infinite;
            }}
            
            @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
            .cursor {{ animation: blink 1s step-end infinite; }}
        </style>
    </defs>

    <!-- Background -->
    <rect width="1280" height="740" fill="url(#bg-grad)" />
    
    <!-- Outer Border -->
    <rect x="15" y="15" width="1250" height="710" rx="20" fill="none" stroke="#ff71ce" stroke-width="2" stroke-opacity="0.2" />

    <!-- Ambient floaties -->
    <text x="450" y="140" fill="#ff71ce" opacity="0.6" font-size="24">✨</text>
    <text x="800" y="320" fill="#b967ff" opacity="0.4" font-size="30">👾</text>
    <text x="1220" y="350" fill="#ff71ce" opacity="0.8" font-size="36" filter="url(#glow-light)">❤</text>

    <!-- Terminal Line -->
    <text x="45" y="60" class="terminal-top">
        <tspan fill="#50fa7b">masoom@developer:</tspan><tspan fill="#8be9fd">~$</tspan> <tspan fill="#f8f8f2">cat </tspan><tspan fill="#ff79c6">README.md</tspan> <tspan fill="#50fa7b" class="cursor">█</tspan>
    </text>

    <!-- Greeting -->
    <text x="45" y="115" class="title">Hi, I'm 👋</text>
    
    <!-- Name -->
    <text x="45" y="200" class="name">Masoom Mulla<tspan font-family="sans-serif" font-size="55" fill="#ff71ce">🤍</tspan></text>

    <!-- Subtitle -->
    <text x="45" y="260" class="terminal-top" fill="#b967ff" font-weight="bold" letter-spacing="1">&lt; Full Stack Developer /&gt;</text>

    <!-- Quote Box -->
    <g transform="translate(45, 290)">
        <rect width="380" height="90" rx="8" fill="none" stroke="#3b2259" stroke-width="2" />
        <rect width="4" height="90" rx="2" fill="#ff71ce" filter="url(#glow-light)" />
        <text x="25" y="40" class="terminal" fill="#e2d9f3" font-weight="bold" letter-spacing="0.5">I don't watch anime,</text>
        <text x="25" y="70" class="terminal" fill="#e2d9f3" font-weight="bold" letter-spacing="0.5"><tspan fill="#ff71ce">I code</tspan> anime.</text>
    </g>

    <!-- Tech I Know -->
    <text x="45" y="420" class="text-md">🧩 Tech I Know</text>
    <g transform="translate(45, 440)">
        <!-- Row 1 -->
        <rect x="0" y="0" width="80" height="34" rx="17" fill="#150824" stroke="#e34c26" stroke-width="2" />
        <text x="40" y="22" class="text-sm" fill="#e34c26" font-weight="bold" text-anchor="middle">HTML</text>
        
        <rect x="95" y="0" width="70" height="34" rx="17" fill="#150824" stroke="#264de4" stroke-width="2" />
        <text x="130" y="22" class="text-sm" fill="#264de4" font-weight="bold" text-anchor="middle">CSS</text>
        
        <rect x="180" y="0" width="120" height="34" rx="17" fill="#150824" stroke="#f7df1e" stroke-width="2" filter="url(#glow-light)" />
        <text x="240" y="22" class="text-sm" fill="#f7df1e" font-weight="bold" text-anchor="middle">JavaScript</text>
        
        <rect x="315" y="0" width="80" height="34" rx="17" fill="#150824" stroke="#61dafb" stroke-width="2" />
        <text x="355" y="22" class="text-sm" fill="#61dafb" font-weight="bold" text-anchor="middle">React</text>
        
        <!-- Row 2 -->
        <rect x="0" y="50" width="80" height="34" rx="17" fill="#150824" stroke="#339933" stroke-width="2" />
        <text x="40" y="72" class="text-sm" fill="#339933" font-weight="bold" text-anchor="middle">Node</text>
        
        <rect x="95" y="50" width="70" height="34" rx="17" fill="#150824" stroke="#00758f" stroke-width="2" />
        <text x="130" y="72" class="text-sm" fill="#00758f" font-weight="bold" text-anchor="middle">SQL</text>
        
        <rect x="180" y="50" width="150" height="34" rx="17" fill="#150824" stroke="#b967ff" stroke-width="2" />
        <text x="255" y="72" class="text-sm" fill="#b967ff" font-weight="bold" text-anchor="middle">Responsive UI</text>
    </g>

    <!-- About Me -->
    <text x="45" y="560" class="text-md">💗 About Me</text>
    <g transform="translate(45, 590)">
        <text x="0" y="0" class="terminal" fill="#50fa7b">&gt;_</text>
        <text x="25" y="0" class="text-sm" fill="#d1c5e5">I build responsive, user-friendly and impactful web experiences.</text>
        
        <text x="0" y="30" class="text-sm">💡</text>
        <text x="25" y="30" class="text-sm" fill="#d1c5e5">Always learning, always building.</text>
        
        <text x="0" y="60" class="text-sm">🚀</text>
        <text x="25" y="60" class="text-sm" fill="#d1c5e5">Turning ideas into real world solutions.</text>
    </g>

    <!-- Static Stats Box (Matching Reference exactly) -->
    <g transform="translate(45, 680)">
        <rect width="480" height="70" rx="12" fill="#11071c" stroke="#3b2259" stroke-width="2"/>
        <text x="60" y="30" class="text-sm" fill="#a596bb" text-anchor="middle">📦 Repos</text>
        <text x="60" y="55" class="text-md" fill="#ff71ce" font-weight="bold" text-anchor="middle">8+</text>
        
        <text x="180" y="30" class="text-sm" fill="#a596bb" text-anchor="middle">💻 Commits</text>
        <text x="180" y="55" class="text-md" fill="#ff71ce" font-weight="bold" text-anchor="middle">500+</text>
        
        <text x="300" y="30" class="text-sm" fill="#a596bb" text-anchor="middle">⭐ Stars</text>
        <text x="300" y="55" class="text-md" fill="#ffb86c" font-weight="bold" text-anchor="middle">50+</text>
        
        <text x="420" y="30" class="text-sm" fill="#a596bb" text-anchor="middle">👥 Followers</text>
        <text x="420" y="55" class="text-md" fill="#b967ff" font-weight="bold" text-anchor="middle">25+</text>
    </g>

    <!-- Code Card (dreams.jsx) -->
    <g transform="translate(560, 45)">
        <rect width="360" height="230" rx="15" fill="#11071c" stroke="#3b2259" stroke-width="2"/>
        <!-- Header -->
        <rect width="360" height="35" rx="15" fill="#1a0b2e"/>
        <rect y="20" width="360" height="15" fill="#1a0b2e"/>
        <!-- Mac Dots -->
        <circle cx="20" cy="17" r="6" fill="#ff5f56"/>
        <circle cx="40" cy="17" r="6" fill="#ffbd2e"/>
        <circle cx="60" cy="17" r="6" fill="#27c93f"/>
        <text x="180" y="23" class="text-sm" text-anchor="middle" font-size="14">dreams.jsx</text>
        
        <!-- Code Content -->
        <text x="20" y="65" class="terminal" fill="#ff79c6">function <tspan fill="#50fa7b">buildDreams</tspan>() {{</text>
        <text x="35" y="88" class="terminal" fill="#ff79c6">return (</text>
        <text x="50" y="111" class="terminal" fill="#8be9fd">&lt;<tspan fill="#ffb86c">div</tspan> <tspan fill="#50fa7b">className</tspan>=<tspan fill="#f1fa8c">"dreams"</tspan>&gt;</text>
        <text x="70" y="134" class="terminal" fill="#8be9fd">&lt;<tspan fill="#bd93f9">Code</tspan> /&gt;</text>
        <text x="70" y="157" class="terminal" fill="#8be9fd">&lt;<tspan fill="#f1fa8c">Coffee</tspan> /&gt;</text>
        <text x="70" y="180" class="terminal" fill="#8be9fd">&lt;<tspan fill="#50fa7b">Success</tspan> /&gt;</text>
        <text x="50" y="203" class="terminal" fill="#8be9fd">&lt;/<tspan fill="#ffb86c">div</tspan>&gt;);</text>
        <text x="20" y="226" class="terminal" fill="#f8f8f2">}} <tspan fill="#6272a4">// export default</tspan></text>
    </g>

    <!-- Neon Sign Box -->
    <g transform="translate(950, 45)">
        <rect width="280" height="130" rx="15" fill="none" stroke="#b967ff" stroke-width="3" filter="url(#glow-light)"/>
        <text x="140" y="50" class="title" fill="#ff71ce" text-anchor="middle" filter="url(#glow)" font-size="38">&lt; / &gt;</text>
        <text x="140" y="85" class="text-md" fill="#ff71ce" text-anchor="middle" font-weight="bold" letter-spacing="3" filter="url(#glow-light)">KEEP CODING</text>
        <text x="140" y="115" class="text-md" fill="#b967ff" text-anchor="middle" font-weight="bold" letter-spacing="3" filter="url(#glow-light)">KEEP GROWING</text>
    </g>

    <!-- Avatar Image (Transperant.png zoomed and aligned to bottom right) -->
    <!-- Placing it so it acts like the character sitting on the right side -->
    <g transform="translate(700, 200)">
        <image href="{b64_image}" x="0" y="0" width="550" height="550" preserveAspectRatio="xMidYMax slice" />
    </g>

    <!-- Footer Links -->
    <g transform="translate(45, 780)">
        <!-- Wait, viewBox height is 740, this is cut off! Needs to be higher. -->
    </g>

    <!-- Adjusted Footer Links -->
    <g transform="translate(45, 765)">
        <!-- Wait, viewBox is 740, let's put footer at y=765? No, it needs to be inside 740. Let's make height 780 -->
    </g>
</svg>"""

# Fix height to 780 to fit the footer
banner_svg = banner_svg.replace('height="740"', 'height="780"').replace('viewBox="0 0 1280 740"', 'viewBox="0 0 1280 780"')
banner_svg = banner_svg.replace('<rect width="1280" height="740"', '<rect width="1280" height="780"')
banner_svg = banner_svg.replace('height="710"', 'height="750"')

footer_xml = """
    <!-- Adjusted Footer Links -->
    <g transform="translate(45, 760)">
        <text x="0" y="0" class="text-sm">🐙 github.com/masoommulla</text>
        <text x="240" y="0" class="text-sm">✉️ masoommulla</text> 
        <text x="400" y="0" class="text-sm">📷 masoommulla</text>
        
        <circle cx="680" cy="-5" r="5" fill="#50fa7b" filter="url(#glow-light)" />
        <text x="695" y="0" class="text-sm" fill="#50fa7b">open to collaborate</text>
        
        <text x="1200" y="0" class="text-sm" fill="#b967ff" text-anchor="end" font-style="italic">"Code is my art, Logic is my superpower." 🤍</text>
    </g>
"""

# Let's rebuild the scanline so it sits at the absolute very end of the SVG (over everything)
scanline_xml = """
    <!-- Full page scanline -->
    <rect x="0" y="0" width="1280" height="8" fill="rgba(255, 113, 206, 0.4)" filter="url(#glow)" style="animation: scanline 4s linear infinite; pointer-events: none;" />
</svg>"""

banner_svg = banner_svg.replace('</svg>', footer_xml + scanline_xml)

with open("banner.svg", "w", encoding="utf-8") as f:
    f.write(banner_svg)

# Since this aesthetic is purely dark mode cyberpunk, we will write banner-light.svg as a carbon copy
# so it doesn't break in light mode (it will just display the dark banner, which is standard for these designs)
with open("banner-light.svg", "w", encoding="utf-8") as f:
    f.write(banner_svg)

# Update README to make sure we just use the banner (no complex picture tags needed if they are identical, but we'll leave the picture tag as is)
print("Banner perfectly reconstructed.")
