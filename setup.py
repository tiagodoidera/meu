from setuptools import setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='bitcoin_vanity',
    version='0.1',
    description='Bitcoin vanity address miner',
    url='https://github.com/jcsongor/bitcoin_vanity',
    author='Jozsa Csongor',
    author_email='jozsa.csongor@gmail.com',
    license='MIT',
    long_description=long_description,
    packages=['bitcoin_vanity'],
    install_requires=[
        'ecdsa==0.13',
        'base58==1.0.2',
    ],
    extras_require={
        'dev': [
            'coverage==4.5.2',
            'coveralls==1.5.1',
        ]
    },
    zip_safe=False
)
