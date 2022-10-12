import os

from ..paths import MAIN_DIR
PACKAGE_NAME = os.path.split(MAIN_DIR)[-1]
PACKAGE_NAME, MAIN_DIR

init_py_text = f'''
print("The library {PACKAGE_NAME} is importable")

__version__ = "0.1.0"

'''


def create_src_dir_n_init_file():
    global init_py_text
    # create main_package folder and init.py
    src_files_dir = os.path.join(MAIN_DIR, PACKAGE_NAME)
    if not os.path.isdir(src_files_dir):
        os.mkdir(src_files_dir)
    
    
    with open(os.path.join(src_files_dir, "__init__.py"), 'w') as f:
        f.write(init_py_text)

