from setuptools import setup, find_packages

setup(
    name='py_package_maker',
    version='0.1.0',    
    description='This library will initialise the working directory as a package that can be installed by pip',
    url='https://github.com/santokalayil/py_package_maker',
    author='Santo K Thomas',
    author_email='santokalayil@gmail.com',
    license='MIT',
    packages=find_packages(include=('py_package_maker','py_package_maker.*')),
    install_requires=['setuptools', 'jinja2>=3.1.0'],

    classifiers=[
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)