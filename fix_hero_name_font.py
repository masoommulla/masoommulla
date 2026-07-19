import re
import sys

# Read hero banner SVGs
for fname in ['banner-hacker.svg', 'banner-hacker-light.svg']:
    with open(fname, 'r', encoding='utf-8') as f:
        svg = f.read()

    # Replace old Comic Sans / cursive font-family on the MASOOM name (both shadow + main)
    # Pattern: font-family="'Comic Sans MS', 'Brush Script MT', cursive, sans-serif" font-style="italic" font-size="65"
    old_font_attr = """font-family="'Comic Sans MS', 'Brush Script MT', cursive, sans-serif" font-style="italic" font-size="65" font-weight="bold\""""
    new_font_attr = """font-family="Black Ops One" font-size="65" font-weight="bold\""""
    svg = svg.replace(old_font_attr, new_font_attr)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Done: {fname}")

# Verify
with open('banner-hacker.svg', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(118, 124):
    print(f"{i+1}: {lines[i].strip()[:120]}")
