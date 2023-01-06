from setuptools import find_packages, setup

setup(
    name='Civi',
    packages=find_packages(include=['Ci']),
    version='0.1.0',
    description='Library help you to create level system to your discord bot',
    author='Eris#1318/discord',
    license='MIT',
    install_requires=['sqlite3'],
    test_suite='none',
)