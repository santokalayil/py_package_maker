import os
import jinja2
from ..paths import MAIN_DIR

PACKAGE_NAME = os.path.split(MAIN_DIR)[-1]
AUTHOR_NAME = "Santo K Thomas"

install_requires = ['setuptools', 'jinja2>=3.1.0']

SETUP_PY_TEMPLATE = '''
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py

class install_py(build_py):
    def run(self) -> None:
        # do somethis here
        print("INSTALLING [ {{ name }} ] for Ezetap..")

        super().run()



setup(
    name='{{ name }}',
    version='{{ version }}',    
    description='{{ description }}',
    url='{{ url }}',
    author='{{ author }}',
    author_email='{{ author_email }}',
    license='{{ license }}',
    # packages=find_packages(include=('{{ name }}','{{ name }}.*')),

    packages=find_packages(
        include=(
            '{{ name }}',
            # '{{ name }}.*', 
            # '{{ name }}.errors.*',
        )
    ),

    install_requires={{ install_requires }},

    cmdclass={'build_py': install_py},

    # this is to include datafiles listed in the MANIFEST.in  file
    # include_package_data=True,
    # package_data={
    #     '{{ name }}': [
    #         'assets/configuration.yaml',
    #         # 'media/.*',
    #         'assets/media/logos/manual_references/*.png',
    #         'assets/media/logos/ideal_references/*',
    #         'assets/media/screenshots/original/*.png',
    #         'assets/media/screenshots/cropped/*.png',
    #         'assets/media/screenshots/padded/*.png',
    #         
    #     ]
    # },

    classifiers=[
        'License :: OSI Approved :: {{ license_name }} License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
'''.lstrip()


def create_setup_py_file():
    global SETUP_PY_TEMPLATE, PACKAGE_NAME, AUTHOR_NAME, MAIN_DIR, install_requires
    # creating setup.py file
    env = jinja2.Environment()
    template = env.from_string(SETUP_PY_TEMPLATE)
    rendered = template.render(
        name=PACKAGE_NAME, 
        version="0.1.0",
        description="This library will initialise the working directory as a package that can be installed by pip",
        url = "https://github.com/santokalayil/py_package_maker",
        author=AUTHOR_NAME,
        author_email = "santokalayil@gmail.com",
        license = "MIT",
        license_name = "MIT",
        install_requires = str(install_requires)
    )
    with open(os.path.join(MAIN_DIR, "setup.py"), 'w') as f:
        f.write(rendered)
