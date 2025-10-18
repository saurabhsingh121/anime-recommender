from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="anime-recommender",
    version="0.1.0",
    author="Saurabh Singh",
    description="Anime Recommender System",
    packages=find_packages(),
    install_requires=requirements,
)