import os
import glob
import re

base_dir = r"c:\Users\yooma\OneDrive\Desktop\duniahub\client\15. Celios6-WPEmbedded\celios-streamlit"

# Use forward slashes to avoid regex escape issues
logo_path_str = '"c:/Users/yooma/OneDrive/Desktop/duniahub/client/15. Celios6-WPEmbedded/celios-streamlit/assets/logo_celios.png"'

# 1. Update app.py
app_path = os.path.join(base_dir, "app.py")
with open(app_path, "r", encoding="utf-8") as f:
    app_content = f.read()

# Replace existing page_icon
if "page_icon=" in app_content:
    # Use lambda to avoid interpreting replacement string as regex
    app_content = re.sub(r'page_icon="[^"]+"', lambda m: f'page_icon={logo_path_str}', app_content)
else:
    # Inject if missing
    app_content = re.sub(r'(st\.set_page_config\([^)]+)(?=\))', lambda m: f'{m.group(1)}, page_icon={logo_path_str}', app_content)

with open(app_path, "w", encoding="utf-8") as f:
    f.write(app_content)

# 2. Update all pages
pages_path = os.path.join(base_dir, "pages", "*.py")
for page_file in glob.glob(pages_path):
    with open(page_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "page_icon=" in content:
        content = re.sub(r'page_icon="[^"]+"', lambda m: f'page_icon={logo_path_str}', content)
    else:
        # Match st.set_page_config(...) up to the closing parenthesis
        content = re.sub(r'(st\.set_page_config\([^)]+)(?=\))', lambda m: f'{m.group(1)}, page_icon={logo_path_str}', content)
        
    with open(page_file, "w", encoding="utf-8") as f:
        f.write(content)

print("Favicon CELIOS berhasil ditambahkan ke app.py dan seluruh halaman!")
