import os
import re
from html.parser import HTMLParser

class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attrs_dict = dict(attrs)
            href = attrs_dict.get("href")
            if href:
                self.links.append(href)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
dist_dir = os.path.join(PROJECT_DIR, "dist")
html_files = [f for f in os.listdir(dist_dir) if f.endswith(".html")]

broken_links_count = 0
total_links_checked = 0

print("=== VERIFYING WEBSITE LINKS ===")
for html_file in html_files:
    file_path = os.path.join(dist_dir, html_file)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    collector = LinkCollector()
    collector.feed(content)

    print(f"\nChecking {html_file}...")
    for link in collector.links:
        # Ignore external links, anchors, mailto, tel, whatsapp
        if link.startswith("http") or link.startswith("mailto:") or link.startswith("tel:") or link.startswith("#"):
            continue
            
        total_links_checked += 1
        
        # Clean query parameters or hash anchors from link
        link_clean = link.split("?")[0].split("#")[0]
        
        if not link_clean:
            continue
            
        target_path = os.path.join(dist_dir, link_clean)
        
        # Check if the linked file exists in the dist folder
        if not os.path.exists(target_path):
            print(f"  ❌ Broken Link Found: '{link}' points to non-existent file.")
            broken_links_count += 1
        else:
            # Check passing
            pass

print(f"\n=== VERIFICATION SUMMARY ===")
print(f"Total HTML files checked: {len(html_files)}")
print(f"Total internal links checked: {total_links_checked}")
print(f"Total broken links: {broken_links_count}")

if broken_links_count == 0:
    print("✅ SUCCESS: All internal links are working perfectly!")
else:
    print("❌ ERROR: Broken links detected. Please resolve.")
