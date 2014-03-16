#!/usr/bin/env python

from setuptools import setup

setup(
    name='mergejs',
    version='1.0.0',
    description='Merge multiple JavaScript source code files into one',
    long_description='',
    url='https://github.com/Turbo87/mergejs.py',
    download_url='https://pypi.python.org/pypi/mergejs',
    author='Tobias Bieniek',
    author_email='tobias.bieniek@gmx.de',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Topic :: Software Development :: Build Tools',
    ],
    py_modules=['toposort', 'mergejs'],
    package_dir={'': 'tools'},
    scripts=['tools/mergejs.py']
)
