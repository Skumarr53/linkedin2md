#!/usr/bin/env python3

import os
from setuptools import find_packages, setup
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
import linkedin2md


PROJECT_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
install_requirements = parse_requirements(
    os.path.join(PROJECT_ROOT_DIR, 'requirements.txt'), session=False
)
try:
    requirements = [str(ir.req) for ir in install_requirements]
except:
    requirements = [str(ir.requirement) for ir in install_requirements]

setup(
    packages=find_packages(exclude=["linkedin2md.bin"]),
    scripts=["linkedin2md/bin/linkedin2md"],
    install_requires=requirements,
    name="linkedin2md",
    version=linkedin2md.__version__,
    author="Shun-Yi Jheng",
    author_email="M157q.tw@gmail.com",
    url="https://github.com/M157q/linkedin2md",
    keywords="LinkedIn, markdown, resume",
    description="Export public LinkedIn resume to markdown format",
    platforms=['Linux'],
    license='GPLv3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
)
