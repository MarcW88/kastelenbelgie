#!/usr/bin/env python3
"""
Add JSON-LD BreadcrumbList to all HTML files based on existing HTML breadcrumbs
"""

import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser

class BreadcrumbParser(HTMLParser):
    """Parse HTML breadcrumbs to extract links and text"""
    def __init__(self):
        super().__init__()
        self.breadcrumbs = []
        self.in_breadcrumbs = False
        self.in_link = False
        self.current_href = None
        self.current_text = ""
        self.in_current = False
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "div" and attrs_dict.get("class") == "breadcrumbs-nav":
            self.in_breadcrumbs = True
        elif self.in_breadcrumbs and tag == "a":
            self.in_link = True
            self.current_href = attrs_dict.get("href", "")
            self.current_text = ""
        elif self.in_breadcrumbs and tag == "span" and "breadcrumbs-current" in attrs_dict.get("class", ""):
            self.in_current = True
            self.current_text = ""
            
    def handle_endtag(self, tag):
        if tag == "div" and self.in_breadcrumbs:
            self.in_breadcrumbs = False
        elif tag == "a" and self.in_link:
            self.breadcrumbs.append({
                "href": self.current_href,
                "text": self.current_text.strip()
            })
            self.in_link = False
        elif tag == "span" and self.in_current:
            self.breadcrumbs.append({
                "href": None,
                "text": self.current_text.strip()
            })
            self.in_current = False
            
    def handle_data(self, data):
        if self.in_link or self.in_current:
            self.current_text += data

def extract_breadcrumbs(html_content):
    """Extract breadcrumb items from HTML"""
    parser = BreadcrumbParser()
    try:
        parser.feed(html_content)
    except:
        return []
    return parser.breadcrumbs

def create_breadcrumb_jsonld(breadcrumbs, base_url="https://kastelenbelgie.be"):
    """Create JSON-LD BreadcrumbList from breadcrumb items"""
    if not breadcrumbs:
        return None
    
    items = []
    for i, crumb in enumerate(breadcrumbs, 1):
        item = {
            "@type": "ListItem",
            "position": i,
            "name": crumb["text"]
        }
        if crumb["href"]:
            # Convert relative URL to absolute
            href = crumb["href"]
            if not href.startswith("http"):
                href = f"{base_url}/{href}"
            item["item"] = href
        items.append(item)
    
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

def has_breadcrumb_jsonld(html_content):
    """Check if file already has BreadcrumbList JSON-LD"""
    return '"@type": "BreadcrumbList"' in html_content or '"@type":"BreadcrumbList"' in html_content

def add_jsonld_to_file(filepath):
    """Add BreadcrumbList JSON-LD to a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has BreadcrumbList
    if has_breadcrumb_jsonld(content):
        return False, "already has BreadcrumbList"
    
    # Skip if no breadcrumbs HTML
    if 'class="breadcrumbs-nav"' not in content:
        return False, "no breadcrumbs HTML"
    
    # Extract breadcrumbs
    breadcrumbs = extract_breadcrumbs(content)
    if not breadcrumbs:
        return False, "could not parse breadcrumbs"
    
    # Create JSON-LD
    jsonld = create_breadcrumb_jsonld(breadcrumbs)
    if not jsonld:
        return False, "could not create JSON-LD"
    
    # Format JSON-LD script tag
    jsonld_script = f'<script type="application/ld+json">\n{json.dumps(jsonld, indent=2, ensure_ascii=False)}\n</script>'
    
    # Insert before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{jsonld_script}\n</head>')
    else:
        return False, "no </head> tag found"
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True, f"{len(breadcrumbs)} items"

def main():
    print("=" * 60)
    print("Adding JSON-LD BreadcrumbList to HTML files")
    print("=" * 60)
    
    html_files = list(Path('.').glob('*.html'))
    added_count = 0
    skipped = []
    
    for filepath in sorted(html_files):
        success, message = add_jsonld_to_file(filepath)
        if success:
            print(f"  ✓ {filepath.name}: {message}")
            added_count += 1
        else:
            skipped.append((filepath.name, message))
    
    print("\n" + "-" * 60)
    print(f"Added BreadcrumbList to {added_count} files")
    print(f"Skipped {len(skipped)} files:")
    
    # Group skipped by reason
    reasons = {}
    for name, reason in skipped:
        reasons.setdefault(reason, []).append(name)
    
    for reason, files in reasons.items():
        print(f"  - {reason}: {len(files)} files")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
