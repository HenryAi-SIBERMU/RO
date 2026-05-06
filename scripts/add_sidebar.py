import os
import glob

# Base directory
base_dir = r"c:\Users\yooma\OneDrive\Desktop\duniahub\client\15. Celios6-WPEmbedded\celios-streamlit"

# 1. Update app.py
app_path = os.path.join(base_dir, "app.py")
with open(app_path, "r", encoding="utf-8") as f:
    app_content = f.read()

if "from components.sidebar import render_sidebar" not in app_content:
    new_app_content = app_content.replace(
        "st.set_page_config(", 
        "from components.embed_layout import apply_embed_mode\nfrom components.sidebar import render_sidebar\n\nst.set_page_config("
    )
    new_app_content += "\napply_embed_mode()\nrender_sidebar()\n"
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(new_app_content)

# 2. Update all pages
pages_path = os.path.join(base_dir, "pages", "*.py")
for page_file in glob.glob(pages_path):
    with open(page_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "render_sidebar" not in content:
        # We know apply_embed_mode() is called in all pages
        content = content.replace(
            "from components.embed_layout import apply_embed_mode",
            "from components.embed_layout import apply_embed_mode\nfrom components.sidebar import render_sidebar"
        )
        content = content.replace(
            "apply_embed_mode()",
            "apply_embed_mode()\nrender_sidebar()"
        )
        
        with open(page_file, "w", encoding="utf-8") as f:
            f.write(content)

print("Berhasil menyisipkan render_sidebar() ke semua halaman!")
