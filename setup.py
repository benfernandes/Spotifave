from setuptools import setup

setup(
    name='Spotifave',
    version='1.0',
    description='Visualize the artists in any Spotify playlist',
    author='Benjamin Fernandes',
    author_email='contact@benfernandes.com',
    packages=['spotifave'],
    install_requires=[
        'spotipy',
        'matplotlib',
        'squarify',
        'attrs'
    ]
)
