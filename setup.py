import setuptools

from requests_random_user_agent import __version__

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name="requests_random_user_agent",
    version=__version__,
    author="David Wittman",
    author_email="david@wittman.com",
    description="Automatically generate a random User Agent for the requests library",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/DavidWittman/requests-random-user-agent",
    install_requires=['requests>=2.0.1,<3.0.0'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
