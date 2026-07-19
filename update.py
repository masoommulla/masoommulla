import base64
import os
import re

def get_base64_image(filepath):
    try:
        with open(filepath, "rb") as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded}"
    except Exception as e:
        print(f"Error reading image: {e}")
        return ""

profile_b64 = get_base64_image("profile.png")

# 1. Update lanyard.svg with profile.png
with open("lanyard.svg", "r", encoding="utf-8") as f:
    lanyard_data = f.read()

# Replace the base64 string in lanyard.svg
new_lanyard_data = re.sub(r'<image href="data:image/png;base64,[^"]+"', f'<image href="{profile_b64}"', lanyard_data)

with open("lanyard.svg", "w", encoding="utf-8") as f:
    f.write(new_lanyard_data)

# 2. Fix banner.svg code snippet box height
with open("banner.svg", "r", encoding="utf-8") as f:
    banner_data = f.read()

# Replace height="200" inside the snippet box
new_banner_data = banner_data.replace('<rect width="400" height="200"', '<rect width="420" height="270"')

with open("banner.svg", "w", encoding="utf-8") as f:
    f.write(new_banner_data)

# Do same for banner-light.svg
with open("banner-light.svg", "r", encoding="utf-8") as f:
    banner_light_data = f.read()

new_banner_light_data = banner_light_data.replace('<rect width="400" height="200"', '<rect width="420" height="270"')

with open("banner-light.svg", "w", encoding="utf-8") as f:
    f.write(new_banner_light_data)

# 3. Create new README.md without stats and snake
readme_md = """<div align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="banner.svg?v=3">
        <source media="(prefers-color-scheme: light)" srcset="banner-light.svg?v=3">
        <img alt="Animated GitHub Banner" src="banner.svg?v=3">
    </picture>
</div>

<br/>

<div align="center">
    <img src="lanyard.svg?v=3" alt="Swinging Lanyard" height="400">
</div>

# masoommulla
"""
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_md)

print("Updates done.")
