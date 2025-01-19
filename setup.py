# topsis_package/setup.py
from setuptools import setup, find_packages

setup(
    name='topsis_package',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy'],
    author='Yajur Chaudhary',
    description='A Python library for performing TOPSIS analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YChaudhary1357/TOPSIS',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
