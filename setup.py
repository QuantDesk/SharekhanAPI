from setuptools import setup, find_packages
setup(
    name='sharekhan',
    version='1.0.0.9',
    author='rg',
    author_email='rimagiri18@email.com',
    description='A short description of your package',
    packages=find_packages(),
    install_requires=[
        'requests==2.28.2',
        'six~=1.16.0'
    ]
)