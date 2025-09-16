import shutil
import os
import sys

from generate_page import generate_page

PUBLIC_DIR = "docs"
STATIC_DIR = "static"

CONTENT_MARKDOWN = "content"
TEMPLATE_HTML = "template.html"
OUTPUT_HTML = PUBLIC_DIR

BASE_PATH = sys.argv[1] if len(sys.argv) > 1 else "/"

def main():
  clean_public_dir()
  copy_static_files_to_public_dir()
  generate_page_recursive(CONTENT_MARKDOWN, TEMPLATE_HTML, OUTPUT_HTML, BASE_PATH)

def generate_page_recursive(content_md: str, template_html: str, output_html: str, base_path: str = "/"):
    if not os.path.exists(content_md):
        print(f"Content markdown file {content_md} does not exist.")
        return
    try:
        if not os.path.exists(output_html):
            os.makedirs(output_html)
        for item in os.listdir(content_md):
            s = os.path.join(content_md, item)
            d = os.path.join(output_html, item.replace('.md', '.html'))
            if os.path.isdir(s):
                generate_page_recursive(s, template_html, d)
            elif s.endswith('.md'):
                generate_page(s, template_html, d, base_path)
    except OSError as e:
        print(f"Error creating directories for {output_html}: {e}")
        return

def copy_static_files_to_public_dir():
    if not os.path.exists(STATIC_DIR):
        print(f"Static directory {STATIC_DIR} does not exist, skipping copy.")
        return
    try:
        copy_file_recursive(STATIC_DIR, PUBLIC_DIR)
    except OSError as e:
        print(f"Error copying directory {STATIC_DIR} to {PUBLIC_DIR}: {e}")

def copy_file_recursive(src: str, dest: str):
    try:
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dest, item)
            if os.path.isdir(s):
                copy_file_recursive(s, d)
            else:
                print("Copying file:", s, "to", d)
                if not os.path.exists(dest):
                    os.makedirs(dest)
                shutil.copy2(s, d)
    except OSError as e:
        print(f"Error copying file {src} to {dest}: {e}")

def clean_public_dir():
  absolute_public_dir = os.path.abspath(PUBLIC_DIR)
  if not os.path.exists(absolute_public_dir):
    os.makedirs(absolute_public_dir)
    return
  try:
    shutil.rmtree(absolute_public_dir)
  except OSError as e:
    print(f"Error deleting directory {absolute_public_dir}: {e}")


main()