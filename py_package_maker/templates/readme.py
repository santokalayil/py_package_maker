import os
import jinja2
from ..paths import MAIN_DIR

PACKAGE_NAME = os.path.split(MAIN_DIR)[-1]

README_TEMPLATE = '''
# {{ package_name }}
---

[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-70x28.png)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat)](https://github.com/santokalayil/mallu/blob/master/LICENSE)
---
{{ description }}

### How to install:
```
$ pip install git+https://github.com/santokalayil/py_package_maker.git@dev
```
'''.lstrip()


def create_readme_file():
    global README_TEMPLATE, PACKAGE_NAME, MAIN_DIR
    # creating licence file
    env = jinja2.Environment()
    template = env.from_string(README_TEMPLATE)
    rendered = template.render(package_name=PACKAGE_NAME, description="Write Description here..")
    with open(os.path.join(MAIN_DIR, "README.md"), 'w') as f:
        f.write(rendered)
