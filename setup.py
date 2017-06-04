from distutils.core import setup

dependencies = [p.rstrip('\n') for p in open('requirements/requirements.txt')]

setup(
    name='trawler',
    version='1.0.0',
    packages=['trawler', ],
    url='https://github.com/invaana/trawler',
    license='',
    author='Ravi RT Merugu',
    author_email='rrmerugu@gmail.com',
    description='A data gathering framework to search and get information from web sources',
    install_requires=dependencies
)