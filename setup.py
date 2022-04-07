import pathlib
from setuptools import setup, find_packages

from rapiddns import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="rapiddns",
    version=__version__.__version__,
    description="Simple python client for rapiddns.io.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nullt3r/rapiddns",
    author="nullt3r",
    author_email="nullt3r@bugdelivery.com",
    license="MIT",
    python_requires='>=3.6, <4',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    install_requires=["requests", "bs4"],
    entry_points={
        "console_scripts": [
            "rapiddns=rapiddns.__main__:main",
        ]
    },
)
