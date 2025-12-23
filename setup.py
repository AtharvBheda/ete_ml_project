from setuptools import setup, find_packages

setup(
    name='mlproject',
    version='0.0.1',
    author='Atharv',
    author_email='atharvbheda@gmail.com',
    packages=find_packages(),
    install_requires = ['pandas', 'numpy', 'seaborn']
)