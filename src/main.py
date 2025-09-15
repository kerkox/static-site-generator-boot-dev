import shutil
import os

PUBLIC_DIR = "public"
STATIC_DIR = "static"

def main():
  clean_public_dir()
  copy_static_files_to_public_dir()


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