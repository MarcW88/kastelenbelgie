#!/usr/bin/env python3
"""
Remove microdata attributes (itemscope, itemtype, itemprop) from HTML files
Keep only JSON-LD structured data
"""

import os
import re
from pathlib import Path

def remove_microdata_from_file(filepath):
    """Remove microdata attributes from a single HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove itemscope="" or itemscope
    content = re.sub(r'\s+itemscope=""', '', content)
    content = re.sub(r'\s+itemscope', '', content)
    
    # Remove itemtype="..." 
    content = re.sub(r'\s+itemtype="[^"]*"', '', content)
    
    # Remove itemprop="..."
    content = re.sub(r'\s+itemprop="[^"]*"', '', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("=" * 50)
    print("Removing microdata from HTML files")
    print("=" * 50)
    
    html_files = list(Path('.').glob('*.html'))
    modified_count = 0
    
    for filepath in html_files:
        if remove_microdata_from_file(filepath):
            print(f"  ✓ Cleaned: {filepath}")
            modified_count += 1
    
    print("\n" + "=" * 50)
    print(f"Modified {modified_count}/{len(html_files)} files")
    print("=" * 50)

if __name__ == "__main__":
    main()
