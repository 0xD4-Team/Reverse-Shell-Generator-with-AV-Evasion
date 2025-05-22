from setuptools import setup, find_packages

setup(
    name="ReverseShellGenerator",
    version="1.0",
    author="0xD4 Team",
    description="Advanced Reverse Shell Generator with AV Evasion",
    packages=find_packages(),
    install_requires=[
        'requests>=2.28.1',
        'pycryptodome>=3.15.0',
        'argparse>=1.4.0',
        'colorama>=0.4.6',
        'fake-useragent>=1.1.3',
        'dnslib',
        'pathlib',
        'argparse',
        'abc',
        'httpserver',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'rsg=main:main',
        ],
    },
)