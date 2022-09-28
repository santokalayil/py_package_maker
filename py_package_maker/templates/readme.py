import os
import jinja2
from ..paths import MAIN_DIR

PACKAGE_NAME = os.path.split(MAIN_DIR)[-1]

README_TEMPLATE = '''
# {{ package_name }}
{{ description }}
'''.lstrip()


def create_readme_file():
    global README_TEMPLATE, PACKAGE_NAME, MAIN_DIR
    # creating licence file
    env = jinja2.Environment()
    template = env.from_string(README_TEMPLATE)
    rendered = template.render(package_name=PACKAGE_NAME, description="Write Description here..")
    with open(os.path.join(MAIN_DIR, "README.rst"), 'w') as f:
        f.write(rendered)
