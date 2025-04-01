from setuptools import find_packages, setup

setup(
    name="poliastro2",
    version="0.2.dev0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    requires=[
        "astropy >=5.0,<6",
        "astroquery >=0.3.9",
        "jplephem",
        "matplotlib >=2.0,!=3.0.1",
        "numba >=0.46 ; python_version<'3.9'",
        "numba >=0.53.0 ; python_version>='3.9'",
        "numpy",
        "pandas",
        "plotly >=4.0,<6",
        "pyerfa",
        "scipy >=1.4.0",
    ],
    author="Xiyuan Li",
    author_email="xli2522@uwo.ca",
    description="A project for orbital dynamics calculations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nra-research/poliastro2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    keywords = [
    "aero",
    "aerospace",
    "engineering",
    "astrodynamics",
    "poliastro",
    "orbits",
    "kepler",
    "orbital mechanics"
    ]
)