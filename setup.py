from setuptools import setup

setup(name="phanes",
    version='0.1',
    description='Integer Vector Friendly Homomorphic Encryption Library',
    url="https://github.com/vikene/Phanes.git",
    author="Vigneash Sundararajan",
    author_email="vigneashsundar@live.com",
    license="MIT",
    zip_safe=False,
    install_requires=[
        'numpy',
        'bitstring'
    ],
    packages=['phanes'])