from setuptools import setup, find_packages

setup(
    name = 'ECGXML',
    version = '0.1.1',
    packages = find_packages(),
    instal_requires = [
        'xmltodict',
        'numpy'
            ]
)